from google.colab import files
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
uploaded = files.upload()
# 1. 파일을 읽고 amount 빈 값이 있는 행은 뺀다 / 读取文件并去掉 amount 缺失的行
df = pd.read_csv('payments.csv').dropna(subset=['amount'])
# 2. Seaborn이 히스토그램을 그린다 / 用 Seaborn 画直方图
plt.figure(figsize=(8, 4.2))
sns.histplot(df['amount'], bins=30, color='#0b7a86')
# 3. Matplotlib으로 평균선(빨강 점선)과 중앙값선(파랑 실선)을 더한다 / 用 Matplotlib 加平均线 (红色虚线) 和中位数线 (蓝色实线)
plt.axvline(df['amount'].mean(), color='#b91c1c', linestyle='--', label='Mean ' + str(round(df['amount'].mean(), 1)))
plt.axvline(df['amount'].median(), color='#1e3a8a', label='Median ' + str(round(df['amount'].median(), 1)))
# 4. 제목·축 이름·범례로 다듬는다 / 用标题、坐标轴名称和图例来润色
plt.title('Long right tail: mean is higher than median')
plt.xlabel('Payment amount (CNY)')
plt.ylabel('Number of payments')
plt.legend()
print(df['amount'].describe().round(1))
plt.show()
