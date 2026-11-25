**[한국어](#ko) · [中文](#zh)**

---

<a id="ko"></a>

# 데이터 시각화 디자인 연구실

2026학년도 2학기 강남대학교 데이터사이언스전공 「데이터시각화」(EB24201-03) 강의를, 데이터와 코드를 처음 공부하는 분이 혼자서도 따라올 수 있게 다시 쓴 해설 블로그입니다. 15층짜리 **디자인 연구실** 건물의 한 층이 한 주차입니다.

바로 보기: https://adminmrobo.github.io/Data_visuialization_lecture_lab/

글 · 안상선 ((주)M-Robo 대표) · [소개 페이지](https://adminmrobo.github.io/who_am_i/who_am_i.html) · 라이선스 CC BY-NC 4.0

## 언어

이 시리즈는 한국어 원본과 외국어판 1개로 볼 수 있다.

- 고르는 방법: 화면 최상단 메뉴의 🌐 언어 선택 상자나 오른쪽 아래 🌐 배너에서 고른다. 고른 언어는 브라우저에 기억된다.
- 자동 전환: 한국어 페이지에 처음 들어오면, 브라우저 언어가 지원 언어일 때 그 언어판으로 옮겨 간다. 번역판 주소로 들어오면 그대로 연다.
- 주소 끝에 `?lang=en`처럼 붙이면 그 언어로 바로 연다.
- 언어판 파일은 `이름.언어코드.html` 꼴이다.

<!-- i18n:langtable -->
| 언어 | 파일 이름 | 바로 보기 |
|---|---|---|
| 한국어 | `index.html` | [바로 보기](https://adminmrobo.github.io/Data_visuialization_lecture_lab/index.html) |
| 中文 | `index.zh.html` | [바로 보기](https://adminmrobo.github.io/Data_visuialization_lecture_lab/index.zh.html) |
<!-- /i18n:langtable -->

## 등장인물과 수업 방식

- **박사** — 심판. 발표마다 판정하고, 숫자를 업무 말로 해석해 줍니다.
- **초파리 조** — 조장 초파리, 조원 하루·시아·X1. “그 숫자, 정말 맞아?” 확인하는 쪽.
- **주판봇 조** — 조장 주판봇, 조원 모아·X2·X3. 빠르고 화려한 쪽, 그래서 자주 성급한 쪽.
- 장면은 **조별발표**(2·4·9·11·12층), **개인발표**(3·10층), **상담**(1·8층) 세 가지입니다.

## 층별 안내

| 층 | 주차 | 제목 | 장면 | 페이지 |
|---|---|---|---|---|
| 1층 | 1주 | 차트는 그리는데 결론이 없다 (오리엔테이션) | 상담 | `weeks/w01_orientation.html` |
| 2층 | 2주 | 코드를 잘 쓰는 사람이 아니라 차트를 고르는 사람 | 조별발표 | `weeks/w02_chart-theory.html` |
| 3층 | 3주 | 그리기 전에 씻는다 (데이터 전처리) | 개인발표 | `weeks/w03_data-cleaning.html` |
| 4층 | 4주 | 산업마다 보는 숫자가 다르다 (금융·핀테크) | 조별발표 | `weeks/w04_industry-fintech.html` |
| 5~7층 | 5~7주 | 강의가 끝나는 대로 엽니다 | — | — |
| 8층 | 8주 | 다섯 문항으로 다지는 시각화 기본기 (중간 과제) | 상담 | `weeks/w08_midterm-assignment.html` |
| 9층 | 9주 | 차트는 결정으로 끝난다 (중간 리뷰) | 리뷰 발표회 | `weeks/w09_midterm-review.html` |
| 10층 | 10주 | 건강검진 3만 명을 차트 한 장으로 (헬스케어) | 개인발표 | `weeks/w10_healthcare.html` |
| 11층 | 11주 | 좋은 차트는 이어 묻는 프롬프트에서 나온다 (스마트시티·물류) | 조별발표 | `weeks/w11_smartcity-logistics.html` |
| 12층 | 12주 | 차트 셋이 함께 움직이면 판이 된다 (AI Studio 대시보드) | 조별발표 | `weeks/w12_ai-studio-dashboard.html` |
| 13~14층 | 13~14주 | 강의가 끝나는 대로 엽니다 | — | — |
| 15층 | 15주 | 평가 주간 (기말 쇼케이스) | — | — |
| 옥상 | 마지막 장 | 실전 연습장 — 카페·결제·건강검진·물류센터 | 시뮬레이터 | `practice/index.html` |

## 폴더

- `index.html` — 건물 안내도(전체 목차)
- `weeks/` — 주차별 해설 페이지(한 파일에 그림·데이터 포함)
- `practice/` — 실전 연습장
- `data/` — 수업용 데이터(결제·건강검진 모의 데이터와 열 설명), 지식 색인 등록표
- `assets/img/` — 표지·공유 미리보기 그림
- `build/` — 페이지를 만드는 원고(`build/pages/wNN.py`)와 빌드 도구(`python3 build/build.py`)
- `lecture_01/` ~ `lecture_04/` — 옛 주차별 강의 사이트 자리. 지금은 새 페이지로 자동 이동하는 안내만 남아 있고, 옛 내용은 git 기록에 보존되어 있습니다.

## 데이터 안내

결제·건강검진·교통·배송·대시보드 데이터는 모두 수업용으로 만든 가상·모의 데이터입니다. 실제 개인·기업 기록이 아니며, 페이지의 숫자는 교육용 예시입니다.

---

<a id="zh"></a>

# 数据可视化设计实验室

这是将 2026 学年第 2 学期江南大学数据科学专业「数据可视化」（EB24201-03）课程，改写成初学数据和代码的人也能独自跟上的讲解博客。15 层的**设计实验室**大楼，每一层就是一周。

直接查看：https://adminmrobo.github.io/Data_visuialization_lecture_lab/index.zh.html

文 · Ahn Sangsun（M-Robo 公司 CEO） · [介绍页面](https://adminmrobo.github.io/who_am_i/who_am_i.html) · 许可证 CC BY-NC 4.0

## 语言

本系列可以阅读韩文原版和 1 个外语版。

- 选择方法：在页面最上方菜单的 🌐 语言选择框或右下角的 🌐 横幅中选择。所选语言会被浏览器记住。
- 自动切换：首次进入韩文页面时，如果浏览器语言是支持的语言，会跳转到该语言版本。从译本网址进入则直接打开。
- 在网址末尾加上 `?lang=en` 这样的参数，即可直接以该语言打开。
- 语言版文件采用 `名称.语言代码.html` 的形式。

<!-- i18n:langtable -->
| 语言 | 文件名 | 直接查看 |
|---|---|---|
| 한국어 | `index.html` | [直接查看](https://adminmrobo.github.io/Data_visuialization_lecture_lab/index.html) |
| 中文 | `index.zh.html` | [直接查看](https://adminmrobo.github.io/Data_visuialization_lecture_lab/index.zh.html) |
<!-- /i18n:langtable -->

## 角色与授课方式

- **博士** — 裁判。对每次汇报做出判定，并把数字解读成工作语言。
- **果蝇组** — 组长果蝇，组员 Haru、Sia、X1。负责确认“那个数字，真的对吗？”的一方。
- **算盘宝组** — 组长算盘宝，组员 Moa、X2、X3。快速又华丽的一方，所以也常常是性急的一方。
- 场景有**小组汇报**（2·4·9·11·12 层）、**个人汇报**（3·10 层）、**咨询面谈**（1·8 层）三种。

## 各层导览

| 层 | 周次 | 标题 | 场景 | 页面 |
|---|---|---|---|---|
| 1层 | 第 1 周 | 会画图表却没有结论（课程导论） | 咨询面谈 | `weeks/w01_orientation.html` |
| 2层 | 第 2 周 | 不是会写代码的人，而是会选图表的人 | 小组汇报 | `weeks/w02_chart-theory.html` |
| 3层 | 第 3 周 | 画之前先清洗（数据预处理） | 个人汇报 | `weeks/w03_data-cleaning.html` |
| 4层 | 第 4 周 | 每个行业看的数字不同（金融·金融科技） | 小组汇报 | `weeks/w04_industry-fintech.html` |
| 5~7 层 | 第 5~7 周 | 课程结束后陆续开放 | — | — |
| 8层 | 第 8 周 | 用五道题夯实可视化基本功（期中作业） | 咨询面谈 | `weeks/w08_midterm-assignment.html` |
| 9层 | 第 9 周 | 图表以决定收尾（期中复盘） | 复盘汇报会 | `weeks/w09_midterm-review.html` |
| 10层 | 第 10 周 | 把 3 万人的体检浓缩成一张图表（医疗健康） | 个人汇报 | `weeks/w10_healthcare.html` |
| 11层 | 第 11 周 | 好图表来自连续追问的提示词（智慧城市·物流） | 小组汇报 | `weeks/w11_smartcity-logistics.html` |
| 12层 | 第 12 周 | 三张图表联动起来就成了看板（AI Studio 仪表板） | 小组汇报 | `weeks/w12_ai-studio-dashboard.html` |
| 13~14 层 | 第 13~14 周 | 课程结束后陆续开放 | — | — |
| 15层 | 第15周 | 评估周（期末展示） | — | — |
| 屋顶 | 最后一章 | 实战练习场 — 咖啡馆·支付·体检·物流中心 | 模拟器 | `practice/index.html` |

## 文件夹

- `index.html` — 大楼导览（总目录）
- `weeks/` — 各周讲解页面（一个文件内含图片和数据）
- `practice/` — 实战练习场
- `data/` — 课堂用数据（支付·体检模拟数据及列说明）、知识索引登记表
- `assets/img/` — 封面·分享预览图片
- `build/` — 生成页面的原稿（`build/pages/wNN.py`）和构建工具（`python3 build/build.py`）
- `lecture_01/` ~ `lecture_04/` — 旧的各周课程网站位置。现在只留下自动跳转到新页面的提示，旧内容保存在 git 记录中。

## 数据说明

支付·体检·交通·配送·仪表板数据都是为课堂制作的虚拟·模拟数据。并非真实的个人或企业记录，页面中的数字均为教学示例。
