# 첫 화면 — 디자인 연구실 건물 안내도
IDX['desc'] = '데이터 시각화를 처음 배우는 사람을 위한 15주 연구실 해설. 디자인 연구실 건물을 한 층씩 오르며, 초파리 조와 주판봇 조가 조별발표·개인발표·상담으로 차트 고르기, 전처리, 산업별 시각화, 대시보드를 실제 사례로 익힌다.'
IDX['cover_alt'] = '흰 배경에 디자인 연구실 건물이 서 있고, 옥상에 이젤 네 개, 앞에는 박사를 가운데 두고 두 조 여덟 식구가 선 픽셀 표지'
IDX['body'] = '''
<header class="hero"><div class="wrap">
<div class="kicker">강남대학교 · 데이터시각화 (EB24201-03) · 2026-2학기 강의를 연구실 해설로</div>
<h1>데이터 시각화 디자인 연구실<br><span style="font-size:.5em;color:#5b6874">처음 오신 분을 위한 15층짜리 건물 — 질문에서 차트, 차트에서 결정까지</span></h1>
<p class="question">“숫자는 잔뜩 있는데, 그래서 결론이 뭐야?”</p>
<p>이 건물은 데이터 시각화를 <b>처음</b> 배우는 사람을 위해 지었습니다. 한 주에 한 층씩 올라가며, 박사·조수 하루·초파리 연구원·주판봇과 인턴 시아·모아, 그리고 정체를 밝히지 않은 X1·X2·X3가 실제 강의 자료와 수업용 데이터로 차트를 고르고, 고치고, 결론 한 문장으로 닫는 연습을 합니다. 코드는 생성 AI가 쓰고, 우리는 <b>질문하고 확인하는 사람</b>이 됩니다.</p>
<section class="first3" aria-label="처음 오신 분께"><h3>처음 오신 분께 — 이 건물을 3줄로</h3><ol>
<li><b>무엇을</b> 숫자를 막대·선·점·색으로 바꿔 “어디가 크고, 언제 변했고, 무엇과 함께 움직이는지”를 보이게 하는 법을 배웁니다.</li>
<li><b>왜 중요한가</b> 같은 데이터도 차트를 잘못 고르면 정반대로 읽힙니다. 차트를 고르고 의심하는 눈이 AI 시대의 기본기입니다.</li>
<li><b>업무에서는</b> 보고서 차트 한 장, 대시보드 한 화면, 그리고 그 아래 결론 한 문장 — 이 세 가지를 만드는 일에 그대로 씁니다.</li></ol>
<p class="nocode">코드와 수식을 몰라도 됩니다. 코드는 접힌 상자에만 있고, 수식은 조수 하루가 하나씩 물어봅니다.</p></section>
<section class="kpis"><div><b>15층</b><span>주차 (9개 층 개관, 6개 층 준비 중)</span></div><div><b>2팀</b><span>초파리 조 vs 주판봇 조 · 심판 박사</span></div><div><b>3가지</b><span>장면: 조별발표 · 개인발표 · 상담</span></div><div><b>옥상</b><span>실전 연습장 (4개 사업장 시뮬레이터)</span></div></section>
<div class="talk">''' + say('doc', 'front', '한 층에 한 주씩. 층마다 <b>질문 하나</b>를 들고 올라갑니다. 막히면 그 층의 “풀어서 보면” 상자부터 다시 읽으세요.') + say('asst', 'proud', '저는 초파리 조예요. 어려운 수식이 나오면 제가 먼저 손을 들고 물어볼게요.') + say('robo', 'smile', '난 주판봇 조 조장! 크고 화려한 차트로 이길 거야.') + '''</div>
</div></header>
<section class="level" id="course"><div class="wrap"><h2>강좌 안내</h2>
<p>빅데이터가 어떻게 시각적으로 표현되는지 이해하고, 파이썬과 생성 AI 도구(Qwen, Google AI Studio 등)로 산업별 데이터를 분석해 결론이 있는 시각 결과물을 만드는 과정을 배웁니다. 강의계획서의 원래 실습 언어는 R이었지만, 실제 운영은 <b>파이썬과 생성 AI</b>로 바뀌었습니다.</p>
<div class="tbl"><table><thead><tr><th>항목</th><th>내용 (2026-2학기 강의계획서 기준)</th></tr></thead><tbody>
<tr><td>과목</td><td>데이터시각화 (Data Visualization) · EB24201-03 · 3학점 · 데이터사이언스전공 전공선택(2학년)</td></tr>
<tr><td>운영</td><td>이론·실습 병행(실습 6회) · 이중언어과정(중국어) · 대면 · 목요일 7·8·9교시</td></tr>
<tr><td>담당</td><td>안상선</td></tr>
<tr><td>평가</td><td>중간고사 40 · 기말고사 40 · 출석 10 · 과제 0 · 기타 10 · 절대평가</td></tr>
<tr><td>프로젝트</td><td>중간: AI 기반 EDA 리포트(8·9주) · 기말: 산업별 데이터 시각화와 대시보드 쇼케이스(15주)</td></tr>
<tr><td>AI 활용 범위</td><td>코드 생성, 전처리, 결론 도출 전 과정 허용 — 단, 사용한 도구·프롬프트·코드·확인 절차를 반드시 적는다</td></tr>
<tr><td>교재</td><td>자체 교안(노션 강의 페이지) · 부교재 『혼자 공부하는 머신러닝+딥러닝』(박해선, 한빛미디어)</td></tr></tbody></table></div>
</div></section>
<section class="level" id="building"><div class="wrap"><h2>층별 안내 — 디자인 연구실 건물</h2>
<p>불이 켜진 창은 개관한 층, 회색 창은 아직 준비 중인 층입니다. 초록 층은 리뷰 층입니다. 각 층은 따로 읽어도 되도록 만들었고, 층마다 맨 위의 “30초 복습”이 아래층과 이어 줍니다.</p>
{{BUILDING}}
<p style="font-size:14px;color:#5b6874">층 번호는 강의계획서의 주차 번호와 같습니다. 5·6·7·13·14층은 자료가 들어오는 대로 엽니다. 15층은 기말 쇼케이스(평가) 주간입니다.</p>
</div></section>
<section class="level" id="teams"><div class="wrap"><h2>두 팀과 심판</h2>
<p>이 건물에서는 연구실 식구가 두 조로 나뉘어 같은 데이터로 서로 다른 선택을 합니다. 박사는 어느 편도 들지 않고 <b>데이터대로</b> 판정합니다. 숫자는 점수판을 맡은 조수 하루가 두 조 모두 같은 크기로 읽습니다.</p>
{{TEAMS}}
<div class="steps"><div><span class="n">1</span><b>조별발표</b>두 조가 같은 질문에 다른 차트로 답하고, 박사가 판정합니다. (2·4·9·11·12층)</div><div><span class="n">2</span><b>개인발표</b>조원 한 명씩 자기 차트를 발표하고, 다른 조원이 진단표로 점검합니다. (3·10층)</div><div><span class="n">3</span><b>상담</b>막힌 사람이 박사에게 묻고, 박사가 원리부터 다시 풀어 줍니다. (1·8층)</div></div>
</div></section>
<section class="level" id="how"><div class="wrap"><h2>공부하는 법</h2>
<div class="steps"><div><span class="n">1</span><b>상황부터</b>단계마다 박사의 “상황 질문”이 먼저 나옵니다. 정의보다 장면을 먼저 떠올리세요.</div><div><span class="n">2</span><b>손으로 한 번</b>“숫자로 한 번 해 보기”에서 작은 숫자로 계산을 따라가면, 프로그램이 낸 숫자를 믿을지 판단할 수 있습니다.</div><div><span class="n">3</span><b>AI 결과 의심하기</b>층마다 “AI 결과 판단 코너”에서 그럴듯하지만 틀린 답을 골라냅니다.</div><div><span class="n">4</span><b>퀴즈와 대결</b>단계 끝의 퀴즈로 확인하고, 조별 대결에서 먼저 결과를 맞혀 봅니다.</div><div><span class="n">5</span><b>옥상 연습장</b>배운 것을 카페·결제·건강검진·물류센터 시뮬레이터에서 직접 돌려 봅니다.</div></div>
''' + say('fly', 'point', '막히면 그 단계의 “풀어서 보면”부터 다시 읽어. 막히는 건 실력이 아니라 순서 문제인 경우가 많아.') + '''
</div></section>
<section class="level" id="tools"><div class="wrap"><h2>실습 도구</h2>
<div class="tbl"><table><thead><tr><th>도구</th><th>쓰는 곳</th><th>준비</th></tr></thead><tbody>
<tr><td>Qwen (通义千问)</td><td>차트 하나, 표 설명 듣기, 코드 초안</td><td>계정 만들기</td></tr>
<tr><td>Google AI Studio</td><td>여러 차트가 함께 움직이는 대시보드 (12주)</td><td>구글 계정</td></tr>
<tr><td>Google Colab</td><td>받은 파이썬 코드를 브라우저에서 실행</td><td>구글 계정 — 설치 없음</td></tr>
<tr><td>DeepSeek · Kimi (선택)</td><td>오류 고치기 · 긴 문서 요약과 결론 문장 다듬기</td><td>원자료의 권장 사항, 강제 아님</td></tr>
<tr><td>수업용 데이터</td><td><a href="data/raw/payments.csv">payments.csv</a>(결제 800건) · <a href="data/raw/health_2024_sample5000.csv">건강검진 모의 데이터 표본</a> · <a href="data/raw/codebook.csv">코드표</a></td><td>모두 수업용 합성·모의 데이터</td></tr></tbody></table></div>
</div></section>
<section class="level" id="old"><div class="wrap"><h2>옛 강의 페이지에 대해</h2>
<p>1~4주차는 원래 주차별 강의 슬라이드 사이트(lecture_01~04)로 운영했습니다. 이 건물이 그 내용을 이어받아 처음 배우는 분의 눈높이로 다시 썼으므로, 옛 페이지는 더 이상 보여 주지 않고 이 건물의 같은 층으로 안내합니다.</p>
</div></section>
<footer><div class="wrap"><p>글 · 안상선 ((주)M-Robo 대표) · <a href="https://adminmrobo.github.io/who_am_i/who_am_i.html">소개 페이지</a> · 시리즈 「데이터 시각화 디자인 연구실」 · 라이선스 CC BY-NC 4.0 · <a href="https://github.com/adminmrobo/Data_visuialization_lecture_lab">저장소</a></p>
<p>캐릭터 그림: 연구실 캐릭터 팩(fruitfly-lab-expressions). 결제·건강검진 데이터는 수업용 합성·모의 데이터이며 실제 개인·기업 기록이 아닙니다.</p></div></footer>'''
