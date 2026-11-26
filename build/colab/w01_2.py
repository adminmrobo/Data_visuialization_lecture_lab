from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
uploaded = files.upload()
df = pd.read_csv('payments.csv')
# 1. 도시별 매출을 큰 것부터 정렬한다 / 按销售额从大到小排序
city_sales = df.groupby('city')['amount'].sum().sort_values(ascending=False)
# 2. 전체에서 차지하는 비율(%)을 계산한다 / 计算占总体的比例 (%)
share = (city_sales / city_sales.sum() * 100).round(1)
print(share)
# 3. 1위만 진한 남색, 나머지는 회색으로 칠할 색 목록 / 只有第一名用深蓝色, 其余用灰色
colors = ['#1e3a8a'] + ['#cbd5e1'] * (len(city_sales) - 1)
plt.figure(figsize=(7, 4.4))
bars = plt.bar(city_sales.index, city_sales.values, color=colors)
# 4. 막대 위에 비율을 적는다 / 在柱子上方标注比例
plt.bar_label(bars, labels=share.astype(str) + '%', padding=3)
# 5. 제목은 결론 문장으로 쓴다 / 标题写成结论句
plt.title('Beijing leads with ' + str(share.iloc[0]) + '% of sales')
plt.ylabel('Sales (CNY)')
plt.ylim(0, city_sales.max() * 1.15)
# 6. 출처와 기간을 그림 아래에 적는다 (데이터 3원칙) / 在图下方注明来源和期间 (数据三原则)
plt.figtext(0.01, -0.04, 'Source: payments.csv (class mock data), ' + df['date'].min() + ' ~ ' + df['date'].max(), color='gray', fontsize=9)
plt.show()
