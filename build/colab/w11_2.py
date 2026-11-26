from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
uploaded = files.upload()
df = pd.read_csv('delivery_log.csv')
# 1. 지연된 건만 고른다 (이 조건이 빠지면 정시 배송까지 섞인다) / 只选延误的订单 (漏掉这个条件就会混进准时配送)
late = df[df['delayed'] == 1]
print('all orders =', len(df), '| delayed =', len(late))
# 2. 원인별 건수를 큰 것부터 정렬한다 / 按原因统计笔数并从大到小排序
cnt = late['delay_cause'].value_counts()
# 3. 누적 비율(%) = 앞에서부터 더한 몫 / 累计占比 (%) = 从前往后累加的份额
cum = (cnt.cumsum() / cnt.sum() * 100).round(1)
print(pd.DataFrame({'count': cnt, 'cumulative %': cum}))
fig, ax = plt.subplots(figsize=(9, 4.4))
ax.bar(cnt.index, cnt.values, color='#0b7a86')
ax.set_ylabel('Delayed orders')
# 4. 오른쪽 축에 누적 비율 선과 80% 기준선을 겹친다 / 在右侧坐标轴叠加累计占比线和 80% 基准线
ax2 = ax.twinx()
ax2.plot(cnt.index, cum.values, color='#b45309', marker='o')
ax2.axhline(80, color='gray', linestyle='--')
ax2.set_ylim(0, 105)
ax2.set_ylabel('Cumulative share (%)')
ax.set_title('Top 3 causes make up about 80% of delays')
plt.show()
