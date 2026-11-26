from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
uploaded = files.upload()
df = pd.read_csv('payments.csv')
df['date'] = pd.to_datetime(df['date'])
# 1. KPI 숫자 4개 / 4 个 KPI 数字
total = df['amount'].sum()
orders = len(df)
basket = df['amount'].median()
new_rate = df['is_new_user'].mean() * 100
# 2. 날짜별 매출과 주말·평일 하루 평균 / 每日销售额以及周末、工作日的日均销售额
daily = df.groupby('date')['amount'].sum()
weekend = daily[daily.index.dayofweek >= 5].mean()
weekday = daily[daily.index.dayofweek < 5].mean()
print('weekend / weekday =', round(weekend / weekday, 2))
# 3. 한 화면을 3행으로 나눈다: KPI 줄 · 추세 · 비교 / 把一个画面分成三行: KPI 行、趋势、比较
fig = plt.figure(figsize=(10, 6.4))
fig.suptitle('Weekend days sell about 1.2x more than weekdays', fontsize=14)
fig.text(0.02, 0.86, 'Total sales\n' + format(round(total), ','), fontsize=13)
fig.text(0.27, 0.86, 'Orders\n' + str(orders), fontsize=13)
fig.text(0.52, 0.86, 'Median basket\n' + str(round(basket, 1)), fontsize=13)
fig.text(0.77, 0.86, 'New customers\n' + str(round(new_rate, 1)) + '%', fontsize=13)
ax1 = fig.add_axes([0.07, 0.38, 0.9, 0.38])
ax1.plot(daily.index, daily.values, color='#0b7a86')
ax1.set_ylabel('Daily sales (CNY)')
ax1.set_ylim(0, daily.max() * 1.1)
ax2 = fig.add_axes([0.07, 0.06, 0.9, 0.22])
ax2.barh(['Weekday', 'Weekend'], [weekday, weekend], color=['#cbd5e1', '#1e3a8a'])
ax2.set_xlabel('Average daily sales (CNY)')
plt.show()
