# 3주차 — 생성 AI를 활용한 데이터 전처리 및 기초 시각화 (개인발표)
_CSV = open(HERE + '/data/payments.csv', encoding='utf-8').read()
PAGE = dict(
num='03', slug='data-cleaning', kind='lecture', scene='solo', short='3주', chip='03주차', floor='3층 세척실',
scene_line='조원 한 명씩 “더러운 데이터” 한 종류를 맡아 발표하고, 다른 조원이 점검합니다',
title='그리기 전에 씻는다', title_en='Cleaning data with generative AI before plotting',
subtitle='생성 AI로 데이터 전처리 — 다섯 가지 더러움, 빈 값 처리, AI 검사 3규칙, Matplotlib과 Seaborn',
toc='표기 불일치·형식·빈 값·중복·이상치, 평균이 흔들리는 이유, AI 검사 3규칙, 고급 차트 세 가지',
kicker='데이터시각화 · 3주차 · 생성 AI를 활용한 데이터 전처리 및 기초 시각화',
question='같은 데이터인데, 빈 값을 0으로 채우면 평균이 왜 바뀔까?',
desc='데이터 시각화 3주차 해설: 표기 불일치·형식 오류·빈 값·중복·이상치 다섯 가지 더러운 데이터, 빈 값을 지우기·채우기·두기, AI가 만든 전처리 코드를 행 수와 요약값으로 검사하는 3규칙, Matplotlib과 Seaborn의 역할 나누기, 바이올린·상관 히트맵·요일×시간 히트맵.',
intro='<p>3층 세척실. 오늘은 개인발표 날입니다. 조원 한 명씩 “더러운 데이터” 한 종류를 맡아 발표합니다. 첫 발표자 시아가 칠판에 씁니다. <b>“찾기 → 고치기 → 확인하기.”</b> 요리하기 전에 재료를 씻고 다듬듯, 차트를 그리기 전에 데이터를 씻습니다. 씻지 않고 그리면 차트가 아무리 예뻐도 결론이 바뀝니다.</p>',
first3=('그리기 전에 데이터를 점검하는 다섯 가지(표기 불일치·형식·빈 값·중복·이상치)와, AI가 만든 전처리 코드를 숫자로 검사하는 법을 배웁니다.',
        '빈 값을 0으로 채우는 것 같은 작은 선택 하나가 평균을 4% 깎습니다. 그 평균으로 예산이나 목표를 정하면 결정이 틀어집니다.',
        '매출 보고서를 만들기 전 “중복 결제가 두 번 집계되지 않았나”, “0원 결제가 섞이지 않았나”를 확인하는 일이 실무 데이터 업무의 절반입니다.'),
abbr=[('NaN', 'Not a Number, 비어 있는 값(결측)을 컴퓨터가 표시하는 방식'), ('IQR', 'Interquartile Range, 3사분위수 − 1사분위수. 이상치 기준에 쓴다'),
      ('HTML', '웹 페이지 파일. 더블클릭하면 브라우저에서 열린다'), ('hue', 'Seaborn에서 “이 열로 색을 나눠 그려라”라는 뜻의 인자')],
kpis=[('5가지', '표기 · 형식 · 빈 값 · 중복 · 이상치'), ('1,000 → 970', '중복 30건만 지운 올바른 행 수'), ('3규칙', '코드만 받기 · 행 수 비교 · 지우기 전 표시'), ('−4.0%', '빈 값을 0으로 채웠을 때 평균의 변화')],
kpi_note='campus_tea.csv는 원자료의 가상 대학가 음료 데이터(1,000행)이고, 빈 값 실험은 payments.csv(800건, 금액 결측 32건)로 이 페이지에서 직접 계산합니다.',
hero_talk=[
 ('sia', 'explain', '첫 발표자 시아입니다. 같은 브랜드가 다섯 가지로 적혀 있으면, 컴퓨터는 다섯 개의 다른 가게로 셉니다.'),
 ('robo', 'happy', '빈 값은 0으로 채우면 끝 아니야? 빈 데가 없으니 깔끔하잖아!'),
 ('fly', 'magnify', '깔끔해 보이는 것과 맞는 건 달라. 0을 넣으면 평균이 내려가.'),
 ('doc', 'front', '오늘은 개인발표입니다. 발표가 끝날 때마다 다른 조원이 <b>숫자로</b> 점검합니다.')],
crew=[('doc', 'front', '심판, 발표 점검'), ('sia', 'explain', '발표 ① 다섯 가지 더러움'), ('asst', 'think', '발표 ② 빈 값 처리'),
      ('moa', 'report', '발표 ③ 중복·이상치와 AI 검사'), ('x3', 'smile', '발표 ④ Seaborn 고급 차트'), ('fly', 'magnify', '초파리 조 조장 — 행 수 점검'), ('robo', 'happy', '주판봇 조 조장 — “빈 값은 0으로!”')],
recap='2주차: 세 원칙(단순성·정확성·목적성)과 다섯 갈래(비교·추세·구성·관계·분포). 그리고 payments.csv의 금액 결측 4%는 “일단 빼고” 그렸다.',
prereq=['02'],
why_title='왜 씻어야 하나 — 씻지 않으면 결론이 바뀐다',
why=[('찾기', '그리기 전에 행 수, 열 이름, 열마다 빈 값 개수, 고유값을 먼저 봅니다. “아직 고치지 마”라는 한 줄이 중요합니다.'),
     ('고치기', 'AI에게 고친 데이터를 받지 말고 <b>코드</b>를 받습니다. 그래야 반년 뒤에도 똑같이 다시 돌릴 수 있습니다.'),
     ('확인하기', '고치기 전과 후의 행 수와 요약값(평균·개수)을 비교합니다. 숫자가 예상과 다르면 다음 단계로 가지 않습니다.')],
bigpicture='''<div class="tbl"><table><thead><tr><th>#</th><th>더러움</th><th>예</th><th>처리</th><th>비유</th></tr></thead><tbody>
<tr><td>1</td><td>표기 불일치</td><td>Mixue · MIXUE · mixue · 미쉐 · 蜜雪冰城</td><td>하나의 이름으로 통일</td><td>한 친구의 별명 다섯 개</td></tr>
<tr><td>2</td><td>형식 오류</td><td>“4,500원” · “4500” · “4.5k”</td><td>숫자 4500으로 통일</td><td>같은 값, 다른 글자</td></tr>
<tr><td>3</td><td>빈 값</td><td>별점(rating)이 비어 있음</td><td>지우기 · 채우기 · 두기 중 선택</td><td>시험 안 본 학생의 점수</td></tr>
<tr><td>4</td><td>중복</td><td>같은 주문번호가 두 줄</td><td>한 줄만 남기기</td><td>결제 버튼을 두 번 누름</td></tr>
<tr><td>5</td><td>이상치</td><td>당도 999 · 가격 0원 · 대기 420분</td><td>오타는 비우고, 진짜 사건은 표시</td><td>지우기 전에 이유부터 묻기</td></tr></tbody></table></div>''',
why_say=('doc', 'board', '다섯 줄을 외우지 않아도 됩니다. “찾기 → 고치기 → 확인하기” 세 낱말만 기억하세요.'),
steps=[
dict(id='lv1', short='다섯 더러움', title='다섯 가지 더러운 데이터 — 시아의 발표', concept='데이터 전처리', en='data preprocessing', cid='lab:concept/data-preprocessing',
 tag='방법: 찾기 → 고치기 → 확인하기', analogy='요리 전 재료 손질',
 where='<b>①다섯 가지 더러움</b> → ②빈 값 처리 → ③중복·이상치와 AI 검사 → ④도구와 고급 차트',
 situation='가상 대학가 음료 데이터에 브랜드가 Mixue·MIXUE·mixue·미쉐·蜜雪冰城로 섞여 있습니다. 브랜드별 주문 수 막대를 그리면, 1위는 어느 가게가 될까요?',
 whybox=dict(problem='사람 눈에는 같은 가게인데, 컴퓨터는 글자가 하나라도 다르면 다른 가게로 셉니다.',
             limit='그대로 그리면 한 가게의 주문이 다섯 막대로 쪼개져, 실제 1위가 중간 순위로 내려갑니다. “4,500원” 같은 글자는 평균을 낼 수도 없습니다.',
             solution='그리기 전에 다섯 가지(표기·형식·빈 값·중복·이상치)를 <b>찾고 → 고치고 → 확인</b>합니다.',
             easy='요리 전에 재료를 씻고 다듬듯, 차트 전에 데이터를 다듬습니다. 안 씻고 끓이면 맛이 달라집니다.'),
 pair=(('일상으로 치면', '같은 친구를 “지수”, “지수야”, “김지수”, “JS”, “수”로 저장해 두면, 연락처 앱은 친구 다섯 명으로 셉니다. 누구와 가장 자주 연락했는지 순위가 틀어집니다.'),
       ('데이터에서는', '브랜드 표기를 6개 이름(CHAGEE · Mixue · HEYTEA · Auntea Jenny · Mega Coffee · Compose Coffee)으로 통일하고, 가격은 “4,500원”·“4.5k”를 모두 숫자 4500으로 바꿉니다.')),
 talk=[('sia', 'explain', '아래 작은 표는 교안 데이터를 12줄로 줄인 예시입니다. 버튼을 하나씩 눌러 고쳐 보세요.'),
       ('robo', 'coin', '그냥 한꺼번에 다 지우면 되잖아? 이상한 줄은 다 삭제!'),
       ('fly', 'point', '그러면 1,000줄이 700줄이 돼. 무엇을 몇 줄 지웠는지 숫자를 보면서 해.'),
       ('x1', 'think', '확인할게요. 버튼을 누를 때마다 행 수와 평균 가격을 같이 봐요.')],
 panel='''<div class="chips" id="w3fix"></div>
<div id="w3t"></div>
<div class="kpis" id="w3k"></div>
<div class="insight" id="w3o" aria-live="polite">버튼을 순서대로 눌러 보세요. 각 버튼은 한 가지만 고칩니다.</div>''',
 panel_title='직접 해 보기 — 작은 음료 주문표를 씻어 보기 (12줄 예시)',
 sim='음료 주문표 다섯 가지 손질',
 explain='<p>원자료 기준 campus_tea.csv(1,000행)의 목표값: 브랜드 통일 후 Mixue 280 · CHAGEE 200 · Mega Coffee 180 · Compose Coffee 150 · HEYTEA 110 · Auntea Jenny 80, 가격 평균 4,300~5,000원대, 별점 빈 값 약 60건. 교안은 학생 결과가 목표값의 ±5% 안이면 정상으로 봅니다. 원자료는 새로 문을 연 음료 가게 앞의 긴 대기 이야기로 수업을 열지만, 개점 시기 같은 보도 내용은 수업 전 다시 확인할 항목이라 이 페이지에는 옮기지 않았습니다.</p>',
 docline='“사람 눈에 같으면 같다”가 아니라 “<b>컴퓨터 눈에 같아야 같다</b>”. 그리기 전 첫 질문은 늘 “고유값이 몇 개인가”입니다.',
 limit='표기와 형식은 하나로 맞추면 끝나지만, 빈 값은 정답이 하나가 아닙니다. 지울까, 채울까, 둘까?', limit_label='빈 값 처리는 정답이 하나가 아님',
 code=[("df['brand'] = df['brand'].str.strip()", '브랜드 이름 앞뒤의 공백을 지운다'), ("df['brand'] = df['brand'].replace({'MIXUE':'Mixue','mixue':'Mixue','미쉐':'Mixue','蜜雪冰城':'Mixue'})", '여러 표기를 Mixue 하나로 바꾼다'),
       ("df['price_krw'] = df['price_krw'].str.replace('원','').str.replace(',','')", '“원”과 쉼표를 지운다'), ("df['brand'].value_counts()", '브랜드별 개수를 세어 6개가 맞는지 확인한다')],
 quiz=[dict(q='“4,500원”과 “4500”이 섞인 가격 열의 평균을 바로 구할 수 없는 이유는?', o=['숫자가 너무 커서', '“4,500원”은 컴퓨터에게 숫자가 아니라 글자라서', '원화라서', '행이 너무 많아서'], a=1, why='쉼표와 “원”이 붙으면 글자(문자열)로 저장됩니다. 숫자로 바꿔야 평균을 낼 수 있습니다.'),
       dict(q='브랜드 표기 통일 직후 가장 먼저 확인할 숫자는?', o=['브랜드 고유값 개수(6개인가)', '파일 크기', '열 이름의 글자 수', '차트 색깔'], a=0, why='value_counts()로 고유값이 6개인지 봅니다. 7개 이상이면 아직 섞인 표기가 남은 것입니다.')]),
dict(id='lv2', short='빈 값', title='빈 값 — 지울까, 채울까, 둘까 (하루의 발표)', concept='결측치 처리', en='missing value handling', cid='lab:concept/missing-values',
 tag='방법: 같은 데이터, 세 가지 처리 비교', analogy='시험 안 본 학생의 점수',
 where='①다섯 가지 더러움 → <b>②빈 값 처리</b> → ③중복·이상치와 AI 검사 → ④도구와 고급 차트',
 situation='payments.csv 800건 중 결제 금액이 비어 있는 32건. 주판봇 조는 0으로 채웠고, 초파리 조는 비워 둔 채 계산했습니다. 두 조가 발표한 “평균 결제 금액”은 같을까요?',
 whybox=dict(problem='빈 값이 있으면 그래프 도구가 오류를 내거나, 사람마다 다르게 처리합니다.',
             limit='0으로 채우면 “결제를 안 했다”는 뜻이 되어 평균이 내려갑니다. 무조건 지우면 그 행의 다른 정보(도시·채널)까지 사라집니다.',
             solution='세 가지 길 — <b>지우기</b>(그 값이 꼭 필요한 분석에서만), <b>채우기</b>(근거 있는 값으로만), <b>두기</b>(통계에서 자동으로 빠지게 표시만). 교안은 이번 주 가장 안전한 “두기”를 고릅니다.',
             easy='시험을 안 본 학생에게 0점을 주면 반 평균이 내려갑니다. 그 학생을 빼고 평균을 내는 것이 “두기”입니다.'),
 mathbox=dict(q='0을 몇 개 넣었을 뿐인데 평균이 왜 그렇게 많이 바뀌어요?', school='중학교 자료의 정리 — 평균 = 합 ÷ 개수',
   doc='평균은 “합 ÷ 개수”예요. 0을 넣으면 합은 그대로인데 개수만 늘어나니, 나누는 수가 커져서 평균이 작아집니다.',
   rows=[('합', '값이 있는 768건의 금액을 모두 더한 것'), ('÷ 개수', '두기: 768로 나눈다 / 0 채우기: 800으로 나눈다'), ('중앙값', '크기순으로 줄 세웠을 때 한가운데 값 — 이상치에 덜 흔들린다')],
   try_='합 869,640 ÷ 768 = <b>1,132.3</b> (두기)<br>합 869,640 ÷ 800 = <b>1,087.1</b> (0 채우기) → 약 <b>4.0% 낮아짐</b><br>빈 값을 중앙값 960.3으로 채우면 (869,640 + 32×960.3) ÷ 800 = <b>1,125.5</b>',
   comment='0 채우기는 합은 그대로 두고 개수만 늘리는 거네요. 그래서 평균이 깎이는 거고요.'),
 pair=(('일상으로 치면', '시험을 안 본 학생 3명에게 0점을 주고 반 평균을 내면, 반 전체 실력이 낮아 보입니다.'),
       ('데이터에서는', '결제 금액 빈 값을 0으로 채우면 “0원 결제”가 32건 생긴 셈입니다. 평균 객단가가 1,132 → 1,087로 내려가고, 히스토그램 맨 왼쪽에 없던 막대가 생깁니다.')),
 talk=[('asst', 'think', '세 가지 처리를 버튼으로 바꿔 가며 평균과 히스토그램을 보겠습니다.'),
       ('robo', 'chart', '0으로 채우면 행이 800개 그대로잖아. 데이터를 하나도 안 버렸으니 더 정확하지!'),
       ('fly', 'arms', '행 수가 그대로인 거랑 값이 정확한 건 달라. 히스토그램 맨 왼쪽을 봐.'),
       ('moa', 'think', '0원 결제 32건이 생겼어요… 실제로는 없던 결제인데요.')],
 panel='''<div class="ctrl" id="w3m"><button type="button" class="bt" data-m="keep" aria-pressed="true">두기 (통계에서 제외)</button><button type="button" class="bt" data-m="zero">0으로 채우기</button><button type="button" class="bt" data-m="med">중앙값으로 채우기</button><button type="button" class="bt" data-m="drop">행째 지우기</button></div>
<div class="kpis" id="w3mk"></div><div id="w3mh" class="viz"></div><div class="insight" id="w3mo" aria-live="polite"></div>''',
 panel_title='직접 해 보기 — 빈 값 32건을 어떻게 할까',
 sim='결측치 처리 비교 실험',
 explain='<p>“두기”와 “행째 지우기”는 평균이 같습니다(둘 다 값이 있는 768건만 씁니다). 차이는 <b>도시·채널 같은 다른 열</b>입니다. 행째 지우면 금액이 빈 32건의 도시·채널 정보도 함께 사라져, 도시별 주문 수(건수)가 줄어듭니다. 그래서 교안은 이번 주에 “두기”를 고릅니다. 채우기는 근거가 있을 때만 씁니다 — 예를 들어 같은 주문번호의 다른 기록에 금액이 있을 때.</p>',
 aicheck='<p>함께 받은 실습 노트북(Untitled233.ipynb)에서 AI가 만든 코드 한 줄을 봅시다: <code>df = df.fillna({"items": 0, "amount": 0, "is_new_user": 0})</code>. 주석은 “결측값 채우기(있다면)”. <b>무엇이 문제일까요?</b> ① amount를 0으로 채워 평균 객단가가 약 4% 낮게 나옵니다. ② 그 낮은 평균이 그대로 “자동 결론 보고서”의 평균 객단가 문장에 들어갑니다. ③ 코드가 오류 없이 돌아가서 아무도 눈치채지 못합니다. 확인 질문: “채우기 전과 후의 평균을 나란히 출력해 줘.”</p>',
 docline='빈 값을 채우는 순간 “없는 정보”가 “있는 정보”로 바뀝니다. 채울 때는 <b>근거</b>를, 두기로 했다면 <b>개수</b>를 캡션에 적으세요.',
 limit='빈 값은 “두기”로 정했습니다. 그런데 같은 주문이 두 번 적혀 있거나, 당도 999 같은 값이 섞여 있다면? 그리고 AI에게 “이상한 줄을 정리해 줘”라고 맡기면 어떻게 될까요?', limit_label='중복과 이상치, AI에게 맡길 때의 위험',
 code=[("df['amount'].isna().sum()", 'amount가 비어 있는 행이 몇 개인지 센다 (32)'), ("df['amount'].mean()", '빈 값은 자동으로 빼고 평균을 낸다 (1,132.3)'),
       ("df['amount'].fillna(0).mean()", '빈 값을 0으로 채운 뒤 평균을 낸다 (1,087.1)'), ("df.dropna(subset=['amount'])", '금액이 빈 행을 통째로 지운다 (800 → 768행)')],
 quiz=[dict(q='값이 10, 20, 30, (빈 값)인 네 학생의 평균을 “두기”와 “0 채우기”로 각각 구하면?', o=['20과 20', '20과 15', '15와 20', '30과 15'], a=1, why='두기: (10+20+30) ÷ 3 = 20. 0 채우기: (10+20+30+0) ÷ 4 = 15. 개수만 늘어 평균이 내려갑니다.'),
       dict(q='“두기”와 “행째 지우기”의 평균 결제 금액이 같은데도 두기를 고르는 이유는?', o=['계산이 빨라서', '금액이 빈 행의 도시·채널 정보는 살릴 수 있어서', '차트가 예뻐서', '0이 더 정확해서'], a=1, why='행째 지우면 다른 열의 정보까지 사라집니다. 두기는 금액 통계에서만 빠지고 나머지 정보는 남습니다.')]),
dict(id='lv3', short='AI 검사', title='중복과 이상치, 그리고 AI 검사 3규칙 — 모아의 발표', concept='AI 전처리 검증', en='verifying AI preprocessing', cid='lab:concept/ai-preprocessing-check',
 tag='방법: 행 수 1,000 → 970을 지키기', analogy='결제 버튼 두 번 누르기',
 where='①다섯 가지 더러움 → ②빈 값 처리 → <b>③중복·이상치와 AI 검사</b> → ④도구와 고급 차트',
 situation='AI에게 “이상한 데이터 정리해 줘”라고 맡겼더니 1,000행이 700행이 되어 돌아왔습니다. 정답은 970행입니다. 사라진 270행에는 무엇이 들어 있었을까요?',
 whybox=dict(problem='중복 주문은 매출을 부풀리고, 당도 999·가격 0원 같은 값은 평균을 망칩니다.',
             limit='AI에게 “정리해 줘”라고 맡기면 그럴듯한 값을 지어내거나(Made-up values), 문제처럼 보이는 행을 한꺼번에 지웁니다. 한 줄씩 보면 맞아 보여도 전체는 틀립니다(Missed patterns).',
             solution='<b>AI 검사 3규칙</b>: ① 고친 데이터 말고 <b>코드</b>만 받는다 ② 처리 전후 <b>행 수</b>를 비교한다 ③ 이상치는 지우기 전에 <b>표시</b>한다.',
             easy='결제 버튼을 두 번 누르면 한 번은 취소합니다. 카드를 통째로 정지하지 않습니다.'),
 pair=(('일상으로 치면', '영수증 정리를 맡겼더니 중복 영수증 30장만 빼야 할 것을, 구겨진 것·글씨 흐린 것까지 300장을 버렸습니다. 남은 영수증으로 가계부를 쓰면 지출이 틀립니다.'),
       ('데이터에서는', '정답 970행 = 중복 30건만 삭제. AI의 700행 = 가격 형식 오류 200행 + 빈 값 60행 + 이상치 35행까지 함께 지움(원자료 해설). 당도 999·가격 0원은 오타라 <b>값만 비우고 행은 남기고</b>, 대기 300분 이상은 개점 주의 실제 사건이라 <b>지우지 않고 is_event = 1로 표시</b>합니다.')),
 talk=[('moa', 'report', '제가 맡은 건 중복과 이상치예요. 아래 처리 목록에서 “해도 되는 것”만 골라 970행을 만들어 보세요.'),
       ('robo', 'happy', '전부 체크하면 가장 깨끗한 데이터가 되잖아!'),
       ('fly', 'clip', '깨끗한 게 아니라 작아지는 거야. 행 수 숫자를 봐.'),
       ('x1', 'think', '대기 420분은 지우면 안 될 것 같아요. 그날 실제로 줄이 길었으니까요.')],
 panel='''<div class="ctrl" style="flex-direction:column;align-items:flex-start;gap:2px" id="w3ops">
<label><input type="checkbox" data-n="30" data-ok="1"> 같은 order_id가 두 번 나온 행 지우기 (30행)</label>
<label><input type="checkbox" data-n="200" data-ok="0"> 가격 형식이 이상한 행 지우기 (200행)</label>
<label><input type="checkbox" data-n="60" data-ok="0"> 별점이 비어 있는 행 지우기 (60행)</label>
<label><input type="checkbox" data-n="35" data-ok="0"> 이상치가 있는 행 지우기 (35행)</label>
<label><input type="checkbox" data-n="0" data-ok="1" data-k="flag"> 당도 999·가격 0원은 값만 비우고, 대기 300분 이상은 is_event = 1 표시 (0행)</label></div>
<div class="kpis" id="w3rk"></div><div class="insight" id="w3ro" aria-live="polite"></div>''',
 panel_title='직접 해 보기 — AI가 제안한 처리 중 무엇을 받아들일까',
 sim='행 수 지키기 게임',
 flow=dict(id='fl3', title='1,000행이 지나가는 길', h=220, alt='원본 1,000행이 표기 통일, 형식 변환, 중복 삭제, 이상치 표시를 거쳐 970행이 되는 흐름과, 한꺼번에 지워 700행이 되는 잘못된 흐름',
   cap='정답 흐름에서는 행 수가 “중복 삭제” 단계에서만 줄어듭니다. 빨간 카드는 한꺼번에 지운 AI의 흐름입니다.',
   js='{stations:["원본","표기·형식","중복","이상치","저장"],items:[["1,000행","1,000행 ✓","970행 ✓","970행 · 표시 ✓","970행 ✓"],["1,000행","800행 ✗","740행 ✗","705행 ✗","700행 ✗"]],bad:function(it,i){return /✗/.test(it[i]);},stamp:"원자료 숫자"}'),
 explain='<p>처리 후에는 <b>기록 세 줄</b>을 남깁니다(교안의 마크다운 셀): ① 브랜드 6개로 통일, 가격 정수화 — 행 수 변화 없음 ② order_id 중복 30건 삭제 → 970행, 별점 빈 값은 유지 ③ is_event 열 추가 — 대기 300분 이상은 1, 당도 999·가격 0원은 값만 비움. 저장은 <code>campus_tea_clean.csv</code>. “반년 뒤에 다시 돌려도 같은 결과”가 나오도록 남기는 것은 데이터가 아니라 <b>코드</b>입니다.</p>',
 aicheck='<p>AI가 “전처리 완료! 깨끗한 데이터 700행입니다”라고 답했습니다. 세 숫자로 검사합니다. ① <b>행 수</b>: 1,000 → 700, 정답 970과 다름 → 무엇을 지웠는지 물어본다. ② <b>브랜드 수</b>: 6개인가. ③ <b>별점 빈 값</b>: 약 60건이 그대로 남았는가 — 0이면 별점 빈 행까지 지웠다는 신호. 세 숫자 중 하나라도 어긋나면, 다음 단계로 가지 말고 프롬프트를 고쳐 다시 묻습니다.</p>',
 docline='AI는 정리를 “잘” 합니다. 문제는 <b>너무 잘</b> 지운다는 것입니다. 행 수는 우리가 지키는 숫자입니다.',
 limit='데이터를 씻었습니다. 이제 무엇으로 그릴까요? Matplotlib과 Seaborn은 무엇이 다를까요?', limit_label='그릴 도구를 아직 고르지 않음',
 quiz=[dict(q='AI 검사 3규칙에 해당하지 <b>않는</b> 것은?', o=['고친 데이터 대신 코드를 받는다', '처리 전후 행 수를 비교한다', '이상치는 지우기 전에 표시한다', 'AI가 “완료”라고 하면 바로 차트를 그린다'], a=3, why='“완료”라는 말보다 행 수·고유값·빈 값 개수를 직접 확인합니다.'),
       dict(q='대기 시간 420분이 개점 첫 주의 실제 기록일 때 맞는 처리는?', o=['행을 지운다', '평균으로 바꾼다', '지우지 않고 is_event = 1로 표시한다', '0으로 바꾼다'], a=2, why='실제 사건은 지우면 사건 자체가 사라집니다. 표시해 두고 분석에서 따로 다룹니다.')]),
dict(id='lv4', short='도구', title='Seaborn이 그리고 Matplotlib이 다듬는다 — X3의 발표', concept='Matplotlib과 Seaborn', en='matplotlib and seaborn roles', cid='lab:concept/matplotlib-seaborn',
 tag='방법: 같은 질문, 두 가지 그리기 · 고급 차트 세 가지', analogy='같은 카메라, 두 가지 모드',
 where='①다섯 가지 더러움 → ②빈 값 처리 → ③중복·이상치와 AI 검사 → <b>④도구와 고급 차트</b>',
 situation='씻은 데이터로 “신규 고객과 기존 고객의 결제 금액은 다를까?”, “일주일 중 언제 가장 붐빌까?”를 보려 합니다. 어떤 도구로, 어떤 차트를 그릴까요?',
 whybox=dict(problem='같은 차트도 도구에 따라 코드 길이와 다듬을 수 있는 정도가 다릅니다.',
             limit='Matplotlib만 쓰면 축·격자·색을 하나하나 정해야 해 코드가 길어지고, Seaborn만 쓰면 화살표·설명 같은 세부 손질이 어렵습니다.',
             solution='<b>Seaborn이 그리고, Matplotlib이 다듬는다.</b> 빠른 탐색은 Seaborn, 마지막 보고서용 손질은 Matplotlib, 나눠 보기 좋은 화면은 HTML.',
             easy='같은 카메라(Matplotlib 위에 Seaborn이 얹혀 있음)인데 인물 모드(Seaborn)는 빨리 찍고, 수동 모드(Matplotlib)는 세밀하게 고칩니다.'),
 pair=(('일상으로 치면', '휴대폰 카메라의 인물 모드는 한 번에 그럴듯한 사진을 주고, 수동 모드는 노출·초점을 직접 맞춥니다. 같은 센서를 씁니다.'),
       ('시각화에서는', 'Seaborn은 <code>hue=</code> 한 단어로 그룹별 색을 나누고, 평균·분포·회귀선을 바로 그립니다. Matplotlib은 제목·축 이름·화살표·강조선을 다듬습니다. 둘 다 pandas 표(DataFrame) 위에서 움직입니다.')),
 talk=[('x3', 'proud', '제 발표는 고급 차트 세 장이에요. 상자그림, 상관 히트맵, 요일×시간 히트맵.'),
       ('robo', 'coin', '히트맵은 색만 보면 되니까 숫자는 필요 없지?'),
       ('fly', 'point', '교안에 “색만 있고 숫자 없는 히트맵은 버린 그림”이라고 적혀 있어. 숫자도 써.'),
       ('doc', 'think', '가장 진한 셀을 찾으면, 먼저 “이게 사실인가?”를 한 번 묻고 결론으로 갑니다.')],
 panel='''<div class="chips" id="w3adv"><button type="button" class="bt" data-k="box" aria-pressed="true">① 신규 vs 기존 — 상자그림</button><button type="button" class="bt" data-k="corr">② 숫자 열끼리 — 상관 히트맵</button><button type="button" class="bt" data-k="wh">③ 요일 × 시간 — 주문 수 히트맵</button></div>
<div id="w3av" class="viz"></div><div class="insight" id="w3ao" aria-live="polite"></div>''',
 panel_title='직접 해 보기 — 결제 데이터로 고급 차트 세 장',
 sim='고급 차트 세 가지 비교',
 explain='<p>교안은 campus_tea 데이터로 “비 오는 날 배달이 더 오래 걸리나?”를 바이올린(분포 모양을 보여 주는 차트)으로 봅니다 — 평균만 보면 숨어 버리는 <b>긴 꼬리</b>(가끔 아주 오래 기다린 날)가 바이올린에서는 보입니다. 이 페이지는 같은 생각을 payments.csv로 다시 해 봅니다. 신규 고객의 결제 금액 중앙값(765)은 기존 고객(1,048)보다 낮고, 금액 열과 is_new_user의 상관은 약 −0.19로 약합니다. 요일 × 시간에서 주문 수가 가장 많은 셀은 금요일 12시(16건)입니다.</p><p><b>공유용 HTML 대시보드</b>를 AI에게 맡길 때 네 가지 함정: ① 전체 CSV를 HTML에 통째로 넣지 말고 작은 예시 데이터로 ② 데이터를 인터넷에서 불러오지 않게 ③ 조작 버튼은 핵심 하나만 ④ 대시보드 위에 결론 한 문장.</p>',
 docline='“가장 진한 셀은 금요일 12시”는 관찰이고, “금요일 점심 인력을 늘리자”는 결정입니다. 그 사이에 <b>“이게 사실인가?”</b>라는 한 번의 확인이 있습니다.',
 limit='이번 주까지는 결제 데이터 한 가지만 그렸습니다. 다음 주에는 산업마다 “보는 숫자”가 어떻게 다른지, 금융·핀테크부터 봅니다.', limit_label='산업별 맥락 없이 한 데이터만 다룸',
 code=[("sns.boxplot(data=df, x='is_new_user', y='amount')", 'Seaborn으로 신규/기존 고객별 금액 상자그림을 그린다'), ("sns.heatmap(df[cols].corr(), annot=True)", '숫자 열끼리 상관 히트맵을 그리고 셀에 숫자를 적는다'),
       ("pivot = df.pivot_table(index='weekday', columns='hour', values='amount', aggfunc='count')", '요일×시간 주문 수 표를 만든다'), ("ax.set_title('요일 × 시간 주문 수')", 'Matplotlib으로 제목을 다듬는다')],
 quiz=[dict(q='“발표용 그림에서 데이터 한 점에 화살표와 설명을 달아야 한다” — 어울리는 도구는?', o=['Seaborn', 'Matplotlib', 'HTML 대시보드', '아무거나'], a=1, why='세부 손질(화살표·주석)은 Matplotlib의 몫입니다. 교안의 판단 연습 2번 정답입니다.'),
       dict(q='히트맵을 받았을 때 AI에게 꼭 다시 요청할 것은?', o=['색을 더 화려하게', '각 셀에 숫자도 적어 달라고', '3D로 바꿔 달라고', '범례를 두 개로'], a=1, why='색만 있으면 비슷한 셀을 구분하기 어렵습니다. 숫자를 함께 적게 합니다.')]),
],
duel=dict(q='빈 값 32건 — 0으로 채울까, 비워 둘까', step=1, higher=False, margin=0,
 intro='값이 다 있는 768건에서 무작위로 32건을 “일부러 지운” 다음, 주판봇 조는 0으로 채우고 초파리 조는 비워 둔 채 평균을 냅니다. 지우기 전의 진짜 평균과 얼마나 어긋났는지(오차)를 200번 되풀이해 평균합니다. 오차가 작을수록 좋습니다.',
 fly_pick='비워 두기 (통계에서 제외)', fly_line='모르는 값은 모르는 채로 둬. 아는 768건으로만 평균을 내.',
 robo_pick='0으로 채우기', robo_line='빈 값이 하나도 없어야 깔끔하지! 800건 전부 쓰자!',
 metric='진짜 평균과의 평균 오차 (작을수록 좋음)',
 run='var D=LAB.VIZ.csv(PAYCSV).filter(function(r){return r.amount!=null;}).map(function(r){return r.amount;});var n=D.length,full=D.reduce(function(a,b){return a+b;},0)/n,R=LAB.rng(303),e1=0,e2=0,T=200;for(var t=0;t<T;t++){var idx={},k=0;while(k<32){var j=Math.floor(R()*n);if(!idx[j]){idx[j]=1;k++;}}var s=0,c=0;for(var i=0;i<n;i++){if(!idx[i]){s+=D[i];c++;}}e1+=Math.abs(s/c-full);e2+=Math.abs(s/n-full);}var f=e1/T,r=e2/T;return {fly:+f.toFixed(1),robo:+r.toFixed(1),flyTxt:f.toFixed(1),roboTxt:r.toFixed(1),full:full};',
 announce='return "진짜 평균은 "+LAB.nf(r.full,1)+"이에요. 비워 둔 초파리 조의 평균 오차는 "+r.flyTxt+", 0으로 채운 주판봇 조는 "+r.roboTxt+"이에요. 0 채우기는 매번 같은 방향(아래로)으로 틀려요.";',
 verdict='if(res==="F")return "초파리 조 승. 0은 “모름”이 아니라 “0원 결제”라는 <b>새 정보</b>를 만든다. 비워 둔 쪽의 오차는 무작위로 생기고, 0으로 채운 쪽의 오차는 늘 한쪽으로 쏠린다.";return "결과를 다시 보자.";',
 after='<p style="font-size:14px;color:#5b6874">이 실험은 페이지 안에서 실제 payments.csv 값으로 계산합니다(무작위 시드 고정). 0 채우기의 오차는 “빈 값 비율 4% × 평균”에 가까운 약 45~48입니다.</p>'),
summary='''<div class="tbl"><table><thead><tr><th>#</th><th>발표</th><th>한 줄 결론</th></tr></thead><tbody>
<tr><td>1</td><td>시아 — 다섯 가지 더러움</td><td>표기·형식·빈 값·중복·이상치를 찾고 → 고치고 → 확인한다. 첫 숫자는 고유값 개수</td></tr>
<tr><td>2</td><td>하루 — 빈 값 처리</td><td>0으로 채우면 평균 1,132 → 1,087(−4.0%). 이번 주는 “두기”가 기본</td></tr>
<tr><td>3</td><td>모아 — 중복·이상치와 AI 검사</td><td>정답은 1,000 → 970. AI 검사 3규칙: 코드만 받기, 행 수 비교, 지우기 전 표시</td></tr>
<tr><td>4</td><td>X3 — 도구와 고급 차트</td><td>Seaborn이 그리고 Matplotlib이 다듬는다. 히트맵에는 숫자를, 가장 진한 셀에는 “사실인가?”를</td></tr></tbody></table></div>
<p><b>제출 전 점검 다섯 가지</b>(교안 판단 연습 3): ① 차트의 숫자가 실제 데이터에 있는가 ② 차트의 변수 이름과 코드의 변수 이름이 같은가 ③ 흑백·색약 환경에서도 구분되는가 ④ 제목·축·단위·결론 한 문장이 있는가 ⑤ 도구를 목적에 맞게 골랐는가.</p>''',
outro=[('doc', 'judge', '오늘 개인발표 네 개, 모두 통과. 공통점 하나 — <b>숫자로 확인했다.</b> 행 수, 고유값, 평균.'),
       ('asst', 'proud', '0을 채우면 개수만 늘어서 평균이 깎인다는 거, 이제 손으로 설명할 수 있어요.'),
       ('robo', 'sigh', '빈 값을 0으로 채우는 게 깔끔한 줄 알았는데… 매번 아래로 틀리는구나.'),
       ('fly', 'coffee', '깔끔한 데이터가 아니라 <b>정직한</b> 데이터가 목표야.'),
       ('x3', 'joy', '다음엔 히트맵에 숫자도 꼭 적을게요.')],
next_note='<p>다음 층(4주차)에서는 산업을 나누는 두 가지 자(GICS와 X-Tech), 눈이 데이터를 읽는 정확도 순위, 그리고 은행과 핀테크의 화면을 나란히 봅니다.</p>',
refs=[dict(id='w03_slides', type='document', title='数据可视化 第3周 · 用生成式AI清洗并可视化数据 (중국어판, 50쪽)', who='안상선', issued={'date-parts': [[2026, 9, 17]]}, role='primary'),
      dict(id='payments', type='dataset', title='payments.csv — 수업용 합성 결제 데이터 (800건)', who='강의 자료', role='data', URL='https://github.com/adminmrobo/Data_visuialization_lecture_lab/blob/main/data/raw/payments.csv'),
      dict(id='nb233', type='software', title='실습 노트북 Untitled233.ipynb (AI 생성 결제 분석 코드, 중국어 주석)', who='강의 자료', role='example')],
facts=[('F1', '정답 처리는 order_id 중복 30건만 지워 1,000행을 970행으로 만드는 것이다.', '원자료', 'w03_slides', 'lv3', '판단 연습 1'),
       ('F2', 'amount 빈 값 32건을 0으로 채우면 평균이 1,132.3에서 1,087.1로 약 4.0% 낮아진다.', '계산', 'payments', 'lv2', 'amount 평균'),
       ('F3', '실습 노트북의 AI 생성 코드는 amount 결측을 0으로 채운다.', '원자료', 'nb233', 'lv2', 'fillna 줄'),
       ('F4', '신규 고객 결제 금액 중앙값은 765, 기존 고객은 약 1,048이다.', '계산', 'payments', 'lv4', 'is_new_user별'),
       ('F5', '요일×시간 주문 수가 가장 많은 셀은 금요일 12시(16건)다.', '계산', 'payments', 'lv4', '요일·시간 집계')],
gloss={'전처리': ('전처리', '용어', '분석·시각화 전에 데이터의 표기·형식·빈 값·중복·이상치를 손보는 일.', 'preprocessing', 'lv1'),
       '고유값': ('고유값', '용어', '한 열에 나오는 서로 다른 값의 목록. value_counts()로 센다.', 'unique-values', 'lv1'),
       '중앙값': ('중앙값', '통계', '크기순으로 줄 세웠을 때 한가운데 값. 이상치에 덜 흔들린다.', 'median', 'lv2'),
       '이상치': ('이상치', '용어', '다른 값들에서 멀리 떨어진 값. 오타일 수도, 실제 사건일 수도 있다.', 'outlier', 'lv3'),
       '중복': ('중복', '용어', '같은 기록(예: 같은 주문번호)이 두 번 이상 적힌 것.', 'duplicate', 'lv3'),
       '바이올린': ('바이올린 차트', '차트', '분포의 모양을 좌우 대칭 곡선으로 그려, 상자그림이 놓치는 꼬리까지 보여 주는 차트.', 'violin-plot', 'lv4'),
       '히트맵': ('히트맵', '차트', '행과 열로 된 표의 셀을 값의 크기에 따라 진하기로 칠한 차트.', 'heatmap', 'lv4')},
models=['12줄 음료 주문표는 교안의 campus_tea.csv 문제 유형을 줄여 만든 설명용 예시입니다.', '1,000 → 970, 700행 같은 숫자는 원자료(3주차 교안)의 설계값입니다.', '조별 대결의 오차는 payments.csv 실제 값으로 계산하되, 지울 32건을 무작위(시드 고정)로 골랐습니다.'],
cover_alt='하루가 개수대에서 얼룩진 표 카드를 씻어 깨끗한 카드로 내놓고, 오른쪽 발표대에서 모아와 시아가 발표하는 픽셀 표지',
toc_faces=[('sia', 'explain'), ('moa', 'report'), ('x3', 'proud')],
data='var PAYCSV=' + json.dumps(_CSV) + ';',
js='''var V=LAB.VIZ,$=LAB.$,$$=LAB.$$;
/* 1. 작은 음료 주문표 */
var T0=[["A01","Mixue","4,500원",4.5,30],["A02","MIXUE ","4500",4.0,25],["A03","CHAGEE","5800",null,40],["A04","mixue","4.5k",3.5,20],["A05","미쉐","4,300원",4.0,15],["A06","CHAGEE","5800",4.5,420],["A07","HEYTEA","6,200원",5.0,35],["A03","CHAGEE","5800",null,40],["A08","Mega Coffee","0",4.0,10],["A09","蜜雪冰城","4400",999,25],["A10","Compose Coffee","3,900원",3.5,12],["A11","Auntea Jenny","4,800원",4.0,28]];
var ST={brand:0,price:0,dup:0,out:0};var NM={brand:'① 표기 통일',price:'② 가격을 숫자로',dup:'③ 중복 지우기',out:'④ 이상치: 오타는 비우고 사건은 표시'};
$('#w3fix').innerHTML=Object.keys(NM).map(function(k){return '<button type="button" class="bt" data-k="'+k+'" aria-pressed="false">'+NM[k]+'</button>';}).join('')+'<button type="button" class="bt" id="w3r">처음으로</button>';
function num(p){if(typeof p==='number')return p;var s=String(p).replace('원','').replace(/,/g,'').trim();if(/k$/.test(s))return Math.round(parseFloat(s)*1000);return +s;}
function draw1(){var rows=T0.map(function(r){return r.slice();});
 if(ST.brand)rows.forEach(function(r){var b=r[1].trim();if(/^(mixue|미쉐|蜜雪冰城)$/i.test(b))b='Mixue';r[1]=b;});
 if(ST.price)rows.forEach(function(r){r[2]=num(r[2]);});
 if(ST.dup){var seen={};rows=rows.filter(function(r){if(seen[r[0]])return false;seen[r[0]]=1;return true;});}
 var ev={};if(ST.out)rows.forEach(function(r){if(r[3]===999)r[3]=null;if(num(r[2])===0)r[2]=null;if(r[4]>=300)ev[r[0]]=1;});
 var h='<div class="tbl"><table><thead><tr><th>주문번호</th><th>브랜드</th><th>가격</th><th>별점</th><th>대기(분)</th>'+(ST.out?'<th>is_event</th>':'')+'</tr></thead><tbody>';
 rows.forEach(function(r){var bad=function(i){if(i===1)return !ST.brand&&!/^(Mixue|CHAGEE|HEYTEA|Mega Coffee|Compose Coffee|Auntea Jenny)$/.test(r[1]);if(i===2)return !ST.price&&typeof r[2]==='string'&&/[원k,]/.test(r[2]);if(i===3)return r[3]===999;if(i===4)return r[4]>=300&&!ST.out;return false;};
  h+='<tr>'+[0,1,2,3,4].map(function(i){var v=r[i];return '<td'+(bad(i)?' style="background:#fcebea;color:#c9302c"':'')+'>'+(v==null?'<i style="color:#5b6874">(빈 값)</i>':LAB.esc(typeof v==='number'?LAB.nf(v,i===3?1:0):v))+'</td>';}).join('')+(ST.out?'<td>'+(ev[r[0]]?'<b style="color:#a35c00">1</b>':'0')+'</td>':'')+'</tr>';});
 $('#w3t').innerHTML=h+'</tbody></table></div>';
 var brands={};rows.forEach(function(r){brands[r[1]]=1;});var ps=rows.map(function(r){return typeof r[2]==='number'?r[2]:(ST.price?null:NaN);}).filter(function(v){return v!=null&&!isNaN(v);});
 var mean=ps.length&&ST.price?ps.reduce(function(a,b){return a+b;},0)/ps.length:null;
 $('#w3k').innerHTML='<div><b>'+rows.length+'줄</b><span>행 수 (원래 12)</span></div><div><b>'+Object.keys(brands).length+'개</b><span>브랜드 고유값</span></div><div><b>'+(mean?LAB.nf(mean,0)+'원':'계산 불가')+'</b><span>평균 가격</span></div>';
 var msg=[];if(!ST.brand)msg.push('브랜드 고유값이 '+Object.keys(brands).length+'개예요. Mixue가 다섯 가지로 흩어져 있어요.');if(!ST.price)msg.push('가격에 “원”·쉼표·“k”가 섞여 평균을 낼 수 없어요.');if(ST.price&&!ST.out)msg.push('평균 가격에 0원 결제가 섞여 있어 낮게 나와요.');if(!ST.dup)msg.push('A03이 두 줄이에요.');
 $('#w3o').innerHTML=msg.length?msg.join(' '):'다 씻었어요. 12줄 → 11줄(중복 1줄만 삭제), 브랜드 6개, 평균 가격 '+LAB.nf(mean,0)+'원, 대기 420분은 지우지 않고 is_event = 1로 표시했습니다.';}
$$('#w3fix button[data-k]').forEach(function(b){b.onclick=function(){ST[b.dataset.k]=1;b.setAttribute('aria-pressed','true');draw1();};});
$('#w3r').onclick=function(){Object.keys(ST).forEach(function(k){ST[k]=0;});$$('#w3fix button[data-k]').forEach(function(b){b.setAttribute('aria-pressed','false');});draw1();};draw1();
/* 2. 빈 값 처리 */
var D=V.csv(PAYCSV),vals=D.map(function(r){return r.amount;}),okv=vals.filter(function(v){return v!=null;});
var sorted=okv.slice().sort(function(a,b){return a-b;}),med=(sorted[383]+sorted[384])/2,sum=okv.reduce(function(a,b){return a+b;},0);
function draw2(m){$$('#w3m button').forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.m===m));});
 var arr=m==='zero'?vals.map(function(v){return v==null?0:v;}):m==='med'?vals.map(function(v){return v==null?med:v;}):okv;
 var mean=arr.reduce(function(a,b){return a+b;},0)/arr.length,rows=m==='drop'?768:800;
 $('#w3mk').innerHTML='<div><b>'+LAB.nf(mean,1)+'</b><span>평균 결제 금액</span></div><div><b>'+arr.length+'</b><span>평균에 쓴 값의 개수</span></div><div><b>'+rows+'행</b><span>표에 남은 행 (도시·채널 정보)</span></div><div><b style="color:'+(Math.abs(mean/(sum/768)-1)>.02?'#c9302c':'#13733a')+'">'+(100*(mean/(sum/768)-1)).toFixed(1)+'%</b><span>“두기” 평균과의 차이</span></div>';
 V.hist($('#w3mh'),{values:arr,lo:0,hi:5000,bin:250,unit:'결제 금액 (구간 폭 250)',h:240,refs:[{v:mean,label:'평균 '+LAB.nf(mean,0),color:'#b45309',dash:true}]});
 $('#w3mo').textContent={keep:'값이 있는 768건으로만 평균을 냅니다. 금액이 빈 32건의 도시·채널 정보는 표에 그대로 남습니다.',zero:'맨 왼쪽(0~250)에 없던 결제 32건이 생겼어요. 평균은 4.0% 낮아졌습니다.',med:'중앙값 '+LAB.nf(med,1)+'으로 채우면 평균은 거의 그대로지만, 가운데 구간에 같은 값 32개가 쌓입니다. 근거가 있을 때만 씁니다.',drop:'평균은 “두기”와 같지만, 금액이 빈 32건의 도시·채널 정보까지 표에서 사라졌어요(800 → 768행).'}[m];}
$$('#w3m button').forEach(function(b){b.onclick=function(){draw2(b.dataset.m);};});draw2('keep');
/* 3. 행 수 지키기 */
function draw3(){var n=1000,bad=0,flag=false;$$('#w3ops input').forEach(function(c){if(c.checked){n-=+c.dataset.n;if(c.dataset.ok==='0')bad++;if(c.dataset.k==='flag')flag=true;}});
 $('#w3rk').innerHTML='<div><b style="color:'+(n===970?'#13733a':'#c9302c')+'">'+LAB.nf(n)+'행</b><span>처리 후 행 수 (정답 970)</span></div><div><b>'+(flag?'예':'아니오')+'</b><span>이상치 표시 열(is_event)</span></div>';
 $('#w3ro').innerHTML=n===970&&flag&&!bad?'<b>정답.</b> 중복 30건만 지우고, 오타 값은 비우고, 실제 사건은 표시했어요. 기록 세 줄을 남기면 끝입니다.':n===970?'행 수는 맞았어요. 이상치 처리(값만 비우고 표시)도 함께 해야 끝납니다.':bad?'정답 970보다 '+(970-n)+'행 더 지웠어요. 형식·빈 값·이상치는 “지우기”가 아니라 “고치기·두기·표시”로 다룹니다.':'아직 중복이 남아 있어요.';}
$$('#w3ops input').forEach(function(c){c.onchange=draw3;});draw3();
/* 4. 고급 차트 */
var OK=D.filter(function(r){return r.amount!=null;});
function draw4(k){$$('#w3adv button').forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.k===k));});var el=$('#w3av');
 if(k==='box'){var G=V.box(el,{groups:[{name:'기존 고객',values:OK.filter(function(r){return !r.is_new_user;}).map(function(r){return r.amount;})},{name:'신규 고객',values:OK.filter(function(r){return r.is_new_user;}).map(function(r){return r.amount;})}],mean:true,lo:0,title:'신규 vs 기존 고객 — 결제 금액 상자그림',unit:'결제 금액',h:300});
  $('#w3ao').innerHTML='앰버 선 = 중앙값, ◆ = 평균. 기존 고객 중앙값 '+LAB.nf(G[0].med,0)+' · 신규 고객 '+LAB.nf(G[1].med,0)+'. 신규 고객 쪽이 낮고 흩어짐도 작아요. 동그라미는 1.5×IQR 밖의 이상치 후보('+(G[0].out.length+G[1].out.length)+'건)입니다.';}
 else if(k==='corr'){var cols=['hour','items','amount','is_new_user'],nm=['시간','상품 수','결제 금액','신규 여부'],m=cols.map(function(a){return cols.map(function(b){return V.stats(OK.map(function(r){return r[a];}),OK.map(function(r){return r[b];})).r;});});
  V.heat(el,{rows:nm,cols:nm,m:m,div:true,showVal:true,fmt:function(v){return v.toFixed(2);},cw:110,ch:40,L:80,title:'숫자 열끼리 상관 히트맵 (파랑 +, 앰버 −)'});
  $('#w3ao').textContent='가장 진한 짝은 상품 수 × 결제 금액(+0.56). 신규 여부 × 결제 금액은 −0.19로 약한 음의 관계. 대각선 1.00은 자기 자신과의 상관이라 볼 필요가 없어요.';}
 else{var wd=['월','화','수','목','금','토','일'],hrs=[];for(var h=10;h<=23;h++)hrs.push(h);var m2=wd.map(function(){return hrs.map(function(){return 0;});});
  D.forEach(function(r){var d=new Date(r.date+'T00:00:00').getDay(),w=(d+6)%7;if(r.hour>=10)m2[w][r.hour-10]++;});
  V.heat(el,{rows:wd,cols:hrs.map(String),m:m2,hlMax:true,showVal:true,cw:38,ch:30,title:'요일 × 시간(10~23시) 주문 수 — 가장 많은 셀은 앰버 테두리'});
  $('#w3ao').textContent='가장 진한 셀은 금요일 12시(16건). 점심 무렵(11~13시)과 저녁(18~21시)에 진한 셀이 모여요. 결정 전에 “한 달에 금요일이 4번뿐인데 16건이 우연은 아닐까?”를 한 번 물어보세요.';}}
$$('#w3adv button').forEach(function(b){b.onclick=function(){draw4(b.dataset.k);};});draw4('box');
'''
)
for _s in PAGE['steps']:
    _s['def'] = {'lv1': '그리기 전에 표기·형식·빈 값·중복·이상치를 찾고 고치고 확인하는 일.', 'lv2': '빈 값을 지우기·채우기·두기 중에서 근거에 맞게 고르는 일. 0 채우기는 평균을 낮춘다.',
                 'lv3': 'AI의 전처리를 코드로 받고, 행 수를 비교하고, 이상치를 지우기 전에 표시하는 세 규칙.', 'lv4': 'Seaborn으로 빠르게 그리고 Matplotlib으로 다듬는 역할 나누기와 상자그림·상관 히트맵·요일×시간 히트맵.'}[_s['id']]
    if 'mathbox' in _s:
        _s['mathbox']['try'] = _s['mathbox'].pop('try_')
