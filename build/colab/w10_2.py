from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
uploaded = files.upload()
df = pd.read_csv('health_2024_sample5000.csv').dropna(subset=['waist_cm', 'systolic_bp'])
# 0. 점검 단계에서 찾은 불가능한 값(허리둘레 1,000cm 같은 입력 오류)을 뺀다 / 去掉检查阶段发现的不可能的值 (例如腰围 1000 厘米这样的输入错误)
df = df[df['waist_cm'].between(50, 150) & df['systolic_bp'].between(70, 220)]
print('rows after check =', len(df))
# 1. 연령대 코드(5=20~24세 … 18=85세 이상)를 세 묶음으로 나눈다 / 把年龄段代码 (5=20~24 岁 … 18=85 岁以上) 分成三组
df['age'] = pd.cut(df['age_group_code'], bins=[0, 8, 12, 99], labels=['Under 40', '40-59', '60+'])
# 2. 전체 상관계수와 연령대 안 상관계수를 비교한다 / 比较整体相关系数和各年龄段内部的相关系数
print('all ages r =', round(df['waist_cm'].corr(df['systolic_bp']), 2))
print(df.groupby('age', observed=True)[['waist_cm', 'systolic_bp']].corr().xs('waist_cm', level=1)['systolic_bp'].round(2))
# 3. 연령대마다 색을 달리해 산점도를 그린다 (점이 많아 투명하게) / 按年龄段用不同颜色画散点图 (点多, 所以设为半透明)
plt.figure(figsize=(7.5, 4.6))
plt.scatter(df.loc[df['age'] == 'Under 40', 'waist_cm'], df.loc[df['age'] == 'Under 40', 'systolic_bp'], s=6, alpha=0.3, color='#94a3b8', label='Under 40')
plt.scatter(df.loc[df['age'] == '40-59', 'waist_cm'], df.loc[df['age'] == '40-59', 'systolic_bp'], s=6, alpha=0.3, color='#0b7a86', label='40-59')
plt.scatter(df.loc[df['age'] == '60+', 'waist_cm'], df.loc[df['age'] == '60+', 'systolic_bp'], s=6, alpha=0.3, color='#b45309', label='60+')
plt.title('Within each age group the link shrinks (r 0.31-0.36 vs 0.43 overall)')
plt.xlabel('Waist (cm)')
plt.ylabel('Systolic blood pressure (mmHg)')
plt.legend(markerscale=3)
plt.show()
