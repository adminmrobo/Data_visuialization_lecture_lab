#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""데이터 시각화 디자인 연구실 — 연구실 해설 블로그 빌드
   build/pages/wNN.py (페이지 원고) → weeks/wNN_slug.html (단일 파일), index.html, practice/index.html,
   data/KG_00_registry.json, cover_manifest.json
   사용: python3 build/build.py"""
import os, re, sys, json, base64, html, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
CSS = open(os.path.join(HERE, 'lab.css'), encoding='utf-8').read()
JS = open(os.path.join(HERE, 'lab.js'), encoding='utf-8').read()
KGX = open(os.path.join(HERE, 'kgx.js'), encoding='utf-8').read()
TODAY = '2026-11-26'
SITE = 'https://adminmrobo.github.io/Data_visuialization_lecture_lab/'
REPO = 'https://github.com/adminmrobo/Data_visuialization_lecture_lab'
SERIES = '데이터 시각화 디자인 연구실'
AUTHOR = '안상선'
AUTHOR_FULL = '안상선 ((주)M-Robo 대표)'
AUTHOR_SITE = 'https://adminmrobo.github.io/who_am_i/who_am_i.html'
LICENSE = 'CC BY-NC 4.0'
E = html.escape

NAMES = {'doc': '박사', 'asst': '조수 하루', 'fly': '초파리 연구원', 'robo': '주판봇', 'sia': '인턴 시아', 'moa': '인턴 모아',
         'x1': 'X1', 'x2': 'X2', 'x3': 'X3'}
# 두 팀 — 초파리 조(조장 초파리) · 주판봇 조(조장 주판봇) · 심판 박사
TEAM_F = [('asst', '하루'), ('sia', '시아'), ('x1', 'X1')]
TEAM_R = [('moa', '모아'), ('x2', 'X2'), ('x3', 'X3')]
ALIAS = {'doc_front': 'doc_e08', 'doc_board': 'doc_e07', 'doc_judge': 'doc_e10', 'doc_verdict': 'doc_e18', 'doc_magic': 'doc_e16', 'doc_think': 'doc_e09', 'doc_smile': 'doc_e13',
         'asst_smile': 'asst_e13', 'asst_firm': 'asst_e12', 'asst_report': 'asst_e07', 'asst_spark': 'asst_e01', 'asst_shock': 'asst_e24', 'asst_sigh': 'asst_e02', 'asst_proud': 'asst_e16', 'asst_think': 'asst_e09', 'asst_wow': 'asst_e04',
         'fly_clip': 'fly_e10', 'fly_point': 'fly_e08', 'fly_arms': 'fly_e16', 'fly_coffee': 'fly_e13', 'fly_cry': 'fly_e21', 'fly_type': 'fly_e09', 'fly_magnify': 'fly_e07',
         'robo_smile': 'robo_e13', 'robo_coin': 'robo_e16', 'robo_chart': 'robo_e07', 'robo_happy': 'robo_e12', 'robo_sigh': 'robo_e20', 'robo_meh': 'robo_e18', 'robo_cry': 'robo_e21', 'robo_wow': 'robo_e04', 'robo_blush': 'robo_e14', 'robo_calc': 'robo_e09',
         'sia_smile': 'sia_e13', 'sia_signal': 'sia_e10', 'sia_explain': 'sia_e07', 'sia_guide': 'sia_e08', 'sia_think': 'sia_e09', 'sia_firm': 'sia_e12', 'sia_proud': 'sia_e16', 'sia_doze': 'sia_e17', 'sia_stop': 'sia_e06', 'sia_shock': 'sia_e24', 'sia_sparkle': 'sia_e19',
         'moa_smile': 'moa_e13', 'moa_tea': 'moa_e01', 'moa_cheer': 'moa_e12', 'moa_plant': 'moa_e16', 'moa_report': 'moa_e07', 'moa_guide': 'moa_e08', 'moa_think': 'moa_e09', 'moa_ok': 'moa_e10', 'moa_sparkle': 'moa_e19', 'moa_cry': 'moa_e21', 'moa_shock': 'moa_e24', 'moa_joy': 'moa_e01'}
for _x in ('x1', 'x2', 'x3'):
    ALIAS.update({_x + '_smile': _x + '_e13', _x + '_joy': _x + '_e01', _x + '_sad': _x + '_e02', _x + '_wow': _x + '_e04', _x + '_think': _x + '_e09',
                  _x + '_proud': _x + '_e16', _x + '_flustered': _x + '_e15', _x + '_shock': _x + '_e24', _x + '_anger': _x + '_e03'})
DUEL_KEYS = ['fly_point', 'robo_coin', 'fly_arms', 'robo_sigh', 'doc_judge', 'asst_spark', 'fly_cry', 'fly_coffee', 'robo_happy', 'doc_think', 'asst_smile',
             'robo_meh', 'asst_report', 'robo_calc', 'asst_shock', 'robo_blush', 'doc_front', 'asst_firm', 'sia_smile', 'sia_sparkle', 'moa_smile', 'moa_cheer',
             'x1_smile', 'x1_joy', 'x2_smile', 'x2_joy', 'x3_smile', 'x3_joy', 'moa_joy']
SCENE = {'team': ('s-team', '조별발표'), 'solo': ('s-solo', '개인발표'), 'talk': ('s-talk', '상담'), 'review': ('s-review', '리뷰 발표회')}


def sprite_b64(key):
    k = ALIAS.get(key, key)
    who = k.split('_')[0]
    p = os.path.join(HERE, 'sprites', who, k + '.webp')
    if not os.path.exists(p):
        return None
    return 'data:image/webp;base64,' + base64.b64encode(open(p, 'rb').read()).decode()


def face(who, mood='front', size=56, cls=''):
    return '<img data-who="%s" data-mood="%s" width="%d" height="%d" alt="" aria-hidden="true"%s>' % (who, mood, size, size, (' class="%s"' % cls) if cls else '')


def say(who, mood, text):
    return '<div class="say">%s<div class="bub"><span class="who w-%s">%s</span><p>%s</p></div></div>' % (face(who, mood), who, NAMES[who], text)


def teams_html(note=''):
    f = ''.join('<div>%s%s</div>' % (face(w, 'smile', 52), n) for w, n in TEAM_F)
    r = ''.join('<div>%s%s</div>' % (face(w, 'smile', 52), n) for w, n in TEAM_R)
    return ('<div class="teams"><div class="tm f"><h4>초파리 조 — 조장 초파리 연구원</h4><div class="mem"><div>%s조장</div>%s</div>'
            '<p style="font-size:14px;margin:6px 0 0;color:#5b6874">“그 숫자, 정말 맞아?” 의심하고 확인하는 쪽</p></div>'
            '<div class="judge">%s<b>심판 박사</b>판정은 데이터대로</div>'
            '<div class="tm r"><h4>주판봇 조 — 조장 주판봇</h4><div class="mem"><div>%s조장</div>%s</div>'
            '<p style="font-size:14px;margin:6px 0 0;color:#5b6874">“크고 화려하게!” 자신 있게 밀어붙이는 쪽</p></div></div>%s') % (
        face('fly', 'point', 52), f, face('doc', 'front', 64), face('robo', 'coin', 52), r, note)


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


# ── 지식 그래프 ─────────────────────────────────────────
def build_kg(P):
    page = P['id']
    nodes, edges, seen = [], [], set()

    def N(id, type, ko, en, anchor, **kw):
        if id in seen:
            return
        seen.add(id)
        n = {'id': id, 'type': type, 'label': {'ko': ko, 'en': en}, 'page': page, 'anchor': anchor,
             'domain': ['dataviz'], 'status': 'known', 'confidence': kw.pop('confidence', 'high')}
        n.update({k: v for k, v in kw.items() if v is not None})
        nodes.append(n)

    def L(s, p, o, anchor, conf='high'):
        edges.append({'s': s, 'p': 'lab:' + p, 'o': o, 'anchor': anchor, 'confidence': conf})
    topic = 'lab:topic/dv-w%s' % P['num']
    N(topic, 'Topic', P['title'], P['title_en'], '#top', definition={'ko': P['question']})
    N('lab:topic/data-visualization', 'Area', '데이터 시각화', 'data visualization', '#top', definition={'ko': '숫자·범주·관계를 눈으로 읽히는 모양으로 옮겨 결론과 결정을 돕는 일.'})
    L(topic, 'broader', 'lab:topic/data-visualization', '#top')
    steps = P['steps']
    cids = []
    for i, s in enumerate(steps):
        cid = s.get('cid') or ('lab:concept/' + slugify(s['en']))
        cids.append(cid)
        anc = '#' + s['id']
        N(cid, s.get('ctype', 'Concept'), s['concept'], s['en'], anc, definition={'ko': s['def']}, level=i + 1, family='dataviz',
          evidence=[f[0] for f in P.get('facts', []) if f[4] == s['id']] or None)
        L(cid, 'broader', topic, anc)
        sec = 'lab:section/%s-%s' % (page, s['id'])
        N(sec, 'Section', '%s 단계 %d' % (P['short'], i + 1), 'step %d' % (i + 1), anc)
        L(cid, 'explainedIn', sec, anc)
        if i > 0:
            L(cids[i - 1], 'prerequisiteOf', cid, anc)
        if s.get('limit'):
            lid = 'lab:limitation/%s-%s' % (page, s['id'])
            N(lid, 'Limitation', s['limit_label'], 'limitation of ' + s['en'], anc, definition={'ko': re.sub('<[^>]+>', '', s['limit'])})
            L(cid, 'hasLimitation', lid, anc)
            if i + 1 < len(steps):
                nxt = steps[i + 1].get('cid') or ('lab:concept/' + slugify(steps[i + 1]['en']))
                L(lid, 'addressedBy', nxt, '#' + steps[i + 1]['id'])
        if s.get('pair'):
            aid = 'lab:analogy/%s-%s' % (page, s['id'])
            N(aid, 'Analogy', s.get('analogy', s['pair'][0][0]), 'analogy: ' + s['en'], anc, definition={'ko': re.sub('<[^>]+>', '', s['pair'][0][1])[:160]})
            L(aid, 'analogyOf', cid, anc)
        if s.get('sim'):
            sid = 'lab:simulation/%s-%s' % (page, s['id'])
            N(sid, 'Simulation', s['sim'], 'simulation: ' + s['en'], anc)
            L(cid, 'demonstratedBy', sid, anc)
        for qi, q in enumerate(s.get('quiz', [])):
            qid = 'lab:quiz/%s-%s-%d' % (page, s['id'], qi + 1)
            N(qid, 'QuizItem', re.sub('<[^>]+>', '', q['q'])[:60], 'quiz %s-%d' % (s['id'], qi + 1), anc)
            L(qid, 'assesses', cid, anc)
    ids = [s['id'] for s in steps]
    for k, g in P.get('gloss', {}).items():
        tid = 'lab:term/' + g[3]
        stepid = g[4] if len(g) > 4 and g[4] in ids else ids[0]
        ci = ids.index(stepid)
        N(tid, 'Term', k, g[3].replace('-', ' '), '#' + stepid, definition={'ko': g[2]})
        L(tid, 'explainedIn', 'lab:section/%s-%s' % (page, stepid), '#' + stepid)
        L(tid, 'partOf', cids[ci], '#' + stepid)
    for r in P['refs']:
        N('lab:work/' + r['id'], 'Work', r['title'], r.get('title_en', r['title']), '#sources')
    for f in P.get('facts', []):
        fid, text, kind, ref, stepid, loc = f
        ci = ids.index(stepid) if stepid in ids else 0
        cl = 'lab:claim/%s-%s' % (page, fid.lower())
        if kind == '미확인':
            q = cl.replace('claim', 'question')
            N(q, 'Question', text, 'open question ' + fid, '#' + stepid, confidence='low')
            L(cids[ci], 'raises', q, '#' + stepid, 'low')
            continue
        N(cl, 'Claim', text, 'claim ' + fid, '#' + stepid, evidence=[fid], source=[{'ref': ref, 'loc': loc}])
        L(cl, 'supports', cids[ci], '#' + stepid)
        L(cl, 'assertedIn', 'lab:work/' + ref, '#' + stepid)
    used = {f[3] for f in P.get('facts', []) if f[2] != '미확인'}
    for r in P['refs']:
        if r['id'] not in used:
            L(topic, 'derivedFrom', 'lab:work/' + r['id'], '#sources')
    N('lab:question/%s-core' % page, 'Question', P['question'], 'core question', '#top')
    L(topic, 'raises', 'lab:question/%s-core' % page, '#top')
    d = P['duel']
    dq = 'lab:question/%s-duel' % page
    N(dq, 'Question', d['q'], 'duel question', '#duel')
    L(cids[-1], 'raises', dq, '#duel')
    m1, m2, mt = 'lab:method/%s-fly' % page, 'lab:method/%s-robo' % page, 'lab:metric/%s' % page
    N(m1, 'Method', d['fly_pick'], 'option A (fly team)', '#duel', definition={'ko': re.sub('<[^>]+>', '', d['fly_line'])})
    N(m2, 'Method', d['robo_pick'], 'option B (jupanbot team)', '#duel', definition={'ko': re.sub('<[^>]+>', '', d['robo_line'])})
    N(mt, 'Metric', d['metric'], 'duel metric', '#duel')
    L(m1, 'contrastsWith', m2, '#duel'); L(m1, 'evaluatedBy', mt, '#duel'); L(m2, 'evaluatedBy', mt, '#duel')
    st = d.get('step', len(cids) - 1)
    L(m1, 'relatedTo', cids[st], '#duel'); L(m2, 'relatedTo', cids[st], '#duel')
    for pre in P.get('prereq', []):
        pid = 'lab:topic/dv-w%s' % pre
        N(pid, 'Topic', '%s주차' % int(pre), 'week %d' % int(pre), '#top')
        L(pid, 'prerequisiteOf', topic, '#top')
    kg = {'version': '1.0', 'page': page, 'domain': ['dataviz'], 'nodes': nodes, 'edges': edges}
    allid = {n['id'] for n in nodes}
    for e in edges:
        assert e['s'] in allid and e['o'] in allid, (page, e)
    deg = {i: 0 for i in allid}
    for e in edges:
        deg[e['s']] += 1; deg[e['o']] += 1
    iso = [i for i, v in deg.items() if v == 0]
    assert not iso, (page, iso)
    return kg


def jsonld(kg, meta):
    ctx = {'@vocab': 'urn:lab:', 'lab': 'urn:lab:', 'skos': 'http://www.w3.org/2004/02/skos/core#', 'schema': 'https://schema.org/',
           'dct': 'http://purl.org/dc/terms/', 'prov': 'http://www.w3.org/ns/prov#', 'rdfs': 'http://www.w3.org/2000/01/rdf-schema#'}
    g = []
    for n in kg['nodes']:
        t = ['lab:' + n['type']]
        if n['type'] in ('Concept', 'Method', 'Term', 'Limitation', 'Metric', 'Topic', 'Area'):
            t += ['skos:Concept', 'schema:DefinedTerm']
        o = {'@id': n['id'], '@type': t, 'skos:prefLabel': [{'@value': n['label']['ko'], '@language': 'ko'}, {'@value': n['label']['en'], '@language': 'en'}]}
        if n.get('definition'):
            o['skos:definition'] = {'@value': n['definition']['ko'], '@language': 'ko'}
        g.append(o)
    for e in kg['edges']:
        g.append({'@id': e['s'], e['p']: {'@id': e['o']}})
    g.append({'@id': meta['url'], '@type': 'schema:LearningResource', 'schema:name': meta['title'], 'schema:inLanguage': 'ko',
              'schema:author': {'@type': 'schema:Person', 'schema:name': AUTHOR}, 'schema:license': LICENSE})
    return {'@context': ctx, '@graph': g}


def esc_json(o):
    return json.dumps(o, ensure_ascii=False).replace('</', '<\\/')


# ── 표지 ─────────────────────────────────────────────────
def cover_img(key, alt, pre):
    f = os.path.join(ROOT, 'assets', 'img', key + '.webp')
    if not os.path.exists(f):
        return None
    return ('<img class="cover-img" src="%sassets/img/%s.webp" width="1920" height="1080" alt="%s" fetchpriority="high" decoding="async" style="image-rendering:pixelated">') % (pre, key, E(alt))


def cover(num, alt, chip, pre, shelf_keys):
    im = cover_img('cover_%s' % num, alt, pre)
    if im:
        return '<header class="cover has-img" id="cover">%s<span class="cover-chip">%s · %s</span></header>' % (im, SERIES, chip)
    import pixel_cover
    shelf = ''.join(face(w, m, 128) for w, m in shelf_keys)
    return ('<header class="cover" id="cover" role="img" aria-label="%s">%s<div class="shelf">%s</div>'
            '<span class="cover-chip">%s · %s</span></header>') % (E(alt), pixel_cover.scene(num), shelf, SERIES, chip)


# ── 단계 블록 ─────────────────────────────────────────────
def why_math(s):
    if not (s.get('whybox') or s.get('mathbox')):
        return ''
    out = ['<div class="wm">']
    w = s.get('whybox')
    if w:
        out.append('<div class="why"><h4>왜 이 방법을 쓰나</h4><ol class="pb"><li><b>문제 상황</b> — %s</li><li><b>앞 방법의 한계</b> — %s</li><li><b>해법</b> — %s</li></ol><div class="easy"><b>쉽게 말하면</b> %s</div></div>' % (
            w['problem'], w['limit'], w['solution'], w['easy']))
    m = s.get('mathbox')
    if m:
        rows = ''.join('<tr><td>%s</td><td>%s</td></tr>' % r for r in m['rows'])
        out.append('<div class="math"><h4>수학 수식을 어려워하는 조수가 대신 물어봅니다</h4>'
                   '<div class="ask">%s<p><b>하루</b> %s</p></div><p class="school">학교 수학으로 보면: %s</p>'
                   '<p><b>박사</b> %s</p><table><thead><tr><th>식 조각</th><th>읽는 법과 뜻</th></tr></thead><tbody>%s</tbody></table>'
                   '<div class="try"><b>숫자로 한 번 해 보기</b><br>%s</div><div class="ask">%s<p><b>하루</b> %s</p></div></div>' % (
                       face('asst', 'shock', 44), m['q'], m['school'], m['doc'], rows, m['try'], face('asst', 'spark', 44), m['comment']))
    out.append('</div>')
    return ''.join(out)


def step_html(P, i, s):
    h = ['<section class="level" id="%s">' % s['id'], '<div class="wrap">']
    h.append('<div class="lvhead"><span class="hex">%d</span><div><h2>%s</h2><span class="tag m">개념: %s</span><span class="tag a">%s</span></div></div>' % (i + 1, s['title'], s['concept'], s['tag']))
    if s.get('where'):
        h.append('<p style="font-size:14px;color:#5b6874;margin-top:8px">지도에서 지금 위치 — %s</p>' % s['where'])
    if s.get('situation'):
        h.append('<div class="docline"><b>박사의 상황 질문</b> %s</div>' % s['situation'])
    h.append(why_math(s))
    if s.get('pair'):
        (lt, lb), (rt, rb) = s['pair']
        h.append('<div class="pair"><div><h4>%s</h4><p>%s</p></div><div><h4>%s</h4><p>%s</p></div></div>' % (lt, lb, rt, rb))
    if s.get('body'):
        h.append(s['body'])
    if s.get('talk'):
        h.append('<div class="steptalk"><span class="lbl">직접 해 보기 전에 — 연구실 대화</span>%s</div>' % ''.join(say(*t) for t in s['talk']))
    if s.get('panel'):
        h.append('<div class="panel"><p class="ptitle">%s</p>%s</div>' % (s.get('panel_title', '직접 해 보기'), s['panel']))
    if s.get('flow'):
        f = s['flow']
        h.append('<div class="panel"><p class="ptitle">행동으로 보기 — %s</p><canvas class="cv flow" id="%s" style="height:%dpx" role="img" aria-label="%s"></canvas><p class="cvcap">%s</p></div>' % (
            f['title'], f['id'], f.get('h', 230), E(f['alt']), f['cap']))
    if s.get('explain'):
        h.append('<div class="explain"><b>풀어서 보면</b>%s</div>' % s['explain'])
    if s.get('calm'):
        h.append('<p class="calm">%s</p>' % s['calm'])
    if s.get('aicheck'):
        h.append('<div class="ai-check"><h4>AI 결과 판단 코너</h4>%s</div>' % s['aicheck'])
    if s.get('bridge'):
        g, f, lim = s['bridge']
        h.append('<div class="bridge"><div class="gen"><h4>일상으로 치면</h4><p>%s</p></div><div class="field"><h4>현장에서는</h4><p>%s</p></div></div><p class="limit">%s</p>' % (g, f, lim))
    if s.get('docline'):
        h.append('<div class="docline"><b>박사의 해석 한 줄</b> %s</div>' % s['docline'])
    if s.get('limit'):
        h.append('<p class="limit"><b>이 단계의 한계 —</b> %s</p>' % s['limit'])
    if s.get('code'):
        rows = ''.join('<tr><td>%s</td><td>%s</td></tr>' % (E(c), m) for c, m in s['code'])
        h.append('<details class="codebox"><summary>%s (몰라도 됩니다)</summary><table><thead><tr><th>코드 한 줄</th><th>뜻 한 줄</th></tr></thead><tbody>%s</tbody></table></details>' % (
            s.get('code_title', '교안의 파이썬 코드로 보면'), rows))
    if s.get('say'):
        h.append(say(*s['say']))
    if s.get('quiz'):
        h.append('<div class="quiz" data-quiz="%s"></div>' % s['id'])
    h.append('</div></section>')
    return '\n'.join(h)


def duel_html(d):
    tf = ''.join(face(w, 'smile', 34) for w, n in TEAM_F)
    tr = ''.join(face(w, 'smile', 34) for w, n in TEAM_R)
    return '''<section class="level" id="duel"><div class="wrap">
<h2>조별 대결 — %s</h2><p>%s</p>
<div class="duel" id="duelbox">
 <div class="head"><div>%s<div><b>초파리 조</b></div><div class="team f">%s</div></div><div class="vs">VS</div><div>%s<div><b>주판봇 조</b></div><div class="team r">%s</div></div></div>
 <div class="cards"><div><b>초파리 조의 선택: %s</b><p>“%s”</p></div><div><b>주판봇 조의 선택: %s</b><p>“%s”</p></div></div>
 <p style="margin:6px 0 4px;font-size:14px;color:#5b6874">먼저 맞혀 보기 — 판정 기준: <b>%s</b></p>
 <div class="ctrl guess"><button type="button" class="bt" aria-pressed="false">초파리 조가 이길 것 같다</button><button type="button" class="bt" aria-pressed="false">주판봇 조가 이길 것 같다</button><span class="gnote" style="font-size:13px;color:#5b6874"></span></div>
 <div class="ctrl"><button type="button" class="bt primary go">결과 보기</button><button type="button" class="bt reset">다시 닫기</button></div>
 <div class="res" aria-live="polite">
  <div class="bars"><div class="bar f"><span>초파리 조</span><i><s></s></i><b></b></div><div class="bar r"><span>주판봇 조</span><i><s></s></i><b></b></div></div>
  <div class="say">%s<div class="bub"><span class="who w-asst">조수 하루 · 점수판</span><p class="ann"></p></div></div>
  <div class="say">%s<div class="bub"><span class="who w-doc">심판 박사</span><p class="ver"></p></div></div>
 </div>
</div>
%s
</div></section>''' % (d['q'], d['intro'], face('fly', 'point', 84), tf, face('robo', 'coin', 84), tr, d['fly_pick'], d['fly_line'], d['robo_pick'], d['robo_line'], d['metric'],
       face('asst', 'report'), face('doc', 'front'), d.get('after', ''))


def sprites_for(body, extra=()):
    keys = set(re.findall(r'data-who="(\w+)" data-mood="(\w+)"', body))
    want = {'%s_%s' % k for k in keys} | set(extra)
    out = {}
    for k in sorted(want):
        b = sprite_b64(k)
        if b:
            out[ALIAS.get(k, k)] = b
    return out


HEAD = '''<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%s</title>%s
<meta property="og:title" content="%s"><meta property="og:type" content="article"><meta property="og:url" content="%s"><meta property="og:image" content="%s"><meta property="og:description" content="%s">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<style>%s%s</style></head>'''


def page_html(P, prev, nxt, fname):
    kg = build_kg(P)
    url = SITE + 'weeks/' + fname
    meta = {'title': P['title'] + ' — ' + P['subtitle'], 'series': SERIES, 'number': P['num'],
            'creator': [{'name': AUTHOR_FULL, 'role': 'author'}], 'contributor': [{'name': 'AI 보조 제작', 'role': 'assistant'}],
            'date': TODAY, 'version': '1.0', 'language': ['ko'], 'license': LICENSE, 'url': url,
            'about': [n['id'] for n in kg['nodes'] if n['type'] == 'Concept'][:6],
            'educationalLevel': '입문 (데이터·코드를 처음 배우는 학부생)', 'learningResourceType': 'interactive explainer',
            'basedOn': [r['id'] for r in P['refs']], 'registry': 'data/KG_00_registry.json',
            'suggestedCitation': '%s (2026). %s — %s. %s %s, v1.0. %s' % (AUTHOR, P['title'], P['subtitle'], SERIES, P['num'], url)}
    refs = []
    for r in P['refs']:
        c = {k: v for k, v in r.items() if k not in ('title_en', 'role', 'verified', 'supports', 'note')}
        c['lab'] = {'work': 'lab:work/' + r['id'], 'role': r.get('role', 'background'), 'supports': r.get('supports', []),
                    'verified': r.get('verified', {'title': True, 'authors': True, 'year': True}), 'checkedBy': '저자 자료 확인 ' + TODAY, 'note': r.get('note', '')}
        refs.append(c)
    sc = SCENE[P['scene']]
    navl = [('top', '처음'), ('crew', '등장인물'), ('why', '왜')] + [(s['id'], '%d %s' % (i + 1, s['short'])) for i, s in enumerate(P['steps'])] + P.get('nav_extra', []) + [('duel', '대결'), ('summary', '정리'), ('kg', '색인'), ('export', '꾸러미')]
    body = []
    body.append('<nav class="top" aria-label="이 페이지 차례"><a class="brand" href="../index.html"><span class="hex">DV</span>%s</a><div class="links">%s</div></nav>' % (
        SERIES, ''.join('<a href="#%s">%s</a>' % a for a in navl)))
    body.append(cover(P['num'], P['cover_alt'], P['chip'] + ' · ' + P['floor'], '../', P.get('cover_faces', (('fly', 'point'), ('asst', 'smile'), ('doc', 'front'), ('robo', 'coin')))))
    talk = ''.join(say(*t) for t in P['hero_talk'])
    kp = ''.join('<div><b>%s</b><span>%s</span></div>' % (a, b) for a, b in P['kpis'])
    f3 = P['first3']
    abbr = ''.join('<li><b>%s</b> — %s</li>' % a for a in P.get('abbr', []))
    first3 = ('<section class="first3" aria-label="처음 오신 분께"><h3>처음 오신 분께 — 이 페이지를 3줄로</h3><ol><li><b>무엇을</b> %s</li><li><b>왜 중요한가</b> %s</li><li><b>업무에서는</b> %s</li></ol>'
              '<p class="nocode">코드와 수식을 몰라도 됩니다. 코드는 접힌 상자에만 있고, 수식은 하루가 하나씩 물어봅니다.</p>'
              '<p class="nocode"><b>처음 읽는 방법</b> — 읽기 약 %d분, 직접 해 보기까지 약 %d분. 처음에는 대화와 「직접 해 보기」만 따라가고, 수학 상자와 코드 상자는 두 번째 읽을 때 열어도 됩니다.</p>%s</section>') % (
        f3[0], f3[1], f3[2], P.get('_read', 15), P.get('_read', 15) * 2, ('<details><summary>이 페이지에 나오는 영어 약어 풀이</summary><ul>%s</ul></details>' % abbr) if abbr else '')
    body.append('<main id="top"><header class="hero"><div class="wrap"><div class="kicker">%s</div><span class="scene %s"><b>%s</b>%s</span><h1>%s<br><span style="font-size:.55em;color:#5b6874">%s</span></h1><p class="question">%s</p>%s%s'
                '<section class="kpis" aria-label="이 페이지의 숫자 요약">%s</section><p style="font-size:13px;color:#5b6874">%s</p><div class="talk">%s</div></div></header>' % (
                    P['kicker'], sc[0], sc[1], P['scene_line'], P['title'], P['subtitle'], P['question'], P['intro'], first3, kp, P.get('kpi_note', ''), talk))
    crew = ''.join('<div>%s<div><b>%s</b><span>%s</span></div></div>' % (face(w, m, 52), NAMES[w], r) for w, m, r in P['crew'])
    body.append('<section class="level" id="crew"><div class="wrap"><h2>등장인물과 이 페이지 사용법</h2>%s<div class="crew">%s</div>'
                '<div class="steps"><div><b>밑줄 친 낱말</b>점선 밑줄을 누르거나 손가락으로 대면 뜻이 나옵니다.</div><div><b>직접 해 보기</b>버튼과 막대(슬라이더)는 눌러도 아무것도 망가지지 않습니다. 언제든 처음으로 돌릴 수 있어요.</div><div><b>진행 표시</b><span id="qprog">퀴즈 0/0</span> · 맨 위 초록 막대는 읽은 만큼 차오릅니다.</div></div>%s</div></section>' % (
                    teams_html(), crew, ('<div class="recap"><b>30초 복습 — </b>%s</div>' % P['recap']) if P.get('recap') else ''))
    why = ''.join('<div><span class="n">%d</span><b>%s</b>%s</div>' % (i + 1, a, b) for i, (a, b) in enumerate(P['why']))
    body.append('<section class="level" id="why"><div class="wrap"><h2>%s</h2><div class="steps">%s</div>%s%s</div></section>' % (P.get('why_title', '왜 이 주제인가'), why, P.get('bigpicture', ''), say(*P['why_say']) if P.get('why_say') else ''))
    for i, s in enumerate(P['steps']):
        body.append(step_html(P, i, s))
    for xs in P.get('extra_sections', []):
        body.append(xs)
    body.append(duel_html(P['duel']))
    body.append('<section class="level" id="summary"><div class="wrap"><h2>정리 — 한 장으로</h2>%s</div></section>' % P['summary'])
    body.append('<section class="level outro" id="outro"><div class="wrap"><h2>오늘의 마무리</h2><div class="talk">%s</div>%s</div></section>' % (''.join(say(*t) for t in P['outro']), P.get('next_note', '')))
    body.append('<section class="kgx kgx-sec level" id="kg"><div class="kgx-wrap"><h2>지식 색인 — 이 페이지에서 찾아보기</h2><p class="kgx-sub">이 페이지에 나온 개념, 용어, 주장, 열린 질문을 한곳에 모았습니다. 검색하고, 항목을 눌러 관계를 보고, "본문"으로 돌아갑니다.</p><div id="kg-mount"></div></div></section>')
    body.append('<section class="kgx kgx-sec level" id="export"><div class="kgx-wrap"><h2>온톨로지·서지 꾸러미 — 이 페이지의 지식을 가져가기</h2><p class="kgx-sub">지식 색인을 출처와 함께 파일로 내려받습니다. Zotero(BibTeX·RIS), Protégé(Turtle), Neo4j·Gephi(CSV), 여러 페이지 합치기(kg.json)에 씁니다. 몰라도 본문을 읽는 데는 지장이 없습니다.</p><div id="export-mount"></div></div></section></main>')
    src_rows = ''.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (E(r['title']), E(r.get('who', '')), ('<a href="%s" target="_blank" rel="noopener">열기</a>' % E(r['URL'])) if r.get('URL') else '') for r in P['refs'])
    pager = '<div class="pager">%s%s</div>' % (
        ('<a href="%s"><small>← 이전 층</small>%s</a>' % (prev[0], E(prev[1]))) if prev else '<a href="../index.html"><small>← 1층 로비</small>건물 안내도</a>',
        ('<a href="%s" style="text-align:right"><small>다음 층 →</small>%s</a>' % (nxt[0], E(nxt[1]))) if nxt else '<a href="../practice/index.html" style="text-align:right"><small>옥상 →</small>마지막 장 · 실전 연습장</a>')
    foot = ('<footer id="sources"><div class="wrap"><h4>출처</h4><div class="tbl"><table><thead><tr><th>자료</th><th>저자·발행</th><th>링크</th></tr></thead><tbody>%s</tbody></table></div>'
            '<h4>예시값·설명용 모형인 것</h4><ul>%s</ul><h4>이 페이지</h4><p>글 · %s (<a href="%s">소개 페이지</a>) · 강남대학교 데이터사이언스전공 「데이터시각화」(2026-2) 강의 자료 해설 · 시리즈 「%s」 %s · 라이선스 %s · <a href="%s">저장소</a> · <a href="../index.html">건물 안내도</a></p>'
            '<p>캐릭터 그림: 연구실 캐릭터 팩(fruitfly-lab-expressions). X1·X2·X3는 정체를 밝히지 않은 연구실 식구입니다. 차트는 모두 이 페이지 안에서 그린 그림이며, 숫자의 근거는 각 단계와 위 출처에 적었습니다.</p>%s</div></footer>') % (
        src_rows, ''.join('<li>%s</li>' % x for x in P['models']), AUTHOR_FULL, AUTHOR_SITE, SERIES, P['num'], LICENSE, REPO, pager)
    bodytxt = '\n'.join(body) + '\n' + foot
    sprites = sprites_for(bodytxt, DUEL_KEYS + P.get('extra_sprites', []))
    quiz = {s['id']: s['quiz'] for s in P['steps'] if s.get('quiz')}
    quiz.update(P.get('extra_quiz', {}))
    data_js = 'var SPRITE=%s;\nvar QUIZ=%s;\nvar GL=%s;\nvar FLOWS={%s};\nvar CARDS=%s;\n' % (
        esc_json(sprites), esc_json(quiz), esc_json({k: v[:3] for k, v in P.get('gloss', {}).items()}),
        ','.join('%s:%s' % (json.dumps(s['flow']['id']), s['flow']['js']) for s in P['steps'] if s.get('flow')), esc_json(P.get('cards', {})))
    duel_js = 'var DUEL={el:"#duelbox",higherIsBetter:%s,drawMargin:%s,run:function(){%s},announce:function(r){%s},verdict:function(res,r){%s}};' % (
        'true' if P['duel'].get('higher', True) else 'false', P['duel'].get('margin', 0), P['duel']['run'], P['duel']['announce'], P['duel']['verdict'])
    head_meta = ''.join('<meta name="%s" content="%s">' % (k, E(v)) for k, v in [
        ('description', P['desc']), ('citation_title', meta['title']), ('citation_author', AUTHOR), ('citation_publication_date', '2026/11/26'),
        ('citation_language', 'ko'), ('dc.title', meta['title']), ('dc.creator', AUTHOR), ('dc.date', TODAY), ('dc.language', 'ko'), ('dc.rights', LICENSE),
        ('dcterms.isPartOf', SERIES)])
    doc = HEAD % ('%s — %s · %s' % (P['title'], P['subtitle'], SERIES), head_meta, E(meta['title']), url, SITE + 'assets/img/og_%s.png' % P['num'], E(P['desc']), CSS, P.get('css', ''))
    doc += '''
<body><div id="prog"></div><div id="tip" role="tooltip"></div>
%s
<script type="application/json" id="kg-raw">%s</script>
<script type="application/ld+json" id="kg-ld">%s</script>
<script type="application/json" id="refs-csl">%s</script>
<script type="application/json" id="page-meta">%s</script>
<script>%s
%s
%s
var PAGE={init:function(LAB){%s}};
</script>
<script>%s</script>
<script>%s</script>
</body></html>''' % (bodytxt, esc_json(kg), esc_json(jsonld(kg, meta)), esc_json(refs), esc_json(meta), data_js, duel_js, P.get('data', ''), P.get('js', ''), JS, KGX)
    return doc, kg


def simple_page(title, desc, body, sprites_body, pre, og):
    sprites = sprites_for(sprites_body)
    doc = HEAD % (title, '<meta name="description" content="%s">' % E(desc), E(title), SITE, og, E(desc), CSS, '')
    return doc + '<body><div id="prog"></div><div id="tip"></div>%s<script>var SPRITE=%s;</script><script>%s</script></body></html>' % (body, esc_json(sprites), JS)


# ── 목차 (디자인 연구실 건물 안내도) ─────────────────────────
def index_html(pages, slots, IDX):
    rows = []
    allp = {P['num']: (P, fn) for P, fn in pages}
    for n in range(15, 0, -1):
        k = '%02d' % n
        if k in allp:
            P, fn = allp[k]
            rows.append('<div class="fl%s"><div class="no">%d층</div><a class="room" href="weeks/%s"><span class="win" aria-hidden="true"></span><span class="t"><b>%s · %s</b><small>%s</small></span><span class="scene %s"><b>%s</b></span><span class="imgs">%s</span></a></div>' % (
                ' rev' if P['kind'] == 'review' else '', n, fn, P['chip'], E(P['title']), E(P['toc']), SCENE[P['scene']][0], SCENE[P['scene']][1],
                ''.join(face(w, m, 28) for w, m in P.get('toc_faces', [('doc', 'front'), ('asst', 'smile')]))))
        else:
            s = slots.get(k, ('작성 중', '이 층은 지금 쓰고 있습니다.', '작성 중'))
            rows.append('<div class="fl off slot"><div class="no">%d층</div><div class="room"><span class="win" aria-hidden="true"></span><span class="t"><b>%02d주차 · %s</b><small>%s</small></span><span class="pill">%s</span></div></div>' % (
                n, n, E(s[0]), E(s[1]), s[2]))
    bld = ('<div class="bld" role="list" aria-label="디자인 연구실 건물 층별 안내"><div class="roof"><span>옥상 · 마지막 장</span><a href="practice/index.html">실전 연습장 — 카페·결제·건강검진·물류센터를 직접 운영해 보기 →</a></div>%s<div class="ground" aria-hidden="true"></div></div>') % ''.join(rows)
    body = IDX['body'].replace('{{BUILDING}}', bld).replace('{{TEAMS}}', teams_html())
    cov = cover('00', IDX['cover_alt'], '건물 안내도', '', (('fly', 'point'), ('asst', 'proud'), ('doc', 'front'), ('robo', 'smile')))
    nav = '<nav class="top"><a class="brand" href="index.html"><span class="hex">DV</span>%s</a><div class="links"><a href="#course">강좌 안내</a><a href="#building">층별 안내</a><a href="#teams">두 팀</a><a href="#how">공부하는 법</a><a href="#tools">실습 도구</a><a href="#old">옛 강의 페이지</a></div></nav>' % SERIES
    full = nav + cov + '<main id="top">' + body + '</main>'
    return simple_page('%s — 데이터 시각화 15주 연구실 해설' % SERIES, IDX['desc'], full, full, '', SITE + 'assets/img/og_00.png')


def main():
    import importlib.util
    _sp = importlib.util.spec_from_file_location('persona_fixes', os.path.join(HERE, 'persona_fixes.py')); PF = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(PF)
    specs = sorted(glob.glob(os.path.join(HERE, 'pages', 'w*.py')))
    pages = []
    for f in specs:
        g = {'say': say, 'face': face, 'E': E, 'teams_html': teams_html, 'HERE': HERE, 'json': json}
        exec(open(f, encoding='utf-8').read(), g)
        P = g['PAGE']
        P.setdefault('id', 'dv_w' + P['num'])
        _txt = re.sub(r'<[^>]+>', ' ', json.dumps({k: v for k, v in P.items() if k not in ('js', 'css', 'data', 'refs', 'facts', 'models', 'gloss')}, ensure_ascii=False, default=str))
        _txt = re.sub(r'[{}\[\]",:]', ' ', _txt)
        P['_read'] = max(10, int(round(len(_txt.split()) / 180.0 / 5.0)) * 5)
        for st in P['steps']:
            c = PF.CALM.get(P['num'], {}).get(st['id'])
            if c and not st.get('calm'):
                st['calm'] = c
        pages.append((P, 'w%s_%s.html' % (P['num'], P['slug'])))
    os.makedirs(os.path.join(ROOT, 'weeks'), exist_ok=True)
    registry = {'version': '1.0', 'series': SERIES, 'updated': TODAY, 'domain': 'dataviz', 'ids': {}}
    report = []
    for i, (P, fn) in enumerate(pages):
        prev = (pages[i - 1][1], pages[i - 1][0]['chip'] + ' ' + pages[i - 1][0]['title']) if i else None
        nxt = (pages[i + 1][1], pages[i + 1][0]['chip'] + ' ' + pages[i + 1][0]['title']) if i + 1 < len(pages) else None
        doc, kg = page_html(P, prev, nxt, fn)
        open(os.path.join(ROOT, 'weeks', fn), 'w', encoding='utf-8').write(doc)
        for n in kg['nodes']:
            if n['type'] in ('Concept', 'Term', 'Topic', 'Area', 'Method', 'Work'):
                registry['ids'].setdefault(n['id'], {'ko': n['label']['ko'], 'en': n['label']['en'], 'type': n['type'], 'pages': []})
                if P['id'] not in registry['ids'][n['id']]['pages']:
                    registry['ids'][n['id']]['pages'].append(P['id'])
        nq = sum(len(s.get('quiz', [])) for s in P['steps'])
        report.append('%s %-34s %6.0f KB  nodes %3d edges %3d quiz %2d' % (P['num'], fn, len(doc.encode()) / 1024, len(kg['nodes']), len(kg['edges']), nq))
    g = {'say': say, 'face': face, 'E': E}
    exec(open(os.path.join(HERE, 'pages', 'slots.py'), encoding='utf-8').read(), g)
    IDX = {}
    exec(open(os.path.join(HERE, 'pages', 'index.py'), encoding='utf-8').read(), {'face': face, 'say': say, 'E': E, 'IDX': IDX})
    open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(index_html(pages, g['SLOTS'], IDX))
    # 실전 연습장
    PR = {}
    exec(open(os.path.join(HERE, 'practice.py'), encoding='utf-8').read(), {'face': face, 'say': say, 'E': E, 'PR': PR, 'json': json})
    nav = '<nav class="top"><a class="brand" href="../index.html"><span class="hex">DV</span>%s</a><div class="links">%s</div></nav>' % (SERIES, PR['nav'])
    full = nav + cover('99', PR['cover_alt'], '옥상 · 실전 연습장', '../', (('robo', 'coin'), ('sia', 'smile'), ('doc', 'front'), ('fly', 'point'), ('moa', 'cheer'))) + PR['body']
    os.makedirs(os.path.join(ROOT, 'practice'), exist_ok=True)
    doc = simple_page('실전 연습장 — ' + SERIES, PR['desc'], full, full + ' '.join('data-who="%s" data-mood="%s"' % tuple(k.split('_', 1)) for k in PR['moods']), '../', SITE + 'assets/img/og_99.png')
    doc = doc.replace('</body>', '<script>%s</script></body>' % PR['js'])
    open(os.path.join(ROOT, 'practice', 'index.html'), 'w', encoding='utf-8').write(doc)
    report.append('99 practice/index.html %6.0f KB' % (len(doc.encode()) / 1024))
    os.makedirs(os.path.join(ROOT, 'data'), exist_ok=True)
    json.dump(registry, open(os.path.join(ROOT, 'data', 'KG_00_registry.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    items = [{'id': 'cover_%s' % k, 'role': 'cover', 'path': 'assets/img/cover_%s.webp' % k if os.path.exists(os.path.join(ROOT, 'assets', 'img', 'cover_%s.webp' % k)) else None,
              'status': 'ok' if os.path.exists(os.path.join(ROOT, 'assets', 'img', 'cover_%s.webp' % k)) else 'pixel-fallback', 'prompt': 'docs/COVER_PROMPTS.md#cover_%s' % k}
             for k in ['00'] + [P['num'] for P, fn in pages] + ['99']]
    json.dump({'series_ko': SERIES, 'site_url': SITE, 'updated': TODAY, 'style': '16-bit RPG pixel art, white background', 'items': items},
              open(os.path.join(ROOT, 'cover_manifest.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    # 표지: 원래 픽셀 격자 그대로 저장한 그림을 정수배로만 키워 보이게 한다 (자르지 않음)
    _cf = importlib.util.spec_from_file_location('cover_fit', os.path.join(HERE, 'tools', 'cover_fit.py')); CF = importlib.util.module_from_spec(_cf); _cf.loader.exec_module(CF)
    for _p in [os.path.join(ROOT, 'weeks', fn) for P, fn in pages] + [os.path.join(ROOT, 'index.html'), os.path.join(ROOT, 'practice', 'index.html')]:
        CF.patch(_p)
    print('\n'.join(report))


if __name__ == '__main__':
    main()
