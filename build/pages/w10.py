# 10주차 — 산업별 데이터 시각화 3: 헬스케어/의료 (개인발표)
_H = open(HERE + '/data/health_summary.json', encoding='utf-8').read()
_CODE = [
 ("# [KO] 필요한 도구를 불러온다 / [ZH] 导入需要的工具", "주석 줄 — 한국어와 중국어로 이 아래 코드가 하는 일을 적는다"),
 ("import io", "올린 파일을 메모리에서 읽는 도구"), ("import pandas as pd", "표를 다루는 도구 pandas"), ("import matplotlib.pyplot as plt", "그림 도구"),
 ("from google.colab import files", "Colab의 파일 올리기 도구"),
 ("# [KO] CSV 파일을 직접 올린다 / [ZH] 直接上传 CSV 文件", "주석 줄"), ("uploaded = files.upload()", "파일 고르기 창을 띄운다"),
 ("file_name = list(uploaded.keys())[0]", "올린 파일의 이름을 꺼낸다"), ("df = pd.read_csv(io.BytesIO(uploaded[file_name]))", "올린 CSV를 표(df)로 읽는다"),
 ("df = df.rename(columns={'age_code': 'age_group_code', 'blood_glucose': 'fasting_glucose'})", "2020·2021년 파일의 다른 열 이름을 2022년 이후 이름으로 맞춘다 (없으면 그대로)"),
 ("# [KO] 범위를 벗어난 값은 결측으로 / [ZH] 超出范围的值设为缺失", "주석 줄 — 제거 기준은 사람이 정한다"),
 ("df.loc[~df['waist_cm'].between(50, 150), 'waist_cm'] = None", "허리둘레 50~150cm 밖의 값(예: 999)을 비운다"),
 ("df.loc[~df['systolic_bp'].between(70, 250), 'systolic_bp'] = None", "수축기 혈압 70~250 밖의 값(예: 0, 400)을 비운다"),
 ("df.loc[~df['fasting_glucose'].between(50, 500), 'fasting_glucose'] = None", "공복혈당 50~500 밖의 값(예: 0)을 비운다"),
 ("df['bmi'] = df['weight_5kg'] / (df['height_5cm'] / 100) ** 2", "BMI = 체중 ÷ (키 m)² — 5cm·5kg 구간 값이라 근삿값"),
 ("df['obese'] = (df['bmi'] >= 25).astype(int)", "BMI 25 이상이면 1, 아니면 0"),
 ("rate = df.groupby('sido_code')['obese'].mean().mul(100).sort_values()", "시도별 비만율(%)을 계산해 정렬한다"),
 ("ax = rate.plot(kind='barh', color='#1E3A8A', figsize=(8, 7))", "가로 막대로 그린다 (X축은 0부터)"),
 ("ax.axvline(df['obese'].mean() * 100, color='#B45309', linestyle='--', label='National average')", "전국 평균을 세로 점선으로"),
 ("ax.set_title('Obesity rate by province (BMI >= 25), 2024')", "제목은 영어로 — Colab 글꼴 문제를 피한다"),
 ("ax.set_xlabel('Obesity rate (%)')", "X축 제목(영어, 단위 포함)"), ("ax.legend()", "범례(영어)를 붙인다"), ("plt.show()", "그림을 띄운다"),
]
PAGE = dict(
num='10', slug='healthcare', kind='lecture', scene='solo', short='10주', chip='10주차', floor='10층 진료 기록실',
scene_line='조원 다섯 명이 건강검진 3만 명 데이터로 차트 한 장씩을 맡아 발표합니다',
title='건강검진 3만 명을 차트 한 장으로', title_en='Industry visualization 3: healthcare check-up data',
subtitle='헬스케어 데이터 × 프롬프트 × 진단표 — 기준선, 평균의 꼬리, 숨은 변수, 이중축 금지, 프롬프트로 앱 만들기',
toc='모의 건강검진 데이터 전처리와 BMI, 시도별 비만율, 공복혈당 분포, 허리둘레와 혈압의 숨은 변수, 흡연 구성과 연도별 추세, 앱 만들기 프롬프트 규칙',
kicker='데이터시각화 · 10주차 · 산업별 데이터 시각화 3 — 헬스케어/의료',
question='혈당 평균이 “정상”이면, 이 집단은 건강한 걸까?',
desc='데이터 시각화 10주차 해설: 국민건강보험공단 건강검진정보와 같은 모양의 모의 데이터 3만 명으로 시도별 비만율 정렬 막대, 공복혈당 히스토그램과 임상 기준선, 허리둘레·혈압 산점도와 연령이라는 숨은 변수, 흡연 구성, 연도별 추세를 그리고, 일부러 나쁜 차트를 만들어 진단한다. 프롬프트로 Colab 앱을 만드는 규칙(들여쓰기·함수·for문 없이, 영어 차트, 중·한 주석)도 다룬다.',
intro='<p>10층 진료 기록실. 오늘은 개인발표입니다. 조원 다섯 명이 같은 건강검진 데이터 3만 명으로 차트 한 장씩을 맡았습니다. 의료 차트는 다른 산업과 하나가 다릅니다. Now What이 <b>사람의 건강 행동</b>으로 이어집니다. 그래서 박사의 경고도 하나 더 늘었습니다. “평균이 위험군을 숨기는 일이 특히 많고, 상관을 인과로 읽는 순간 잘못된 건강 정보가 됩니다.”</p>',
first3=('건강검진 모의 데이터로 다섯 장의 차트(비교·분포·관계·구성·추세)를 그리고, 임상 기준선(공복혈당 100·126, 혈압 140, BMI 25)으로 결론을 씁니다.',
        '의료 차트는 결론이 사람의 행동으로 이어집니다. 평균 하나로 “대체로 정상”이라고 쓰면, 재검이 필요한 1,551명이 사라집니다.',
        '보건소·병원·보험사의 건강 통계 보고, 사내 건강검진 결과 요약, 공공데이터 분석에 그대로 쓰는 순서입니다. 같은 프롬프트를 실제 공공데이터 100만 행에도 쓸 수 있습니다.'),
abbr=[('BMI', 'Body Mass Index, 체질량지수 = 체중(kg) ÷ 키(m)²'), ('mmHg', '혈압 단위, 수은주 밀리미터'), ('mg/dL', '혈당 단위, 혈액 1데시리터당 밀리그램'),
      ('r', '상관계수, −1~1'), ('cp949', '한글 문자 인코딩의 하나. 원본 공공데이터가 이 방식으로 저장된다'), ('hexbin', '점 대신 육각형 타일의 진하기로 밀도를 보여 주는 차트')],
kpis=[('30,000명', '2024년 모의 검진 (2020~2023년 각 2만 명)'), ('41.6%', '비만율 (BMI 25 이상) 전국'), ('5.2%', '공복혈당 126 이상 — 1,551명'), ('0.42 → 0.30~0.33', '허리둘레·혈압 상관, 연령대로 나누면')],
kpi_note='모든 숫자는 수업용 모의 데이터(실제 개인 기록 아님)로 이 페이지에서 계산했습니다. 모의 데이터의 숫자를 실제 통계처럼 인용하지 않습니다.',
hero_talk=[
 ('doc', 'front', '오늘의 질문은 하나입니다. <b>혈당 평균이 정상이면, 이 집단은 건강한가?</b> 히스토그램이 답할 거예요.'),
 ('robo', 'calc', '평균 혈당 93.9! 기준 100보다 낮으니까 모두 건강하네. 끝!'),
 ('fly', 'magnify', '평균 말고 오른쪽 꼬리를 봐. 126 넘는 사람이 몇 명인지.'),
 ('asst', 'firm', '저는 첫 발표예요. 그리기 전에 데이터부터 의심해 볼게요.')],
crew=[('doc', 'front', '심판, 임상 기준선 해설'), ('asst', 'firm', '발표 ① 데이터 점검과 BMI'), ('sia', 'explain', '발표 ② 비교와 분포'), ('x1', 'think', '발표 ③ 관계와 숨은 변수'),
      ('moa', 'report', '발표 ④ 구성과 추세, 함정 재현'), ('x2', 'smile', '발표 ⑤ 프롬프트로 앱 만들기'), ('fly', 'magnify', '초파리 조 조장 — 꼬리 찾기'), ('robo', 'calc', '주판봇 조 조장 — “평균이면 충분해!”')],
recap='9주차: 차트 한 장 = What · So What · Now What 세 문장. 8주차: 나쁜 차트 5함정 T1 축 절단 · T2 맞지 않는 차트 · T3 이중축·눈금 · T4 상관=인과 · T5 장식 과잉.',
prereq=['08', '09'],
why_title='왜 의료 데이터인가 — 차트가 “위험하다/안전하다”를 말한다',
why=[('기준선이 있다', '공복혈당 100(공복혈당장애 시작)·126(당뇨 의심), 수축기 혈압 140, BMI 25. 기준선이 So What을 만들어 줍니다.'),
     ('평균이 위험하다', '평균 한 줄이 위험군을 숨기는 일이 특히 많습니다. 분포부터 봅니다.'),
     ('인과가 위험하다', '“뱃살이 혈압을 올린다”처럼 쓰는 순간 잘못된 건강 정보가 됩니다. 관계만 말합니다.')],
bigpicture='''<div class="tbl"><table><thead><tr><th>발표</th><th>질문</th><th>패턴</th><th>진단 포인트</th></tr></thead><tbody>
<tr><td>① 하루</td><td>데이터는 어떻게 생겼나, 무엇을 지우고 무엇을 만들까</td><td>—</td><td>이상치 · 열 이름 · BMI 근삿값</td></tr>
<tr><td>② 시아</td><td>어느 시도가 비만율이 높나 / 공복혈당은 어떻게 퍼져 있나</td><td>A 비교 · C 분포</td><td>T1 · 정렬 · 평균의 함정</td></tr>
<tr><td>③ X1</td><td>허리둘레와 혈압은 함께 움직이나</td><td>D 관계</td><td>T4 · 숨은 변수(연령)</td></tr>
<tr><td>④ 모아</td><td>흡연 구성은 / 연도별로 달라졌나</td><td>E 구성 · B 시계열</td><td>파이 조건 · T3 · 빠진 연도</td></tr>
<tr><td>⑤ X2</td><td>이 모든 걸 프롬프트 하나로 Colab 앱으로</td><td>—</td><td>들여쓰기·함수·for문 없는 코드</td></tr></tbody></table></div>''',
why_say=('doc', 'board', '같은 데이터를 다섯 가지 질문으로 다시 봅니다. 질문이 바뀌면 차트가 바뀌어요.'),
steps=[
dict(id='lv1', short='점검', title='그리기 전에 네 가지를 의심한다 — 하루의 발표', concept='의료 데이터 점검', en='health data checking and BMI', cid='lab:concept/health-data-check',
 tag='방법: 생김새 → 이상치 → 파생 변수', analogy='진료 전 문진표',
 where='<b>①점검</b> → ②비교와 분포 → ③관계와 숨은 변수 → ④구성·추세·함정 → ⑤앱 만들기',
 situation='describe()로 요약을 뽑았더니 허리둘레 최댓값 999cm, 수축기 혈압 최댓값 400, 공복혈당 최솟값 0이 보입니다. 이대로 평균을 내면 어떻게 될까요?',
 whybox=dict(problem='공공 건강검진 데이터는 원본부터 입력 오류와 빈 값이 섞여 있습니다(모의 데이터도 같은 “더러움”을 넣었습니다).',
             limit='그대로 그리면 평균이 튀고, 열 이름이 해마다 달라 여러 해를 합치면 연도가 비어 버립니다.',
             solution='그리기 전에 <b>네 가지</b>를 의심합니다 — ① 해상도(키 5cm·몸무게 5kg 구간 → BMI는 근삿값) ② 이상치(0·999) ③ 기준선(100·126·140·25) ④ 해석의 한계(표본 통계는 진단이 아님).',
             easy='진료 전에 문진표를 받듯, 그리기 전에 데이터에게 “어디가 이상하니?”를 먼저 묻습니다.'),
 mathbox=dict(q='BMI는 어떻게 계산해요? 왜 “근삿값”이에요?', school='중학교 거듭제곱(제곱), 단위 바꾸기 (cm → m)',
   doc='몸무게를 키(미터)의 제곱으로 나눕니다. 이 데이터는 키를 5cm, 몸무게를 5kg 단위로 묶어 적어서, 실제 값과 조금 다를 수 있어요.',
   rows=[('키(cm) ÷ 100', '센티미터를 미터로 바꾼다'), ('(키 m)²', '키 × 키 — “제곱”으로 읽는다'), ('몸무게 ÷ (키 m)²', 'BMI. 25 이상이면 비만으로 분류(이 수업의 기준)')],
   try_='키 165cm, 몸무게 80kg → 1.65 × 1.65 = 2.7225 → 80 ÷ 2.7225 ≈ <b>29.4</b> (25 이상)<br>실제 키가 167cm였다면 80 ÷ 2.7889 ≈ 28.7 — 구간 기록이라 개인 판정이 아니라 <b>집단 비율</b>에만 쓴다',
   comment='5cm 차이로 BMI가 0.7이나 바뀌네요. 그래서 “환자 수”가 아니라 “위험군 비율”이라고 써야 하는군요.'),
 pair=(('일상으로 치면', '체중계 눈금이 5kg 단위라면 “내가 정확히 몇 kg”이라고는 못 해도 “70kg대 사람이 몇 %”라고는 말할 수 있습니다.'),
       ('데이터에서는', '2024년 파일 3만 행 기준 이상치 — 허리둘레 50~150 밖 12건, 수축기 혈압 70~250 밖 7건, 공복혈당 50~500 밖 12건. 빈 값 — 허리둘레 314, 혈압 159, 혈당 254, 흡연 79건. 2020·2021년 파일은 열 이름이 <code>age_code</code>·<code>blood_glucose</code>로 다릅니다.')),
 talk=[('asst', 'firm', '“아직 그래프는 그리지 마”라는 한 줄을 넣어서 요약부터 받았어요. 아래 버튼으로 전후를 비교해 볼게요.'),
       ('robo', 'happy', '999는 큰 숫자니까 오히려 좋은 거 아니야? 데이터가 많아 보여!'),
       ('fly', 'clip', '허리둘레 999cm인 사람은 없어. 입력 오류야. 범위는 사람이 정하고, 몇 건 지웠는지 캡션에 적어.')],
 panel='''<div class="ctrl"><button type="button" class="bt" id="w10raw" aria-pressed="true">원본 요약</button><button type="button" class="bt" id="w10cl">범위 밖 값을 비운 뒤</button></div>
<div id="w10t"></div><div class="insight" id="w10o" aria-live="polite"></div>''',
 panel_title='직접 해 보기 — 범위 밖 값을 비우기 전과 후',
 sim='이상치 처리 전후 요약',
 explain='<p>원자료의 모의 데이터는 공공데이터포털 「국민건강보험공단_건강검진정보」(연도별 약 100만 명)와 <b>같은 열 구조</b>로 만든 수업용 데이터입니다. 원자료 슬라이드는 한글 열 이름과 cp949 인코딩을 쓰지만, 받은 최신 파일(재생성판)은 영어 열 이름(<code>sido_code</code>, <code>fasting_glucose</code> 등)과 코드표(codebook.csv)를 씁니다. 이 페이지는 최신 파일 기준입니다. 코드표의 시도·연령대 번호는 AI가 추측하게 두지 말고 프롬프트에 그대로 붙여 넣습니다.</p>',
 docline='제거 기준은 <b>내가</b> 정합니다. AI가 정하게 두면 이유를 설명할 수 없습니다. “범위를 50~500으로 잡은 이유”를 한 문장으로 말할 수 있어야 합니다.',
 limit='데이터를 정리했습니다. 이제 첫 질문 — 어느 시도가 비만율이 높은가, 그리고 혈당은 어떻게 퍼져 있는가.', limit_label='아직 아무 질문에도 답하지 않음',
 quiz=[dict(q='키 160cm, 몸무게 64kg의 BMI는?', o=['약 20', '약 25', '약 40', '약 2.5'], a=1, why='1.6 × 1.6 = 2.56, 64 ÷ 2.56 = 25.0.'),
       dict(q='이 데이터의 BMI를 개인 판정이 아니라 집단 비율에만 쓰는 이유는?', o=['BMI가 의미 없어서', '키·몸무게가 5cm·5kg 구간으로 기록되어 근삿값이라서', '3만 명이 너무 많아서', '영어 열 이름이라서'], a=1, why='구간 기록이라 개인의 정확한 BMI가 아닙니다.')]),
dict(id='lv2', short='비교·분포', title='비교와 분포 — 정렬 막대와 오른쪽 꼬리 (시아의 발표)', concept='기준선이 있는 분포 읽기', en='comparison and distribution with clinical thresholds', cid='lab:concept/clinical-thresholds',
 tag='방법: 정렬 · 0축 · 기준선 / 평균 + 기준선 두 개', analogy='반 평균과 낙제생',
 where='①점검 → <b>②비교와 분포</b> → ③관계와 숨은 변수 → ④구성·추세·함정 → ⑤앱 만들기',
 situation='시도 17곳의 비만율 차이가 35%에서 51% 사이라 AI가 X축을 30%부터 잘라 그렸습니다. 그리고 공복혈당 평균은 93.9 — 기준 100보다 낮습니다. 두 차트 모두 “무엇을 숨기고” 있을까요?',
 whybox=dict(problem='시도별 차이가 작으면 축을 자르고 싶어지고, 평균이 기준 아래면 “정상”이라고 쓰고 싶어집니다.',
             limit='축을 자르면 막대 길이가 2~3배씩 차이 나 보이고(T1), 평균 한 줄은 오른쪽 꼬리(고혈당 위험군)를 숨깁니다.',
             solution='비교는 <b>정렬 · 0축 · 전국 평균선</b>, 분포는 <b>히스토그램 + 평균선 + 임상 기준선(100·126)</b>과 “126 이상 비율”을 글자로.',
             easy='반 평균이 70점이어도 낙제생이 다섯 명일 수 있습니다. 평균만 보는 담임은 그 다섯 명을 놓칩니다.'),
 mathbox=dict(q='“126 이상이 5.2%”는 몇 명이에요? 평균은 왜 중앙값보다 커요?', school='초등 백분율, 중학교 대푯값(평균·중앙값)',
   doc='비율에 전체 수를 곱하면 사람 수가 나와요. 그리고 오른쪽에 큰 값이 꼬리처럼 있으면 평균만 그쪽으로 끌려가요. 중앙값은 한가운데 순서라 덜 끌립니다.',
   rows=[('126 이상 인원 ÷ 전체 인원', '고혈당 의심 비율'), ('평균 > 중앙값', '오른쪽으로 꼬리가 긴(right-skewed) 분포의 신호'), ('100~125', '공복혈당장애 구간')],
   try_='혈당 값이 있는 29,734명 중 126 이상 <b>1,551명</b> → 1,551 ÷ 29,734 ≈ <b>5.2%</b><br>평균 <b>93.9</b> &gt; 중앙값 <b>90</b> → 오른쪽 꼬리<br>100~125 구간은 <b>10.8%</b>',
   comment='평균만 보면 “정상”, 그런데 1,551명이 재검 대상이에요. 3만 명 중 5%는 작은 숫자가 아니네요.'),
 pair=(('비교 — 시도별 비만율', '가로 막대(17개라 세로 막대면 이름이 겹침) · 큰 값부터 정렬 · X축 0부터 · 전국 평균 점선 · 1위 하나만 앰버.'),
       ('분포 — 공복혈당', 'X축 50~300 mg/dL, 구간 폭 5 · 평균 점선(앰버) · 100과 126에 회색 기준선 · 126 이상 비율을 글자로 · 제목에 “분포”.')),
 talk=[('sia', 'explain', '시도별 막대와 혈당 히스토그램을 차례로 보여 드릴게요. 축을 잘랐을 때와 비교도 할게요.'),
       ('robo', 'chart', '축을 30%부터 자르면 제주가 압도적이잖아! 극적이야!'),
       ('fly', 'arms', '제주 50.9%, 대전 35.0%. 1.45배야. 잘린 축에선 몇 배로 보이는지 봐.'),
       ('x3', 'think', '혈당 히스토그램은 126 오른쪽이 얇지만 길어요.')],
 panel='''<div class="chips" id="w10a"><button type="button" class="bt" data-k="bar" aria-pressed="true">시도별 비만율 (0축)</button><button type="button" class="bt" data-k="cut">같은 차트, 축 30%부터 (T1 예시)</button><button type="button" class="bt" data-k="glu">공복혈당 분포</button></div>
<div id="w10av" class="viz"></div><div class="insight" id="w10ao" aria-live="polite"></div>''',
 panel_title='직접 해 보기 — 비교와 분포',
 sim='시도별 비만율·혈당 분포',
 explain='<p>원자료의 “정답 확인”표는 전국 비만율 약 38%, 시도 약 32~49%로 적었지만, 받은 모의 데이터(2024년, 3만 명)로 계산하면 <b>전국 41.6%, 시도 35.0%(대전)~50.9%(제주)</b>입니다. 이 페이지는 계산값으로 바꿉니다. 순서(제주·강원 상위, 서울·대전 하위)는 원자료와 같습니다. 혈당은 원자료 기대값과 일치합니다(평균 약 94, 중앙값 90, 126 이상 약 5%, 100~125 약 11%).</p><p>3문장 예: <b>What</b> 제주의 비만율이 50.9%로 가장 높다. <b>So What</b> 전국 평균 41.6%보다 9.3%p 높고, 최하위 대전(35.0%)과는 15.9%p 차이. <b>Now What</b> 상위 3개 시도를 다음 분석(연령·성별 구성 차이)의 우선 대상으로 — 시도 차이에는 연령 구성 차이가 섞여 있다(다음 단계의 숨은 변수).</p>',
 docline='의료 차트의 So What은 <b>임상 기준선</b>에서 나옵니다. 평균선 하나보다 기준선 두 개(100·126)가 더 많은 것을 말합니다.',
 limit='분포와 비교를 봤습니다. 다음 질문은 “허리둘레와 혈압이 함께 움직이는가” — 함께 움직인다면, 그것은 원인일까요?', limit_label='두 변수의 관계와 원인을 구분하지 않음',
 quiz=[dict(q='혈당 평균 93.9, 중앙값 90일 때 분포 모양은?', o=['좌우 대칭', '오른쪽으로 꼬리가 길다', '왼쪽으로 꼬리가 길다', '알 수 없다'], a=1, why='평균이 중앙값보다 크면 오른쪽의 큰 값들이 평균을 끌어올린 것입니다.'),
       dict(q='시도별 비만율 막대에서 X축을 30%부터 시작하면 걸리는 함정은?', o=['T1 축 절단', 'T2 맞지 않는 차트', 'T4 상관=인과', 'T5 장식 과잉'], a=0, why='차이가 작아 AI가 축을 자르는 경우가 많습니다. 0부터 다시 그립니다.')]),
dict(id='lv3', short='숨은 변수', title='관계와 숨은 변수 — 허리둘레가 혈압을 올리나, 나이가 둘 다 올리나 (X1의 발표)', concept='상관과 숨은 변수', en='correlation and confounding by age', cid='lab:concept/confounding',
 tag='방법: 전체 산점도 → 연령대별 작은 패널', analogy='키 큰 아이와 어휘력',
 where='①점검 → ②비교와 분포 → <b>③관계와 숨은 변수</b> → ④구성·추세·함정 → ⑤앱 만들기',
 situation='허리둘레와 수축기 혈압의 상관계수가 0.42입니다. 주판봇이 제목을 “뱃살이 혈압을 올린다!”로 달았습니다. 같은 데이터를 연령대별로 나누면 상관은 어떻게 될까요?',
 whybox=dict(problem='두 값이 함께 오르면 한쪽이 다른 쪽의 원인처럼 보입니다.',
             limit='나이가 들수록 허리둘레도 늘고 혈압도 오르면, 나이(숨은 변수)가 두 값을 함께 움직여 전체 상관을 부풀립니다.',
             solution='같은 산점도를 <b>연령대별 작은 패널</b>(small multiples)로 나눠 r을 비교합니다. 줄어들면, 전체 상관의 일부는 연령 몫입니다. 결론은 “관계가 있다/약해진다”까지만.',
             easy='초등학생은 키가 클수록 아는 낱말이 많습니다. 키가 어휘력을 키운 게 아니라, 학년(나이)이 둘 다 키운 겁니다.'),
 mathbox=dict(q='상관계수 0.42와 0.33은 얼마나 달라요?', school='중학교 일차함수의 기울기, 고등학교 확률과 통계의 상관관계',
   doc='상관계수 r은 −1부터 1 사이예요. 0에 가까우면 점이 흩어져 있고, 1에 가까우면 오른쪽 위로 한 줄에 가깝게 놓여요. 원인이 있다는 뜻은 담겨 있지 않습니다.',
   rows=[('r > 0', '한쪽이 클 때 다른 쪽도 큰 경향'), ('r ≈ 0', '함께 움직이는 경향이 거의 없음'), ('0.42 → 0.30~0.33', '연령대를 고정하자 관계가 약해짐 = 일부는 나이 몫')],
   try_='전체 r = <b>0.42</b><br>20~39세 0.33 · 40대 0.32 · 50대 0.30 · 60세 이상 0.33<br>→ 같은 연령대 안에서는 약 <b>0.30~0.33</b>으로 줄어든다',
   comment='관계가 없어진 건 아니고 약해졌네요. 그래서 “원인”이 아니라 “관계가 있다, 연령을 고려하면 약해진다”까지만 쓰는 거군요.'),
 pair=(('전체 산점도', '무작위 표본(이 페이지는 700명), 점은 투명하게 작게, 회귀선 앰버, 혈압 140에 회색 점선, r을 그림 안에. 제목·해석에 “때문에·원인·일으킨다”를 쓰지 않는다.'),
       ('점이 줄무늬로 찍히는 이유', '혈압은 정수, 허리둘레는 소수 한 자리라 같은 값이 많아 점이 겹쳐 줄처럼 보입니다. 오류가 아니라 데이터의 해상도입니다. 수만 개면 hexbin(육각형 타일의 진하기로 밀도)으로 바꿉니다.')),
 talk=[('x1', 'think', '전체 산점도와 연령대별로 색을 나눈 그림을 번갈아 보여 드릴게요.'),
       ('robo', 'wow', '0.42면 꽤 강한데? 뱃살 빼면 혈압이 바로 내려가겠어!'),
       ('fly', 'magnify', '연령대별 버튼을 눌러 봐. r이 줄어들면 나이가 한몫한 거야. 그리고 이 데이터로는 원인을 말할 수 없어.'),
       ('doc', 'think', '결과가 어떻게 나오든 결론 문장은 “관계가 있다 / 약해진다”까지입니다.')],
 panel='''<div class="chips" id="w10s"><button type="button" class="bt" data-k="all" aria-pressed="true">전체 (r 하나)</button><button type="button" class="bt" data-k="age">연령대별 색 · r 비교</button><button type="button" class="bt" data-k="mean">연령대별 평균 (숨은 변수 보기)</button></div>
<div id="w10sv" class="viz"></div><div class="insight" id="w10so" aria-live="polite"></div>''',
 panel_title='직접 해 보기 — 숨은 변수 찾기',
 sim='허리둘레·혈압 숨은 변수 실험',
 explain='<p>원자료의 기대값(“전체 r 약 0.4, 연령대로 나누면 줄어듦”)과 계산이 일치합니다. 연령대 그룹은 원자료대로 20-39 · 40-49 · 50-59 · 60+ 네 개입니다. 각 패널의 X·Y축 범위를 <b>똑같이</b> 맞춰야 패널끼리 비교가 정직합니다.</p>',
 aicheck='<p>AI가 산점도 아래에 “허리둘레가 1cm 늘 때마다 혈압이 오르므로, 허리둘레를 줄이면 혈압이 내려갑니다”라고 썼습니다. <b>점검</b>: ① 이 데이터는 한 시점의 관찰이다 — 한 사람의 변화를 따라간 것이 아니다 ② 연령을 나누면 관계가 약해진다 — 숨은 변수가 있다 ③ 의료 행동 권고는 이 데이터가 감당할 수 없는 결론이다. 고친 문장: “허리둘레와 수축기 혈압 사이에 양의 관계(r ≈ 0.42)가 있고, 연령대별로 보면 약해진다(r ≈ 0.30~0.33). 인과는 이 데이터로 말할 수 없다.”</p>',
 docline='함께 움직임은 원인이 아닙니다. <b>숨은 변수(연령)로 나눠 보면</b> 관계의 일부가 어디서 왔는지 보입니다.',
 limit='관계까지 봤습니다. 남은 질문은 두 가지 — 흡연 구성은 성별로 어떻게 다른가, 그리고 5년 동안 무엇이 바뀌었나. 여기서 이중축이라는 마지막 함정을 만납니다.', limit_label='구성과 시간 변화, 이중축 함정이 남음',
 quiz=[dict(q='전체 r 0.42가 연령대별로 0.30~0.33으로 줄었다. 가장 알맞은 해석은?', o=['허리둘레가 혈압의 원인이다', '관계가 사라졌다', '전체 관계의 일부는 연령이라는 숨은 변수 몫이다', '데이터가 틀렸다'], a=2, why='관계는 남아 있지만 약해졌습니다. 일부는 연령이 두 값을 함께 움직인 결과입니다.'),
       dict(q='수만 명의 산점도에서 점이 뭉개질 때 쓰는 차트는?', o=['파이', 'hexbin(육각 밀도)', '3D 막대', '레이더'], a=1, why='점 대신 육각형 타일의 진하기로 밀도를 보여 줍니다.')]),
dict(id='lv4', short='구성·추세', title='구성과 추세, 그리고 일부러 만드는 나쁜 차트 (모아의 발표)', concept='구성·시계열과 함정 재현', en='composition time series and reproducing traps', cid='lab:concept/reverse-learning',
 tag='방법: 조건부 파이 → 100% 누적 막대 · 두 패널 꺾은선 · 나쁜 프롬프트 → 진단 → 고치는 프롬프트', analogy='위조지폐 감별 교육',
 where='①점검 → ②비교와 분포 → ③관계와 숨은 변수 → <b>④구성·추세·함정</b> → ⑤앱 만들기',
 situation='비만율과 “공복혈당 126 이상 비율”을 한 그래프의 왼쪽·오른쪽 축에 그렸더니, 두 선이 나란히 오릅니다. 정말 둘 다 올랐을까요?',
 whybox=dict(problem='두 지표를 한 그림에 넣고 싶어서 이중축을 쓰기 쉽습니다.',
             limit='이중축은 각 축 범위를 마음대로 정할 수 있어서, 평평한 선도 오르는 선처럼 보이게 만들 수 있습니다(T3).',
             solution='두 지표는 <b>위아래 두 패널</b>, 각 Y축 0부터, 연도 간격 고르게, 빠진 해는 평균으로 메우지 않고 비워 둡니다. 그리고 <b>나쁜 차트를 일부러 만들어</b> 진단해 봅니다(차트에 “T○ 예시” 표시).',
             easy='위조지폐를 직접 만져 본 은행원이 위조지폐를 잘 찾습니다. 함정을 직접 만들어 봐야 남의 차트에서 보입니다.'),
 pair=(('구성 — 흡연', '범주 3개(비흡연·과거·현재) ≤ 5, 한 사람이 한 범주 → 합 100% → 파이 <b>조건부 허용</b>. 그런데 질문이 “남녀 비교”라면 100% 누적 가로 막대 두 줄이 더 빨리 읽힙니다(각도 비교보다 길이 비교).'),
       ('추세 — 5년', '다섯 해 파일을 합칠 때 열 이름을 맞추는 코드를 넣습니다(안 맞추면 2020·2021이 빈다). 비만율은 35.5% → 41.6%로 늘었고, 혈당 126 이상 비율은 5.0~5.4%로 거의 평평합니다.')),
 talk=[('moa', 'report', '흡연 구성과 5년 추세를 준비했어요. 그리고 이중축 스위치도 만들었어요.'),
       ('robo', 'happy', '이중축으로 그리니까 비만도 고혈당도 같이 쑥쑥 올라! 대단한 발견이야!'),
       ('fly', 'arms', '오른쪽 축 범위를 4.9~5.5로 좁혀 놨잖아. 두 패널로 나눠서 각각 0부터 봐.'),
       ('sia', 'think', '변화가 작아 보이는 게 정직한 결과일 수도 있네요.')],
 panel='''<div class="chips" id="w10c"><button type="button" class="bt" data-k="pie" aria-pressed="true">흡연 — 파이 두 개</button><button type="button" class="bt" data-k="stack">흡연 — 100% 누적 막대</button><button type="button" class="bt" data-k="twin">5년 추세 — 이중축 (T3 예시)</button><button type="button" class="bt" data-k="two">5년 추세 — 두 패널</button><button type="button" class="bt" data-k="t1">혈압 남녀 — 축 115부터 (T1 예시)</button></div>
<div id="w10cv" class="viz"></div><div id="w10cv2" class="viz" hidden></div><div class="insight" id="w10co" aria-live="polite"></div>''',
 panel_title='직접 해 보기 — 구성, 추세, 함정 재현',
 sim='구성·추세·함정 재현 실험',
 explain='<p>원자료의 기대값과 비교: 흡연 — 현재 흡연 남 약 30% / 여 약 5% → 계산값 <b>남 29.9% / 여 4.9%</b>(일치). 추세 — 원자료 “2020 약 33% → 2024 약 38%” → 계산값 <b>35.5% → 41.6%</b>(방향은 같고 값이 다름, 이 페이지는 계산값으로 바꿉니다). 고혈당 비율 약 5%로 평평 → <b>5.0~5.4%</b>(일치). 남녀 평균 수축기 혈압 차이는 <b>6.3mmHg</b>(126.7 대 120.4, 약 5%)로, 원자료의 T1 재현 예시 “6mmHg 차이를 압도적 차이로 만들기”와 같습니다.</p><p>원자료의 <b>“이런 결과가 나왔다면 함정”</b>표: 시도 막대가 2~3배씩 차이 → T1 / 혈당 평균이 50대거나 최댓값 999 → 전처리 누락 / 연도 그래프에 2020·2021이 빔 → 열 이름 불일치 / 비만율과 고혈당이 같이 오르는 것처럼 보임 → T3 이중축 / 해석에 “허리둘레가 혈압을 높인다” → T4.</p>',
 docline='두 지표는 이중축 대신 <b>두 패널</b>로. 이중축은 사실이 아닌 일(고혈당 급증)을 만들어 냅니다.',
 limit='다섯 장의 차트를 손으로 하나씩 받았습니다. 마지막 발표는 이 흐름 전체를 <b>프롬프트 하나</b>로 Colab 앱처럼 만드는 규칙입니다.', limit_label='한 번에 돌아가는 코드로 묶지 않음',
 quiz=[dict(q='흡연 구성 파이가 “조건부 허용”인 이유로 맞지 <b>않는</b> 것은?', o=['범주가 3개(5개 이하)', '한 사람이 한 범주에만 속함(합 100%)', '파이가 가장 정확한 차트라서', '질문이 구성 비율이라서'], a=2, why='파이는 정확도가 높은 차트가 아닙니다. 조건을 만족할 때만 허용됩니다. 비교가 목적이면 막대가 이깁니다.'),
       dict(q='5년 추세에서 2020·2021년 값이 비어 있다. 가장 먼저 의심할 것은?', o=['그해 검진이 없었다', '연도별 열 이름이 달라 합칠 때 맞추지 않았다', '차트 색', '이중축'], a=1, why='2020·2021 파일은 age_code·blood_glucose처럼 열 이름이 다릅니다.')]),
dict(id='lv5', short='앱 만들기', title='프롬프트로 앱 만들기 — 들여쓰기·함수·for문 없는 코드 (X2의 발표)', concept='앱 만들기 프롬프트 규칙', en='prompt rules for a beginner-readable Colab app', cid='lab:concept/app-prompt-rules',
 tag='방법: 데이터 일부 기억시키기 → 업로드 구조 → 영어 차트·중한 주석 → 금지 규칙 셋', analogy='요리 레시피 카드',
 where='①점검 → ②비교와 분포 → ③관계와 숨은 변수 → ④구성·추세·함정 → <b>⑤앱 만들기</b>',
 situation='X2가 처음 받은 AI 코드에는 함수(def)가 다섯 개, for문이 세 개, 들여쓰기가 네 겹이었습니다. 처음 배우는 친구가 이 코드에서 오류가 나면, 어디부터 봐야 할까요?',
 whybox=dict(problem='AI는 “잘 짜인” 코드를 주려고 함수와 반복문으로 감쌉니다. 전문가에게는 좋은 코드입니다.',
             limit='처음 배우는 사람에게는 위에서 아래로 읽히지 않습니다. 오류가 함수 안 반복문 안에서 나면 어느 줄이 문제인지 찾기 어렵습니다.',
             solution='프롬프트에 <b>규칙 네 가지</b>를 넣습니다 — ① 데이터 일부를 먼저 보여 주고 기억시키기 ② Colab 업로드로 직접 불러오는 구조 ③ 차트 제목·축 제목·범례는 영어, 주석은 중국어와 한국어로 자세히 ④ 들여쓰기 금지 · 함수 정의(def) 금지 · for문 금지.',
             easy='레시피 카드는 “1. 물을 끓인다 2. 면을 넣는다”처럼 위에서 아래로 한 줄씩입니다. “면 넣기 함수를 3번 반복” 같은 레시피는 없습니다.'),
 pair=(('왜 영어 차트, 중·한 주석인가', 'Colab은 한글·중국어 글꼴을 따로 설치해야 해서 차트 글자가 □□□로 깨지기 쉽습니다. 차트 글자는 영어로 두면 깨지지 않고, 코드를 읽는 사람(한국·중국 학생)을 위한 설명은 주석에 두 언어로 적습니다.'),
       ('왜 들여쓰기·함수·for문 금지인가', '한 줄이 한 가지 일을 하면, 셀을 위에서부터 한 줄씩 실행하며 결과를 확인할 수 있습니다. 반복이 필요하면 pandas의 <code>groupby</code>·<code>between</code>처럼 표 전체에 한 번에 적용하는 명령으로 바꿉니다.')),
 body='''<div class="grid2"><div class="prompt"><span class="lang">한</span>1) 다음을 잘 기억해라. 이것은 엑셀(CSV) 파일의 일부이다.
year,id,sido_code,sex_code,age_group_code,height_5cm,weight_5kg,waist_cm,systolic_bp,diastolic_bp,fasting_glucose,total_cholesterol,smoking_status,drinking
2024,1,43,1,14,165,80,99.8,155,93,137,145,3,1
2024,2,47,2,11,150,50,76.3,121,73,98,153,1,1
(…5줄)
2) 나는 이것을 파이썬으로 불러온다. COLAB을 쓸 것이고 파일을 UPLOAD 기능으로 직접 불러오는 구조이다.
3) 각 데이터에 적절한 차트와 그래프, 그리고 분석을 진행할 것이다. 차트·표의 제목, 축 제목, 범례는 모두 영어로, 주석은 아주 자세하게 중국어와 한글로 기재한다.
4) 코드 작성 시 들여쓰기 금지. DEFINE 함수 금지. FOR문 금지.</div>
<div class="prompt"><span class="lang">中</span>1) 请注意以下事项。这是 Excel (CSV) 文件的一部分。
（同上 CSV 片段）
2) 我会将其导入 Python。我打算使用 Colab，并通过其上传功能直接导入该文件。
3) 我将针对每个数据集制作相应的图表，并进行必要的分析。由于此项工作在 Colab 中完成，所有图表标题、坐标轴标签及图例均采用英文，而详细注释则会同时提供中文和韩文版本。
4) 编写代码时禁止缩进，禁止定义函数，禁止使用 for 循环。</div></div>
<p style="font-size:14px;color:#5b6874">원자료(10주차 프롬프트)의 문장을 그대로 옮겼습니다. 원래 메시지의 CSV 일부는 줄바꿈 없이 붙어 있었는데, 이 페이지에서는 읽기 쉽게 열 이름 줄과 데이터 줄로 나눴습니다. 중국어 4)는 한국어 원문에 맞춰 이 페이지에서 번역해 넣었습니다.</p>''',
 talk=[('x2', 'smile', '규칙을 넣고 다시 받은 코드는 위에서 아래로 한 줄씩이에요. 아래 접힌 상자에서 볼 수 있어요.'),
       ('robo', 'meh', '함수 없이 코드를 쓰면 길어지잖아. 프로처럼 보이지 않는데?'),
       ('fly', 'point', '이 수업의 목표는 프로처럼 보이는 코드가 아니라 <b>내가 설명할 수 있는</b> 코드야. 설명 못 하면 감점이야.'),
       ('asst', 'spark', '한 줄씩 실행하니까 어디서 오류가 났는지 바로 보여요!')],
 panel='<div id="w10rule"></div>',
 panel_title='직접 해 보기 — 이 코드 줄은 규칙을 지켰을까',
 sim='앱 만들기 규칙 점검 게임',
 explain='<p>규칙을 지킨 코드의 특징: ① 모든 줄이 왼쪽 끝에서 시작한다 ② <code>def</code>와 <code>for</code>가 한 번도 나오지 않는다 ③ 반복은 <code>groupby</code>(묶어서 한 번에), <code>between</code>(범위를 한 번에), <code>.plot()</code>(표 전체를 한 번에)으로 대신한다 ④ 차트 글자는 영어(<code>set_title(\'Obesity rate by province\')</code>) ⑤ 주석은 <code># [KO] … / [ZH] …</code>. <code>if</code>문도 들여쓰기가 필요하므로 같은 이유로 쓰지 않고, 조건은 <code>df.loc[조건, 열]</code>처럼 한 줄로 씁니다.</p>',
 aicheck='<p>AI에게 규칙 네 가지를 보냈는데도 답에 <code>for col in cols:</code>가 섞여 왔습니다. 확인 질문: “방금 코드에 for문이 있어. 금지 규칙을 다시 지켜서, 같은 일을 pandas 명령 한 줄로 바꿔 줘.” 규칙을 지켰다는 AI의 말보다 <b>코드 안에서 def·for·들여쓰기를 직접 찾아보는 것</b>이 확인입니다. 이 페이지의 예시 코드도 Python으로 문법 검사를 했습니다.</p>',
 docline='좋은 코드의 기준은 상황마다 다릅니다. 이 수업에서는 <b>처음 보는 사람이 위에서 아래로 따라 읽을 수 있는 코드</b>가 좋은 코드입니다.',
 limit='헬스케어 층 끝. 다음 층(11층)에서는 시간·장소가 들어간 도시·물류 데이터 — 히트맵과 파레토 차트, 그리고 “한 번에 묻지 말고 이어 묻는” 프롬프트 사슬을 배웁니다.', limit_label='시간·장소 데이터와 이어 묻기는 아직',
 code=_CODE, code_title='규칙을 지킨 Colab 코드로 보면 (시도별 비만율 한 장)',
 quiz=[dict(q='다음 중 “들여쓰기·함수·for문 금지” 규칙을 지킨 줄은?', o=['for c in cols:', 'def clean(df):', "rate = df.groupby('sido_code')['obese'].mean()", '    df = df.dropna()'], a=2, why='groupby는 표 전체를 한 번에 묶어 계산합니다. 반복문 없이 한 줄로 끝납니다.'),
       dict(q='Colab 차트의 제목·축·범례를 영어로 쓰게 한 가장 큰 이유는?', o=['영어가 더 멋있어서', '한글·중국어 글꼴이 없으면 □□□로 깨지기 쉬워서', '채점이 영어라서', 'AI가 영어만 알아서'], a=1, why='차트 글자는 깨지지 않게 영어로, 설명은 주석에 두 언어로 둡니다.')]),
],
duel=dict(q='재검 안내 대상은 몇 명인가', step=1,
 intro='2024년 모의 검진 3만 명. 주판봇 조는 “공복혈당 평균 93.9, 기준 100 미만 — 이 집단은 정상”이라고 발표하고, 초파리 조는 히스토그램에서 126 이상 구간을 셉니다. 심판 박사는 <b>재검 안내가 필요한 사람(126 이상)을 몇 명 찾았는가</b>로 판정합니다.',
 fly_pick='히스토그램 + 기준선 126', fly_line='평균 말고 꼬리를 세. 126 오른쪽이 몇 명이야?',
 robo_pick='평균 한 줄', robo_line='평균 93.9! 기준 아래니까 다들 괜찮아!',
 metric='찾아낸 재검 대상 인원',
 run='var H=HOBJ;return {fly:H.glu.n126,robo:0,flyTxt:LAB.nf(H.glu.n126)+"명",roboTxt:"0명",p:H.glu.ge126,n:H.glu.n};',
 announce='return "혈당 값이 있는 "+LAB.nf(r.n)+"명 중 126 이상은 "+r.flyTxt+"("+r.p+"%)예요. 평균만 본 주판봇 조는 재검 대상을 한 명도 찾지 못했어요.";',
 verdict='if(res==="F")return "초파리 조 승. 평균은 꼬리를 숨긴다. 의료 차트에서 숨겨진 꼬리는 <b>사람</b>이다. Now What: 평균 기반 메시지 대신 “126 이상 구간” 대상 재검 안내를 먼저.";return "결과를 다시 보자.";',
 after='<p style="font-size:14px;color:#5b6874">인원은 모의 데이터에서 직접 센 값입니다. 모의 데이터의 숫자를 실제 통계처럼 인용하지 않습니다.</p>'),
summary='''<div class="tbl"><table><thead><tr><th>차트</th><th>질문</th><th>패턴</th><th>피한 함정</th><th>계산 결과 (모의 데이터)</th></tr></thead><tbody>
<tr><td>시도별 비만율</td><td>어디가 높나</td><td>A 정렬 가로 막대</td><td>T1, 정렬 누락</td><td>제주 50.9% ~ 대전 35.0%, 전국 41.6%</td></tr>
<tr><td>공복혈당 분포</td><td>어떻게 퍼졌나</td><td>C 히스토그램 + 기준선</td><td>평균 착시</td><td>평균 93.9 · 중앙값 90 · 126 이상 5.2%(1,551명)</td></tr>
<tr><td>허리둘레–혈압</td><td>함께 움직이나</td><td>D 산점도(hexbin)</td><td>T4</td><td>r 0.42 → 연령대별 0.30~0.33</td></tr>
<tr><td>흡연 구성</td><td>비중은</td><td>E 파이 / 100% 누적 막대</td><td>T2</td><td>현재 흡연 남 29.9% · 여 4.9%</td></tr>
<tr><td>연도별 추이</td><td>변했나</td><td>B 꺾은선 두 패널</td><td>T3</td><td>비만율 35.5% → 41.6%, 고혈당 5.0~5.4%로 평평</td></tr></tbody></table></div>
<p><b>오늘 가져갈 것</b>: ① 의료 차트의 So What은 임상 기준선에서(100 · 126 · 140 · BMI 25) ② 평균은 꼬리를 숨긴다 → 분포부터 ③ 함께 움직임은 원인이 아니다 → 숨은 변수(연령)로 나눠 본다 ④ 두 지표는 이중축 대신 두 패널 ⑤ AI는 그리고, 진단과 결론은 사람이 한다. 오늘의 프롬프트는 실제 공공데이터 100만 행에도 그대로 통합니다 — 바꿀 것은 파일 이름, 행 수 안내, 산점도는 반드시 표본 추출 또는 hexbin.</p>''',
outro=[('doc', 'judge', '개인발표 다섯 개 통과. 오늘의 핵심 장면은 둘이다. 1,551명의 꼬리, 그리고 이중축이 만든 <b>가짜 급증</b>.'),
       ('asst', 'proud', '그리기 전에 999를 찾아낸 게 제일 뿌듯해요.'),
       ('x1', 'joy', '연령대로 나누니까 0.42가 0.3대로 줄었어요. 원인이라고 안 쓰길 잘했어요.'),
       ('robo', 'sigh', '평균 93.9로 “모두 건강”이라고 했던 거… 1,551명에게 미안하네.'),
       ('x2', 'proud', '들여쓰기 없는 코드, 위에서 아래로 한 줄씩 다 설명할 수 있어요.')],
next_note='<p>다음 층(11층)에서는 시간대별 교통량과 배송 기록으로 “언제·어디서·얼마나”를 읽고, 프롬프트를 다섯 번 이어 물어 히트맵과 파레토 차트를 완성합니다.</p>',
refs=[dict(id='w10_slides', type='document', title='산업별 데이터시각화 · 헬스케어/의료 — 건강검진 3만 명을 차트 한 장으로 (40쪽)', who='안상선', issued={'date-parts': [[2026, 11, 12]]}, role='primary'),
      dict(id='mock', type='dataset', title='건강검진 모의 데이터 health_2020~2024.csv · codebook.csv (재생성판)', who='강의 자료', issued={'date-parts': [[2026, 11, 5]]}, role='data', URL='https://github.com/adminmrobo/Data_visuialization_lecture_lab/tree/main/data/raw'),
      dict(id='w10_prompt', type='document', title='10주차 프롬프트 — 프롬프트로 앱 만들기 (한·중)', who='안상선', role='primary'),
      dict(id='nhis', type='dataset', title='국민건강보험공단_건강검진정보 (모의 데이터의 원형)', who='공공데이터포털', URL='https://www.data.go.kr/', role='background')],
facts=[('F1', '2024년 모의 데이터 3만 명의 비만율(BMI 25 이상)은 41.6%이고, 시도별로 35.0%(대전)~50.9%(제주)다.', '계산', 'mock', 'lv2', '시도별 obese 평균'),
       ('F2', '공복혈당 평균은 93.9, 중앙값은 90, 126 이상은 5.2%(1,551명), 100~125는 10.8%다.', '계산', 'mock', 'lv2', 'fasting_glucose'),
       ('F3', '허리둘레와 수축기 혈압의 상관은 0.42이고 연령대별로는 0.30~0.33이다.', '계산', 'mock', 'lv3', '연령대 4그룹'),
       ('F4', '현재 흡연 비율은 남 29.9%, 여 4.9%다.', '계산', 'mock', 'lv4', 'smoking_status'),
       ('F5', '비만율은 2020년 35.5%에서 2024년 41.6%로 늘었고, 혈당 126 이상 비율은 5.0~5.4%다.', '계산', 'mock', 'lv4', '연도별 파일'),
       ('F6', '원자료의 기대값(전국 비만율 약 38%, 2020 약 33%)은 받은 재생성판 데이터의 계산값과 다르다.', '계산', 'w10_slides', 'lv2', 'S36 정답 확인')],
gloss={'BMI': ('BMI', '지표', '체중(kg) ÷ 키(m)². 이 수업에서는 25 이상을 비만으로 분류.', 'bmi', 'lv1'),
       '공복혈당': ('공복혈당', '지표', '식사 전 혈당(mg/dL). 100부터 공복혈당장애, 126 이상 당뇨 의심(이 수업의 기준선).', 'fasting-glucose', 'lv2'),
       '기준선': ('기준선', '용어', '차트에 그어 비교 기준을 보여 주는 선. 임상 기준값, 평균 등.', 'reference-line', 'lv2'),
       '숨은 변수': ('숨은 변수', '용어', '두 변수를 함께 움직이게 하는 제3의 변수. 여기서는 연령.', 'confounder', 'lv3'),
       'small multiples': ('작은 패널 여러 장(small multiples)', '방법', '같은 축의 작은 차트를 그룹별로 나란히 놓아 비교하는 방법.', 'small-multiples', 'lv3'),
       '이중축': ('이중축', '용어', '왼쪽·오른쪽에 다른 Y축을 둔 차트. 축 범위로 없는 관계를 만들 수 있다(T3).', 'dual-axis', 'lv4'),
       '코드표': ('코드표(codebook)', '용어', '숫자 코드(예: 시도 11)를 이름(서울)으로 바꾸는 표.', 'codebook', 'lv1')},
models=['건강검진 데이터는 공공데이터와 같은 모양의 수업용 모의 데이터이며 실제 개인 기록이 아닙니다.', '산점도는 3만 명 중 무작위 700명 표본(random_state=42)입니다.', '이중축 예시는 함정을 보여 주려고 일부러 만든 그림(T3 예시)입니다.'],
cover_alt='진료 기록실 벽 화면에 오른쪽 꼬리 근처 앰버 점선이 그어진 히스토그램이 뜨고, 식구들이 차트 카드를 한 장씩 들고 선 픽셀 표지',
toc_faces=[('asst', 'firm'), ('x1', 'think'), ('x2', 'smile')],
data='var HOBJ=' + json.dumps(json.loads(_H), ensure_ascii=False) + ';',
js='''var V=LAB.VIZ,$=LAB.$,$$=LAB.$$,H=HOBJ;
/* 1. 전처리 전후 */
function t1(cl){$('#w10raw').setAttribute('aria-pressed',String(!cl));$('#w10cl').setAttribute('aria-pressed',String(cl));
 var rows=cl?[['허리둘레 (cm)','314 + 12 = 326','55.6','149.8 이하','50~150 밖 12건 비움'],['수축기 혈압 (mmHg)','159 + 7 = 166','70 이상','250 이하','70~250 밖 7건 비움'],['공복혈당 (mg/dL)','254 + 12 = 266','50 이상','291','50~500 밖 12건 비움']]
  :[['허리둘레 (cm)','314','55.6','<b style="color:#c9302c">999</b>','사람에게 불가능한 값'],['수축기 혈압 (mmHg)','159','<b style="color:#c9302c">0</b>','<b style="color:#c9302c">400</b>','0과 400'],['공복혈당 (mg/dL)','254','<b style="color:#c9302c">0</b>','291','0']];
 $('#w10t').innerHTML='<div class="tbl"><table><thead><tr><th>열</th><th>빈 값</th><th>최솟값</th><th>최댓값</th><th>메모</th></tr></thead><tbody>'+rows.map(function(r){return '<tr>'+r.map(function(c){return '<td>'+c+'</td>';}).join('')+'</tr>';}).join('')+'</tbody></table></div>';
 $('#w10o').innerHTML=cl?'범위 밖 값 31건(12 + 7 + 12)을 비웠어요. 행은 3만 그대로입니다. 캡션 예: “혈당 범위 밖 12건 결측 처리”. BMI 평균 '+H.bmi_mean+', 비만율 '+H.obese_nat+'%.':'describe()의 최솟값·최댓값부터 봅니다. 허리둘레 999cm, 혈압 0과 400, 혈당 0 — 입력 오류입니다.';}
$('#w10raw').onclick=function(){t1(false);};$('#w10cl').onclick=function(){t1(true);};t1(false);
/* 2. 비교와 분포 */
function a2(k){$$('#w10a button').forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.k===k));});var el=$('#w10av'),S=H.sido;
 if(k==='bar'||k==='cut'){V.bar(el,{labels:S.map(function(s){return s[0];}),values:S.map(function(s){return s[1];}),horizontal:true,hl:0,dec:1,unitShort:'%',ref:H.obese_nat,refLabel:'전국 '+H.obese_nat+'%',y0:k==='cut'?30:0,yMax:55,title:k==='cut'?'T1 예시 — X축 30%부터':'시도별 비만율 (BMI 25 이상), 2024 모의 검진',w:560,L:52});
  $('#w10ao').textContent=k==='cut'?'축을 30%부터 그리면 제주 막대가 대전 막대의 약 '+((50.9-30)/(35.0-30)).toFixed(1)+'배 길이로 보여요. 실제 비만율은 약 '+(50.9/35).toFixed(2)+'배입니다.':'제주 50.9% · 강원 50.3%가 위, 서울 35.6% · 대전 35.0%가 아래. 점선은 전국 '+H.obese_nat+'%. 0축 · 정렬 · 평균선이 있으면 3초 안에 읽힙니다.';}
 else{var g=H.glu;V.hist(el,{edges:g.edges,counts:g.counts,refs:[{v:100,label:'100 공복혈당장애 시작',color:'#5b6874'},{v:126,label:'126 당뇨 의심',color:'#5b6874',dy:16},{v:g.mean,label:'평균 '+g.mean,color:'#b45309',dash:true,dy:32}],unit:'공복혈당 (mg/dL, 구간 폭 5)',yunit:'인원 (명)',title:'공복혈당 분포 — 2024 모의 검진',h:300});
  $('#w10ao').innerHTML='평균 '+g.mean+' &gt; 중앙값 '+g.median+' → 오른쪽 꼬리. <b>126 이상 '+g.ge126+'% ('+LAB.nf(g.n126)+'명)</b>, 100~125 '+g.b100_125+'%. 평균만 보면 놓치는 사람들입니다.';}}
$$('#w10a button').forEach(function(b){b.onclick=function(){a2(b.dataset.k);};});a2('bar');
/* 3. 숨은 변수 */
var AC=['#93a5cf','#1e3a8a','#0b7a86','#b45309'],AN=['20-39','40-49','50-59','60+'];
function s3(k){$$('#w10s button').forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.k===k));});var el=$('#w10sv');
 if(k==='all'){V.scatter(el,{pts:H.pts.map(function(p){return [p[0],p[1]];}),fit:true,alpha:.3,r:2.5,ref:140,refLabel:'140 고혈압 기준',xlab:'허리둘레 (cm)',ylab:'수축기 혈압 (mmHg)',title:'허리둘레와 수축기 혈압의 관계 (표본 700명)',h:320});
  $('#w10so').textContent='전체 3만 명 기준 r = '+H.r_all+' (표본 700명 그림의 r은 조금 다를 수 있어요). 제목에 “때문에·원인”을 쓰지 않고 “관계”만 씁니다. 점이 가로 줄무늬처럼 보이는 건 혈압이 정수라서예요.';}
 else if(k==='age'){var W=560,Hh=320,s='<svg viewBox="0 0 '+W+' '+Hh+'" width="100%" style="max-width:'+W+'px" role="img" aria-label="연령대별 색으로 나눈 산점도">';var xs=H.pts.map(function(p){return p[0];}),ys=H.pts.map(function(p){return p[1];}),x0=55,x1=125,y0=80,y1=190,L=50,T=30,B=40,R=14;
  var sx=function(v){return L+(W-L-R)*(v-x0)/(x1-x0);},sy=function(v){return Hh-B-(Hh-T-B)*(v-y0)/(y1-y0);};
  s+='<text x="'+W/2+'" y="18" text-anchor="middle" font-size="14" font-weight="700" fill="#16212b">연령대별 색 — 같은 연령대 안의 관계</text>';
  H.pts.forEach(function(p){if(p[0]<x0||p[0]>x1||p[1]<y0||p[1]>y1)return;s+='<circle cx="'+sx(p[0]).toFixed(1)+'" cy="'+sy(p[1]).toFixed(1)+'" r="2.4" fill="'+AC[p[2]]+'" fill-opacity=".55"/>';});
  [0,1,2,3].forEach(function(g){var P=H.pts.filter(function(p){return p[2]===g;}),st=V.stats(P.map(function(p){return p[0];}),P.map(function(p){return p[1];}));s+='<line x1="'+sx(x0+3)+'" y1="'+sy(st.a+st.b*(x0+3))+'" x2="'+sx(x1-3)+'" y2="'+sy(st.a+st.b*(x1-3))+'" stroke="'+AC[g]+'" stroke-width="2.5"/>';s+='<rect x="'+(L+8+g*120)+'" y="'+(Hh-18)+'" width="10" height="10" fill="'+AC[g]+'"/><text x="'+(L+22+g*120)+'" y="'+(Hh-9)+'" font-size="12">'+AN[g]+'세 r '+H.r_age[g][1]+'</text>';});
  s+='<line x1="'+L+'" x2="'+L+'" y1="'+T+'" y2="'+(Hh-B)+'" stroke="#9aa5b1"/><line x1="'+L+'" x2="'+(W-R)+'" y1="'+(Hh-B)+'" y2="'+(Hh-B)+'" stroke="#9aa5b1"/>';
  [60,80,100,120].forEach(function(t){s+='<text x="'+sx(t)+'" y="'+(Hh-B+14)+'" font-size="11" text-anchor="middle">'+t+'</text>';});[100,140,180].forEach(function(t){s+='<text x="'+(L-6)+'" y="'+(sy(t)+4)+'" font-size="11" text-anchor="end">'+t+'</text>';});
  el.innerHTML=s+'</svg>';$('#w10so').textContent='연령대 안에서는 r이 '+H.r_age.map(function(a){return a[1];}).join(' · ')+'로 전체('+H.r_all+')보다 작아요. 선들이 위아래로 층을 이루는 것 — 나이 든 그룹일수록 같은 허리둘레에서도 혈압이 높은 것 — 이 숨은 변수의 흔적입니다.';}
 else{var A=H.age_waist_bp;V.line(el,{labels:A.map(function(a){return a[0];}),series:[{name:'평균 허리둘레 (cm)',values:A.map(function(a){return a[1];}),vlab:true},{name:'평균 수축기 혈압 (mmHg)',values:A.map(function(a){return a[2];}),vlab:true}],y0:0,yMax:160,dec:1,title:'나이가 들수록 둘 다 오른다 (같은 축, 0부터)',h:300});
  $('#w10so').textContent='20대 → 80세 이상: 허리둘레 81.8 → 90.6cm, 혈압 110.8 → 140.8mmHg. 나이가 두 값을 함께 올리면, 나이를 나누지 않은 전체 상관은 부풀려집니다.';}}
$$('#w10s button').forEach(function(b){b.onclick=function(){s3(b.dataset.k);};});s3('all');
/* 4. 구성·추세·함정 */
function c4(k){$$('#w10c button').forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.k===k));});var el=$('#w10cv'),el2=$('#w10cv2');el2.hidden=true;var SM=H.smoke,T=H.trend,col=['#1e3a8a','#93a5cf','#b45309'];
 if(k==='pie'){el2.hidden=false;V.pie(el,{labels:['비흡연','과거 흡연','현재 흡연'],values:SM['남'],colors:col,title:'남성 흡연 상태',h:240,w:400});V.pie(el2,{labels:['비흡연','과거 흡연','현재 흡연'],values:SM['여'],colors:col,title:'여성 흡연 상태',h:240,w:400});$('#w10co').textContent='범주 3개, 합 100% — 파이 조건 충족. 두 파이의 범주 순서와 색을 똑같이 맞췄어요. 그런데 “현재 흡연이 남녀 몇 %p 차이?”는 각도로 읽기 어렵습니다.';}
 else if(k==='stack'){var W=560,s='<svg viewBox="0 0 '+W+' 170" width="100%" style="max-width:'+W+'px" role="img" aria-label="성별 흡연 상태 100% 누적 막대"><text x="'+W/2+'" y="18" text-anchor="middle" font-size="14" font-weight="700" fill="#16212b">성별 흡연 상태 (100% 누적 가로 막대)</text>';
  ['남','여'].forEach(function(g,i){var x=60,y=40+i*50;SM[g].forEach(function(v,j){var w=(W-80)*v/100;s+='<rect x="'+x+'" y="'+y+'" width="'+w+'" height="32" fill="'+col[j]+'"/>'+(v>6?'<text x="'+(x+w/2)+'" y="'+(y+21)+'" text-anchor="middle" font-size="12" fill="#fff">'+v+'%</text>':'');x+=w;});s+='<text x="50" y="'+(y+21)+'" text-anchor="end" font-size="13">'+g+'</text>';});
  ['비흡연','과거','현재'].forEach(function(n,j){s+='<rect x="'+(60+j*110)+'" y="148" width="10" height="10" fill="'+col[j]+'"/><text x="'+(74+j*110)+'" y="157" font-size="12">'+n+'</text>';});el.innerHTML=s+'</svg>';$('#w10co').textContent='현재 흡연(앰버) 길이를 비교하면 남 29.9% · 여 4.9%, 약 25%p 차이가 바로 읽힙니다. 질문이 “비교”로 바뀌면 차트도 바뀝니다.';}
 else if(k==='twin'){var o=T.map(function(t){return t[2];}),g=T.map(function(t){return t[3];}),lo=4.9,hi=5.5;V.line(el,{labels:T.map(function(t){return String(t[0]);}),series:[{name:'비만율 (왼쪽 축 34~42%)',values:o.map(function(v){return (v-34)/8*100;})},{name:'혈당 126 이상 (오른쪽 축 4.9~5.5%)',values:g.map(function(v){return (v-lo)/(hi-lo)*100;})}],y0:0,yMax:110,title:'T3 예시 — 이중축: “비만도 고혈당도 급증!”',h:290});$('#w10co').textContent='오른쪽 축을 4.9~5.5%로 좁히면 거의 평평한 고혈당 비율(5.0~5.4%)이 비만율처럼 가파르게 오르는 것처럼 보입니다. 이 그림은 함정을 보여 주려고 일부러 만든 것입니다.';}
 else if(k==='two'){el2.hidden=false;V.line(el,{labels:T.map(function(t){return String(t[0]);}),series:[{name:'비만율 (%)',values:T.map(function(t){return t[2];}),vlab:true}],y0:0,yMax:50,dec:1,title:'비만율 (%) — Y축 0부터',h:220});V.line(el2,{labels:T.map(function(t){return String(t[0]);}),series:[{name:'혈당 126 이상 (%)',values:T.map(function(t){return t[3];}),vlab:true,color:'#b45309'}],y0:0,yMax:50,dec:1,title:'혈당 126 이상 비율 (%) — 같은 축 0~50',h:220});$('#w10co').textContent='두 패널, 각 Y축 0부터. 비만율은 35.5% → 41.6%로 늘었고, 고혈당 비율은 5.0~5.4%로 거의 평평합니다. 작아 보이는 변화가 정직한 결과입니다.';}
 else{el2.hidden=false;V.bar(el,{labels:['남','여'],values:H.bp_sex,y0:115,yMax:128,hl:0,dec:1,title:'T1 예시 — Y축 115부터: “남성 혈압 압도적!”',h:240,w:420});V.bar(el2,{labels:['남','여'],values:H.bp_sex,y0:0,yMax:140,dec:1,color:'#6b7280',title:'고친 그림 — Y축 0부터: 차이 6.3mmHg (약 5%)',h:240,w:420});$('#w10co').textContent='평균 수축기 혈압 남 126.7 · 여 120.4. 오른쪽이 “재미없어” 보인다면, 그게 정직한 차이의 크기입니다.';}}
$$('#w10c button').forEach(function(b){b.onclick=function(){c4(b.dataset.k);};});c4('pie');
/* 5. 규칙 점검 */
LAB.Pick($('#w10rule'),[
 {q:"df['bmi'] = df['weight_5kg'] / (df['height_5cm'] / 100) ** 2",a:0,why:'한 줄이 표 전체에 한 번에 계산합니다. 들여쓰기·함수·for문 없음.'},
 {q:"for col in ['waist_cm', 'systolic_bp']:",a:1,why:'for문입니다. between이나 loc로 열마다 한 줄씩 쓰면 됩니다.'},
 {q:"def make_chart(data):",a:1,why:'함수 정의(def)는 금지입니다. 위에서 아래로 바로 씁니다.'},
 {q:"ax.set_title('Fasting glucose distribution, 2024')",a:0,why:'차트 제목을 영어로 썼어요. 규칙 3을 지켰습니다.'},
 {q:"ax.set_title('시도별 비만율')",a:1,why:'차트 글자는 영어로. 한글은 Colab에서 □□□로 깨지기 쉽습니다. 한글은 주석에.'},
 {q:"# [KO] 126 이상 비율을 계산한다 / [ZH] 计算 126 以上的比例",a:0,why:'주석을 한국어와 중국어로 함께 적었어요.'}],['규칙 지킴','규칙 위반']);
'''
)
for _s in PAGE['steps']:
    _s['def'] = {'lv1': '그리기 전에 해상도·이상치·기준선·해석의 한계를 의심하고 BMI 같은 파생 변수를 만드는 일.', 'lv2': '정렬·0축·평균선으로 비교하고, 히스토그램에 임상 기준선을 그어 평균이 숨기는 꼬리를 보는 일.',
                 'lv3': '두 변수의 관계를 숨은 변수(연령)로 나눠 다시 보고, 인과 대신 관계만 말하는 일.', 'lv4': '조건부 파이와 100% 누적 막대, 이중축 대신 두 패널, 나쁜 차트를 일부러 만들어 진단하는 역방향 학습.',
                 'lv5': '데이터 일부 기억시키기·업로드 구조·영어 차트와 중한 주석·들여쓰기/함수/for문 금지로 처음 배우는 사람이 읽는 Colab 코드를 받는 프롬프트 규칙.'}[_s['id']]
    if 'mathbox' in _s:
        _s['mathbox']['try'] = _s['mathbox'].pop('try_')
