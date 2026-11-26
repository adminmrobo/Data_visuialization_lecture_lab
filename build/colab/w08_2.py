from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
uploaded = files.upload()
df = pd.read_csv('payments.csv')
# 1. 날짜에서 요일 이름을 뽑는다 / 从日期中提取星期名称
df['weekday'] = pd.to_datetime(df['date']).dt.day_name().str[:3]
order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# 2. 요일 × 시간 결제 건수 표 (없는 조합은 0) / 星期 × 小时 的支付笔数表 (没有的组合为 0)
table = pd.crosstab(df['weekday'], df['hour']).reindex(order).fillna(0)
# 3. 가장 많은 셀을 찾는다 / 找出笔数最多的格子
best = table.stack().idxmax()
print('busiest cell =', best[0], int(best[1]), 'h ->', int(table.stack().max()), 'payments')
plt.figure(figsize=(10, 3.8))
plt.imshow(table.values, cmap='GnBu', aspect='auto')
plt.colorbar(label='Number of payments')
plt.xticks(range(len(table.columns)), table.columns)
plt.yticks(range(len(order)), order)
plt.xlabel('Hour')
plt.title('Friday noon is the busiest time')
plt.show()
