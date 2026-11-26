from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
uploaded = files.upload()
df = pd.read_csv('payments.csv')
# 1. 날짜 글자를 날짜 형식으로 바꾼다 / 把日期文字转换成日期格式
df['date'] = pd.to_datetime(df['date'])
# 2. 날짜별 매출 합계 / 每天的销售额合计
daily = df.groupby('date')['amount'].sum()
top_day = daily.idxmax()
print('days =', len(daily), '| mean =', round(daily.mean(), 1), '| max =', top_day.date(), round(daily.max(), 1))
plt.figure(figsize=(9, 4))
plt.plot(daily.index, daily.values, color='#0b7a86', marker='o', markersize=3)
# 3. 평균선은 회색 점선 / 平均线用灰色虚线
plt.axhline(daily.mean(), color='gray', linestyle='--', label='Daily mean')
# 4. 가장 높은 날 한 곳에만 주석을 단다 / 只在最高的那一天加注释
plt.annotate('Peak ' + str(top_day.date()), xy=(top_day, daily.max()), xytext=(top_day, daily.max() * 1.08), ha='center', arrowprops=dict(arrowstyle='->', color='#b45309'), color='#b45309')
plt.ylim(0, daily.max() * 1.2)
plt.title('Sales peaked on March 27')
plt.ylabel('Sales (CNY)')
plt.legend()
plt.show()
