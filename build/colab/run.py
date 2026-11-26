# Colab 화면용 코드 실행기: build/colab/wNN_k.py 를 실제로 실행해 출력과 그림을 남긴다
import os, sys, io, json, glob, tempfile, contextlib, runpy, ast, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(HERE, 'stub'))
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
sys.path.insert(0, HERE)
from manifest import CELLS
only = sys.argv[1:]
for key, c in CELLS.items():
    if only and key not in only:
        continue
    src = open(os.path.join(HERE, key + '.py'), encoding='utf-8').read()
    tree = ast.parse(src)
    bad = [type(n).__name__ for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.For, ast.While, ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp, ast.Lambda, ast.If, ast.With, ast.Try, ast.ClassDef))]
    indented = [l for l in src.split('\n') if l[:1] in (' ', '\t')]
    assert not bad and not indented, (key, bad, indented[:2])
    imgs = []
    def show(*a, **k):
        n = len(imgs) + 1
        png = os.path.join(tempfile.gettempdir(), '%s_%d.png' % (key, n))
        plt.gcf().savefig(png, dpi=110, bbox_inches='tight', facecolor='white')
        w = os.path.join(ROOT, 'assets', 'img', 'colab', '%s_%d.webp' % (key, n))
        Image.open(png).convert('RGB').save(w, 'WEBP', quality=88, method=6)
        imgs.append('%s_%d.webp' % (key, n)); plt.close('all')
    plt.show = show
    os.environ['COLAB_UPLOAD'] = os.pathsep.join(os.path.join(ROOT, 'data', 'raw', f) for f in c['files'])
    buf = io.StringIO(); cwd = os.getcwd(); td = tempfile.mkdtemp(); os.chdir(td)
    try:
        with contextlib.redirect_stdout(buf):
            runpy.run_path(os.path.join(HERE, key + '.py'), run_name='__main__')
    finally:
        os.chdir(cwd)
    out = buf.getvalue().rstrip()
    json.dump({'code': src.rstrip(), 'stdout': out, 'imgs': imgs}, open(os.path.join(HERE, 'out', key + '.json'), 'w'), ensure_ascii=False, indent=1)
    print(key, 'lines', src.count('\n') + 1, 'imgs', imgs, 'stdout', len(out))
