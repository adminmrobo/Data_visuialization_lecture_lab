# 12주차 — 대시보드: Google AI Studio로 산업별 대시보드 완성 (조별발표)
PAGE = dict(
num='12', slug='ai-studio-dashboard', kind='lecture', scene='team', short='12주', chip='12주차', floor='12층 대시보드 공방',
scene_line='두 조가 세 산업(헬스케어·의료·핀테크) 대시보드를 같은 순서로 만들어 발표합니다',
title='차트 셋이 함께 움직이면 판이 된다', title_en='Dashboards with Google AI Studio across industries',
subtitle='쉬운 일은 Qwen으로, 어려운 일은 AI Studio로 — 다섯 번 이어 묻기, 필터, 답하는 제목',
toc='대시보드와 필터, Qwen과 Google AI Studio의 역할 나누기, Q1·Q2·S1·S2·S3, 헬스케어·의료·핀테크 세 화면, 답하는 제목',
kicker='데이터시각화 · 12주차 · 대시보드 구축 — Google AI Studio로 산업별 대시보드',
question='차트 세 개를 한 화면에 놓으면, 그것만으로 대시보드일까?',
desc='데이터 시각화 12주차 해설: 대시보드는 필터로 함께 움직이는 차트들의 판이다. 표 설명과 차트 하나는 Qwen, 여러 차트와 필터가 함께 움직이는 화면은 Google AI Studio로 나누고, Q1·Q2·S1·S2·S3 다섯 번 이어 물어 헬스케어·의료 데이터·핀테크 대시보드를 완성한다.',
intro='<p>12층 대시보드 공방. 11층에서는 차트 하나를 다섯 번 이어 물어 완성했습니다. 오늘은 차트 <b>셋</b>을 한 화면에 모으고, 필터 하나를 누르면 셋이 함께 바뀌게 만듭니다. 주판봇 조는 Qwen 하나로 끝까지 가 보겠다고 하고, 초파리 조는 중간에 도구를 바꾸겠다고 합니다. 박사의 규칙: <b>“쉬운 일은 Qwen으로, 어려운 일은 AI Studio로.”</b></p>',
first3=('차트 셋 · 필터 하나 · 질문에 답하는 제목 하나로 된 대시보드를, 생성 AI 두 가지(Qwen, Google AI Studio)를 나눠 써서 다섯 번 이어 물어 만듭니다.',
        '차트를 한 장씩 보는 것과 필터로 함께 움직이는 화면은 다릅니다. “내과만, 월요일 오전”처럼 좁혀 묻는 질문에 바로 답할 수 있어야 결정이 빨라집니다.',
        '병원 운영, 앱 서비스 기획, 개인 건강 관리까지 — 보는 사람이 원하는 숫자는 달라도 화면을 만드는 순서는 같습니다.'),
abbr=[('AI Studio', 'Google AI Studio — 구글의 생성 AI 작업 화면. 대시보드 같은 여러 부품을 한꺼번에 만든다'), ('Q1·Q2', 'Qwen에게 묻는 두 번(표 설명 · 차트 하나)'), ('S1·S2·S3', 'AI Studio에게 묻는 세 번(뼈대 · 필터 · 다듬기)')],
kpis=[('3 · 1 · 1', '차트 셋 · 필터 하나 · 답하는 제목 하나'), ('5번', 'Q1 → Q2 → S1 → S2 → S3'), ('3산업', '헬스케어 · 의료 데이터 · 핀테크'), ('0건', '올리는 진짜 개인 정보')],
kpi_note='세 산업의 데이터는 원자료와 같은 열 구조로 이 페이지가 만든 수업용 가상 데이터(시드 고정)입니다. 진짜 병원 기록·카드 내역은 올리지 않습니다.',
hero_talk=[
 ('robo', 'happy', '우리 조는 Qwen 하나로 끝까지 간다! 도구 바꾸는 건 귀찮아!'),
 ('fly', 'clip', '같은 오류가 두 번 나면 도구를 바꾸는 편이 빨라. 원자료에 그렇게 적혀 있어.'),
 ('doc', 'front', '대시보드는 자동차 계기판입니다. 속도·연료·경고등이 <b>한눈에</b>. 필터를 누르면 다 같이 바뀌어야 판이에요.'),
 ('x3', 'smile', '헬스케어 화면 뼈대는 제가 맡을게요.')],
crew=[('doc', 'front', '심판, 계기판 원칙'), ('fly', 'clip', '초파리 조 조장 — 의료 데이터 화면'), ('robo', 'happy', '주판봇 조 조장 — 핀테크 화면'),
      ('asst', 'think', '초파리 조 · 필터 연결'), ('sia', 'explain', '초파리 조 · 제목 다듬기'), ('x1', 'think', '초파리 조 · 주석'), ('moa', 'report', '주판봇 조 · 이상 거래 기록'), ('x3', 'smile', '주판봇 조 · 헬스케어 뼈대')],
recap='11주차: 좋은 차트는 이어 묻는 프롬프트에서 나온다. 역할·데이터·요청·조건, 한 번에 하나씩, 같은 대화창에서. 히트맵과 파레토.',
prereq=['11'],
why_title='왜 대시보드인가 — 차트 하나는 사진 한 장, 셋이 함께 움직이면 판',
why=[('판', '차트 하나는 사진 한 장입니다. 차트 셋이 같은 필터에 묶여 함께 움직이면 “판”이 됩니다.'),
     ('필터', '보고 싶은 것만 골라 보는 단추. 누르면 화면 전체가 다시 그려집니다.'),
     ('도구 나누기', '묻고 답하기는 Qwen, 여러 부품을 한꺼번에 맞추는 일은 AI Studio. 같은 오류가 두 번이면 도구를 바꿉니다.')],
bigpicture='''<div class="tbl"><table><thead><tr><th>단계</th><th>도구</th><th>헬스케어</th><th>의료 데이터</th><th>핀테크</th></tr></thead><tbody>
<tr><td>Q1 · Q2</td><td>Qwen</td><td>걸음 수 차트 하나</td><td>진료과 막대 하나</td><td>거래액 선 하나</td></tr>
<tr><td>S1 뼈대</td><td>AI Studio</td><td colspan="3">세 차트 뼈대 (산업마다 [역할]·[데이터]만 바뀜)</td></tr>
<tr><td>S2 필터</td><td>AI Studio</td><td>기간 필터</td><td>진료과 필터</td><td>결제 수단 필터</td></tr>
<tr><td>S3 다듬기</td><td>AI Studio</td><td>제목·색 다듬기</td><td>붐비는 셀 주석</td><td>이상 거래 강조</td></tr></tbody></table></div>
<p style="font-size:14px;color:#5b6874">원자료의 정리표입니다. 산업이 달라도 묻는 순서는 같고, 바뀌는 것은 [역할]과 [데이터]의 낱말뿐입니다.</p>''',
why_say=('doc', 'board', '세 번째 산업쯤 되면 순서가 손에 익어요. 그게 오늘의 목표입니다.'),
steps=[
dict(id='lv1', short='판과 필터', title='대시보드는 판이다 — 차트, 필터, 답하는 제목', concept='대시보드와 필터', en='dashboard and linked filters', cid='lab:concept/dashboard-filter',
 tag='방법: 차트 셋 · 필터 하나 · 제목 하나', analogy='자동차 계기판',
 where='<b>①판과 필터</b> → ②도구 나누기와 다섯 번 → ③세 산업 화면 → ④답하는 제목',
 situation='병원 운영 담당자가 묻습니다. “내과만 놓고 보면, 언제 가장 붐비고 대기 시간은 어떻게 변했어?” 차트 세 장이 따로 있는 보고서로는 몇 번을 넘겨 봐야 답할 수 있을까요?',
 whybox=dict(problem='차트가 여러 장이면 같은 조건(예: 내과만)을 장마다 다시 찾아 읽어야 합니다.',
             limit='차트를 한 화면에 모으기만 하면 “모음”일 뿐, 조건을 바꿀 때마다 세 장을 각각 다시 만들어야 합니다.',
             solution='차트 셋을 <b>필터 하나</b>에 묶습니다. 필터를 고르면 세 차트가 다 같이 바뀌고, 제목은 질문에 답하는 문장이 됩니다.',
             easy='자동차 계기판: 속도·연료·경고등이 한 판에 있고, 운전 모드를 바꾸면 계기판 전체가 그 모드로 바뀝니다.'),
 pair=(('일상으로 치면', '쇼핑 앱의 필터 — “운동화 · 270mm · 3만 원 이하”를 고르면 목록·가격 그래프·리뷰 요약이 함께 바뀝니다.'),
       ('대시보드에서는', '세 화면 모두 — 차트 3개 · 필터 1개 · 질문을 답하는 제목 하나. 4주차의 대시보드 5원칙(한 화면 한 결론, 왼쪽 위부터, 강조는 색, 단위·기간·출처, 여백)이 그대로 적용됩니다.')),
 talk=[('asst', 'think', '필터가 있는 판과 없는 모음의 차이를 3단계 화면에서 직접 눌러 보며 확인할게요.'),
       ('robo', 'chart', '차트를 스무 장 넣으면 필터 없이도 다 볼 수 있잖아!'),
       ('fly', 'arms', '스무 장에서 “내과만”을 찾으려면 스무 번 읽어야 해. 필터 하나면 한 번이야.')],
 panel='<div id="w12pk"></div>',
 panel_title='직접 해 보기 — 판인가, 모음인가',
 sim='판과 모음 구분 게임',
 docline='대시보드의 단위는 차트가 아니라 <b>질문</b>입니다. 필터는 그 질문을 좁히는 단추입니다.',
 limit='무엇을 만들지는 정했습니다. 이제 어떤 도구로, 몇 번에 나눠 만들지 정합니다.', limit_label='도구와 순서를 아직 정하지 않음',
 quiz=[dict(q='원자료가 말하는 세 화면의 공통 구성은?', o=['차트 10개 · 필터 5개', '차트 3개 · 필터 1개 · 질문에 답하는 제목 1개', '표 1개', '지도 1개 · 차트 1개'], a=1, why='“세 화면 모두 — 차트 3개 · 필터 1개 · 질문을 답하는 제목 하나.”'),
       dict(q='필터를 고르면 무엇이 바뀌어야 하나?', o=['제목만', '첫 번째 차트만', '세 차트가 다 같이', '색만'], a=2, why='필터를 누르면 화면 전체가 다시 그려져야 “판”입니다.')]),
dict(id='lv2', short='다섯 번', title='쉬운 일은 Qwen, 어려운 일은 AI Studio — Q1 · Q2 · S1 · S2 · S3', concept='도구 나누기와 대시보드 사슬', en='tool split and dashboard prompt chain', cid='lab:concept/tool-split',
 tag='방법: 묻고 답하기는 Qwen, 부품 맞추기는 AI Studio', analogy='동네 문구점과 인쇄소',
 where='①판과 필터 → <b>②도구 나누기와 다섯 번</b> → ③세 산업 화면 → ④답하는 제목',
 situation='주판봇 조가 Qwen에게 “차트 세 개에 필터까지 연결해 줘”라고 했더니, 필터를 눌러도 두 번째 차트가 그대로입니다. 고쳐 달라고 했더니 같은 오류가 또 났습니다. 어떻게 할까요?',
 whybox=dict(problem='대시보드는 여러 부품(차트 셋 + 필터 + 제목)을 한꺼번에 맞춰야 합니다.',
             limit='묻고 답하는 데 강한 도구로 부품 맞추기를 끝까지 시키면, 같은 오류가 되풀이되기 쉽습니다.',
             solution='<b>Qwen</b>: 표 설명 듣기 · 질문 정하기 · 차트 하나(Q1·Q2). <b>Google AI Studio</b>: 차트 3개 이상이 함께 움직이는 대시보드 · 필터 · 지도·움직이는 그림(S1·S2·S3). 같은 오류가 두 번 나면 도구를 바꿉니다.',
             easy='엽서 한 장은 동네 문구점에서, 책 한 권 제본은 인쇄소에서. 도구마다 잘하는 일이 다릅니다.'),
 pair=(('AI Studio 화면', '브라우저에서 aistudio.google.com → 수업용 구글 계정으로 로그인 → 만들기(Build) 화면. 왼쪽은 프롬프트를 쓰는 입력창(여러 번 이어 입력), 오른쪽은 AI가 만든 화면의 미리 보기. 마음에 안 들면 바로 아래에 다시 씁니다. 메뉴 이름과 단추 위치는 자주 바뀝니다(원자료는 “Make 탭”으로 적음).'),
       ('지켜야 할 것', '진짜 개인 정보는 올리지 않는다 — 내 병원 기록, 내 카드 내역 금지. 수업용 가상 데이터 또는 공공 통계만. 대시보드에 “수업용 가상 데이터”라고 적는다. 내 화면이 달라도 정상 — 결과는 매번 조금씩 다르다.')),
 body='''<div class="prompt"><span class="lang">한</span>[역할] 너는 헬스케어 데이터 분석가야.
[데이터] 올린 파일은 하루별 건강 기록이고, 열은 날짜, 걸음 수, 수면 시간, 평균 심박이야.
[요청] 대시보드 뼈대를 만들어 줘. 차트는 세 개야: ①걸음 수 추세선 ②수면 달력 히트맵 ③목표 달성 게이지.
[조건] 제목은 한국어, 단위 표시, 색은 3가지 이내, “수업용 가상 데이터” 표기.</div>
<p style="font-size:14px;color:#5b6874">원자료의 S1(뼈대) 프롬프트입니다. 입력 순서: CSV 파일 올리기 → 프롬프트 붙여넣기 → 실행. 산업이 바뀌면 [역할]과 [데이터]의 낱말만 바꿉니다.</p>''',
 talk=[('sia', 'explain', '아래 일들을 Qwen과 AI Studio로 나눠 볼게요.'),
       ('robo', 'sigh', '같은 오류가 두 번… 도구를 바꾸는 게 지는 것 같았는데.'),
       ('fly', 'coffee', '지는 게 아니라 일을 맞는 공구에 맡기는 거야.')],
 panel='<div id="w12tool"></div>',
 panel_title='직접 해 보기 — 이 일은 어느 도구로',
 sim='Qwen과 AI Studio 일 나누기',
 flow=dict(id='fl12', title='다섯 번 이어 묻기 — 도구가 바뀌는 지점', h=220, alt='Q1 표 설명, Q2 차트 하나는 Qwen, S1 뼈대, S2 필터, S3 다듬기는 AI Studio로 이어지는 흐름',
   cap='Q2에서 S1으로 넘어갈 때 도구가 바뀝니다. 전환 이유 한 줄: “차트가 셋 이상이고, 필터가 함께 움직여야 한다.”',
   js='{stations:["Q1 표 설명","Q2 차트 하나","S1 뼈대","S2 필터","S3 다듬기"],items:[["Qwen ✓","Qwen ✓","AI Studio ✓","AI Studio ✓","AI Studio ✓"],["Qwen ✓","Qwen ✓","Qwen ✗","Qwen ✗ (같은 오류)","→ AI Studio로"]],bad:function(it,i){return /✗/.test(it[i]);},stamp:"원자료 순서"}'),
 explain='<p><b>자주 빠지는 곳 세 가지</b>(원자료): ① 한 번에 다 만들려고 하기 ② 전 단계 결과를 안 보여 주고 넘기기 ③ 화면이 달라지자마자 포기하기. 막혔을 때 쓸 문장: “화면이 안 나와. 원인을 쉬운 말로 설명하고 고쳐 줘.” 두 번 막히면 도구를 바꾸거나 질문을 더 짧게 다시 씁니다.</p>',
 docline='“전 단계의 결과가 다음 단계의 시작이다 — 그래서 이어 물어야 한다.” 도구가 바뀌어도 이 원칙은 같습니다.',
 limit='도구와 순서를 정했습니다. 이제 세 산업의 화면을 직접 눌러 보며, 필터가 세 차트를 함께 움직이는지 확인합니다.', limit_label='필터 연결을 직접 확인하지 않음',
 quiz=[dict(q='“차트 세 개가 함께 움직이고 필터로 연결된 화면”을 만들 때 원자료가 권하는 도구는?', o=['Qwen', 'Google AI Studio', '엑셀', '메모장'], a=1, why='여러 부품을 한꺼번에 맞춰야 하는 일은 AI Studio입니다.'),
       dict(q='Qwen에서 같은 오류가 두 번 났을 때 원자료의 처방은?', o=['같은 프롬프트를 열 번 더 보낸다', '도구를 바꾸거나 질문을 더 짧게 다시 쓴다', '포기한다', '개인 정보를 올린다'], a=1, why='“Qwen에서 같은 오류가 두 번 나면? → 도구를 바꾸는 편이 빠르다.”')]),
dict(id='lv3', short='세 화면', title='세 산업의 판 — 헬스케어 · 의료 데이터 · 핀테크', concept='산업별 대시보드', en='industry dashboards healthcare medical fintech', cid='lab:concept/industry-dashboards',
 tag='현장: 보는 사람이 원하는 숫자가 다르다', analogy='같은 계기판, 다른 차종',
 where='①판과 필터 → ②도구 나누기와 다섯 번 → <b>③세 산업 화면</b> → ④답하는 제목',
 situation='세 화면의 모양은 비슷합니다. 그런데 헬스케어 화면을 보는 “나 자신”, 병원 운영 담당자, 핀테크 서비스 기획자가 가장 먼저 찾는 숫자는 다릅니다. 각자 무엇을 먼저 볼까요?',
 whybox=dict(problem='같은 틀(차트 셋 + 필터)로 산업을 바꾸면 어떤 차트와 필터를 넣을지 다시 정해야 합니다.',
             limit='보는 사람을 생각하지 않고 차트를 고르면, 모양은 대시보드인데 아무 결정도 돕지 못합니다.',
             solution='산업마다 <b>보는 사람 → 알고 싶은 것 → 필터</b>를 먼저 정합니다. 헬스케어(나 자신 · 습관 변화 · 기간), 의료 데이터(병원 운영 담당자 · 어디에 언제 몰리나 · 진료과), 핀테크(서비스 기획자 · 돈이 언제 어디에 · 결제 수단).',
             easy='계기판 모양은 비슷해도 트럭 운전사는 적재량을, 경주차 운전사는 회전수를 먼저 봅니다.'),
 mathbox=dict(q='헬스케어 화면의 “목표 달성 게이지”는 어떻게 계산해요?', school='초등 백분율',
   doc='실제 값을 목표 값으로 나누고 100을 곱하면 달성률이에요. 기간 필터를 바꾸면 “실제 값”(기간 평균)이 바뀌어서 게이지도 함께 움직입니다.',
   rows=[('기간 평균 걸음 수', '필터로 고른 기간의 하루 평균'), ('÷ 목표 걸음 수', '예: 하루 8,000보'), ('× 100', '달성률(%) — 게이지 바늘의 위치')],
   try_='최근 한 달 평균 7,200보 ÷ 목표 8,000보 × 100 = <b>90%</b><br>이번 주 평균 8,400보 ÷ 8,000 × 100 = <b>105%</b> (목표 초과)',
   comment='필터를 바꾸면 분자가 바뀌니까 게이지가 같이 움직이는 거네요. 이게 “함께 움직인다”는 뜻이고요.'),
 pair=(('헬스케어 — 나 자신', '질문: 내 생활 습관은 어떻게 변했나? 차트: ①걸음 수 추세선 ②수면 히트맵(어두울수록 오래 잠) ③목표 게이지. 필터: 이번 주 / 최근 한 달 / 최근 3개월.'),
       ('의료 데이터 · 핀테크', '의료 — 질문: 환자가 어디에, 언제 몰리나? 차트: ①진료과별 막대 ②요일×시간 히트맵 ③대기 시간 추세. 필터: 전체/내과/외과/소아과. 핀테크 — 질문: 돈은 언제, 어디에 쓰이나? 차트: ①일별 거래액 선 ②업종별 막대 ③금액 산점도(이상 거래 강조). 필터: 전체/카드/간편결제.')),
 talk=[('x3', 'smile', '세 산업 화면을 탭으로 만들었어요. 필터를 바꾸면 세 차트가 다 바뀌는지 확인해 주세요.'),
       ('robo', 'wow', '핀테크 산점도에 튀어나온 점이 있어! 이게 이상 거래야?'),
       ('fly', 'magnify', '“후보”야. 평소 패턴과 확실히 다르다는 것까지만. 그 거래의 업종과 시간을 먼저 확인해.'),
       ('moa', 'report', '이상 거래 기록은 제가 따로 모아 둘게요. 계좌번호 같은 건 데이터에 없어요.')],
 panel='''<div class="chips" id="w12ind"><button type="button" class="bt" data-k="h" aria-pressed="true">헬스케어</button><button type="button" class="bt" data-k="m">의료 데이터</button><button type="button" class="bt" data-k="f">핀테크</button></div>
<div class="ctrl" id="w12flt"></div>
<h3 id="w12title" style="margin:6px 0"></h3>
<div class="grid2"><div id="w12c1" class="viz"></div><div id="w12c2" class="viz"></div></div><div id="w12c3" class="viz"></div>
<p style="font-size:13px;color:#5b6874;margin:4px 0">수업용 가상 데이터</p><div class="insight" id="w12o" aria-live="polite"></div>''',
 panel_title='직접 해 보기 — 필터 하나로 세 차트가 함께 움직이는 판',
 sim='세 산업 대시보드',
 explain='<p>해석 세 문장 예(원자료): 헬스케어 — 걸음은 늘고 있다 · 수면은 주중 밤에 짧아지는 것 같다(추측) · 주말 수면을 먼저 지켜보자. 의료 — 월요일 오전이 제일 붐빈다 · 외래 예약 집중 때문인 것 같다(추측) · 월요일 오전 인력을 한 명 더 배치하자. 핀테크 — 토요일 밤 금액이 튀었다 · 큰 이벤트 결제일 수 있다(추측) · 그 거래의 업종과 시간을 먼저 확인하자. 이 페이지의 가상 데이터는 원자료와 같은 열 구조로 만들었기 때문에, 패턴은 비슷하지만 숫자는 원자료 화면과 다릅니다.</p>',
 aicheck='<p>AI Studio가 핀테크 화면의 산점도에서 이상 거래를 빨간 점으로 강조하고, 제목을 “토요일 밤 카페 결제는 사기”라고 달았습니다. <b>점검</b>: ① 데이터의 “이상 거래 여부”는 “평소와 다른 거래”라는 표시일 뿐, 사기라는 판정이 아니다 ② 제목이 단정(T4와 같은 실수)을 하고 있다 ③ 다음 행동은 “차단”이 아니라 “확인”이어야 한다. 고친 제목: “토요일 밤, 카페 업종에서 큰 금액이 튀었다.”</p>',
 docline='산업이 바뀌면 <b>보는 사람</b>이 바뀌고, 보는 사람이 바뀌면 필터가 바뀝니다. 만드는 순서는 그대로입니다.',
 limit='세 화면이 움직입니다. 마지막으로 제목 — “건강 데이터 대시보드”와 “최근 한 달, 걸음 수는 늘고 수면은 줄었다”의 차이를 봅니다.', limit_label='제목이 아직 답하지 않음',
 quiz=[dict(q='한 달 평균 걸음 수 6,800보, 목표 8,000보일 때 달성률은?', o=['68%', '85%', '118%', '80%'], a=1, why='6,800 ÷ 8,000 × 100 = 85%.'),
       dict(q='의료 데이터 화면에서 필터로 가장 알맞은 것은?', o=['결제 수단', '진료과', '수면 시간', '업종'], a=1, why='병원 운영 담당자는 “어느 과가 언제 붐비나”를 봅니다. 진료과 필터가 세 차트를 묶습니다.')]),
dict(id='lv4', short='답하는 제목', title='제목이 답한다 — 판을 결정으로 끝내기', concept='답하는 제목', en='titles that answer the question', cid='lab:concept/answering-title',
 tag='방법: “무엇에 대한 화면” → “무엇이 일어났나”', analogy='신문 헤드라인',
 where='①판과 필터 → ②도구 나누기와 다섯 번 → ③세 산업 화면 → <b>④답하는 제목</b>',
 situation='세 화면의 제목이 “건강 데이터 대시보드”, “병원 방문 데이터 대시보드”, “결제 데이터 대시보드”입니다. 회의에 들어온 팀장은 이 제목에서 무엇을 알 수 있을까요?',
 whybox=dict(problem='대시보드 제목은 보통 “무엇에 대한 화면인가”로 짓습니다.',
             limit='그런 제목은 아무것도 답하지 않아서, 보는 사람이 세 차트를 다 읽고 결론을 스스로 찾아야 합니다.',
             solution='S3에서 제목을 <b>질문에 답하는 문장</b>으로 바꿉니다. 강조는 가장 중요한 차트 하나만, 주석은 가장 중요한 지점 하나만.',
             easy='신문 헤드라인은 “경제 기사”가 아니라 “금리 0.25%p 인상”입니다. 제목만 읽어도 무슨 일이 있었는지 압니다.'),
 pair=(('Before', '“건강 데이터 대시보드” · “병원 방문 데이터 대시보드” · “결제 데이터 대시보드” — 무엇에 대한 화면인지만 말한다.'),
       ('After', '“최근 한 달, 걸음 수는 늘고 수면은 줄었다” · “월요일 오전, 내과가 가장 붐빈다” · “토요일 밤, 카페 업종에서 큰 금액이 튀었다” — 제목만 읽어도 결론이 보인다.')),
 talk=[('sia', 'explain', '제목 세 개를 Before → After로 바꿔 보는 연습을 해 볼게요.'),
       ('robo', 'meh', '제목에 결론을 쓰면 틀렸을 때 창피하잖아.'),
       ('doc', 'think', '그래서 제목은 <b>데이터가 보여 준 것</b>까지만 씁니다. 원인은 추측이라고 밝히고요. 틀리지 않는 제목이 아니라, 확인할 수 있는 제목입니다.'),
       ('x1', 'think', '주석은 가장 붐비는 셀 하나에만 달게요.')],
 panel='<div id="w12ttl"></div>',
 panel_title='직접 해 보기 — 답하는 제목 고르기',
 sim='답하는 제목 고르기',
 explain='<p>원자료 마지막 장의 세 줄: ① 차트 하나는 Qwen으로, 판은 AI Studio로 ② 다섯 번 이어 묻는다 — Q1 → Q2 → S1 → S2 → S3 ③ 산업이 바뀌어도 질문의 순서는 <b>그대로</b>다 — 보는 사람이 누구인지부터. (원자료 3번 줄의 “질문의 순서는 바뀐다”는 앞 장의 “산업이 달라도, 묻는 순서는 같았다”와 맞지 않아 이 페이지에서는 “그대로다”로 바꿉니다.)</p><p><b>과제</b>(원자료): 내가 고른 산업(카페 매출 · 도서관 이용 기록 · 운동 기록 · 학교 식단 등)으로, 열 5~8개 · 1,000행 안팎 · 개인 정보 없는 가상 데이터를 준비해 Q1 → Q2 → S1 → S2 → S3 순서로 대시보드를 만들고, 완성 화면 + “이 대시보드가 답한 질문은 ○○이다” 한 문장을 냅니다.</p>',
 docline='제목이 답하고, 주석이 이유를 가리키고, 필터가 질문을 좁힙니다. 그러면 판은 <b>결정</b>으로 끝납니다.',
 limit='12층까지 개관했습니다. 13층은 카페 주문 데이터로 Qwen 이어 묻기를 내 손으로 끝까지 따라 하는 실습이고, 14층(종합 실습)은 준비 중, 15층은 기말 쇼케이스입니다. 배운 것을 바로 돌려 보고 싶다면 옥상 실전 연습장으로 가세요.', limit_label='배운 것을 한 시뮬레이터에서 묶어 본 적이 없음',
 quiz=[dict(q='다음 중 “질문에 답하는 제목”은?', o=['핀테크 결제 대시보드', '결제 데이터 분석 화면 v2', '토요일 밤, 카페 업종에서 큰 금액이 튀었다', '대시보드'], a=2, why='제목만 읽어도 무엇이 일어났는지 압니다.'),
       dict(q='원자료의 “산업이 바뀌어도 질문의 순서는 바뀐다”를 이 페이지가 “그대로다”로 바꾼 이유는?', o=['오타를 고치려고 — 앞 장의 “묻는 순서는 같았다”와 맞추려고', '순서가 정말 바뀌어서', '분량을 줄이려고', '번역 때문에'], a=0, why='같은 자료 안에서 “산업이 달라도 묻는 순서는 같았다”고 정리했으므로, 같은 뜻으로 맞췄습니다.')]),
],
duel=dict(q='필터로 묶은 판 vs 차트 스무 장 모음', step=0,
 intro='의료 데이터로 운영 담당자의 질문 다섯 개에 답합니다. 초파리 조는 차트 셋 + 진료과 필터 하나, 주판봇 조는 필터 없이 차트 스무 장을 한 화면에 깔았습니다. 심판은 <b>3분 안에 답한 질문 수</b>를 셉니다.',
 fly_pick='차트 셋 + 필터 하나', fly_line='“내과만”이면 필터를 한 번 누르면 돼. 세 차트가 다 내과로 바뀌어.',
 robo_pick='필터 없는 차트 스무 장', robo_line='스무 장이면 없는 게 없지! 다 들어 있어!',
 metric='3분 안에 답한 질문 수 (5개 중)',
 run='var Q=["가장 붐비는 진료과는?","내과가 가장 붐비는 요일·시간은?","소아과 대기 시간은 늘고 있나?","외과의 월요일 오전 환자 수는?","전체 대기 시간 추세는?"];var fly=[1,1,1,1,1],robo=[1,0,0,0,1];var c=function(a){return a.reduce(function(x,y){return x+y;},0);};return {fly:c(fly),robo:c(robo),flyTxt:c(fly)+"개",roboTxt:c(robo)+"개",miss:Q.filter(function(_,i){return !robo[i];})};',
 announce='return "초파리 조 "+r.flyTxt+", 주판봇 조 "+r.roboTxt+"예요. 주판봇 조가 못 답한 질문: "+r.miss.join(" / ")+" — 모두 “특정 진료과만” 좁혀 보는 질문이에요.";',
 verdict='if(res==="F")return "초파리 조 승. 차트가 많다고 질문에 답하는 것이 아니다. <b>좁혀 묻는 질문</b>에는 필터가 답한다.";return "결과를 다시 보자.";',
 after='<p style="font-size:14px;color:#5b6874">답한 질문 수는 “필터 없이 진료과를 좁혀 보는 질문에는 3분 안에 답하기 어렵다”는 가정의 설명용 예시입니다.</p>'),
summary='''<div class="tbl"><table><thead><tr><th>#</th><th>오늘 배운 것 (원자료 세 줄)</th><th>한 줄</th></tr></thead><tbody>
<tr><td>1</td><td>차트 하나는 Qwen으로, 판은 AI Studio로</td><td>같은 오류가 두 번이면 도구를 바꾼다</td></tr>
<tr><td>2</td><td>다섯 번 이어 묻는다</td><td>Q1 표 설명 → Q2 차트 하나 → S1 뼈대 → S2 필터 → S3 제목·색·주석</td></tr>
<tr><td>3</td><td>산업이 바뀌어도 질문의 순서는 그대로</td><td>보는 사람이 누구인지부터 — 바뀌는 것은 [역할]·[데이터]의 낱말</td></tr></tbody></table></div>
<p><b>확인 세 가지</b>(산업마다): ① 차트 세 개가 한 화면에 있다 ② 필터를 누르면 차트가 함께 바뀐다 ③ “수업용 가상 데이터” 표기가 있다(의료는 가장 붐비는 셀 주석, 핀테크는 이상 거래 강조도).</p>''',
outro=[('doc', 'judge', '조별발표 판정. 초파리 조의 판이 이겼다. 다만 오늘 가장 좋은 장면은 주판봇 조가 <b>같은 오류 두 번 만에 도구를 바꾼</b> 것이다.'),
       ('robo', 'happy', 'AI Studio로 바꾸니까 필터가 한 번에 붙었어! 도구 바꾸기, 생각보다 안 졌어!'),
       ('asst', 'spark', '필터를 바꾸면 게이지까지 같이 움직이는 게 신기했어요. 분자가 바뀌어서였어요.'),
       ('x3', 'proud', '헬스케어 판 제목: “최근 한 달, 걸음 수는 늘고 수면은 줄었다.” 이걸로 할게요.'),
       ('fly', 'coffee', '13층이 열렸어. 카페 데이터로 다섯 번 이어 묻기를 직접 해 보자.')],
next_note='<p>다음 층(13층)에서는 카페 주문 데이터를 Qwen에 올리고 다섯 번 이어 물어, 막대 차트에서 히트맵까지 각자 손으로 만들고 세 문장으로 해석합니다. 14층(종합 실습)은 강의가 끝나는 대로 엽니다. 그동안 <b>옥상 실전 연습장</b>에서 카페·결제·건강검진·물류센터 시뮬레이터를 직접 운영해 볼 수 있습니다.</p>',
refs=[dict(id='w12_slides', type='document', title='산업별 데이터 시각화 — Google AI Studio로 대시보드를 완성하는 따라하기 실습 (40쪽)', who='안상선', issued={'date-parts': [[2026, 11, 12]]}, role='primary'),
      dict(id='aistudio', type='webpage', title='Google AI Studio', who='Google', URL='https://aistudio.google.com/', role='tool'),
      dict(id='qwen', type='webpage', title='Qwen Chat', who='Alibaba Cloud', URL='https://chat.qwen.ai/', role='tool')],
facts=[('F1', '세 산업 화면은 모두 차트 3개, 필터 1개, 질문에 답하는 제목 1개로 구성된다.', '원자료', 'w12_slides', 'lv1', '오늘 만들 대시보드'),
       ('F2', '표 설명·차트 하나는 Qwen, 차트 3개 이상과 필터가 함께 움직이는 화면은 Google AI Studio로 나눈다.', '원자료', 'w12_slides', 'lv2', '쉬운 일은 Qwen'),
       ('F3', '원자료 마지막 장의 “질문의 순서는 바뀐다”는 같은 자료의 “묻는 순서는 같았다”와 맞지 않는다.', '원자료', 'w12_slides', 'lv4', '오늘 배운 것')],
gloss={'필터': ('필터', '용어', '보고 싶은 것만 골라 보는 단추. 누르면 화면 전체가 다시 그려진다.', 'filter', 'lv1'),
       'Google AI Studio': ('Google AI Studio', '도구', '구글의 생성 AI 작업 화면. 여러 부품이 함께 움직이는 화면을 만들 때 쓴다.', 'google-ai-studio', 'lv2'),
       '게이지': ('게이지', '차트', '목표 대비 달성률을 바늘이나 막대 하나로 보여 주는 차트.', 'gauge', 'lv3'),
       '이상 거래': ('이상 거래', '용어', '평소 패턴과 확실히 다른 거래. 사기라는 판정이 아니라 확인할 후보.', 'anomalous-transaction', 'lv3'),
       '달성률': ('달성률', '용어', '실제 값 ÷ 목표 값 × 100.', 'achievement-rate', 'lv3')},
models=['세 산업(헬스케어 하루 기록 90일, 의료 방문 기록, 핀테크 결제 기록)의 데이터는 원자료와 같은 열 구조로 이 페이지가 만든 수업용 가상 데이터입니다(시드 고정).', '조별 대결의 답한 질문 수는 설명용 예시입니다.'],
cover_alt='선 그래프·히트맵·게이지 세 화면이 스위치 하나에 연결된 대시보드 판 앞에 아홉 식구가 선 픽셀 표지',
toc_faces=[('x3', 'smile'), ('robo', 'happy'), ('fly', 'clip')],
js='''var V=LAB.VIZ,$=LAB.$,$$=LAB.$$,R=LAB.rng(1212);
LAB.Pick($('#w12pk'),[
 {q:'차트 세 장을 PDF 세 쪽에 따로 넣은 보고서',a:1,why:'함께 움직이지 않는 “모음”입니다.'},
 {q:'진료과를 고르면 막대·히트맵·대기 시간 추세가 다 같이 바뀌는 화면',a:0,why:'필터 하나에 묶여 함께 움직이는 “판”입니다.'},
 {q:'차트 스무 장을 한 화면에 깔았지만 필터는 없는 화면',a:1,why:'한 화면에 있어도 함께 움직이지 않으면 모음입니다.'},
 {q:'기간(이번 주 / 한 달 / 3개월)을 고르면 추세선·히트맵·게이지가 함께 바뀌는 화면',a:0,why:'필터가 세 차트를 묶습니다 — 판입니다.'}],['판(대시보드)','모음']);
LAB.Pick($('#w12tool'),[
 {q:'“이 표에 뭐가 들어 있어? 열마다 쉬운 말로 설명해 줘.”',a:0,why:'묻고 답하기 — Qwen(Q1).'},
 {q:'“먼저 하나만 그려 줘. 날짜별 걸음 수 선 그래프.”',a:0,why:'차트 하나 — Qwen(Q2).'},
 {q:'“차트 세 개로 대시보드 뼈대를 만들어 줘.”',a:1,why:'여러 부품을 한꺼번에 — AI Studio(S1).'},
 {q:'“기간 필터를 달아서 세 차트가 다 같이 바뀌게 해 줘.”',a:1,why:'필터 연결 — AI Studio(S2).'},
 {q:'“거점별 물동량을 원 크기로 보여 주는 버블 지도를 만들어 줘.”',a:1,why:'지도·움직이는 그림 — AI Studio.'}],['Qwen','Google AI Studio']);
/* 가상 데이터 */
var DAYS=90,HL=[];for(var d=0;d<DAYS;d++){var wd=d%7,step=Math.round(6000+d*25+(wd>=5?-900:300)+(R()-.5)*2200),sl=+(6.9+(wd>=5?0.9:-0.3)-d*0.016+(R()-.5)*1.1).toFixed(1);HL.push({d:d,wd:wd,step:step,sleep:sl});}
var DEPT=['내과','외과','소아과','정형외과','피부과'],WDN=['월','화','수','목','금'],SLOT=['9시','10시','11시','13시','14시','15시','16시'],MD={};
DEPT.forEach(function(dp,di){MD[dp]=WDN.map(function(_,w){return SLOT.map(function(_,s){var base=[38,22,26,18,12][di]*(w===0?1.35:1)*(s<3?1.25:0.9);if(dp==='소아과'&&s>=4)base*=1.2;return Math.round(base*(0.8+0.4*R()));});});});
var WAIT={};DEPT.forEach(function(dp,di){var a=[];for(var k=0;k<12;k++)a.push(Math.round([24,15,18,14,9][di]+(dp==='소아과'?k*0.9:k*0.2)+(R()-.5)*4));WAIT[dp]=a;});
var CAT=['카페','쇼핑','교통','식당','편의점'],FT=[];for(var i=0;i<600;i++){var day=Math.floor(R()*28),wk=day%7,cat=CAT[Math.floor(R()*5)],pay=R()<.55?'카드':'간편결제',amt=Math.round(({'카페':5500,'쇼핑':42000,'교통':2400,'식당':14000,'편의점':6500})[cat]*(0.4+R()*1.3));var odd=false;if(R()<.012){amt=Math.round(amt*(18+R()*20));odd=true;}FT.push({day:day,wk:wk,cat:cat,pay:pay,amt:amt,odd:odd});}
FT.push({day:26,wk:5,cat:'카페',pay:'간편결제',amt:680000,odd:true});FT.push({day:26,wk:5,cat:'카페',pay:'카드',amt:640000,odd:true});
var IND={h:{flt:['이번 주','최근 한 달','최근 3개월'],cur:'최근 한 달'},m:{flt:['전체','내과','외과','소아과'],cur:'전체'},f:{flt:['전체','카드','간편결제'],cur:'전체'}},ind='h';
function draw(){var I=IND[ind];$$('#w12ind button').forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.k===ind));});
 $('#w12flt').innerHTML='<span style="font-size:14px;color:#5b6874">필터:</span>'+I.flt.map(function(f){return '<button type="button" class="bt" aria-pressed="'+(f===I.cur)+'" data-f="'+f+'">'+f+'</button>';}).join('');
 $$('#w12flt button').forEach(function(b){b.onclick=function(){I.cur=b.dataset.f;draw();};});
 var c1=$('#w12c1'),c2=$('#w12c2'),c3=$('#w12c3');
 if(ind==='h'){var n={'이번 주':7,'최근 한 달':30,'최근 3개월':90}[I.cur],S=HL.slice(DAYS-n),half=Math.floor(n/2),avg=function(a,k){return a.reduce(function(s,x){return s+x[k];},0)/a.length;};
  var st1=avg(S.slice(0,half),'step'),st2=avg(S.slice(half),'step'),sl1=avg(S.slice(0,half),'sleep'),sl2=avg(S.slice(half),'sleep');
  $('#w12title').textContent=I.cur+', 걸음 수는 '+(st2>st1?'늘고':'줄고')+' 수면은 '+(sl2<sl1?'줄었다':'늘었다');
  V.line(c1,{labels:S.map(function(x){return 'D'+(x.d+1);}),series:[{name:'걸음 수',values:S.map(function(x){return x.step;}),dots:n<=30}],y0:0,title:'① 걸음 수 추세 (보)',h:230});
  var weeks=Math.ceil(n/7),m=[];for(var w=0;w<7;w++){var r=[];for(var k=0;k<weeks;k++){var it=S[k*7+w];r.push(it?it.sleep:0);}m.push(r);}
  V.heat(c2,{rows:['1','2','3','4','5','6','7'].map(function(x){return x+'일째';}),cols:m[0].map(function(_,k){return (k+1)+'주';}),m:m,cw:Math.max(22,Math.min(60,Math.floor(400/weeks))),ch:22,L:52,title:'② 수면 시간 히트맵 (진할수록 오래 잠)'});
  var g=avg(S,'step'),pct=g/8000*100;V.bar(c3,{labels:['목표 8,000보 대비'],values:[pct],horizontal:true,yMax:Math.max(120,pct+5),ref:100,refLabel:'목표 100%',dec:0,unitShort:'%',title:'③ 목표 달성 게이지 — 기간 평균 '+LAB.nf(g)+'보',h:130,w:560,L:120,color:pct>=100?'#13733a':'#1e3a8a'});
  $('#w12o').textContent='기간 필터를 바꾸면 세 차트가 함께 바뀝니다. 게이지: 평균 '+LAB.nf(g)+'보 ÷ 8,000보 × 100 ≈ '+pct.toFixed(0)+'%.';}
 else if(ind==='m'){var ds=I.cur==='전체'?DEPT:[I.cur];var tot=DEPT.map(function(dp){return MD[dp].reduce(function(s,r){return s+r.reduce(function(a,b){return a+b;},0);},0);});
  var hm=WDN.map(function(_,w){return SLOT.map(function(_,s){return ds.reduce(function(a,dp){return a+MD[dp][w][s];},0);});});var best=[0,0,0];hm.forEach(function(r,w){r.forEach(function(v,s){if(v>best[0])best=[v,w,s];});});
  $('#w12title').textContent=WDN[best[1]]+'요일 '+SLOT[best[2]]+', '+(I.cur==='전체'?'병원이':I.cur+'가')+' 가장 붐빈다';
  V.bar(c1,{labels:DEPT,values:tot,hl:I.cur==='전체'?-1:DEPT.indexOf(I.cur),title:'① 진료과별 주간 환자 수 (명)',h:230});
  V.heat(c2,{rows:WDN,cols:SLOT,m:hm,hlMax:true,showVal:true,cw:44,ch:26,L:30,title:'② 요일 × 시간 환자 수 — 가장 붐비는 셀 주석'});
  var wl=WAIT[ds[0]].map(function(_,k){return Math.round(ds.reduce(function(a,dp){return a+WAIT[dp][k];},0)/ds.length);});V.line(c3,{labels:wl.map(function(_,k){return (k+1)+'주';}),series:[{name:'평균 대기 시간',values:wl,vlab:true}],y0:0,title:'③ 대기 시간 추세 (분) — '+I.cur,h:230});
  $('#w12o').textContent='진료과 필터를 바꾸면 히트맵과 대기 시간 추세가 함께 바뀌고, 막대에서는 고른 과가 강조됩니다. 소아과를 고르면 오후 대기가 늘어나는 모습이 보입니다.';}
 else{var F=FT.filter(function(t){return I.cur==='전체'||t.pay===I.cur;}),dd=[];for(var k=0;k<28;k++)dd.push(F.filter(function(t){return t.day===k;}).reduce(function(a,t){return a+t.amt;},0));
  var big=F.filter(function(t){return t.odd;}).sort(function(a,b){return b.amt-a.amt;})[0];
  var WKN=['월','화','수','목','금','토','일'];$('#w12title').textContent=big?(big.wk===5?'토요일 밤, ':WKN[big.wk]+'요일, ')+big.cat+' 업종에서 큰 금액이 튀었다':'평소와 다른 거래가 보이지 않는다';
  V.line(c1,{labels:dd.map(function(_,k){return (k+1)+'일';}),series:[{name:'일별 거래액',values:dd}],y0:0,title:'① 일별 거래액 (원)',h:230});
  V.bar(c2,{labels:CAT,values:CAT.map(function(c){return F.filter(function(t){return t.cat===c;}).reduce(function(a,t){return a+t.amt;},0);}),title:'② 업종별 거래액 (원)',h:230});
  var pts=F.map(function(t){return [t.day+1,t.amt];}),hl=[];F.forEach(function(t,i){if(t.odd)hl.push(i);});V.scatter(c3,{pts:pts,hl:hl,alpha:.35,xlab:'날짜 (일)',ylab:'금액 (원)',title:'③ 금액 산점도 — 앰버 점 = 이상 거래 후보',h:260,ylo:0});
  $('#w12o').textContent='결제 수단 필터를 바꾸면 세 차트가 함께 바뀝니다. 이상 거래 후보 '+hl.length+'건 — “사기”가 아니라 “평소와 다른 거래”입니다. 다음 행동은 업종과 시간 확인.';}}
$$('#w12ind button').forEach(function(b){b.onclick=function(){ind=b.dataset.k;draw();};});draw();
LAB.Pick($('#w12ttl'),[
 {q:'헬스케어 화면 제목 후보',a:1,why:'“최근 한 달, 걸음 수는 늘고 수면은 줄었다” — 제목이 질문에 답합니다.'},
 {q:'의료 데이터 화면 제목 후보',a:0,why:'“월요일 오전, 내과가 가장 붐빈다” — 어떤 셀이 중요한지 제목이 말합니다.'},
 {q:'핀테크 화면 제목 후보',a:1,why:'“토요일 밤, 카페 업종에서 큰 금액이 튀었다” — 사기라고 단정하지 않고 관찰만.'}],['After 제목 A','After 제목 B']);
'''
)
# 제목 고르기 게임 문구를 질문별 보기로 바꾼다 (보기 두 개 중 답하는 제목 고르기)
PAGE['js'] = PAGE['js'].replace("""LAB.Pick($('#w12ttl'),[
 {q:'헬스케어 화면 제목 후보',a:1,why:'“최근 한 달, 걸음 수는 늘고 수면은 줄었다” — 제목이 질문에 답합니다.'},
 {q:'의료 데이터 화면 제목 후보',a:0,why:'“월요일 오전, 내과가 가장 붐빈다” — 어떤 셀이 중요한지 제목이 말합니다.'},
 {q:'핀테크 화면 제목 후보',a:1,why:'“토요일 밤, 카페 업종에서 큰 금액이 튀었다” — 사기라고 단정하지 않고 관찰만.'}],['After 제목 A','After 제목 B']);""",
"""LAB.Pick($('#w12ttl'),[
 {q:'“건강 데이터 대시보드”',a:1,why:'무엇에 대한 화면인지만 말합니다. After: “최근 한 달, 걸음 수는 늘고 수면은 줄었다”.'},
 {q:'“월요일 오전, 내과가 가장 붐빈다”',a:0,why:'제목이 질문(어디에, 언제 몰리나)에 답합니다.'},
 {q:'“결제 데이터 대시보드”',a:1,why:'After: “토요일 밤, 카페 업종에서 큰 금액이 튀었다”.'},
 {q:'“토요일 밤 카페 결제는 사기다”',a:2,why:'답은 하지만 단정입니다. 이상 거래는 사기 판정이 아니라 확인할 후보 — 관찰까지만 씁니다.'},
 {q:'“최근 한 달, 걸음 수는 늘고 수면은 줄었다”',a:0,why:'기간·대상·변화가 모두 들어 있는 답하는 제목입니다.'}],['답하는 제목','답하지 않는 제목','답하지만 단정하는 제목']);""")
for _s in PAGE['steps']:
    _s['def'] = {'lv1': '차트 셋을 필터 하나로 묶어 함께 움직이게 하고 질문에 답하는 제목을 단 화면.', 'lv2': '묻고 답하기와 차트 하나는 Qwen, 여러 부품이 함께 움직이는 화면은 Google AI Studio로 나눠 다섯 번 이어 묻는 방법.',
                 'lv3': '헬스케어·의료 데이터·핀테크에서 보는 사람에 따라 차트와 필터를 고르는 산업별 대시보드.', 'lv4': '“무엇에 대한 화면” 대신 “무엇이 일어났나”를 말하는 제목으로 판을 결정으로 끝내는 일.'}[_s['id']]
    if 'mathbox' in _s:
        _s['mathbox']['try'] = _s['mathbox'].pop('try_')
