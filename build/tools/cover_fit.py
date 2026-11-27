#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""표지 선명하게 보이기 — 이미 만들어진(번역판 포함) HTML에 표지 맞춤 CSS와 작은 스크립트를 넣는다.

표지 그림은 원래 픽셀 격자 그대로(예: 480×270) 저장하고, 화면에는 격자의 정수배(2배·3배…)로만 키워
픽셀 경계가 번지지 않게 한다. 그림 전체가 보이도록 위아래를 자르지 않는다.
여러 번 돌려도 한 번만 들어간다.  사용: python3 build/tools/cover_fit.py
"""
import glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CSS = ('/* cover-fit */.cover.has-img{aspect-ratio:auto;max-height:none;height:auto;display:flex;justify-content:center;align-items:flex-end;background:#fff}'
       '.cover.has-img img.cover-img{position:relative;inset:auto;display:block;width:min(100%,calc(min(78vh,820px)*16/9));height:auto;aspect-ratio:16/9;object-fit:contain;image-rendering:pixelated}'
       '.cover.has-img .cover-chip{top:12px;bottom:auto}@media (max-width:600px){.cover.has-img{flex-direction:column;align-items:center}.cover.has-img .cover-chip{position:static;margin:6px 0 10px}}/* /cover-fit */')
JS = ('<script data-i18n-skip data-cover-fit>(function(){var i=document.querySelector("img.cover-img");if(!i)return;'
      'function f(){var c=i.parentNode,d=window.devicePixelRatio||1,g=i.naturalWidth||480,'
      'm=Math.min(c.clientWidth,Math.min(window.innerHeight*.78,820)*16/9),r=m*d/g,k=Math.floor(r);'
      'if(r>=3||(d<2&&r>=1)){i.style.width=(k*g/d)+"px";i.style.imageRendering="pixelated";}'
      'else{i.style.width=m+"px";i.style.imageRendering=r>=1?"pixelated":"auto";}}'
      'if(i.complete)f();else i.addEventListener("load",f);window.addEventListener("resize",f);})();</script>')


def patch(path):
    s = open(path, encoding='utf-8').read()
    if 'class="cover-img"' not in s:
        return False
    o = s
    s = re.sub(r'/\* cover-fit \*/.*?/\* /cover-fit \*/', '', s, flags=re.S)
    s = re.sub(r'<script data-i18n-skip data-cover-fit>.*?</script>', '', s, flags=re.S)
    head_end = s.index('</head>')
    k = s.rindex('</style>', 0, head_end)
    s = s[:k] + CSS + s[k:]
    s = re.sub(r'(<img class="cover-img"[^>]*>)', lambda m: m.group(1) + JS, s, count=1)
    if s != o:
        open(path, 'w', encoding='utf-8').write(s)
    return s != o


if __name__ == '__main__':
    n = 0
    for p in sorted(glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)):
        if '/lecture_0' in p or '/dist/' in p:
            continue
        if patch(p):
            n += 1
            print('patched', os.path.relpath(p, ROOT))
    print(n, 'files')
