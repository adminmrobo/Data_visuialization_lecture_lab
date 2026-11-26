# 1. 파일 올리기 도구를 불러온다 / 导入文件上传工具
from google.colab import files
# 2. 표를 다루는 pandas와 그림을 그리는 matplotlib을 불러온다 / 导入处理表格的 pandas 和绘图的 matplotlib
import pandas as pd
import matplotlib.pyplot as plt
# 3. 내 컴퓨터의 payments.csv를 골라 올린다 / 从电脑中选择并上传 payments.csv
uploaded = files.upload()
# 4. CSV 파일을 표(DataFrame)로 읽는다 / 把 CSV 文件读成表格 (DataFrame)
df = pd.read_csv('payments.csv')
# 5. 처음 5행과 행·열 수를 확인한다 / 查看前 5 行以及行数和列数
print(df.head())
print('rows, columns =', df.shape)
# 6. 도시별 매출 합계를 계산한다 (빈 값은 자동으로 빠진다) / 按城市计算销售额合计 (缺失值会自动排除)
city_sales = df.groupby('city', sort=False)['amount'].sum()
print(city_sales.round(1))
# 7. 막대 그래프를 그린다 / 绘制柱状图
plt.figure(figsize=(7, 4))
plt.bar(city_sales.index, city_sales.values, color='#0b7a86')
# 8. 제목과 축 이름은 영어로 쓴다 / 标题和坐标轴名称用英文
plt.title('Sales by City')
plt.xlabel('City')
plt.ylabel('Sales (CNY)')
plt.show()
