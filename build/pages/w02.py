# 2주차 — 차트 이론과 첫 시각화 실습 (조별발표)
_CSV = open(HERE + '/data/payments.csv', encoding='utf-8').read()
PAGE = dict(
num='02', slug='chart-theory', kind='lecture', scene='team', short='2주', chip='02주차', floor='2층 발표실',
scene_line='두 조가 같은 결제 데이터로 차트를 골라 발표하고, 박사가 판정합니다',
title='코드를 잘 쓰는 사람이 아니라 차트를 고르는 사람', title_en='Chart principles and choosing the right chart',
subtitle='차트 이론 — 단순성·정확성·목적성, 다섯 갈래 차트 고르기, 첫 실습',
toc='차트 정크와 데이터-잉크, Y축 0의 규칙, 비교·추세·구성·관계·분포, P·R·C·O 실습',
kicker='데이터시각화 · 2주차 · 차트 이론과 첫 시각화 실습',
question='같은 결제 데이터인데, 왜 어떤 차트는 3초 만에 읽히고 어떤 차트는 거짓말을 할까?',
desc='데이터 시각화 2주차 해설: 차트 정크와 데이터-잉크 비율, 막대 Y축 0의 규칙, 합이 100%일 때만 파이, 질문 키워드로 비교·추세·구성·관계·분포 차트 고르기, 프롬프트 4요소와 P·R·C·O 실습.',
intro='<p>2층 발표실. 두 조가 같은 과제를 받았습니다. “payments.csv(결제 800건)로 차트를 만들어 발표하라.” 주판봇 조는 입체 막대에 그림자와 무지개색을 입혔고, 초파리 조는 단색 막대 하나에 결론 한 줄을 달았습니다. 박사는 판정 전에 <b>세 가지 원칙</b>을 꺼냅니다. 단순한가, 정직한가, 목적이 있는가.</p>',
first3=('좋은 차트의 세 원칙(단순성·정확성·목적성)과, 질문의 낱말을 보고 다섯 갈래 차트 중 하나를 고르는 법을 배웁니다.',
        '같은 숫자라도 축을 자르거나 장식을 더하면 읽는 사람이 정반대로 판단합니다. 차트를 고르는 눈이 결론의 정확도를 정합니다.',
        '“어느 지점이 가장 많이 팔렸나”에는 막대, “언제 변했나”에는 꺾은선. 보고서 차트의 80%는 이 고르기에서 성패가 납니다.'),
abbr=[('P·R·C·O', 'Prompt(프롬프트 설계) · Result(결과 확인) · Code(코드 요청) · Output(실행과 점검)'), ('CSV', 'Comma-Separated Values, 쉼표로 값을 나눈 표 파일'),
      ('bin', '히스토그램의 구간. 값을 몇 단위씩 묶어 셀지 정하는 폭'), ('jitter', '점이 겹치지 않게 옆으로 살짝 흔들어 그리는 것')],
kpis=[('3원칙', '단순성 · 정확성 · 목적성'), ('5갈래', '비교 · 추세 · 구성 · 관계 · 분포'), ('4요소', '역할 · 데이터 · 목표 · 출력 형식'), ('0.56', '상품 수와 결제 금액의 상관계수')],
kpi_note='모든 차트는 수업용 합성 데이터 payments.csv(2026-03-02 ~ 03-29, 800건, 금액 결측 32건=4%)로 이 페이지에서 직접 그립니다.',
hero_talk=[
 ('robo', 'happy', '우리 조 차트 봤어? 입체 막대에 그림자에 무지개색! 발표장이 환해졌지!'),
 ('fly', 'arms', '환해진 건 좋은데, 베이징이 청두의 몇 배인지 읽혀?'),
 ('doc', 'board', '오늘 판정 기준은 세 가지입니다. <b>단순한가, 정직한가, 목적이 있는가.</b> 그리고 하나 더 — 질문을 보고 차트를 골랐는가.'),
 ('x2', 'flustered', '(……무지개색을 칠한 손을 슬쩍 감춘다)')],
crew=[('doc', 'front', '심판, 세 원칙 해설'), ('asst', 'smile', '초파리 조 · 숫자 발표'), ('fly', 'arms', '초파리 조 조장 — “축부터 봐”'),
      ('robo', 'happy', '주판봇 조 조장 — “화려할수록 좋아”'), ('sia', 'explain', '초파리 조 · 차트 고르기 발표'), ('moa', 'report', '주판봇 조 · 프롬프트 기록'),
      ('x1', 'think', '초파리 조 · 조용한 확인 담당'), ('x2', 'flustered', '주판봇 조 · 무지개색 담당'), ('x3', 'smile', '주판봇 조 · 히스토그램 담당')],
recap='1주차: 시각화는 통역이다. 표는 정확하고 차트는 빠르다. 그리고 질문 → 명세 → 코드 → 실행·수정 → 검증의 5단계로 AI에게 코드를 받는다.',
prereq=['01'],
why_title='왜 원칙부터인가 — 좋은 차트는 10초 안에 바르게, 나쁜 차트는 10초 안에 틀리게 읽힌다',
why=[('세 원칙', '단순성(장식 빼기), 정확성(축과 비율의 정직), 목적성(누구에게 무엇을). 오늘 모든 판정의 기준입니다.'),
     ('다섯 갈래', '비교 · 추세 · 구성 · 관계 · 분포. 질문의 낱말이 갈래를 정하고, 갈래가 차트를 정합니다.'),
     ('첫 실습', '프롬프트 4요소를 채워 AI에게 차트를 받고, 세 원칙으로 점검한 뒤 한 문장으로 해석합니다.')],
bigpicture='''<div class="tbl"><table><thead><tr><th>3원칙 \\ 5갈래</th><th>비교</th><th>추세</th><th>구성</th><th>관계</th><th>분포</th></tr></thead><tbody>
<tr><td><b>단순성</b></td><td>정렬 · 색 최소화</td><td>선 4개까지</td><td>항목 5개 이하</td><td>점 겹치면 흔들기</td><td>필요 없는 범례 빼기</td></tr>
<tr><td><b>정확성</b></td><td>Y축 0부터</td><td>X축 시간 순서</td><td>합 = 100%</td><td>축 눈금 분명히</td><td>구간 폭 정직하게</td></tr>
<tr><td><b>목적성</b></td><td>어떤 차이가 큰가</td><td>언제 변했나</td><td>무엇으로 나뉘나</td><td>함께 변하나</td><td>어디에 몰리나</td></tr></tbody></table></div>
<p style="font-size:14px;color:#5b6874">교안의 “오늘의 뼈대” 표입니다. 이 페이지의 네 단계가 이 표를 한 번씩 다시 지나갑니다.</p>''',
why_say=('doc', 'board', '표가 커 보이지만 줄은 세 개뿐이에요. 장식을 빼고, 축을 정직하게, 질문에 맞게.'),
steps=[
dict(id='lv1', short='단순성', title='단순성 — 차트 정크, 접시 위 장식을 치우자', concept='차트 정크와 데이터-잉크 비율', en='chart junk and data-ink ratio', cid='lab:concept/chart-junk',
 tag='방법: 장식을 하나씩 꺼 보기', analogy='접시 위 장식',
 where='<b>①단순성</b> → ②정확성 → ③목적성과 다섯 갈래 → ④첫 실습',
 situation='주판봇 조 차트에는 입체 효과, 그라데이션 배경, 풍경 사진, 촘촘한 세로 격자, 같은 뜻의 범례 두 개가 붙어 있습니다. 회의에서 이 차트를 3초 보여 주면, 사람들은 무엇을 기억할까요?',
 whybox=dict(problem='차트를 “보고서용으로 예쁘게” 만들라고 하면 입체 효과와 색이 늘어납니다.',
             limit='장식은 데이터와 상관없는 잉크입니다. 입체 효과는 거리감 때문에 비율까지 다르게 보이게 합니다.',
             solution='<b>데이터-잉크 비율</b>을 높입니다 — 데이터를 나타내는 잉크만 남기고 나머지를 지웁니다.',
             easy='메뉴를 보려는 손님에게 접시 가장자리 꽃무늬는 필요 없습니다. 음식(데이터)만 깔끔하게 보이면 됩니다.'),
 mathbox=dict(q='데이터-잉크 “비율”이라는데, 잉크를 어떻게 재요?', school='초등 분수, 중학교 비율',
   doc='정확히 재는 공식이라기보다 “전체 잉크 중 데이터에 쓴 몫”이라는 생각의 틀이에요. 분수로 쓰면 이렇습니다.',
   rows=[('데이터에 쓴 잉크', '막대·선·점처럼 숫자를 나타내는 부분'), ('÷ 전체 잉크', '장식·격자·배경까지 포함한 모든 그림'), ('= 비율 (0~1)', '1에 가까울수록 데이터만 남은 차트')],
   try_='막대 잉크 50, 장식 잉크 50이면 50 ÷ (50+50) = <b>0.5</b><br>장식을 40만큼 지우면 50 ÷ (50+10) ≈ <b>0.83</b>',
   comment='데이터는 하나도 안 건드렸는데 비율만 올라가네요. 지운 건 장식뿐이고요.'),
 pair=(('일상으로 치면', '레스토랑 접시: 음식 주위의 꽃·소스 장식·옛날 사진은 메뉴를 고르는 데 도움이 되지 않습니다.'),
       ('시각화에서는', '정크의 다섯 얼굴: ① 입체 효과 ② 그라데이션·그림자 ③ 상관없는 사진 ④ 촘촘한 장식 격자 ⑤ 같은 뜻의 범례 중복. 지워도 데이터는 그대로입니다.')),
 talk=[('doc', 'think', '아래 차트에서 장식을 하나씩 꺼 보세요. 데이터(막대 길이)는 그대로인지 확인하면서요.'),
       ('robo', 'chart', '장식을 끄면 심심해 보이잖아. 심심하면 아무도 안 봐!'),
       ('fly', 'magnify', '심심한지 아닌지 말고, 베이징이 몇 배인지 몇 초 만에 읽히는지 재 봐.'),
       ('x2', 'flustered', '(무지개색 스위치를 조심스럽게 끈다)')],
 panel='''<div class="chips" id="w2j"></div>
<div id="w2jv" class="viz"></div>
<div class="insight" id="w2jo" aria-live="polite"></div>''',
 panel_title='직접 해 보기 — 장식 스위치를 하나씩 끄기',
 sim='차트 정크 끄기 실험',
 explain='<p>입체 효과는 단순히 보기 싫은 것이 아니라 <b>비율을 틀리게</b> 보이게 합니다. 막대 뒤의 그림자와 옆면 때문에 앞에서 보는 높이가 실제 값과 달라지기 때문입니다. 교안의 자기 점검 다섯 문항: ① 그림자가 있는가 ② 입체 효과가 있는가 ③ 필요한 격자만 남았는가 ④ 범례가 색 정보를 다 설명하는가 ⑤ 위·오른쪽 축선은 지웠는가.</p>',
 docline='단순함은 게으름이 아니라 <b>속도</b>입니다. 장식을 지우면 같은 데이터가 더 빨리, 더 정확히 읽힙니다.',
 limit='장식을 다 지워도 거짓말을 하는 차트가 있습니다. 축을 0이 아닌 곳에서 시작하면 어떻게 될까요?', limit_label='장식이 없어도 축이 비율을 속일 수 있음',
 quiz=[dict(q='다음 중 차트 정크(데이터와 상관없는 시각 요소)가 <b>아닌</b> 것은?', o=['막대 뒤 그림자', '배경 풍경 사진', '막대의 길이', '같은 뜻의 범례 두 개'], a=2, why='막대의 길이는 데이터 그 자체입니다. 나머지는 지워도 데이터가 그대로인 장식입니다.'),
       dict(q='데이터 잉크 60, 장식 잉크 40인 차트의 데이터-잉크 비율은?', o=['0.4', '0.6', '1.5', '0.67'], a=1, why='60 ÷ (60+40) = 0.6. 장식을 지우면 이 값이 1에 가까워집니다.')]),
dict(id='lv2', short='정확성', title='정확성 — 막대의 Y축은 0에서 시작한다', concept='축의 정직성', en='honest axis and zero baseline', cid='lab:concept/zero-baseline',
 tag='방법: 축 시작점을 움직여 보기', analogy='0을 잘라 낸 자',
 where='①단순성 → <b>②정확성</b> → ③목적성과 다섯 갈래 → ④첫 실습',
 situation='같은 다섯 도시 결제 합계입니다. 누군가 Y축을 0이 아니라 120,000에서 시작하게 그렸습니다. 베이징은 청두의 몇 배로 <b>보일까요?</b>',
 whybox=dict(problem='도시 간 차이가 작아 보이면 “차이를 키워 보이고 싶은” 마음이 생깁니다.',
             limit='막대그래프는 <b>길이</b>로 값을 말합니다. 시작점을 0이 아닌 곳에 두면 길이의 비율이 실제 값의 비율과 달라집니다.',
             solution='막대·파이·도넛은 0(또는 합계 100%)을 기준으로 그립니다. 꺾은선은 변화를 보는 그림이라 0이 아니어도 됩니다.',
             easy='0을 잘라 낸 자로 키를 재면, 150cm와 160cm가 “두 배 차이”처럼 보입니다.'),
 mathbox=dict(q='축을 자르면 “보이는 배율”이 왜 바뀌어요?', school='중학교 일차함수의 그래프 평행이동, 분수의 계산',
   doc='막대 길이는 “값 − 시작점”입니다. 시작점이 0이면 비율이 그대로지만, 시작점을 올리면 분자와 분모에서 같은 수를 빼게 되어 비율이 커져요.',
   rows=[('큰 값 − 시작점', '큰 막대의 화면 길이'), ('작은 값 − 시작점', '작은 막대의 화면 길이'), ('두 길이의 나눗셈', '눈에 보이는 배율')],
   try_='시작점 0: 245,996 ÷ 130,592 ≈ <b>1.9배</b><br>시작점 120,000: (245,996 − 120,000) ÷ (130,592 − 120,000) = 125,996 ÷ 10,592 ≈ <b>11.9배</b>',
   comment='데이터는 같은데 축 하나 바꿨더니 1.9배가 11.9배로 보이네요. 이게 축이 거짓말한다는 거군요.'),
 pair=(('일상으로 치면', '자의 0을 잘라 내고 길이만 재는 사람과 같습니다. 숫자는 맞게 읽어도 비교는 틀립니다.'),
       ('시각화에서는', '정확성 체크 세 가지: ① 막대·파이·도넛은 0부터(또는 합계 기준) ② 꺾은선은 X축이 시간 순서, Y축 0은 강제 아님 ③ 축 눈금은 데이터에 맞게 정직하게.')),
 talk=[('doc', 'board', '막대(슬라이더)로 축 시작점을 올려 보세요. 보이는 배율과 실제 배율이 언제부터 벌어지는지 봅니다.'),
       ('robo', 'wow', '와, 축을 올리니까 베이징이 압도적이야! 이게 더 극적이잖아?'),
       ('fly', 'arms', '극적인 거랑 정직한 건 달라. 아래 실제 배율 숫자를 봐. 그대로야.'),
       ('asst', 'report', '실제 배율은 계속 1.88배예요. 보이는 배율만 바뀌어요.')],
 panel='''<div class="ctrl"><label>Y축 시작점 <input type="range" id="w2y" min="0" max="125000" step="5000" value="0"> <b id="w2yv">0</b></label><button type="button" class="bt" id="w2y0">0으로 되돌리기</button></div>
<div id="w2yc" class="viz"></div>
<div class="kpis" id="w2yk"></div>''',
 panel_title='직접 해 보기 — 축을 자르면 무엇이 달라지나',
 sim='Y축 시작점 바꾸기 실험',
 explain='<p>원자료 슬라이드의 예시(서울 2,540 / 부산 1,210 …, 축 1,000~2,700)는 이 페이지에서 실제 payments.csv 값으로 바꿨습니다. 원리는 같습니다. <b>파이·도넛</b>은 다른 방식으로 정직해야 합니다 — 조각을 모두 더하면 100%여야 합니다. 결측(빈 값)을 어디에 넣을지 정하지 않으면 합계가 100%가 아닌 파이가 됩니다. 2주차에서는 결측 4%를 빼고 나머지로 100%를 계산하고, 결측 처리는 3주차에 다시 다룹니다.</p>',
 aicheck='<p>AI에게 “도시별 차이가 잘 보이게 막대그래프를 그려 줘”라고 했더니, Y축이 120,000에서 시작하는 차트를 돌려줬습니다. 제목은 “베이징, 압도적 1위”. <b>확인 질문</b>: ① 막대인데 축이 0부터인가? → 아니오. ② 제목의 “압도적”이 실제 배율(1.9배)과 맞는가? → 과장. 다시 요청할 문장: “Y축을 0부터 시작하게 다시 그려 줘. 제목은 ‘도시별 결제 합계’로 중립적으로.”</p>',
 docline='비율은 거짓말하지 않는다. <b>축이 거짓말한다.</b> 막대를 보면 먼저 축의 시작점부터 확인하세요.',
 limit='단순하고 정직한 차트라도, 질문과 맞지 않는 종류를 고르면 답을 주지 못합니다. 질문을 보고 차트를 고르는 법이 다음 단계입니다.', limit_label='질문에 맞는 차트 종류를 고르는 기준이 없음',
 quiz=[dict(q='막대 값 106과 101을 Y축 100부터 그리면, 큰 막대는 작은 막대의 몇 배 길이로 보일까?', o=['약 1.05배', '약 2배', '6배', '106배'], a=2, why='(106−100) ÷ (101−100) = 6 ÷ 1 = 6배. 실제 차이는 약 5%(106 ÷ 101 ≈ 1.05)인데 6배로 보입니다. 8주차 과제의 그래프 A가 바로 이 경우입니다.'),
       dict(q='Y축이 0부터 시작하지 <b>않아도</b> 괜찮은 차트는?', o=['막대 그래프', '꺾은선 그래프', '파이 차트', '도넛 차트'], a=1, why='꺾은선은 시간에 따른 변화(기울기)를 보는 그림이라 0을 강제하지 않습니다. 막대·파이·도넛은 길이나 면적으로 값을 말하므로 0 또는 합계 기준이 필요합니다.')]),
dict(id='lv3', short='다섯 갈래', title='목적성 — 질문 낱말이 차트를 고른다', concept='목적별 차트 선택', en='choosing chart by question type', cid='lab:concept/chart-choice',
 tag='방법: 질문 → 갈래 → 차트', analogy='질문 낱말 사전',
 where='①단순성 → ②정확성 → <b>③목적성과 다섯 갈래</b> → ④첫 실습',
 situation='시아가 질문 다섯 개를 받았습니다. “어느 도시가 가장 많이?” “날짜에 따라 어떻게 변했나?” “채널별 비중은?” “상품 수가 많으면 금액도 큰가?” “금액은 어디에 몰려 있나?” 차트 다섯 개를 고를 수 있을까요?',
 whybox=dict(problem='“그래프 그려줘”라고만 하면 AI도 사람도 아무 차트나 고릅니다.',
             limit='차트 종류는 50가지가 넘어서, 모양을 외우는 방식으로는 고를 수 없습니다.',
             solution='차트를 만들기 전에 두 가지를 정합니다: ① 누구에게 보여 주나 ② 무엇을 말하고 싶나. 그리고 질문 낱말로 <b>다섯 갈래</b> 중 하나를 고릅니다.',
             easy='“어느·더·순위”가 들리면 막대, “언제·변화”는 꺾은선, “구성·비율”은 도넛, “함께·영향”은 산점도, “어디에·몰려”는 히스토그램.'),
 pair=(('일상으로 치면', '길을 물을 때 “어디야?”에는 지도를, “얼마나 걸려?”에는 시간표를 보여 주는 것과 같습니다. 질문의 낱말이 보여 줄 것을 정합니다.'),
       ('시각화에서는', '비교 → 막대 · 추세 → 꺾은선 · 구성 → 파이/도넛(합 100%, 5개 이하) · 관계 → 산점도 · 분포 → 히스토그램(그룹 비교는 상자그림).')),
 talk=[('sia', 'explain', '초파리 조 발표를 맡았습니다. 질문 낱말에 밑줄을 긋고 차트를 고르겠습니다.'),
       ('robo', 'coin', '전부 막대로 그리면 되잖아? 막대가 제일 튼튼해!'),
       ('fly', 'point', '“날짜에 따라”를 막대로 그리면 30개 막대가 줄 서. 흐름이 안 보여. 아래 게임으로 확인해.'),
       ('x1', 'think', '(……“함께”라는 낱말에 동그라미를 친다)')],
 panel='''<div id="w2pick"></div>
<h3 style="margin-top:14px">같은 데이터, 다섯 갈래 — 버튼을 누르면 차트가 바뀝니다</h3>
<div class="chips" id="w2five"></div><div id="w2fv" class="viz"></div><div class="insight" id="w2fo" aria-live="polite"></div>''',
 panel_title='직접 해 보기 — 질문을 보고 차트 고르기',
 sim='질문 낱말 차트 고르기 게임',
 explain='<p>원자료의 채널 비중(앱 58% · 웹 28% · 오프라인 14%)은 이 페이지에서 실제 데이터 값(앱 66.3% · 오프라인 17.1% · 웹 16.6%, 결측 제외)으로 바꿉니다. 도넛은 <b>항목이 5개 이하이고 합이 100%</b>일 때만 씁니다. 6개를 넘으면 조각이 얇아져 라벨이 읽히지 않으므로 “상위 5개 + 기타”로 묶거나 막대로 바꿉니다. 꺾은선도 선이 4개를 넘으면 엉킵니다 — 작은 차트 여러 장(small multiples)으로 나눠 그립니다.</p>',
 docline='차트 종류를 외우지 마세요. <b>질문의 낱말</b>을 읽으면 차트는 따라옵니다.',
 limit='차트를 고를 줄 알게 됐습니다. 이제 이 선택을 AI에게 정확히 전달해 코드를 받아야 합니다. 어떻게 써야 원하는 차트가 한 번에 나올까요?', limit_label='고른 차트를 AI에게 전달하는 방법을 아직 모름',
 quiz=[dict(q='“결제 금액은 어느 구간에 가장 많이 몰려 있나?”에 맞는 차트는?', o=['꺾은선', '파이', '히스토그램', '산점도'], a=2, why='“어디에 몰려”는 분포 질문입니다. 값을 구간으로 나눠 세는 히스토그램이 맞습니다.'),
       dict(q='항목이 8개인 구성 비율을 보여 줄 때 가장 좋은 선택은?', o=['8조각 파이', '상위 5개 + 기타로 묶거나 정렬 막대', '입체 파이', '꺾은선'], a=1, why='파이는 5개 이하일 때만. 그 이상이면 묶거나 막대로 바꿉니다.')]),
dict(id='lv4', short='첫 실습', title='첫 실습 — 프롬프트 4요소와 P·R·C·O', concept='프롬프트 4요소와 실습 사이클', en='prompt elements and PRCO cycle', cid='lab:concept/prompt-elements',
 tag='방법: 역할 · 데이터 · 목표 · 출력 형식', analogy='배달 주문서',
 where='①단순성 → ②정확성 → ③목적성과 다섯 갈래 → <b>④첫 실습</b>',
 situation='모아가 Qwen에 “그래프 그려줘”라고 보냈더니 꺾은선이 나왔습니다. 원했던 건 도시별 막대였어요. 무엇이 빠졌을까요?',
 whybox=dict(problem='AI는 우리가 말하지 않은 것을 추측해서 채웁니다. 추측이 틀리면 엉뚱한 차트가 나옵니다.',
             limit='한 번에 모든 것을 길게 쓰면 절반만 반영되고, 너무 짧게 쓰면 추측이 늘어납니다.',
             solution='프롬프트 <b>4요소</b>(역할·데이터·목표·출력 형식)를 채우고, 특히 목표에는 “무엇을 보여 줄지 + 차트 종류”를 함께 씁니다. 그리고 P·R·C·O 네 단계로 확인합니다.',
             easy='배달 주문서에 메뉴·주소·요청 사항·결제 방법을 다 쓰면 전화가 다시 오지 않습니다.'),
 mathbox=dict(q='히스토그램 “구간 폭(bin)”은 몇으로 정해요?', school='초등 나눗셈, 중학교 도수분포표',
   doc='전체 범위를 구간 폭으로 나누면 막대 개수가 나와요. 막대가 너무 많으면 들쭉날쭉(잡음), 너무 적으면 모양이 뭉개집니다.',
   rows=[('범위 (최대 − 최소)', '값이 퍼져 있는 전체 길이'), ('÷ 구간 폭', '한 막대가 맡는 값의 폭'), ('= 막대 개수', '보통 5~15개 사이에서 모양을 본다')],
   try_='결제 금액 0 ~ 5,000을 폭 500으로 나누면 5,000 ÷ 500 = <b>막대 10개</b><br>폭 100이면 <b>50개</b>(들쭉날쭉), 폭 2,500이면 <b>2개</b>(모양이 사라짐)',
   comment='아래 막대(슬라이더)로 폭을 바꿔 보니 500 근처에서 모양이 제일 잘 보이네요.'),
 pair=(('일상으로 치면', '배달 주문서: “누가(역할) · 무엇을 보고(메뉴=데이터) · 무엇을(목표) · 어떻게(출력 형식)”.'),
       ('시각화에서는', 'P(프롬프트 설계) → R(결과가 의도와 같은지 세 가지 확인: 차트 종류·열·정렬과 색) → C(“그 차트의 코드를 줘”) → O(Colab 실행 → 세 원칙 점검 → 한 문장 해석).')),
 talk=[('moa', 'think', '제 프롬프트에 빠진 요소를 찾아서 체크해 볼게요.'),
       ('robo', 'happy', '요소를 다 넣으면 너무 길어지잖아. 짧은 게 멋있어!'),
       ('fly', 'clip', '짧고 엉뚱한 차트 세 번보다 네 줄짜리 프롬프트 한 번이 빨라.'),
       ('x3', 'proud', '(히스토그램 막대 폭을 500에 맞추고 뿌듯해한다)')],
 panel='''<div class="grid2"><div>
<div class="ctrl" style="flex-direction:column;align-items:flex-start;gap:4px" id="w2el">
<label><input type="checkbox" data-k="role"> ① 역할 — 너는 데이터 시각화 분석가야</label>
<label><input type="checkbox" data-k="data"> ② 데이터 — payments.csv, 열: date, hour, city, channel, items, amount, is_new_user</label>
<label><input type="checkbox" data-k="goal"> ③ 목표 — 도시별 amount 합계를 세로 막대로, 큰 값부터</label>
<label><input type="checkbox" data-k="out"> ④ 출력 형식 — 색 #1E3A8A, 위·오른쪽 테두리 없음, 한국어로 한 줄씩 설명</label></div>
<div class="prompt" id="w2pr"></div></div>
<div><div id="w2prv" class="viz"></div><div class="insight" id="w2pro" aria-live="polite"></div></div></div>
<h3>히스토그램 구간 폭 정하기</h3>
<div class="ctrl"><label>구간 폭 <input type="range" id="w2b" min="100" max="2500" step="100" value="500"> <b id="w2bv">500</b></label></div>
<div id="w2bh" class="viz"></div>''',
 panel_title='직접 해 보기 — 4요소를 채우면 차트가 어떻게 바뀌나',
 sim='프롬프트 4요소 체크 실험',
 explain='<p>오늘의 네 장: ① 비교 막대(도시별 합계) ② 추세 꺾은선(날짜별 합계) ③ 분포 히스토그램(금액) ④ 관계 산점도(상품 수 × 금액). 원자료의 해석 예시 “3월 15일이 최고, 다른 평일의 1.8배”는 실제 데이터와 달라 이 페이지에서 <b>“최고는 3월 27일(금) 46,463, 하루 평균 31,059의 약 1.5배”</b>로 바꿉니다. 산점도의 상관계수는 교안 설계대로 약 <b>0.56</b>입니다. 가장 멀리 떨어진 점은 3월 23일 청두 웹 결제(상품 9개, 4,893)로, 원자료 예시(“상품 13개 2,800”)와 달라 실제 값으로 바꿉니다.</p><p><b>흔한 실수 다섯 가지</b>: ① “그래프 그려줘”만 쓰기 ② 막대 Y축 0을 강제하지 않기 ③ 축 이름 빠뜨리기 ④ 정렬 없이 그리기 ⑤ 한 문장 해석 없이 차트만 내기.</p>',
 aicheck='<p>AI가 날짜별 결제 꺾은선을 그리고 “주말 결제가 평일의 두 배입니다”라고 해석했습니다. 교안의 <b>믿어도 되는가 세 질문</b>으로 확인합니다. ① 축이 0인가(꺾은선은 필수 아님) ② 데이터가 맞는가 ③ 결론이 상식적인가 — 실제로 계산하면 주말 하루 평균 35,534, 평일 하루 평균 29,269로 <b>약 1.21배</b>입니다. “두 배”는 과장입니다. 숫자가 그럴듯해 보여도 한 번은 직접 나눠 보세요.</p>',
 docline='차트 한 장 = 질문 하나 = 해석 한 문장. 예: “2026년 3월 결제 합계에서 베이징(245,996)은 청두(130,592)의 약 1.9배다.”',
 limit='오늘 데이터에는 비어 있는 금액이 4% 있었고, 우리는 그냥 뺐습니다. 빼는 것이 늘 맞을까요? 다음 층에서 더러운 데이터를 씻는 법을 배웁니다.', limit_label='결측치를 무조건 빼는 처리',
 code=[('df = df.dropna(subset=["amount"])', 'amount가 비어 있는 행을 뺀다 (800 → 768행)'), ('city_sum = df.groupby("city")["amount"].sum()', '도시별로 묶어 금액을 더한다'),
       ('city_sum = city_sum.sort_values(ascending=False)', '큰 값부터 정렬한다'), ('plt.bar(city_sum.index, city_sum.values, color="#1E3A8A")', '인디고색 세로 막대로 그린다'),
       ('ax.spines[["top","right"]].set_visible(False)', '위·오른쪽 테두리선을 지운다'), ('plt.show()', '그림을 화면에 띄운다')],
 code_title='교안의 막대 차트 코드로 보면',
 quiz=[dict(q='프롬프트 4요소가 아닌 것은?', o=['역할', '데이터', '목표(무엇을 + 차트 종류)', '좋아하는 색깔 이름'], a=3, why='4요소는 역할·데이터·목표·출력 형식입니다. 색은 출력 형식 안에 조건으로 들어갑니다.'),
       dict(q='AI 응답을 받은 뒤 R(결과 확인) 단계에서 확인할 세 가지가 아닌 것은?', o=['차트 종류가 맞나', 'X·Y축 열이 맞나', '정렬과 색이 맞나', '코드가 몇 줄인가'], a=3, why='코드 줄 수는 상관없습니다. 차트 종류·열·정렬과 색이 의도와 같은지 봅니다.')]),
],
duel=dict(q='도시별 결제 비중 — 파이냐, 정렬 막대냐', step=2,
 intro='질문: “선전과 상하이 중 결제 비중이 더 큰 도시는?” 실제 비중은 선전 20.1%, 상하이 19.7%로 차이가 0.4%p뿐입니다. 초파리 조는 정렬 막대, 주판봇 조는 다섯 조각 파이로 발표합니다. 청중 100명이 차트만 보고 맞힌 사람 수로 판정합니다.',
 fly_pick='정렬 막대', fly_line='길이는 공통 기준선에서 재니까 작은 차이도 보여. 큰 값부터 줄 세우면 순서가 바로 읽혀.',
 robo_pick='다섯 조각 파이', robo_line='전체 중 몇 %인지 묻는 거잖아. 파이가 제일 잘 어울려!',
 metric='차트만 보고 바르게 맞힌 청중 수 (100명 중)',
 run='var R=LAB.rng(20260910),g=function(){var u=1-R(),v=R();return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);};var a=20.1,b=19.7,ok=function(sd){var n=0;for(var i=0;i<100;i++){if(a*(1+sd*g())>b*(1+sd*g()))n++;}return n;};var f=ok(0.02),r=ok(0.10);return {fly:f,robo:r,flyTxt:f+"명",roboTxt:r+"명"};',
 announce='return "정렬 막대를 본 청중은 100명 중 "+r.fly+"명, 파이를 본 청중은 "+r.robo+"명이 선전을 골랐어요. 파이 쪽은 거의 동전 던지기 수준이에요.";',
 verdict='if(res==="F")return "초파리 조 승. 비슷한 크기를 비교할 때는 각도보다 <b>공통 기준선 위의 길이</b>가 정확하다. 파이는 “합 100%·5개 이하”일 때만, 그것도 비교가 목적이면 막대가 이긴다.";if(res==="R")return "주판봇 조 승. 이번 표본에서는 파이도 잘 읽혔다. 하지만 다시 돌리면 결과가 흔들린다 — 기준선 위의 길이가 더 안정적이다.";return "무승부. 차이가 아주 작으면 어떤 차트도 어렵다. 그럴 때는 숫자 라벨을 함께 단다.";',
 after='<p style="font-size:14px;color:#5b6874">청중 점수는 Cleveland와 McGill(1984)의 실험 결과(위치·길이 판단이 각도 판단보다 정확하다)를 바탕으로, 길이 읽기 오차 2%·각도 읽기 오차 10%를 가정한 설명용 모형입니다. 4주차에서 이 순위를 자세히 봅니다.</p>'),
summary='''<div class="tbl"><table><thead><tr><th>#</th><th>오늘 만든 차트</th><th>질문</th><th>갈래 → 차트</th><th>한 문장 해석 (실제 데이터)</th></tr></thead><tbody>
<tr><td>1</td><td>도시별 결제 합계</td><td>어느 도시가 가장 많이?</td><td>비교 → 정렬 막대</td><td>베이징 245,996으로 1위, 청두의 약 1.9배</td></tr>
<tr><td>2</td><td>날짜별 결제 합계</td><td>날짜에 따라 어떻게 변했나?</td><td>추세 → 꺾은선</td><td>최고는 3월 27일(금) 46,463, 하루 평균의 약 1.5배</td></tr>
<tr><td>3</td><td>결제 금액 분포</td><td>금액은 어디에 몰려 있나?</td><td>분포 → 히스토그램</td><td>500~1,000 구간에 가장 많고, 오른쪽으로 꼬리가 길다</td></tr>
<tr><td>4</td><td>상품 수 × 결제 금액</td><td>상품이 많으면 금액도 큰가?</td><td>관계 → 산점도</td><td>상관계수 약 0.56 — 함께 커지는 경향, 흩어짐도 크다</td></tr></tbody></table></div>
<p><b>이번 주 제출</b>: 오늘 만든 차트 중 2개(비교 막대 + 산점도 권장)를 Colab 공유 링크로, 차트마다 해석 한 문장과 함께.</p>''',
outro=[('doc', 'judge', '오늘의 판정 요약. 장식을 지우고, 축을 0부터, 질문 낱말로 차트를 골라라. 그리고 <b>한 문장으로 닫아라.</b>'),
       ('asst', 'spark', '저는 “어느·더·순위 → 막대”를 외웠어요. 다음 주엔 비어 있는 값을 어떻게 할지 궁금해요.'),
       ('fly', 'coffee', '파이로 0.4%p 차이를 맞히는 건 동전 던지기였지. 기억해 둬.'),
       ('robo', 'sigh', '무지개색이 진 건 아쉽지만… 강조색 하나만 남기니까 베이징이 진짜 눈에 띄긴 하더라.'),
       ('x2', 'smile', '(무지개 붓을 내려놓고 인디고 붓 하나를 집는다)')],
next_note='<p>다음 층(3주차)에서는 데이터를 그리기 전에 씻는 법 — 표기 불일치, 형식 오류, 빈 값, 중복, 이상치 — 과 Matplotlib·Seaborn의 차이를 배웁니다.</p>',
refs=[dict(id='w02_slides', type='document', title='제2주차 · 차트 이론과 첫 시각화 실습 (v04, 50쪽)', who='안상선', issued={'date-parts': [[2026, 9, 10]]}, role='primary'),
      dict(id='w02_guide', type='document', title='2주차 강의 슬라이드 지침서 (v04)', who='안상선', role='primary'),
      dict(id='payments', type='dataset', title='payments.csv — 수업용 합성 결제 데이터 (800건)', who='강의 자료', role='data', URL='https://github.com/adminmrobo/Data_visuialization_lecture_lab/blob/main/data/raw/payments.csv'),
      dict(id='tufte1983', type='book', title='The Visual Display of Quantitative Information', who='Edward R. Tufte · Graphics Press, 1983', issued={'date-parts': [[1983]]}, role='background'),
      dict(id='cleveland1984', type='article-journal', title='Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods', who='William S. Cleveland, Robert McGill · Journal of the American Statistical Association 79(387), 1984', issued={'date-parts': [[1984]]}, role='background')],
facts=[('F1', 'payments.csv 800건 중 amount 결측은 32건(4.0%)이다.', '계산', 'payments', 'lv2', '결측 개수'),
       ('F2', 'Y축을 120,000에서 시작하면 베이징·청두 막대는 약 11.9배로 보이지만 실제는 약 1.88배다.', '계산', 'payments', 'lv2', 'city 합계'),
       ('F3', '채널별 결제 비중은 앱 66.3%, 오프라인 17.1%, 웹 16.6%다(결측 제외).', '계산', 'payments', 'lv3', 'channel 합계'),
       ('F4', 'items와 amount의 상관계수는 약 0.56이다.', '계산', 'payments', 'lv4', '결측 제외 768건'),
       ('F5', '날짜별 결제 합계의 최고는 3월 27일 46,463이며 일 평균 31,059의 약 1.5배다.', '계산', 'payments', 'lv4', 'date별 합계'),
       ('F6', '주말 하루 평균 결제 합계는 평일 하루 평균의 약 1.21배다.', '계산', 'payments', 'lv4', '요일별 합계'),
       ('F7', '위치·길이 판단이 각도·면적 판단보다 정확하다.', '문헌', 'cleveland1984', 'lv3', '정확도 순위')],
gloss={'차트 정크': ('차트 정크', '용어', '데이터와 상관없는 시각 요소. 입체 효과, 그림자, 장식 사진, 촘촘한 격자 등.', 'chart-junk', 'lv1'),
       '데이터-잉크 비율': ('데이터-잉크 비율', '용어', '차트 전체 잉크 중 데이터를 나타내는 잉크의 몫. 높을수록 깔끔하다(Tufte).', 'data-ink-ratio', 'lv1'),
       '히스토그램': ('히스토그램', '차트', '값을 구간으로 나눠 구간마다 개수를 막대로 세운 분포 차트.', 'histogram', 'lv3'),
       '산점도': ('산점도', '차트', '두 숫자 변수를 가로·세로 위치로 찍어 함께 변하는지 보는 차트.', 'scatter-plot', 'lv3'),
       '상관계수': ('상관계수', '용어', '두 변수가 함께 움직이는 정도(−1~1). 0.56은 “함께 커지는 경향이 있지만 흩어짐도 크다”.', 'correlation-coefficient', 'lv4'),
       '결측': ('결측', '용어', '값이 비어 있는 것. 이 데이터의 amount는 32건(4%)이 비어 있다.', 'missing-value', 'lv2'),
       '상자그림': ('상자그림(박스 플롯)', '차트', '중앙값, 1·3사분위, 이상치를 한 상자로 요약하는 분포 차트.', 'box-plot', 'lv3')},
models=['조별 대결의 청중 점수는 길이 읽기 오차 2%·각도 읽기 오차 10%를 가정한 설명용 모형(시드 고정)입니다.', '데이터-잉크 비율 계기판의 값은 장식 개수로 어림한 설명용 값입니다.', '결제 데이터는 수업용 합성 데이터이며 금액 단위는 원자료에 표기되어 있지 않습니다.'],
cover_alt='디자인 연구실 건물 2층에 불이 켜지고, 이젤의 단색 막대 차트에서 한 막대만 앰버색으로 강조된 픽셀 표지',
toc_faces=[('fly', 'arms'), ('robo', 'happy'), ('x2', 'flustered')],
data='var PAYCSV=' + json.dumps(_CSV) + ';',
js='''var V=LAB.VIZ,$=LAB.$,$$=LAB.$$;
var D=V.csv(PAYCSV),OK=D.filter(function(r){return r.amount!=null;});
var KO={Beijing:"베이징",Shanghai:"상하이",Shenzhen:"선전",Hangzhou:"항저우",Chengdu:"청두"};
var cs={};OK.forEach(function(r){cs[r.city]=(cs[r.city]||0)+r.amount;});
var CITY=Object.keys(cs).map(function(k){return [KO[k],cs[k]];}).sort(function(a,b){return b[1]-a[1];});
/* 1. 정크 스위치 */
var J={shadow:true,grad:true,photo:true,grid3:true,legend:true,rainbow:true},JN={shadow:'입체·그림자',grad:'그라데이션 배경',photo:'풍경 사진',grid3:'촘촘한 격자',legend:'중복 범례',rainbow:'무지개색'};
function drawJ(){var o={};Object.keys(J).forEach(function(k){if(J[k])o[k]=true;});var n=Object.keys(o).length;
 V.bar($('#w2jv'),{labels:CITY.map(function(r){return r[0];}),values:CITY.map(function(r){return r[1];}),hl:n?-1:0,junk:o,title:'도시별 결제 합계',h:290,vlab:n<3,id:'j'});
 var ratio=50/(50+n*9);$('#w2jo').innerHTML='켜진 장식 '+n+'개 · 데이터-잉크 비율 어림값 <b>'+ratio.toFixed(2)+'</b> (장식 1개를 잉크 9로 어림)'+(n===0?' — 장식을 모두 끄고 가장 큰 막대 하나만 앰버로 강조했습니다. 막대 길이는 처음과 똑같습니다.':' — 막대 길이(데이터)는 그대로입니다.');}
$('#w2j').innerHTML=Object.keys(J).map(function(k){return '<button type="button" class="bt" aria-pressed="true" data-k="'+k+'">'+JN[k]+'</button>';}).join('')+'<button type="button" class="bt" id="w2jall">모두 끄기</button>';
$$('#w2j button[data-k]').forEach(function(b){b.onclick=function(){J[b.dataset.k]=!J[b.dataset.k];b.setAttribute('aria-pressed',String(J[b.dataset.k]));drawJ();};});
$('#w2jall').onclick=function(){Object.keys(J).forEach(function(k){J[k]=false;});$$('#w2j button[data-k]').forEach(function(b){b.setAttribute('aria-pressed','false');});drawJ();};
drawJ();
/* 2. Y축 */
function drawY(){var y0=+$('#w2y').value;$('#w2yv').textContent=V.nf(y0);var big=CITY[0][1],sm=CITY[CITY.length-1][1];
 V.bar($('#w2yc'),{labels:CITY.map(function(r){return r[0];}),values:CITY.map(function(r){return r[1];}),y0:y0,yMax:260000,title:'도시별 결제 합계 — Y축 '+V.nf(y0)+'부터',h:290,unit:'결제 합계',dec:0});
 var seen=(big-y0)/(sm-y0),real=big/sm;
 $('#w2yk').innerHTML='<div><b>'+real.toFixed(2)+'배</b><span>실제 배율 (베이징 ÷ 청두)</span></div><div><b style="color:'+(seen/real>1.3?'#c9302c':'#13733a')+'">'+seen.toFixed(2)+'배</b><span>눈에 보이는 배율 (막대 길이 비)</span></div><div><b>'+(seen/real).toFixed(1)+'배</b><span>과장 정도</span></div>';}
$('#w2y').oninput=drawY;$('#w2y0').onclick=function(){$('#w2y').value=0;drawY();};drawY();
/* 3. 고르기 게임 + 다섯 갈래 */
LAB.Pick($('#w2pick'),[
 {q:'“어느 도시에서 결제가 가장 많았나?”',a:0,why:'“어느·가장·순위”는 비교 → 막대입니다.'},
 {q:'“결제 금액이 날짜에 따라 어떻게 변했나?”',a:1,why:'“날짜에 따라·변했나”는 추세 → 꺾은선입니다.'},
 {q:'“앱·웹·오프라인 중 결제 비중은?”',a:2,why:'“비중·구성”이고 항목 3개, 합 100% → 도넛(파이)입니다.'},
 {q:'“상품 수가 많으면 결제 금액도 큰가?”',a:3,why:'“~하면 ~도”는 두 변수의 관계 → 산점도입니다.'},
 {q:'“결제 금액은 어느 구간에 몰려 있나?”',a:4,why:'“어디에·몰려”는 분포 → 히스토그램입니다.'}],['막대(비교)','꺾은선(추세)','도넛(구성)','산점도(관계)','히스토그램(분포)']);
var day={};OK.forEach(function(r){day[r.date]=(day[r.date]||0)+r.amount;});var days=Object.keys(day).sort();
var ch={};OK.forEach(function(r){ch[r.channel]=(ch[r.channel]||0)+r.amount;});
var FIVE={비교:function(el){V.bar(el,{labels:CITY.map(function(r){return r[0];}),values:CITY.map(function(r){return r[1];}),hl:0,title:'비교 — 도시별 결제 합계 (정렬 막대)',h:290});return '베이징 245,996이 1위, 청두 130,592가 5위. 약 1.9배.';},
 추세:function(el){var vals=days.map(function(d){return day[d];}),mx=vals.indexOf(Math.max.apply(null,vals));V.line(el,{labels:days.map(function(d){return d.slice(5);}),series:[{name:'일별 합계',values:vals}],hl:{s:0,i:mx},y0:0,title:'추세 — 날짜별 결제 합계 (꺾은선)',h:290});return '최고는 '+days[mx]+'(금) '+V.nf(vals[mx])+'. 하루 평균 '+V.nf(vals.reduce(function(a,b){return a+b;},0)/vals.length)+'의 약 1.5배.';},
 구성:function(el){var t=ch.app+ch.web+ch.offline;V.pie(el,{labels:['앱','오프라인','웹'],values:[ch.app,ch.offline,ch.web],donut:true,center:'결측 제외',title:'구성 — 채널별 결제 비중 (도넛)'});return '앱 '+(100*ch.app/t).toFixed(1)+'% · 오프라인 '+(100*ch.offline/t).toFixed(1)+'% · 웹 '+(100*ch.web/t).toFixed(1)+'%. 항목 3개, 합 100%라 도넛이 맞는 경우.';},
 관계:function(el){var mxi=0;OK.forEach(function(r,i){if(r.amount>OK[mxi].amount)mxi=i;});V.scatter(el,{pts:OK.map(function(r){return [r.items,r.amount];}),jitter:.3,fit:true,hl:[mxi],xlab:'상품 수 (items)',ylab:'결제 금액',title:'관계 — 상품 수 × 결제 금액 (산점도)',h:310,alpha:.45});var s=V.stats(OK.map(function(r){return r.items;}),OK.map(function(r){return r.amount;}));return '상관계수 r ≈ '+s.r.toFixed(2)+'. 앰버 점은 가장 큰 결제(3월 23일 청두 웹, 상품 9개, '+V.nf(OK[mxi].amount)+').';},
 분포:function(el){V.hist(el,{values:OK.map(function(r){return r.amount;}),lo:0,hi:5000,bin:500,hlTop:true,unit:'결제 금액 (구간 폭 500)',title:'분포 — 결제 금액 (히스토그램)',h:280});return '500~1,000 구간이 가장 많고(311건), 오른쪽으로 꼬리가 길다. 평균 1,132 > 중앙값 960.';}};
$('#w2five').innerHTML=Object.keys(FIVE).map(function(k){return '<button type="button" class="bt" data-k="'+k+'">'+k+'</button>';}).join('');
function five(k){$$('#w2five button').forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.k===k));});$('#w2fo').textContent=FIVE[k]($('#w2fv'));}
$$('#w2five button').forEach(function(b){b.onclick=function(){five(b.dataset.k);};});five('비교');
/* 4. 프롬프트 4요소 */
var EL={role:'너는 데이터 시각화 분석가야.',data:'코랩에 payments.csv가 있어. 열: date, hour, city, channel, items, amount, is_new_user.',goal:'도시별 amount 합계를 세로 막대 그래프로, 큰 값부터 정렬해서 그려 줘.',out:'색은 #1E3A8A, 위·오른쪽 테두리선은 없애 줘. 한국어로, 코드 한 줄마다 한 문장으로 설명해 줘.'};
function drawP(){var on={};$$('#w2el input').forEach(function(c){on[c.dataset.k]=c.checked;});
 var txt=Object.keys(EL).filter(function(k){return on[k];}).map(function(k){return EL[k];}).join('\\n')||'그래프 그려줘';
 $('#w2pr').innerHTML='<span class="lang">한</span>'+LAB.esc(txt);var n=Object.keys(on).filter(function(k){return on[k];}).length;
 var el=$('#w2prv');
 if(!on.goal){var vals=days.map(function(d){return day[d];});V.line(el,{labels:days.map(function(d){return d.slice(5);}),series:[{name:'',values:vals,color:'#9aa5b1'}],title:'AI가 추측한 차트: 날짜별 꺾은선 (원한 것이 아님)',h:250});$('#w2pro').innerHTML='<b>목표</b>가 없어서 AI가 차트 종류를 추측했어요. 원했던 도시별 막대가 아닙니다.';return;}
 var o={labels:CITY.map(function(r){return r[0];}),values:CITY.map(function(r){return r[1];}),h:250,title:'도시별 결제 합계'};
 if(!on.out){o.color='#6b7280';o.junk={grid3:true};}
 V.bar(el,o);var miss=[];if(!on.role)miss.push('역할');if(!on.data)miss.push('데이터(열 이름)');if(!on.out)miss.push('출력 형식');
 $('#w2pro').innerHTML=miss.length?'차트 종류는 맞았지만 빠진 요소: <b>'+miss.join(', ')+'</b>. '+(!on.data?'열 이름이 없으면 AI가 열 이름을 추측해 KeyError가 나기 쉬워요. ':'')+(!on.out?'색·테두리 조건이 없어 기본 회색과 격자가 그대로 나왔어요.':''):'네 요소를 모두 채웠어요. 한 번에 원하는 차트가 나올 가능성이 가장 높습니다.';}
$$('#w2el input').forEach(function(c){c.onchange=drawP;});drawP();
function drawB(){var b=+$('#w2b').value;$('#w2bv').textContent=b;V.hist($('#w2bh'),{values:OK.map(function(r){return r.amount;}),lo:0,hi:5000,bin:b,hlTop:true,unit:'결제 금액 (구간 폭 '+b+', 막대 '+Math.round(5000/b)+'개)',h:250});}
$('#w2b').oninput=drawB;drawB();
'''
)
for _s in PAGE['steps']:
    _s['def'] = {'lv1': '데이터와 상관없는 장식을 지워 데이터를 나타내는 잉크의 몫을 높이는 원칙.', 'lv2': '막대·파이·도넛은 0 또는 합계 100%를 기준으로 그려 비율을 정직하게 보이는 원칙.',
                 'lv3': '질문 낱말로 비교·추세·구성·관계·분포 다섯 갈래를 정하고 차트를 고르는 방법.', 'lv4': '역할·데이터·목표·출력 형식 4요소로 프롬프트를 쓰고 P·R·C·O로 확인하는 실습 사이클.'}[_s['id']]
    if 'mathbox' in _s:
        _s['mathbox']['try'] = _s['mathbox'].pop('try_')
