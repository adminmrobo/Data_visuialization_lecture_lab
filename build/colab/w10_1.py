from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
# 1. 건강검진 표본과 코드북 두 파일을 함께 올린다 / 同时上传体检样本和代码本两个文件
uploaded = files.upload()
df = pd.read_csv('health_2024_sample5000.csv')
code = pd.read_csv('codebook.csv')
# 2. 시도 코드를 이름으로 바꿀 대응표를 만든다 / 制作把省市代码换成名称的对照表
sido = code[code['column'] == 'sido_code'].set_index('code')['label']
df['sido'] = df['sido_code'].map(sido)
# 3. BMI = 몸무게(kg) ÷ 키(m)의 제곱, 25 이상이면 비만 / BMI = 体重 (kg) ÷ 身高 (m) 的平方, 25 以上为肥胖
df['bmi'] = df['weight_5kg'] / (df['height_5cm'] / 100) ** 2
df['obese'] = df['bmi'] >= 25
# 4. 시도별 비만율(%)을 큰 것부터 정렬 / 按省市计算肥胖率 (%) 并从大到小排序
rate = (df.groupby('sido')['obese'].mean() * 100).sort_values()
national = df['obese'].mean() * 100
print('people =', len(df), '| national obesity rate =', round(national, 1), '%')
print(rate.round(1).tail(3))
plt.figure(figsize=(7, 5.4))
plt.barh(rate.index, rate.values, color='#0b7a86')
# 5. 전국 평균선 / 全国平均线
plt.axvline(national, color='#b45309', linestyle='--', label='National ' + str(round(national, 1)) + '%')
plt.title('Obesity rate by region (BMI 25+), sorted')
plt.xlabel('Obesity rate (%)')
plt.legend(loc='lower right')
plt.show()
