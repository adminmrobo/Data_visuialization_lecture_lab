# 건강검진 모의 데이터(health_2020~2024.csv) → 10주차 페이지용 요약 JSON
# 사용: python3 build/tools/make_health_summary.py <mock 폴더>
import sys, json, os
import pandas as pd, numpy as np
src = sys.argv[1]
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'health_summary.json')
SIDO = {11:'서울',26:'부산',27:'대구',28:'인천',29:'광주',30:'대전',31:'울산',36:'세종',41:'경기',42:'강원',43:'충북',44:'충남',45:'전북',46:'전남',47:'경북',48:'경남',49:'제주'}
def load(y):
    d = pd.read_csv(os.path.join(src, 'health_%d.csv' % y)).rename(columns={'age_code': 'age_group_code', 'blood_glucose': 'fasting_glucose'})
    raw = d.copy()
    d.loc[~d.waist_cm.between(50, 150), 'waist_cm'] = np.nan
    d.loc[~d.systolic_bp.between(70, 250), 'systolic_bp'] = np.nan
    d.loc[~d.fasting_glucose.between(50, 500), 'fasting_glucose'] = np.nan
    d['bmi'] = (d.weight_5kg / (d.height_5cm / 100) ** 2).round(1)
    d['obese'] = (d.bmi >= 25).astype(int)
    return raw, d
raw, d = load(2024)
S = {}
S['rows'] = len(d)
S['outliers'] = {'waist': int((raw.waist_cm.notna() & ~raw.waist_cm.between(50, 150)).sum()),
                 'bp': int((raw.systolic_bp.notna() & ~raw.systolic_bp.between(70, 250)).sum()),
                 'glucose': int((raw.fasting_glucose.notna() & ~raw.fasting_glucose.between(50, 500)).sum())}
S['missing'] = {k: int(raw[k].isna().sum()) for k in ['waist_cm', 'systolic_bp', 'fasting_glucose', 'smoking_status']}
S['raw_max'] = {'waist': float(raw.waist_cm.max()), 'bp': float(raw.systolic_bp.max()), 'glucose_min': float(raw.fasting_glucose.min())}
s = d.groupby('sido_code').obese.mean().mul(100).round(1).sort_values(ascending=False)
S['sido'] = [[SIDO[int(k)], float(v)] for k, v in s.items()]
S['obese_nat'] = round(float(d.obese.mean() * 100), 1)
S['bmi_mean'] = round(float(d.bmi.mean()), 1)
g = d.fasting_glucose.dropna()
edges = list(range(50, 305, 5))
cnt, _ = np.histogram(g.clip(upper=299.9), bins=edges)
S['glu'] = {'edges': edges, 'counts': [int(c) for c in cnt], 'mean': round(float(g.mean()), 1), 'median': float(g.median()),
            'ge126': round(float((g >= 126).mean() * 100), 1), 'n126': int((g >= 126).sum()), 'b100_125': round(float(g.between(100, 125.999).mean() * 100), 1), 'n': int(len(g))}
x = d[['waist_cm', 'systolic_bp', 'age_group_code']].dropna()
S['r_all'] = round(float(x[['waist_cm', 'systolic_bp']].corr().iloc[0, 1]), 2)
ag = pd.cut(x.age_group_code, [4, 8, 10, 12, 18], labels=['20-39', '40-49', '50-59', '60+'])
S['r_age'] = [[str(k), round(float(v[['waist_cm', 'systolic_bp']].corr().iloc[0, 1]), 2), int(len(v))] for k, v in x.groupby(ag, observed=True)]
smp = x.sample(700, random_state=42)
grp = pd.cut(smp.age_group_code, [4, 8, 10, 12, 18], labels=[0, 1, 2, 3]).astype(int)
S['pts'] = [[float(a), float(b), int(c)] for a, b, c in zip(smp.waist_cm, smp.systolic_bp, grp)]
S['age_waist_bp'] = [[str(k), round(float(v.waist_cm.mean()), 1), round(float(v.systolic_bp.mean()), 1)] for k, v in x.groupby(pd.cut(x.age_group_code, [4, 6, 8, 10, 12, 14, 16, 18], labels=['20대', '30대', '40대', '50대', '60대', '70대', '80+']), observed=True)]
sm = d.groupby('sex_code').smoking_status.value_counts(normalize=True).mul(100).round(1)
S['smoke'] = {'남': [float(sm[1][1.0]), float(sm[1][2.0]), float(sm[1][3.0])], '여': [float(sm[2][1.0]), float(sm[2][2.0]), float(sm[2][3.0])]}
S['bp_sex'] = [round(float(d[d.sex_code == 1].systolic_bp.mean()), 1), round(float(d[d.sex_code == 2].systolic_bp.mean()), 1)]
T = []
for y in range(2020, 2025):
    _, dy = load(y)
    gy = dy.fasting_glucose.dropna()
    T.append([y, len(dy), round(float(dy.obese.mean() * 100), 1), round(float((gy >= 126).mean() * 100), 1)])
S['trend'] = T
json.dump(S, open(out, 'w', encoding='utf-8'), ensure_ascii=False)
print(json.dumps({k: v for k, v in S.items() if k not in ('pts', 'glu')}, ensure_ascii=False))
print(S['glu']['mean'], S['glu']['median'], S['glu']['ge126'], S['glu']['n126'], S['glu']['n'])
