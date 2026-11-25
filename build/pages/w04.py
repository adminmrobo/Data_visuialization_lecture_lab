# 4주차 — 산업별 데이터 시각화 1: 금융/핀테크 (조별발표)
PAGE = dict(
num='04', slug='industry-fintech', kind='lecture', scene='team', short='4주', chip='04주차', floor='4층 산업관',
scene_line='초파리 조는 은행, 주판봇 조는 핀테크 화면을 맡아 나란히 발표합니다',
title='산업마다 보는 숫자가 다르다', title_en='Industry visualization 1: finance and fintech',
subtitle='산업 분류(GICS·X-Tech), 시각 부호화의 정확도, 차트 고르기 표, 은행 vs 핀테크, 대시보드 원칙과 윤리',
toc='GICS와 X-Tech 두 개의 자, 위치·길이·각도·면적의 정확도 순위, 파이와 평균의 함정, 대시보드 5원칙과 윤리 8문항',
kicker='데이터시각화 · 4주차 · 산업별 데이터 시각화 1 — 금융/핀테크',
question='같은 “금융”인데, 은행 화면과 핀테크 화면은 왜 다른 차트를 쓸까?',
desc='데이터 시각화 4주차 해설: GICS(11·25·74·163)와 X-Tech 두 가지 산업 분류, 베르탱의 시각 변수와 클리블랜드·맥길의 정확도 순위, 색 부호화 세 종류, 파이와 평균의 함정, 은행 vs 핀테크, 대시보드 5원칙, 오해를 부르는 차트 네 가지와 윤리 8문항.',
intro='<p>4층 산업관. 오늘은 조별발표입니다. 초파리 조는 은행 화면을, 주판봇 조는 핀테크 화면을 맡았습니다. 두 조가 준비하다 같은 질문에 부딪힙니다. “우리는 어느 산업이지?” 은행 앱을 만드는 핀테크 회사는 금융일까, 기술 회사일까. 박사가 자 두 개를 꺼냅니다. <b>“산업을 재는 자는 하나가 아닙니다.”</b></p>',
first3=('산업을 나누는 두 가지 기준(GICS·X-Tech), 눈이 숫자를 가장 정확히 읽는 방법(위치·길이 → 각도 → 면적 → 색), 그리고 은행과 핀테크 화면의 차이를 봅니다.',
        '같은 숫자도 길이로 보여 주면 정확히, 면적이나 색으로 보여 주면 대충 읽힙니다. 고객과 경영진이 결정을 내리는 화면일수록 이 차이가 큽니다.',
        '은행·카드사·핀테크 회사의 대시보드, 보고서의 산업 비교표, 투자 자료의 섹터 차트가 모두 오늘 배우는 원칙 위에 있습니다.'),
abbr=[('GICS', 'Global Industry Classification Standard, 세계 산업 분류 기준 (MSCI와 S&P가 함께 만듦)'), ('X-Tech', '기존 산업 X + 기술 Tech. 핀테크·에듀테크 같은 비공식 이름'),
      ('KPI', 'Key Performance Indicator, 핵심 성과 지표'), ('MAU', 'Monthly Active Users, 한 달 동안 한 번 이상 쓴 이용자 수')],
kpis=[('11 · 25 · 74 · 163', 'GICS 섹터 · 산업그룹 · 산업 · 하위산업'), ('7가지', '베르탱의 시각 변수'), ('위치 > 각도 > 면적', '눈이 읽는 정확도 순서'), ('8문항', '발표 전 윤리 점검')],
kpi_note='GICS 숫자는 S&P Dow Jones Indices·MSCI 공개 자료 기준(2026년 확인)입니다. 원자료의 24·69·158은 옛 구조라 바꿨습니다.',
hero_talk=[
 ('robo', 'chart', '핀테크는 빠르고 반짝여! 우리 조 화면엔 거품 차트(버블)에 원을 크게크게 그릴 거야.'),
 ('fly', 'magnify', '원의 크기로 숫자를 읽으면 사람들이 얼마나 틀리는지 알아? 면적은 정확도 순위 아래쪽이야.'),
 ('doc', 'front', '오늘은 두 가지를 봅니다. <b>산업을 나누는 자</b>, 그리고 <b>눈이 숫자를 읽는 자</b>. 둘 다 하나가 아닙니다.'),
 ('moa', 'cheer', '주판봇 조 힘내요! 저는 핀테크 KPI를 모아 왔어요.')],
crew=[('doc', 'front', '심판, 분류와 부호화 해설'), ('fly', 'magnify', '초파리 조 조장 — 은행 화면'), ('robo', 'chart', '주판봇 조 조장 — 핀테크 화면'),
      ('asst', 'think', '초파리 조 · 정확도 실험'), ('sia', 'explain', '초파리 조 · 윤리 점검표'), ('moa', 'report', '주판봇 조 · KPI 모으기'), ('x2', 'think', '주판봇 조 · 색 부호화'), ('x3', 'smile', '주판봇 조 · 대시보드 초안')],
recap='3주차: 그리기 전에 씻는다(표기·형식·빈 값·중복·이상치). 빈 값을 0으로 채우면 평균이 깎인다. AI의 전처리는 행 수로 검사한다.',
prereq=['03'],
why_title='왜 산업별 시각화인가 — 산업이 바뀌면 “보는 숫자”가 바뀐다',
why=[('분류', '어떤 회사를 어느 산업에 넣느냐에 따라 비교 대상과 평균이 바뀝니다. 자를 먼저 정해야 비교가 공정합니다.'),
     ('부호화', '숫자를 위치·길이·각도·면적·색 중 무엇으로 보여 주느냐에 따라 읽는 정확도가 달라집니다.'),
     ('맥락', '같은 대시보드도 은행은 안정과 규제를, 핀테크는 속도와 전환을 봅니다. 질문이 다르면 차트가 다릅니다.')],
bigpicture='''<div class="tbl"><table><thead><tr><th>연도</th><th>사건</th><th>오늘과의 연결</th></tr></thead><tbody>
<tr><td>1786</td><td>플레이페어 — 막대·선·원으로 무역 통계를 그림</td><td>막대와 꺾은선의 시작</td></tr>
<tr><td>1854</td><td>존 스노 — 런던 지도 위에 콜레라 사망과 우물을 찍음</td><td>지도 위 점으로 원인을 좁힘</td></tr>
<tr><td>1967</td><td>베르탱 — 일곱 가지 시각 변수 정리</td><td>2단계 시각 부호화</td></tr>
<tr><td>1977</td><td>튜키 — 탐색적 데이터 분석(EDA)</td><td>8주차 중간 프로젝트</td></tr>
<tr><td>1983</td><td>터프티 — 데이터-잉크 비율, 차트 정크</td><td>2주차 단순성</td></tr>
<tr><td>1984</td><td>클리블랜드·맥길 — 시각 채널의 정확도 순위 실험</td><td>2단계 정확도 순위</td></tr></tbody></table></div>
<p style="font-size:14px;color:#5b6874">원자료 연표의 “1967 · 1983 — 베르탱 · 튜키”는 이 페이지에서 베르탱 1967, 튜키 1977(EDA), 터프티 1983으로 나눠 바꿉니다.</p>''',
why_say=('doc', 'board', '연표는 외우지 않아도 됩니다. 오늘 쓰는 원칙들이 “누가, 왜” 만들었는지 한 번 보는 것으로 충분해요.'),
steps=[
dict(id='lv1', short='두 개의 자', title='산업을 재는 두 개의 자 — GICS와 X-Tech', concept='산업 분류', en='industry classification GICS and X-Tech', cid='lab:concept/industry-classification',
 tag='방법: 하나의 회사, 두 개의 이름표', analogy='회사의 부서 이름과 별명',
 where='<b>①산업 분류</b> → ②시각 부호화 → ③차트 고르기와 함정 → ④은행 vs 핀테크와 윤리',
 situation='인터넷 전문은행은 은행일까요, 기술 회사일까요? 두 조가 이 회사를 서로 다른 그룹에 넣으면, “업계 평균”과의 비교 차트가 달라집니다.',
 whybox=dict(problem='회사들을 비교하려면 먼저 같은 그룹으로 묶어야 합니다. 묶는 기준이 다르면 평균과 순위가 달라집니다.',
             limit='공식 분류 하나만 보면 “돈은 은행처럼 벌지만 일하는 방식은 IT 회사” 같은 차이가 가려집니다.',
             solution='두 개의 자를 함께 씁니다. <b>GICS</b>는 “무엇으로 돈을 버나”, <b>X-Tech</b>는 “어떻게 일하나”. 한 회사가 두 이름표를 동시에 가질 수 있습니다.',
             easy='회사원 한 명이 “재무팀”(공식 부서)이면서 동시에 “우리 팀 엑셀 장인”(별명)일 수 있는 것과 같습니다.'),
 pair=(('일상으로 치면', '학교에서 학생은 “2학년 3반”(공식 반)이면서 “방송부”(활동)입니다. 반 평균을 낼 때와 방송부 평균을 낼 때 비교 대상이 다릅니다.'),
       ('산업에서는', 'GICS는 4단계 구조 — 섹터 11 → 산업그룹 25 → 산업 74 → 하위산업 163. X-Tech는 기존 산업 X + 기술(AI·모바일·클라우드·오픈 API) = 핀테크·푸드테크·에듀테크·리걸테크 같은 이름입니다. 중국 국가통계국의 「국민경제 업종 분류」, 한국 통계청의 한국표준산업분류(KSIC)도 같은 역할을 합니다.')),
 talk=[('doc', 'think', '아래 회사 유형마다 두 이름표를 붙여 봅시다. 하나만 맞으면 반만 맞은 겁니다.'),
       ('robo', 'happy', '핀테크는 기술이니까 무조건 정보기술(IT) 섹터지!'),
       ('fly', 'arms', 'GICS는 “무엇으로 돈을 버나”를 봐. 이자와 수수료로 번다면 금융이야.'),
       ('x2', 'think', '그럼 핀테크라는 이름은 GICS가 아니라 X-Tech 쪽 이름표군요.')],
 panel='<div id="w4cls"></div>',
 panel_title='직접 해 보기 — 두 이름표 붙이기',
 sim='산업 이름표 붙이기 게임',
 explain='<p>원자료의 GICS 구조(섹터 11 → 산업그룹 24 → 산업 69 → 하위산업 158)는 2023년 개편 전 숫자입니다. S&P Dow Jones Indices와 MSCI가 공개한 현재 구조는 <b>11 · 25 · 74 · 163</b>이라 이 페이지에서는 바꿔 씁니다. 섹터 11개는 그대로입니다: 에너지(10) · 소재(15) · 산업재(20) · 경기소비재(25) · 필수소비재(30) · 헬스케어(35) · 금융(40) · 정보기술(45) · 커뮤니케이션 서비스(50) · 유틸리티(55) · 부동산(60).</p>',
 docline='회사 하나에 이름표 둘. 비교 차트를 그리기 전에 <b>어느 자로 묶었는지</b>를 제목이나 캡션에 적으세요.',
 limit='무엇을 비교할지 정했습니다. 이제 그 숫자를 화면에 어떻게 옮길까요? 길이, 각도, 면적, 색 중 무엇이 가장 정확할까요?', limit_label='숫자를 어떤 시각 요소로 옮길지 정하지 않음',
 quiz=[dict(q='GICS가 회사를 나누는 기준은?', o=['직원 수', '주요 매출(무엇으로 돈을 버나)', '설립 연도', '본사 위치'], a=1, why='GICS는 회사의 주요 사업 활동, 대개 매출의 대부분을 만드는 사업으로 나눕니다.'),
       dict(q='현재 GICS의 네 단계 숫자로 맞는 것은?', o=['11 · 24 · 69 · 158', '11 · 25 · 74 · 163', '10 · 20 · 50 · 100', '12 · 30 · 80 · 170'], a=1, why='2023년 개편 이후 11개 섹터, 25개 산업그룹, 74개 산업, 163개 하위산업입니다. 원자료의 24·69·158은 옛 구조입니다.')]),
dict(id='lv2', short='부호화', title='시각 부호화 — 눈은 길이를 가장 정확히 읽는다', concept='시각 부호화와 정확도 순위', en='visual encoding and perceptual accuracy', cid='lab:concept/visual-encoding',
 tag='방법: 같은 두 숫자를 네 가지로 보여 주고 맞혀 보기', analogy='숫자를 나르는 일곱 개의 손',
 where='①산업 분류 → <b>②시각 부호화</b> → ③차트 고르기와 함정 → ④은행 vs 핀테크와 윤리',
 situation='주판봇 조는 핀테크 회사들의 이용자 수를 원의 크기(버블)로, 초파리 조는 같은 숫자를 막대 길이로 그렸습니다. 청중은 어느 쪽에서 “몇 배”를 더 정확히 읽을까요?',
 whybox=dict(problem='숫자를 화면에 옮기는 방법은 여러 가지입니다 — 위치, 길이, 각도, 면적, 진하기, 색.',
             limit='보기 좋은 방법이 정확한 방법은 아닙니다. 면적·색으로 크기를 보여 주면 사람마다 다르게 읽습니다.',
             solution='<b>“얼마나 큰가”는 위치·길이에, “어느 그룹인가”는 색·모양에</b> 맡깁니다. 베르탱(1967)의 일곱 시각 변수와 클리블랜드·맥길(1984)의 정확도 순위가 근거입니다.',
             easy='숫자를 나르는 손이 일곱 개 있는데, 크기를 정확히 나르는 손은 위치와 길이 두 개뿐입니다.'),
 mathbox=dict(q='원의 반지름을 두 배로 하면 왜 “두 배”보다 커 보여요?', school='중학교 원의 넓이 πr², 제곱',
   doc='원의 넓이는 반지름을 두 번 곱한 값에 비례해요. 반지름 2배면 넓이는 2×2 = 4배가 됩니다. 눈은 넓이를 보니까 4배쯤으로 느껴요.',
   rows=[('π (파이)', '약 3.14. 원이면 늘 같은 수'), ('r²', '반지름 × 반지름 — “r 제곱”으로 읽는다'), ('넓이 ∝ r²', '넓이는 반지름의 제곱에 비례한다')],
   try_='반지름 1 → 넓이 3.14 × 1 × 1 = <b>3.14</b><br>반지름 2 → 넓이 3.14 × 2 × 2 = <b>12.56</b> → 넓이는 <b>4배</b><br>값이 2배인데 4배로 보이지 않게 하려면 반지름을 √2 ≈ 1.41배만 키웁니다',
   comment='그래서 버블 차트는 “값을 넓이에 맞췄는지, 반지름에 맞췄는지”부터 확인해야 하는군요.'),
 pair=(('일상으로 치면', '피자 크기를 “지름 2배”로 광고하면 실제 양은 4배입니다. 사람들은 지름보다 넓이를 먼저 느낍니다.'),
       ('시각화에서는', '정확도 순서(클리블랜드·맥길): ① 공통 축 위의 위치 ② 공통 축 없는 위치 ③ 길이 ④ 각도·기울기 ⑤ 면적 ⑥ 부피 ⑦ 진하기·채도 ⑧ 색상. 색은 크기가 아니라 “어느 그룹인가”를 말할 때 씁니다.')),
 talk=[('asst', 'think', '같은 두 값(A와 B)을 네 가지 방법으로 보여 드릴게요. B가 A의 몇 %인지 막대(슬라이더)로 맞혀 보세요.'),
       ('robo', 'coin', '원 크기쯤은 한눈에 알 수 있어!'),
       ('fly', 'point', '네 번 다 해 보고 오차를 비교해. 기분 말고 숫자로.')],
 panel='''<div class="chips" id="w4enc"></div>
<div id="w4ev" class="viz" style="min-height:200px"></div>
<div class="ctrl"><label>B는 A의 몇 %? <input type="range" id="w4g" min="5" max="100" value="50"> <b id="w4gv">50</b>%</label><button type="button" class="bt primary" id="w4go">답하기</button><button type="button" class="bt" id="w4nx">새 문제</button></div>
<div class="insight" id="w4eo" aria-live="polite"></div><div class="kpis" id="w4ek"></div>''',
 panel_title='직접 해 보기 — 길이·각도·면적·색, 어느 쪽이 정확한가',
 sim='시각 채널 정확도 실험',
 explain='<p><b>색 부호화 세 종류</b>: ① <b>순차형</b> — 낮음 → 높음 한 방향(한 색의 진하기를 단계로) ② <b>발산형</b> — 가운데 0을 두고 양쪽으로(손익, 평균 대비 ±) ③ <b>범주형</b> — 그룹마다 다른 색, 밝기는 비슷하게. 잘못 고르면 읽는 사람이 뜻을 잃습니다. 또 흔히 인용되는 값으로 남성의 약 8%, 여성의 약 0.5%가 어떤 형태든 색각 이상을 가집니다. 색만으로 정보를 전하지 말고 모양·라벨을 함께 씁니다.</p>',
 docline='“얼마나 큰가”는 길이로, “어느 편인가”는 색으로. 손마다 맡기는 질문이 다릅니다.',
 limit='정확한 채널을 알았으니, 이제 질문마다 차트 표를 정리하고, 가장 자주 쓰이면서 가장 자주 틀리는 두 함정(파이와 평균)을 봅시다.', limit_label='자주 쓰는 차트의 함정을 아직 모름',
 quiz=[dict(q='크기를 가장 정확히 비교할 수 있는 시각 채널은?', o=['색상', '면적', '공통 축 위의 위치(길이)', '부피'], a=2, why='클리블랜드·맥길의 실험에서 공통 축 위의 위치가 가장 정확했습니다. 막대와 산점도가 강한 이유입니다.'),
       dict(q='값이 2배인 원을 “넓이 2배”로 그리려면 반지름은?', o=['2배', '4배', '약 1.41배(√2)', '그대로'], a=2, why='넓이는 반지름의 제곱에 비례하므로 반지름을 √2 ≈ 1.41배만 키우면 넓이가 2배가 됩니다.')]),
dict(id='lv3', short='함정', title='차트 고르기 표와 두 함정 — 파이, 그리고 평균', concept='차트 선택과 평균의 함정', en='chart selection and the trap of averages', cid='lab:concept/average-trap',
 tag='방법: 같은 숫자를 파이와 막대로, 같은 평균을 상자그림으로', analogy='평균 키 170cm인 두 반',
 where='①산업 분류 → ②시각 부호화 → <b>③차트 고르기와 함정</b> → ④은행 vs 핀테크와 윤리',
 situation='콜센터 “평균 응답 시간 12분”. 3월과 4월이 똑같습니다. 4월에 고객 불만이 쏟아졌는데, 평균은 왜 아무 말도 하지 않았을까요?',
 whybox=dict(problem='보고서는 짧아야 해서 숫자 하나(평균)나 그림 하나(파이)로 끝내기 쉽습니다.',
             limit='파이는 비슷한 조각(19%와 22%)을 구분하지 못하고, 평균은 퍼짐(1분 만에 받은 전화와 40분 기다린 전화)을 숨깁니다.',
             solution='비교가 목적이면 <b>정렬 가로 막대</b>, 분포가 중요하면 <b>상자그림·히스토그램</b>을 평균과 함께 보여 줍니다.',
             easy='평균 키 170cm인 두 반 — 한 반은 다들 168~172cm, 다른 반은 150cm와 190cm가 섞였습니다. 평균은 같아도 다른 반입니다.'),
 pair=(('일상으로 치면', '“평균 대기 12분”이라는 식당 안내판. 대부분 2분이면 들어가는데 가끔 40분 기다리는 집과, 늘 12분인 집은 다른 식당입니다.'),
       ('시각화에서는', '차트 고르기 표 — 크기 비교: 막대 · 시간 추세: 꺾은선 · 구성: 트리맵(또는 5개 이하 파이) · 분포: 히스토그램·상자그림·히트맵 · 두 변수 관계: 산점도·버블 · 여러 항목 강약: 레이더 · 흐름과 갈림: 샌키.')),
 talk=[('doc', 'board', '왼쪽은 파이 함정, 오른쪽은 평균 함정입니다. 둘 다 직접 확인해 봅시다.'),
       ('robo', 'meh', '평균이 같으면 같은 거 아니야? 숫자가 같잖아.'),
       ('fly', 'magnify', '상자그림 버튼을 눌러 봐. 4월에는 30분 넘게 기다린 전화가 있어.'),
       ('sia', 'think', '파이에서 C(19%)와 D(22%) 중 큰 쪽을 고르는 데 한참 걸렸어요.')],
 panel='''<div class="grid2"><div><div class="ctrl"><button type="button" class="bt" id="w4pie" aria-pressed="true">파이로</button><button type="button" class="bt" id="w4barh">정렬 가로 막대로</button></div><div id="w4pv" class="viz"></div></div>
<div><div class="ctrl"><button type="button" class="bt" id="w4avg" aria-pressed="true">평균만</button><button type="button" class="bt" id="w4bx">상자그림으로</button></div><div id="w4mv" class="viz"></div><div class="insight" id="w4mo" aria-live="polite"></div></div></div>''',
 panel_title='직접 해 보기 — 파이의 함정, 평균의 함정',
 sim='파이·평균 함정 비교',
 explain='<p>파이 예시(A 17% · B 25% · C 19% · D 22% · E 17%)는 원자료 그대로입니다. 평균 함정의 두 달 응답 시간 열 건씩은 설명용 예시로, 두 달 모두 합계 120분, 평균 12분입니다. 4월에는 30분 이상 기다린 전화가 3건(30·38·40분) 있습니다. 상자그림은 <b>다섯 숫자</b>(최솟값·1사분위·중앙값·3사분위·최댓값)로 모양을 보여 주어, 평균 하나보다 정직합니다.</p>',
 aicheck='<p>AI에게 “3월과 4월 고객 응답을 비교해 줘”라고 했더니 “두 달 평균 응답 시간이 12분으로 같아 서비스 품질에 변화가 없습니다”라고 답했습니다. <b>어디가 이상할까요?</b> 평균이 같다는 사실은 맞지만 “변화가 없다”는 결론은 근거가 부족합니다. 다시 물을 문장: “두 달의 응답 시간을 상자그림으로 그리고, 30분 이상 기다린 건수를 함께 알려 줘.”</p>',
 docline='평균은 대표값 하나일 뿐입니다. <b>모양</b>(퍼짐과 꼬리)을 함께 보여 주지 않으면, 평균은 가장 중요한 사람(오래 기다린 고객)을 가립니다.',
 limit='차트 하나하나는 고를 줄 알게 됐습니다. 이제 여러 차트를 한 화면에 모은 대시보드 — 은행과 핀테크는 무엇을 다르게 볼까요?', limit_label='여러 차트를 모은 화면의 원칙을 모름',
 quiz=[dict(q='평균이 같은 두 달의 응답 시간을 비교할 때 가장 정직한 차트는?', o=['평균 막대 두 개', '상자그림 두 개', '파이 두 개', '3D 막대'], a=1, why='상자그림은 중앙값과 퍼짐, 이상치를 함께 보여 줍니다. 평균 막대는 차이를 숨깁니다.'),
       dict(q='비슷한 크기의 다섯 항목(17·25·19·22·17%)을 비교할 때 파이 대신 쓸 차트는?', o=['정렬 가로 막대', '꺾은선', '레이더', '샌키'], a=0, why='공통 기준선 위의 길이는 각도보다 정확합니다. 정렬하면 순서가 바로 읽힙니다.')]),
dict(id='lv4', short='은행·핀테크', title='은행 vs 핀테크 — 대시보드 5원칙과 윤리 8문항', concept='산업별 대시보드 원칙', en='industry dashboards and ethics', cid='lab:concept/dashboard-ethics',
 tag='현장: 두 조의 화면을 나란히', analogy='묶음 상품과 낱개 상품',
 where='①산업 분류 → ②시각 부호화 → ③차트 고르기와 함정 → <b>④은행 vs 핀테크와 윤리</b>',
 situation='초파리 조는 은행 지점 화면을, 주판봇 조는 핀테크 앱 화면을 발표합니다. 같은 “금융”인데 첫 화면 맨 위의 숫자가 다릅니다. 왜일까요?',
 whybox=dict(problem='대시보드에 넣을 수 있는 숫자는 수십 개인데, 화면은 하나입니다.',
             limit='다 넣으면 결론이 묻히고, 산업 맥락 없이 고르면 엉뚱한 숫자가 맨 위에 옵니다.',
             solution='<b>대시보드 5원칙</b>: ① 한 화면, 한 결론(제목만 읽어도 답) ② 왼쪽 위 → 오른쪽 아래 읽는 순서 ③ 강조는 색, 나머지는 회색 ④ 숫자에 단위·기간·출처 ⑤ 여백도 도구. 그리고 데이터 옆에 사람이 읽는 문장 한 줄.',
             easy='묶음 상품(은행: 예금·대출·외환·자산관리를 한 회사가)과 낱개 상품(핀테크: 송금 하나를 아주 빠르게)은 진열대가 다릅니다.'),
 pair=(('은행 화면에서는', '<b>안정과 규제</b>가 중심. 수익원: 예대 마진·수수료·판매 중개. 대표 차트: 채널 지도, 지점 대시보드, 자산 포트폴리오.'),
       ('핀테크 화면에서는', '<b>속도와 전환</b>이 중심. 수익원: 결제 수수료·제휴·광고·예대 마진. 대표 차트: 사용자 여정 비교, 샌키 흐름, 알림 효과. 두 세계는 서로 닮아 갑니다 — 은행은 앱을 만들고 핀테크는 인가를 받습니다.')),
 body='''<div class="tbl"><table><thead><tr><th>산업</th><th>핵심 KPI 1</th><th>핵심 KPI 2</th><th>자주 쓰는 시각화</th></tr></thead><tbody>
<tr><td>금융</td><td>자산 · 예대 마진</td><td>앱 MAU</td><td>꺾은선 추세, 고객 여정, 샌키, 레이더</td></tr>
<tr><td>제조</td><td>가동률</td><td>불량률</td><td>라인별 막대, 시계열, 분포 히트맵</td></tr>
<tr><td>의료</td><td>대기 시간</td><td>입원율</td><td>요일별 막대, 가용 병상 막대, 흐름도</td></tr>
<tr><td>전자상거래</td><td>전환율</td><td>객단가</td><td>깔때기 막대, 채널 비중 막대</td></tr>
<tr><td>교육</td><td>학습 진도</td><td>중도 이탈률</td><td>과목 히트맵, 학습자 레이더</td></tr>
<tr><td>공공·도시</td><td>이용량</td><td>환경 지수</td><td>막대+꺾은선, 누적 막대</td></tr>
<tr><td>마케팅</td><td>도달·클릭</td><td>ROAS(광고비 대비 매출)</td><td>매체 비중 막대, 시계열 비교</td></tr></tbody></table></div>''',
 talk=[('sia', 'explain', '발표 전에 윤리 8문항 점검표를 돌리겠습니다. 하나라도 “아니오”면 다시 봅니다.'),
       ('robo', 'chart', '우리 핀테크 화면은 증가율이 엄청 커 보이게 Y축을 90부터 시작했어!'),
       ('fly', 'arms', '그거 1번 문항에서 바로 걸려. 잘린 축은 가짜 상승을 만들어.'),
       ('x3', 'flustered', '대시보드 초안에… 출처를 안 적었어요. 3번에서 걸리겠네요.')],
 panel='''<div id="w4eth"></div><div class="insight" id="w4etho" aria-live="polite"></div>
<h3>4주차 실습 코드 (Colab)</h3><p style="font-size:15px">수업에서 쓴 Colab 실습 #1~#5입니다. 트리맵·레이더·샌키·사업 구조 도식 같은 3장의 시각화를 직접 만들어 보는 코드입니다. 먼저 프롬프트로 AI에게 코드를 받은 뒤, 아래 코드와 비교해 차이를 찾아보세요.</p>
<div class="chips"><a class="bt" href="https://colab.research.google.com/drive/1yLeg4s1MjjiZS0enSRKgTgY1StZR1i1E?usp=sharing" target="_blank" rel="noopener">실습 #1 ↗</a><a class="bt" href="https://colab.research.google.com/drive/17fTWb1jsU3HyS_Ye0sqv4lE4fqtLFmYY?usp=sharing" target="_blank" rel="noopener">실습 #2 ↗</a><a class="bt" href="https://colab.research.google.com/drive/1LYyHkqjojKCS4ryOHYrxoY7pc5g2iyeA?usp=sharing" target="_blank" rel="noopener">실습 #3 ↗</a><a class="bt" href="https://colab.research.google.com/drive/1XLdtzkREePflMkoXPpuditlcaueaCZeo?usp=sharing" target="_blank" rel="noopener">실습 #4 ↗</a><a class="bt" href="https://colab.research.google.com/drive/1B8SaTQcat3IQlsRYb7Ma1-dwEAqHCz0V?usp=sharing" target="_blank" rel="noopener">실습 #5 ↗</a></div>''',
 panel_title='직접 해 보기 — 발표 전 윤리 8문항 점검',
 sim='윤리 8문항 점검표',
 explain='<p><b>오해를 부르는 차트 네 가지</b>(악의가 없어도 생깁니다): ① 잘린 Y축 — 작은 차이를 크게 ② 잘못된 채널 — 가로·세로를 함께 키우면 면적은 곱으로 커짐 ③ 잘못된 기준 — 누적 그래프는 각 부분이 그대로여도 늘어나 보임 ④ 비교 대상 없음 — 기준선·평균·작년 같은 기간을 함께 놓지 않으면 답이 부풀려짐. 대부분은 축·단위·비교선 같은 <b>작은 정직</b>으로 막을 수 있습니다.</p><p>4주차 과제(원자료): 핀테크 말고 다른 X-Tech 분야 하나(푸드테크·리걸테크·에듀테크·프롭테크·헬스테크)를 골라 기존 산업과 비교하는 작은 보고서 — 도식 1개, 정보그래픽 1개, 차트 1개 이상, 프롬프트 원문과 직접 고친 부분 기록.</p>',
 docline='윤리 8문항은 취향이 아니라 <b>약속</b>입니다. 매주 같은 화면을 같은 기준으로 점검합니다.',
 limit='4주차로 이론과 산업 맥락이 모였습니다. 5~7층(마케팅/리테일·Plotly·스토리텔링)은 준비 중이고, 다음으로 열린 층은 8층 — 중간 프로젝트입니다.', limit_label='배운 것을 하나의 리포트로 묶어 본 적이 없음',
 quiz=[dict(q='대시보드 5원칙에 해당하지 <b>않는</b> 것은?', o=['한 화면, 한 결론', '숫자에 단위·기간·출처', '강조는 색, 나머지는 회색', '가능한 한 많은 차트를 넣는다'], a=3, why='차트가 많을수록 결론이 묻힙니다. 한 화면에는 한 결론입니다.'),
       dict(q='누적 막대에서 “전체가 늘어 보이는데 각 부분은 그대로”인 경우는 어떤 함정인가?', o=['잘린 축', '잘못된 기준', '색각 이상', '데이터-잉크'], a=1, why='무엇을 기준으로 쌓았는지(부분인가 누적인가)를 제목에 밝혀야 합니다.')]),
],
duel=dict(q='평균 응답 12분 — 3월과 4월, 같은 달일까', step=2,
 intro='콜센터 응답 시간 열 건씩(설명용 예시). 두 달 모두 평균 12분입니다. 주판봇 조는 평균 막대 두 개로 “차이 없음”을, 초파리 조는 상자그림으로 “4월이 위험”을 발표합니다. 심판은 <b>30분 넘게 기다린 고객을 몇 명 찾아냈는가</b>로 판정합니다.',
 fly_pick='상자그림 + 30분 기준선', fly_line='평균 말고 모양을 봐. 꼬리에 오래 기다린 사람이 있어.',
 robo_pick='평균 막대 두 개', robo_line='12분이랑 12분. 숫자가 같으면 같은 거지!',
 metric='30분 이상 기다린 고객을 찾아낸 수',
 run='var M=[11,12,13,12,12,11,13,12,12,12],A=[1,2,1,3,2,40,38,1,2,30];var f=A.filter(function(v){return v>=30;}).length;return {fly:f,robo:0,flyTxt:f+"명",roboTxt:"0명",mm:M.reduce(function(a,b){return a+b;},0)/10,am:A.reduce(function(a,b){return a+b;},0)/10};',
 announce='return "두 달 평균은 "+r.mm+"분과 "+r.am+"분으로 같아요. 상자그림을 본 초파리 조는 30분 이상 기다린 고객 "+r.flyTxt+"(30·38·40분)을 찾았고, 평균 막대만 본 주판봇 조는 한 명도 찾지 못했어요.";',
 verdict='if(res==="F")return "초파리 조 승. 평균이 같다는 것은 사실이고, 차이가 없다는 것은 결론이다. 그 사이에 <b>분포</b>가 있다.";return "결과를 다시 보자.";',
 after='<p style="font-size:14px;color:#5b6874">응답 시간 열 건씩은 설명용 예시입니다(두 달 모두 합계 120분).</p>'),
summary='''<div class="tbl"><table><thead><tr><th>#</th><th>원칙</th><th>한 줄</th></tr></thead><tbody>
<tr><td>1</td><td>시각화는 결론의 통역</td><td>그림이 아니라 읽는 사람의 이해가 바뀐다</td></tr>
<tr><td>2</td><td>질문이 도구를 정한다</td><td>구조는 도식, 의미는 정보그래픽, 수치는 차트</td></tr>
<tr><td>3</td><td>위치와 길이가 가장 정확</td><td>수치 비교는 막대·산점도부터. 색·면적은 그다음</td></tr>
<tr><td>4</td><td>평균 하나는 분포를 가린다</td><td>상자그림(다섯 숫자)이 가장 정직한 출발점</td></tr>
<tr><td>5</td><td>작은 정직이 큰 거짓을 이긴다</td><td>축 · 단위 · 출처 · 비교선</td></tr></tbody></table></div>
<p><b>스스로 점검 다섯 가지</b>: ① 산업을 나누는 두 축을 말할 수 있나 ② 정보 종류로 차트를 고를 수 있나 ③ 색 부호화 세 종류를 구분하나 ④ 오해를 부르는 차트 네 가지를 아나 ⑤ 한 차트에 오늘의 약속을 모두 적용할 수 있나 — “이 차트가 무엇을 말하는지”를 한 문장으로 남에게 설명하면 통과입니다.</p>''',
outro=[('doc', 'judge', '조별발표 판정. 은행 화면도 핀테크 화면도 같은 원칙 위에 있다. 다른 것은 <b>맨 위에 올리는 숫자</b>다.'),
       ('asst', 'spark', '원 크기 맞히기에서 제가 오차가 제일 컸어요. 이제 버블 차트를 보면 반지름부터 의심할래요.'),
       ('robo', 'sigh', 'Y축을 90부터 시작한 건… 윤리 1번에서 바로 걸렸지. 다음엔 0부터 할게.'),
       ('fly', 'coffee', '평균 12분 뒤에 40분 기다린 사람이 있었어. 그 사람이 고객센터에 전화한 사람이야.'),
       ('moa', 'tea', '수고하셨어요! 5~7층은 아직 공사 중이라, 다음은 8층에서 만나요.')],
next_note='<p>5·6·7층(마케팅/리테일, Plotly 인터랙티브, 스토리텔링)은 준비 중입니다. 다음으로 열린 층은 <b>8층 — 중간 프로젝트 상담실</b>입니다.</p>',
refs=[dict(id='w04_slides', type='document', title='数据可视化 CHAPTER 01 · 从一张张图读懂不同产业 (중국어판 학생 교재, 47쪽)', who='안상선', issued={'date-parts': [[2026, 10, 1]]}, role='primary'),
      dict(id='w04_dash', type='document', title='第4周 · 按产业的数据可视化 仪表盘 (중국어판 HTML)', who='안상선', role='primary'),
      dict(id='gics', type='webpage', title='Global Industry Classification Standard (GICS)', who='S&P Dow Jones Indices · MSCI', URL='https://www.spglobal.com/spdji/en/landing/topic/gics/', role='background'),
      dict(id='bertin1967', type='book', title='Sémiologie graphique', who='Jacques Bertin · 1967', issued={'date-parts': [[1967]]}, role='background'),
      dict(id='cleveland1984', type='article-journal', title='Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods', who='William S. Cleveland, Robert McGill · JASA 79(387), 1984', issued={'date-parts': [[1984]]}, role='background'),
      dict(id='tukey1977', type='book', title='Exploratory Data Analysis', who='John W. Tukey · Addison-Wesley, 1977', issued={'date-parts': [[1977]]}, role='background')],
facts=[('F1', 'GICS는 11개 섹터, 25개 산업그룹, 74개 산업, 163개 하위산업으로 이루어진다(원자료의 24·69·158은 옛 구조).', '문헌', 'gics', 'lv1', 'GICS 개요'),
       ('F2', '공통 축 위의 위치 판단이 각도·면적·색 판단보다 정확하다.', '문헌', 'cleveland1984', 'lv2', '정확도 순위'),
       ('F3', '베르탱은 1967년 일곱 가지 시각 변수를 정리했다.', '문헌', 'bertin1967', 'lv2', '시각 변수'),
       ('F4', '탐색적 데이터 분석(EDA) 책은 1977년에 나왔다(원자료 연표의 1983과 다름).', '문헌', 'tukey1977', 'lv1', '연표'),
       ('F5', '남성의 약 8%, 여성의 약 0.5%가 색각 이상을 가진다는 값이 흔히 인용된다.', '원자료', 'w04_slides', 'lv2', '6.5 색각과 접근성')],
gloss={'GICS': ('GICS', '기준', 'MSCI와 S&P가 만든 세계 산업 분류. 섹터 11, 산업그룹 25, 산업 74, 하위산업 163.', 'gics', 'lv1'),
       'X-Tech': ('X-Tech', '용어', '기존 산업 X에 기술을 더한 분야의 비공식 이름. 핀테크·에듀테크 등.', 'x-tech', 'lv1'),
       '시각 변수': ('시각 변수', '용어', '데이터를 나르는 시각 요소. 위치·크기·모양·밝기·색·방향·질감(베르탱).', 'visual-variable', 'lv2'),
       '발산형': ('발산형 색', '용어', '가운데 0을 두고 양쪽으로 다른 색이 진해지는 색 배열. 손익·평균 대비에 쓴다.', 'diverging-palette', 'lv2'),
       '트리맵': ('트리맵', '차트', '전체를 사각형으로 나눠 면적으로 비중과 계층을 함께 보여 주는 차트.', 'treemap', 'lv3'),
       '샌키': ('샌키 차트', '차트', '흐름의 굵기로 양을 보여 주는 차트. 고객 이동, 예산 흐름 등.', 'sankey', 'lv3'),
       '대시보드': ('대시보드', '용어', '여러 차트를 한 화면에 모아 한눈에 보는 판.', 'dashboard', 'lv4')},
models=['시각 채널 정확도 실험의 두 값은 무작위(시드 고정)로 만든 연습 문제입니다.', '콜센터 응답 시간 두 달 열 건씩은 설명용 예시입니다.', '파이 함정의 다섯 비율(17·25·19·22·17%)은 원자료의 예시입니다.'],
cover_alt='디자인 연구실 건물 4층에 불이 켜지고, 이젤에 세 가지 색으로 나뉜 원형 차트와 범례가 걸린 픽셀 표지',
toc_faces=[('fly', 'magnify'), ('robo', 'chart'), ('moa', 'cheer')],
js='''var V=LAB.VIZ,$=LAB.$,$$=LAB.$$;
LAB.Pick($('#w4cls'),[
 {q:'전국에 지점이 있고 예금·대출로 이자 수익을 버는 은행',a:0,why:'GICS: 금융(은행). 기술을 앞세운 새 방식이 아니라 X-Tech 이름표는 따로 붙지 않습니다.'},
 {q:'지점 없이 앱으로만 계좌·대출을 파는 인터넷 전문은행',a:1,why:'돈은 은행처럼 벌어서 GICS는 금융, 일하는 방식은 모바일 중심이라 X-Tech로는 핀테크. 두 이름표가 동시에 붙습니다.'},
 {q:'은행 대신 송금·간편결제 수수료로 버는 앱 회사',a:1,why:'수수료가 주 매출인 금융 서비스(GICS 금융) + 모바일 기술(X-Tech 핀테크).'},
 {q:'반도체를 설계·생산해 파는 회사',a:2,why:'GICS: 정보기술(반도체). 기존 산업에 기술을 더한 X-Tech 이름이 아니라 기술 산업 그 자체입니다.'}],['금융만','금융 + 핀테크','정보기술']);
/* 부호화 실험 */
var R=LAB.rng(401),A=0,B=0,mode='len',err={len:[],ang:[],area:[],col:[]},NM={len:'길이(막대)',ang:'각도(파이)',area:'면적(원)',col:'진하기(색)'};
$('#w4enc').innerHTML=Object.keys(NM).map(function(k){return '<button type="button" class="bt" data-k="'+k+'">'+NM[k]+'</button>';}).join('');
function newQ(){A=100;B=Math.round(15+R()*75);draw();$('#w4eo').textContent='B가 A의 몇 %인지 어림해 막대(슬라이더)로 고르고 「답하기」.';}
function draw(){$$('#w4enc button').forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.k===mode));});var el=$('#w4ev'),s='<svg viewBox="0 0 520 200" width="100%" style="max-width:520px" role="img" aria-label="'+NM[mode]+'로 그린 두 값">';
 if(mode==='len'){s+='<line x1="60" y1="180" x2="500" y2="180" stroke="#9aa5b1"/>';[[A,'A',140],[B,'B',300]].forEach(function(p){var h=150*p[0]/100;s+='<rect x="'+p[2]+'" y="'+(180-h)+'" width="80" height="'+h+'" fill="#1e3a8a"/><text x="'+(p[2]+40)+'" y="196" text-anchor="middle" font-size="13">'+p[1]+'</text>';});}
 else if(mode==='ang'){var tot=A+B,a1=2*Math.PI*A/tot;s+='<path d="M260 100 L260 20 A80 80 0 '+(a1>Math.PI?1:0)+' 1 '+(260+80*Math.sin(a1))+' '+(100-80*Math.cos(a1))+' Z" fill="#1e3a8a"/><path d="M260 100 L'+(260+80*Math.sin(a1))+' '+(100-80*Math.cos(a1))+' A80 80 0 '+(2*Math.PI-a1>Math.PI?1:0)+' 1 260 20 Z" fill="#93a5cf"/><text x="380" y="80" font-size="13">진한 쪽 = A</text><text x="380" y="100" font-size="13">옅은 쪽 = B</text>';}
 else if(mode==='area'){var ra=70,rb=70*Math.sqrt(B/A);s+='<circle cx="160" cy="100" r="'+ra+'" fill="#1e3a8a"/><circle cx="360" cy="'+(170-rb)+'" r="'+rb+'" fill="#1e3a8a"/><text x="160" y="196" text-anchor="middle" font-size="13">A</text><text x="360" y="196" text-anchor="middle" font-size="13">B</text>';}
 else{var c=function(v){return 'rgba(30,58,138,'+(0.08+0.9*v/100)+')';};s+='<rect x="120" y="40" width="110" height="110" fill="'+c(A)+'"/><rect x="290" y="40" width="110" height="110" fill="'+c(B)+'"/><text x="175" y="172" text-anchor="middle" font-size="13">A</text><text x="345" y="172" text-anchor="middle" font-size="13">B</text>';}
 el.innerHTML=s+'</svg>';}
function kp(){$('#w4ek').innerHTML=Object.keys(NM).map(function(k){var e=err[k];return '<div><b>'+(e.length?(e.reduce(function(a,b){return a+b;},0)/e.length).toFixed(1)+'%p':'—')+'</b><span>'+NM[k]+' 평균 오차 · '+e.length+'번</span></div>';}).join('');}
$$('#w4enc button').forEach(function(b){b.onclick=function(){mode=b.dataset.k;newQ();};});
$('#w4g').oninput=function(){$('#w4gv').textContent=this.value;};
$('#w4go').onclick=function(){var g=+$('#w4g').value,e=Math.abs(g-B);err[mode].push(e);kp();$('#w4eo').innerHTML='정답은 <b>'+B+'%</b>, 내 답은 '+g+'% — 오차 '+e+'%p. 다른 방법으로도 몇 번 풀어 평균 오차를 비교해 보세요.';};
$('#w4nx').onclick=newQ;mode='len';newQ();kp();
/* 파이·평균 함정 */
var PV=[['A',17],['B',25],['C',19],['D',22],['E',17]];
function pie(b){$('#w4pie').setAttribute('aria-pressed',String(!b));$('#w4barh').setAttribute('aria-pressed',String(b));
 if(!b)V.pie($('#w4pv'),{labels:PV.map(function(p){return p[0];}),values:PV.map(function(p){return p[1];}),title:'파이 — C와 D 중 어느 쪽이 클까?',h:260,pct:false,colors:['#1e3a8a','#3b5fb0','#5b7cc4','#7d99d4','#a5b8e3']});
 else{var s=PV.slice().sort(function(a,b){return b[1]-a[1];});V.bar($('#w4pv'),{labels:s.map(function(p){return p[0];}),values:s.map(function(p){return p[1];}),horizontal:true,unitShort:'%',title:'정렬 가로 막대 — D 22% > C 19%가 바로 보인다',w:460});}}
$('#w4pie').onclick=function(){pie(false);};$('#w4barh').onclick=function(){pie(true);};pie(false);
var M=[11,12,13,12,12,11,13,12,12,12],AP=[1,2,1,3,2,40,38,1,2,30];
function avg(b){$('#w4avg').setAttribute('aria-pressed',String(!b));$('#w4bx').setAttribute('aria-pressed',String(b));
 if(!b){V.bar($('#w4mv'),{labels:['3월','4월'],values:[12,12],title:'평균 응답 시간 (분)',h:250,w:420});$('#w4mo').textContent='평균만 보면 두 달은 똑같아 보여요.';}
 else{V.box($('#w4mv'),{groups:[{name:'3월',values:M},{name:'4월',values:AP}],mean:true,lo:0,hi:45,title:'응답 시간 상자그림 (분)',h:280,w:420});$('#w4mo').textContent='3월은 11~13분에 모여 있고, 4월은 대부분 1~3분이지만 30·38·40분이 꼬리에 있어요. ◆(평균)는 둘 다 12분.';}}
$('#w4avg').onclick=function(){avg(false);};$('#w4bx').onclick=function(){avg(true);};avg(false);
/* 윤리 8문항 */
var Q=['축이 0에서 시작하는가 (막대·면적)','단위와 기간을 적었는가','출처와 기준일을 적었는가','표본 크기와 정의를 밝혔는가','비교 대상(기준선·평균·작년)이 있는가','분포도 함께 보여 주는가','색만으로 정보를 전하지 않는가 (모양·라벨 병행)','비판을 받아도 결론이 유지되는가'];
$('#w4eth').innerHTML='<p style="margin:0 0 6px;font-size:15px">주판봇 조의 핀테크 화면(Y축 90부터, 출처 없음)을 점검한다고 생각하고, “예”인 항목만 체크하세요.</p><div class="ctrl" style="flex-direction:column;align-items:flex-start;gap:2px">'+Q.map(function(q,i){return '<label><input type="checkbox" data-i="'+i+'"'+([1,4,6].indexOf(i)>=0?' checked':'')+'> '+(i+1)+'. '+q+'</label>';}).join('')+'</div>';
function eth(){var no=[];$$('#w4eth input').forEach(function(c){if(!c.checked)no.push(+c.dataset.i+1);});$('#w4etho').innerHTML=no.length?'“아니오” '+no.length+'개: '+no.join(', ')+'번 — 하나라도 있으면 다시 검토합니다. 주판봇 조는 1번(잘린 축)과 3번(출처)부터 고치면 됩니다.':'모두 “예”. 발표해도 됩니다.';}
$$('#w4eth input').forEach(function(c){c.onchange=eth;});eth();
'''
)
for _s in PAGE['steps']:
    _s['def'] = {'lv1': '무엇으로 돈을 버는지(GICS)와 어떻게 일하는지(X-Tech) 두 기준으로 산업을 나누는 일.', 'lv2': '숫자를 위치·길이·각도·면적·색 중 무엇으로 보여 줄지 정하는 일. 위치와 길이가 가장 정확하다.',
                 'lv3': '질문에 맞는 차트를 고르고, 파이의 비교 한계와 평균이 분포를 가리는 함정을 피하는 일.', 'lv4': '한 화면 한 결론 등 대시보드 5원칙과 발표 전 윤리 8문항 점검.'}[_s['id']]
    if 'mathbox' in _s:
        _s['mathbox']['try'] = _s['mathbox'].pop('try_')
