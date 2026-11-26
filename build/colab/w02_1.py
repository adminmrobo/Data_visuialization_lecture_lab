from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
uploaded = files.upload()
df = pd.read_csv('payments.csv')
# 1. 채널별 결제 건수를 센다 / 统计各渠道的支付笔数
cnt = df['channel'].value_counts()
print(cnt)
# 2. 그림 두 개를 나란히 만든다 / 并排创建两张图
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
# 3. 왼쪽: Y축을 가장 작은 값 근처에서 시작한 잘못된 예 / 左图: Y 轴从最小值附近开始的错误示例
low = cnt.min() * 0.9
ax[0].bar(cnt.index, cnt.values, color='#b45309')
ax[0].set_ylim(low, cnt.max() * 1.05)
ax[0].set_title('Wrong: Y axis starts at ' + str(int(low)))
ax[0].set_ylabel('Number of payments')
# 4. 오른쪽: Y축을 0부터 시작한 바른 예 / 右图: Y 轴从 0 开始的正确示例
ax[1].bar(cnt.index, cnt.values, color='#0b7a86')
ax[1].set_ylim(0, cnt.max() * 1.05)
ax[1].set_title('Right: Y axis starts at 0')
# 5. 1위와 2위 막대의 눈에 보이는 길이 비와 실제 비를 비교한다 / 比较第一、第二名柱子的视觉长度比和实际比
print('real ratio      =', round(cnt.iloc[0] / cnt.iloc[1], 2))
print('wrong-chart ratio =', round((cnt.iloc[0] - low) / (cnt.iloc[1] - low), 2))
plt.show()
