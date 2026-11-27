# 픽셀 대체 표지 — 디자인 연구실 건물
# 장면은 48×22 격자 SVG (shape-rendering="crispEdges"). 왼쪽에 건물 정면, 오른쪽에 그 주차의 주제 소품.
W, H = 48, 22
K = '#2a2f3a'
C = dict(k=K, w='#ffffff', g='#e3e8ee', G='#c9d2dc', s='#9aa5b1', b='#cfe0f7', B='#1e3a8a', y='#fde68a', Y='#f4c95d',
         a='#b45309', A='#fbe7b0', t='#bfe6ea', T='#0b7a86', p='#f3d6ea', P='#c42a6e', m='#cdeedd', M='#2f9a62', r='#f6c6c3', R='#c93030', l='#e6dcf7', L='#7a3fd6')


class Grid:
    def __init__(s):
        s.c = [[None] * W for _ in range(H)]

    def px(s, x, y, col):
        if 0 <= x < W and 0 <= y < H:
            s.c[y][x] = col

    def box(s, x, y, w, h, fill, line=K):
        for j in range(h):
            for i in range(w):
                edge = line and (i in (0, w - 1) or j in (0, h - 1))
                s.px(x + i, y + j, line if edge else fill)

    def svg(s):
        out = []
        for y in range(H):
            x = 0
            while x < W:
                col = s.c[y][x]
                if col is None:
                    x += 1
                    continue
                run = 1
                while x + run < W and s.c[y][x + run] == col:
                    run += 1
                out.append('<rect x="%d" y="%d" width="%d" height="1" fill="%s"/>' % (x, y, run, col))
                x += run
        return ('<svg class="px-scene" viewBox="0 0 %d %d" preserveAspectRatio="xMidYMid meet" shape-rendering="crispEdges" aria-hidden="true">%s</svg>' % (W, H, ''.join(out)))


def building(g, lit):
    # 건물: x 2~17, 아래에서부터 1~5층. lit = 불 켤 층 번호 집합(1~5), 0이면 전부
    g.box(2, 3, 16, 19, C['g'])
    for x in range(4, 16):
        g.px(x, 1, C['a'])
    g.px(9, 1, C['y']); g.px(10, 1, C['y'])
    for x in range(2, 18):
        g.px(x, 2, K)
    for fl in range(1, 6):
        y = 18 - fl * 3
        on = (0 in lit) or (fl in lit)
        for k in range(4):
            x = 4 + k * 3
            g.box(x, y, 2, 2, C['y'] if on else C['s'], None)
        if on and not (0 in lit):
            g.px(3, y, C['a']); g.px(3, y + 1, C['a'])
    g.box(8, 18, 4, 4, C['a'])


def props(g, kind):
    # 오른쪽 소품: 이젤 위 차트, 바닥 소품
    g.box(22, 3, 24, 15, C['w'])
    for x in range(22, 46):
        g.px(x, 18, C['s'])
    g.px(26, 19, K); g.px(27, 20, K); g.px(41, 19, K); g.px(40, 20, K)  # 이젤 다리
    base = 16
    if kind == 'bar':
        for i, h in enumerate([5, 9, 7, 11, 4]):
            for j in range(h):
                for w in range(3):
                    g.px(25 + i * 4 + w, base - j, C['a'] if i == 3 else C['B'])
    elif kind == 'line':
        ys = [13, 11, 12, 9, 8, 10, 6, 5, 7, 4]
        for i in range(len(ys) - 1):
            x0, x1 = 25 + i * 2, 25 + (i + 1) * 2
            for x in range(x0, x1 + 1):
                t = (x - x0) / 2
                g.px(x, round(ys[i] + (ys[i + 1] - ys[i]) * t), C['B'])
        g.px(37, 5, C['a']); g.px(38, 5, C['a'])
    elif kind == 'hist':
        for i, h in enumerate([2, 6, 10, 8, 5, 3, 2, 1, 1]):
            for j in range(h):
                for w in range(2):
                    g.px(25 + i * 2 + w, base - j, C['a'] if i == 2 else C['B'])
        for y in range(5, 17):
            g.px(39, y, C['R'] if y % 2 else C['w'])
    elif kind == 'scatter':
        pts = [(25, 15), (27, 13), (28, 14), (30, 12), (31, 10), (33, 11), (34, 9), (36, 8), (37, 9), (39, 6), (40, 7), (42, 5), (29, 8)]
        for x, y in pts:
            g.px(x, y, C['B'])
        g.px(29, 8, C['a'])
        for x in range(25, 43):
            g.px(x, round(15 - (x - 25) * 0.55), C['A'])
        for x, y in pts:
            g.px(x, y, C['B'])
    elif kind == 'pie':
        for y in range(5, 16):
            for x in range(27, 38):
                d = (x - 32) ** 2 + (y - 10) ** 2
                if d <= 26:
                    col = C['B'] if x <= 32 and y <= 10 else C['a'] if x > 32 else C['t']
                    g.px(x, y, col)
        for i in range(3):
            g.box(39, 6 + i * 3, 2, 2, [C['B'], C['a'], C['t']][i], None)
            for x in range(42, 45):
                g.px(x, 6 + i * 3, C['s'])
    elif kind == 'heat':
        for r in range(5):
            for c in range(7):
                v = (r * 3 + c * 5) % 9
                col = [C['b'], C['b'], C['t'], C['t'], C['T'], C['T'], C['B'], C['B'], C['a']][v]
                g.box(25 + c * 2, 5 + r * 2, 2, 2, col, None)
    elif kind == 'pareto':
        for i, h in enumerate([10, 7, 4, 3, 2]):
            for j in range(h):
                for w in range(3):
                    g.px(25 + i * 4 + w, base - j, C['B'])
        ys = [7, 5, 4, 3, 3]
        for i in range(4):
            for x in range(26 + i * 4, 30 + i * 4):
                g.px(x, ys[i] if x < 28 + i * 4 else ys[i + 1], C['a'])
    elif kind == 'dash':
        for k, (x, y, col) in enumerate([(25, 5, C['B']), (31, 5, C['a']), (37, 5, C['T'])]):
            g.box(x, y, 5, 3, col)
        g.box(25, 9, 17, 7, C['w'])
        for i, h in enumerate([2, 3, 2, 4, 5, 3, 4]):
            for j in range(h):
                g.px(27 + i * 2, 14 - j, C['B'])
    elif kind == 'clean':
        for r in range(5):
            for c in range(4):
                bad = (r, c) in [(1, 2), (3, 1)]
                g.box(25 + c * 4, 5 + r * 2, 4, 2, C['r'] if bad else C['b'])
        for y in range(6, 14):
            g.px(43, y, C['n'] if False else C['a'])
        g.box(41, 13, 5, 3, C['A'])
    elif kind == 'map':
        g.box(25, 5, 18, 11, C['m'], None)
        for x, y, r in [(29, 8, 2), (36, 11, 3), (40, 7, 1)]:
            for yy in range(y - r, y + r + 1):
                for xx in range(x - r, x + r + 1):
                    if (xx - x) ** 2 + (yy - y) ** 2 <= r * r:
                        g.px(xx, yy, C['a'] if r == 3 else C['B'])
    else:  # door / building
        for i in range(5):
            g.box(26 + i * 3, 6, 2, 9, [C['B'], C['a'], C['T'], C['P'], C['L']][i], None)


KIND = {'00': 'door', '01': 'bar', '02': 'bar', '03': 'clean', '04': 'pie', '08': 'scatter', '09': 'dash', '10': 'hist',
        '11': 'pareto', '12': 'dash', '13': 'heat', '99': 'heat'}


def scene(num):
    g = Grid()
    for y in range(H):
        for x in range(W):
            g.px(x, y, '#f4f7fb' if y < 18 else C['G'])
    n = int(num) if num.isdigit() else 0
    lit = {0} if n in (0, 99) else {(n - 1) % 5 + 1}
    building(g, lit)
    props(g, KIND.get(num, 'bar'))
    return g.svg()
