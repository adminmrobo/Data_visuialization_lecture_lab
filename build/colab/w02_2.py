from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
uploaded = files.upload()
df = pd.read_csv('payments.csv')
# 1. 도시별 매출 비중(%)을 계산한다 / 计算各城市销售额占比 (%)
share = (df.groupby('city')['amount'].sum() / df['amount'].sum() * 100).round(1)
fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
# 2. 왼쪽: 파이 차트 (비율 숫자는 일부러 빼서 눈으로만 읽게 한다) / 左图: 饼图 (故意不标数字, 只靠眼睛读)
ax[0].pie(share.values, labels=share.index, startangle=90, counterclock=False)
ax[0].set_title('Pie: which is bigger, Shenzhen or Shanghai?')
# 3. 오른쪽: 같은 숫자를 큰 것부터 정렬한 가로 막대 / 右图: 同样的数字按从大到小排序的横向柱状图
s = share.sort_values()
bars = ax[1].barh(s.index, s.values, color='#0b7a86')
ax[1].bar_label(bars, labels=s.astype(str) + '%', padding=3)
ax[1].set_xlim(0, s.max() * 1.2)
ax[1].set_title('Sorted bar: Shenzhen 20.1% > Shanghai 19.7%')
ax[1].set_xlabel('Share of sales (%)')
print(share.sort_values(ascending=False))
plt.show()
