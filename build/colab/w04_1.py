from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
uploaded = files.upload()
# 1. 파일을 읽고 결제액 빈 값은 뺀다 / 读取文件并去掉支付金额的缺失值
df = pd.read_csv('payments.csv').dropna(subset=['amount'])
# 2. 채널별 평균과 중앙값을 함께 계산한다 / 同时计算各渠道的平均值和中位数
stat = df.groupby('channel')['amount'].agg(['mean', 'median', 'count']).round(1)
print(stat)
# 3. 평균과 중앙값을 나란히 막대로 그린다 / 把平均值和中位数并排画成柱状图
ax = stat[['mean', 'median']].plot(kind='bar', figsize=(7, 4), color=['#b45309', '#1e3a8a'], rot=0)
ax.set_title('In every channel the mean is above the median')
ax.set_xlabel('Channel')
ax.set_ylabel('Payment amount (CNY)')
ax.legend(['Mean', 'Median'])
plt.show()
