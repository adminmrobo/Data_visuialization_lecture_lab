from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
uploaded = files.upload()
df = pd.read_csv('payments.csv')
# 1. 열마다 빈 값(NaN)이 몇 개인지 센다 / 统计每一列有多少缺失值 (NaN)
print(df.isna().sum())
# 2. 세 가지 처리 방법으로 amount를 만든다 / 用三种方法处理 amount
fill_zero = df['amount'].fillna(0)
fill_median = df['amount'].fillna(df['amount'].median())
drop_rows = df['amount'].dropna()
# 3. 방법별 평균과 건수를 표로 만든다 / 把每种方法的平均值和笔数做成表
result = pd.DataFrame({'method': ['Fill with 0', 'Fill with median', 'Drop missing rows'], 'mean': [fill_zero.mean(), fill_median.mean(), drop_rows.mean()], 'rows': [len(fill_zero), len(fill_median), len(drop_rows)]}).round(2)
print(result)
# 4. 평균을 막대로 비교한다 (Y축은 0부터) / 用柱状图比较平均值 (Y 轴从 0 开始)
plt.figure(figsize=(7, 4))
bars = plt.bar(result['method'], result['mean'], color=['#b45309', '#0b7a86', '#1e3a8a'])
plt.bar_label(bars, labels=result['mean'].astype(str), padding=3)
plt.ylim(0, result['mean'].max() * 1.15)
plt.title('Filling missing amounts with 0 pulls the mean down')
plt.ylabel('Mean payment (CNY)')
plt.show()
