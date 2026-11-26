from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
uploaded = files.upload()
df = pd.read_csv('clinic_visits.csv')
# 1. 진료과별 주간 평균 환자 수 = 전체 합계 ÷ 주 수 / 各科室每周平均患者数 = 总数 ÷ 周数
weeks = pd.to_datetime(df['date']).dt.isocalendar().week.nunique()
dept = (df.groupby('department')['patients'].sum() / weeks).sort_values()
print('weeks =', weeks)
print(dept.round(1))
plt.figure(figsize=(8, 4))
colors = ['#cbd5e1'] * (len(dept) - 1) + ['#1e3a8a']
bars = plt.barh(dept.index, dept.values, color=colors)
plt.bar_label(bars, labels=dept.round(0).astype(int).astype(str), padding=3)
plt.xlim(0, dept.max() * 1.15)
plt.title('Internal Medicine sees the most patients each week')
plt.xlabel('Patients per week')
plt.show()
