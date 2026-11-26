from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
uploaded = files.upload()
df = pd.read_csv('payments.csv').dropna(subset=['amount'])
# 1. 다섯 숫자 요약: 최솟값·Q1·중앙값·Q3·최댓값 / 五数概括: 最小值、Q1、中位数、Q3、最大值
five = df.groupby('channel')['amount'].quantile([0, 0.25, 0.5, 0.75, 1]).unstack().round(1)
five.columns = ['min', 'Q1', 'median', 'Q3', 'max']
print(five)
# 2. 채널별 상자그림을 그린다 / 按渠道画箱线图
ax = df.boxplot(column='amount', by='channel', figsize=(7, 4.4), grid=False)
# 3. 제목과 축 이름을 다듬는다 (pandas가 붙이는 위 제목은 지운다) / 润色标题和坐标轴 (去掉 pandas 自动加的总标题)
plt.suptitle('')
ax.set_title('Web has the highest median, and every channel has a long upper tail')
ax.set_xlabel('Channel')
ax.set_ylabel('Payment amount (CNY)')
plt.show()
