# 데이터 시각화 디자인 연구실 — Genspark 표지 그림 요청서

모든 그림은 **16비트 RPG 픽셀아트**, **흰 배경**, **16:9 (1920×1080)** 입니다. 그림 안에는 글자를 넣지 않습니다(층 이름·제목은 페이지가 위에 얹습니다).

## 순서

1. 대화 하나를 열고 캐릭터 기본 그림을 첨부합니다: 박사, 조수 하루, 초파리, 주판봇, 시아, 모아, X1, X2, X3 (연구실 캐릭터 팩의 정면 그림).
2. **먼저 `cover_00` 하나만** 요청해 그림체를 확인합니다.
3. 마음에 들면, 같은 대화에서 `cover_00`을 참고 그림으로 함께 올리고 나머지를 3~5장씩 요청합니다.
4. 받은 PNG는 아래 저장 이름 그대로 보내 주세요. 반영할 때 원래 픽셀 격자를 찾아 정수배로만 키워 무손실 WebP로 바꿉니다.

## 모든 요청 앞에 붙일 공통 문장

```
16-bit SNES-era RPG pixel art, crisp hard-edged pixels, limited palette (navy #1E3A8A, teal #0B7A86, amber #B45309, soft grey, warm yellow window light), pure white background, no text, no letters, no numbers, no logos, 16:9 landscape 1920x1080, each art pixel drawn as a clean 4x4 block (native grid 480x270), no blur, no anti-aliasing, no gradients, no photorealism. Keep every attached character exactly as in the reference sheets (same hair, outfit, colors, proportions), chibi RPG sprite scale, standing on the ground line in the lower third.
```

## 그림 목록

| 저장 이름 | 쓰는 곳 | 장면 지시 (공통 문장 뒤에 붙임) |
|---|---|---|
| `cover_00.png` | 건물 안내도(목차) | A tall 15-storey design lab building seen from the front, rooftop with four small easels, windows glowing warm yellow on floors 1–4 and 8–12, floors 5–7 and 13–14 dark with small scaffolding, floor 15 with a little trophy banner shape (no text). In front: the doctor in the center holding a pointer, the fruit-fly team (fruit fly, Haru, Sia, X1) on the left, the abacus-robot team (abacus robot, Moa, X2, X3) on the right, all facing the viewer. |
| `cover_01.png` | 1층 상담실 · 오리엔테이션 | Ground-floor counseling room: small round table with two cups, the doctor smiling and explaining with an open notebook, Sia and Moa sitting across, a board behind them with a simple pixel bar chart and a speech-bubble shape turning into the chart (data becoming a message). |
| `cover_02.png` | 2층 조별발표 · 차트 이론 | Presentation room, two team tables. Left easel: a cluttered chart with 3D blocks and shadows (junk), right easel: a clean sorted bar chart with one amber bar. The fruit fly points at the clean chart, the abacus robot proudly shows the cluttered one, the doctor stands between them with a judge's flag. |
| `cover_03.png` | 3층 개인발표 · 데이터 전처리 | A washing station for data: Haru washing small spreadsheet tiles in a pixel sink, some tiles with holes or smudges going in, clean tiles coming out onto a tray, a small bar chart on a monitor behind. A row of five small podiums on the right, Sia presenting at one while Moa checks her slide with a clipboard. |
| `cover_04.png` | 4층 조별발표 · 금융·핀테크 | Bank-like room with two big rulers on the wall (one long, one short) and a pie chart vs a bar chart on two easels. Left team table with a small bank vault model (fruit fly, Haru), right team table with a phone showing a simple app screen shape (abacus robot, X2), the doctor compares the two charts with a magnifying glass. |
| `cover_08.png` | 8층 상담실 · 중간 과제 | Consultation desk with five stacked question cards, a laptop showing three tiny chart icons, Sia and X1 asking, the doctor answering with a gentle smile, a coffee mug and a checklist clipboard. |
| `cover_09.png` | 9층 리뷰 발표회 · 중간 리뷰 | Review hall with a funnel-shaped chart on a big screen, a small cafe counter model on one table and a bank vault model on another, both teams seated in rows, the doctor at the front with a judge's flag, X3 holding a small trophy. |
| `cover_10.png` | 10층 진료 기록실 · 헬스케어 | Medical records room with a height-and-weight scale, a histogram on a wall monitor with one amber dashed vertical line near the right tail, five team members each holding one small chart card in a row, Moa presenting hers at a podium, Haru taking notes, gentle teal lighting. |
| `cover_11.png` | 11층 관제실 · 스마트시티·물류 | City control room: big wall screen with a grid heat-map of teal squares (one square outlined in amber), beside it a sorted bar chart with an amber rising line on top, small trucks and road shapes on a side monitor. Sia types on a keyboard, the abacus robot carries a pile of seven paper slips, the fruit fly hands one slip at a time. |
| `cover_12.png` | 12층 대시보드 공방 · AI Studio | Workshop with a large dashboard board: three panels (line chart, heat-map, gauge) connected by one cable to a single big switch. X3 builds the board with a wrench, the abacus robot swaps a small tool for a bigger one, the fruit fly flips the switch, the doctor watches with arms crossed and a smile. |
| `cover_99.png` | 옥상 · 실전 연습장 | Rooftop under a light sky (still white background around), four easels in a row: a cafe cup with a bar chart, a coin with a histogram, a heart icon with a dashed line chart, a delivery box with a heat-map. All nine characters gathered, the doctor holding a small flag, the abacus robot excited, the fruit fly checking a clipboard. |

## 받은 뒤 할 일 (제가 합니다)

- 표지를 4배 확대해도 픽셀 경계가 또렷한지 확인하고, 1920×1080 무손실 WebP로 `assets/img/`에 넣습니다.
- 같은 그림에서 공유 미리보기(`og_NN.png`, 1200×630)를 잘라 바꿉니다.
- 표정·인물이 기본 그림과 다르면 “표정만 편집” 요청문을 따로 드립니다.

## 반영 기록 (2026-11-26)

- 받은 10장(`cover_00·01·02·03·04·08·09·11·12·99`) 모두 원래 격자 480×270의 정확한 4배였습니다(다시 줄였다 키워도 차이 0). 원본 격자는 `assets/img/src/`에, 표지는 1920×1080 무손실 WebP로, 공유 미리보기는 480×252로 자른 뒤 3배 키운 1440×756 PNG로 넣었습니다.
- **`cover_10.png`(10층 헬스케어)가 빠져 있습니다.** 위 표의 `cover_10` 요청문으로 한 장만 더 받아 주세요. 그 전까지 10층은 코드로 그린 임시 표지를 씁니다.
- 작은 차이(그대로 둠): 건물 표지의 층 수가 15층보다 적게 그려졌고, 12층 표지의 스위치에 글자처럼 보이는 세로 막대가 있습니다.
