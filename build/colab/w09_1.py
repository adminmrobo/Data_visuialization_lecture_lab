from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
uploaded = files.upload()
df = pd.read_csv('payments.csv').dropna(subset=['amount'])
# 1. 신규(1)·기존(0)을 영어 이름으로 바꾼다 / 把新用户 (1)、老用户 (0) 换成英文名称
df['customer'] = df['is_new_user'].map({1: 'New', 0: 'Returning'})
# 2. 고객 유형별 결제액 중앙값 / 各客户类型的支付金额中位数
med = df.groupby('customer')['amount'].median().round(1)
plt.figure(figsize=(6, 4))
bars = plt.bar(med.index, med.values, color=['#cbd5e1', '#1e3a8a'])
plt.bar_label(bars, padding=3)
plt.ylim(0, med.max() * 1.2)
plt.title('Returning customers pay more per order')
plt.ylabel('Median payment (CNY)')
# 3. 차트 아래에 세 문장을 출력한다 / 在图表下面输出三句话
print('What    : median payment is', med['New'], 'for new and', med['Returning'], 'for returning customers.')
print('So What : a new customer pays about', round(med['New'] / med['Returning'] * 100), '% of a returning customer.')
print('Now What: test a second-visit coupon for new customers and compare next month.')
plt.show()
