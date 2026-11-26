# 11·12주 Colab 실습용 수업 가상 데이터 (시드 고정)
import numpy as np, pandas as pd, os
R = np.random.default_rng(1111)
out = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw')
# 1) 시간대별 교통량: 4주 × 24시간 × 구간 3곳
rows = []
days = pd.date_range('2026-10-05', periods=28, freq='D')
segs = {'Gangnam-daero': 1.15, 'Olympic-ro': 1.0, 'Jongno': 0.8}
for d in days:
    wd = d.dayofweek
    for h in range(24):
        if wd >= 5:
            base = 120 + 380 * np.exp(-((h - 14) / 4) ** 2)
        else:
            base = 60 + 520 * np.exp(-((h - 8) / 1.4) ** 2) + 600 * np.exp(-((h - 18) / 1.6) ** 2) + 180 * np.exp(-((h - 13) / 3) ** 2)
        if wd == 4 and 17 <= h <= 21:
            base *= 1.25
        if h < 5:
            base = 25 + h * 4
        for s, m in segs.items():
            rows.append((d.strftime('%Y-%m-%d'), d.strftime('%a'), h, s, int(round(base * m * (0.9 + 0.2 * R.random())))))
pd.DataFrame(rows, columns=['date', 'weekday', 'hour', 'segment', 'volume']).to_csv(os.path.join(out, 'traffic_hourly.csv'), index=False)
# 2) 배송 기록 1,000건
causes = ['Traffic jam', 'Wrong address', 'Volume surge', 'Bad weather', 'Vehicle failure']
w = [.38, .22, .18, .13, .09]
rows = []
for i in range(1000):
    d = days[R.integers(0, 28)]
    late = R.random() < .27
    c = R.choice(causes, p=w) if late else ''
    mins = int(R.normal(95, 15)) + (int(R.uniform(30, 120)) if late else 0)
    rows.append((f'D{i+1:04d}', d.strftime('%Y-%m-%d'), R.choice(['North', 'South', 'East', 'West']), mins, int(late), c))
pd.DataFrame(rows, columns=['order_id', 'date', 'region', 'delivery_min', 'delayed', 'delay_cause']).to_csv(os.path.join(out, 'delivery_log.csv'), index=False)
# 3) 병원 방문 기록: 4주 × 평일 5일 × 진료과 5 × 시간대 7
depts = {'Internal Medicine': 38, 'Surgery': 22, 'Pediatrics': 26, 'Orthopedics': 18, 'Dermatology': 12}
slots = [9, 10, 11, 13, 14, 15, 16]
rows = []
for k, d in enumerate([x for x in days if x.dayofweek < 5]):
    wd = d.dayofweek
    for dp, b in depts.items():
        for s in slots:
            base = b * (1.35 if wd == 0 else 1) * (1.25 if s < 12 else 0.9)
            if dp == 'Pediatrics' and s >= 14:
                base *= 1.2
            p = int(round(base * (0.8 + 0.4 * R.random())))
            wait = int(round(b * 0.55 + (k * 0.25 if dp == 'Pediatrics' else k * 0.05) + p * 0.15 + R.normal(0, 2)))
            rows.append((d.strftime('%Y-%m-%d'), d.strftime('%a'), s, dp, p, max(wait, 3)))
pd.DataFrame(rows, columns=['date', 'weekday', 'hour', 'department', 'patients', 'wait_min']).to_csv(os.path.join(out, 'clinic_visits.csv'), index=False)
print('ok')
