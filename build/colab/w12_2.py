from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
uploaded = files.upload()
df = pd.read_csv('clinic_visits.csv')
# 1. 필터: 이 한 줄만 바꾸면 세 차트가 함께 바뀐다 / 筛选器: 只要改这一行, 三张图会一起变化
DEPT = 'Pediatrics'
sub = df[df['department'] == DEPT]
order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
# 2. 차트 ①용: 진료과별 환자 수 / 图 ① 用: 各科室患者数
dept = df.groupby('department')['patients'].sum().sort_values()
# 3. 차트 ②용: 고른 과의 요일 × 시간 표 / 图 ② 用: 所选科室的 星期 × 小时 表
table = sub.pivot_table(index='weekday', columns='hour', values='patients', aggfunc='mean').reindex(order)
best = table.stack().idxmax()
# 4. 차트 ③용: 주별 평균 대기 시간 / 图 ③ 用: 每周平均等待时间
sub = sub.assign(week=pd.to_datetime(sub['date']).dt.isocalendar().week)
wait = sub.groupby('week')['wait_min'].mean()
print(DEPT, '| busiest =', best[0], int(best[1]), 'h', '| wait first week =', round(wait.iloc[0], 1), '-> last week =', round(wait.iloc[-1], 1))
fig = plt.figure(figsize=(13, 7))
fig.suptitle(DEPT + ': busiest on ' + best[0] + ' ' + str(best[1]) + 'h, and the wait grew over four weeks', fontsize=14)
ax1 = fig.add_subplot(2, 2, 1)
ax1.barh(dept.index, dept.values, color=dept.index.map({DEPT: '#1e3a8a'}).fillna('#cbd5e1'))
ax1.set_title('1. Patients by department')
ax2 = fig.add_subplot(2, 2, 2)
im = ax2.imshow(table.values, cmap='GnBu', aspect='auto')
fig.colorbar(im, ax=ax2, label='Patients')
ax2.set_xticks(range(len(table.columns)))
ax2.set_xticklabels(table.columns)
ax2.set_yticks(range(5))
ax2.set_yticklabels(order)
ax2.set_title('2. Weekday x hour')
ax3 = fig.add_subplot(2, 1, 2)
ax3.plot(range(1, len(wait) + 1), wait.values, color='#0b7a86', marker='o')
ax3.set_ylim(0, wait.max() * 1.2)
ax3.set_xticks(range(1, len(wait) + 1))
ax3.set_xlabel('Week')
ax3.set_ylabel('Average wait (min)')
ax3.set_title('3. Waiting time trend')
fig.tight_layout()
plt.show()
