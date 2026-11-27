#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""빌드 뒤 한국어 페이지에 언어 전환 상자(i18n switcher)와 hreflang 링크를 다시 넣는다.
기준: git HEAD에 있는 같은 파일의 블록. 새 페이지는 --new 새파일=본보기파일 로 본보기의 블록을 파일 이름만 바꿔 쓴다.
사용: python3 build/tools/i18n_keep.py [--new weeks/w13_x.html=weeks/w12_y.html]"""
import os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SW = re.compile(r'<!-- i18n:switcher -->.*?<!-- /i18n:switcher -->', re.S)
ALT = re.compile(r'(?:<link rel="alternate" hreflang="[^"]+" href="[^"]+">)+')

def head(rel):
    try:
        return subprocess.run(['git', '-C', ROOT, 'show', 'HEAD:' + rel], capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError:
        return None

def put(rel, src, rename=None):
    p = os.path.join(ROOT, rel); s = open(p, encoding='utf-8').read()
    if '<!-- i18n:switcher -->' in s:
        return False
    sw = SW.search(src); alt = ALT.search(src)
    if not sw:
        return False
    sw, alt = sw.group(0), (alt.group(0) if alt else '')
    if rename:
        for a, b in rename:
            sw, alt = sw.replace(a, b), alt.replace(a, b)
    s = s.replace('<meta charset="utf-8">', '<meta charset="utf-8">' + sw, 1)
    if alt:
        s = re.sub(r'</style>(\s*)</head>', lambda m: '</style>' + alt + m.group(1) + '</head>', s, count=1)
    open(p, 'w', encoding='utf-8').write(s)
    return True

if __name__ == '__main__':
    new = dict(a.split('=') for a in sys.argv[sys.argv.index('--new') + 1:]) if '--new' in sys.argv else {}
    import glob
    for p in sorted(glob.glob(os.path.join(ROOT, 'weeks', '*.html')) + [os.path.join(ROOT, 'index.html'), os.path.join(ROOT, 'practice', 'index.html')]):
        rel = os.path.relpath(p, ROOT)
        if re.search(r'\.[a-z]{2}\.html$', rel):
            continue
        if rel in new:
            t = new[rel]; tb = os.path.basename(t)[:-5]; nb = os.path.basename(rel)[:-5]
            ok = put(rel, head(t) or '', [(tb, nb)])
        else:
            h = head(rel); ok = put(rel, h) if h else False
        print(('kept ' if ok else 'skip ') + rel)
