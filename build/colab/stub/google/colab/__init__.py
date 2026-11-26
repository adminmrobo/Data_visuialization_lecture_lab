# 로컬 실행용 가짜 google.colab — files.upload()가 Colab처럼 파일을 현재 폴더에 저장하고 같은 안내를 출력한다
import os, shutil, datetime
class _Files:
    def upload(self):
        out = {}
        for p in os.environ.get('COLAB_UPLOAD', '').split(os.pathsep):
            if not p:
                continue
            n = os.path.basename(p)
            shutil.copy(p, n)
            sz = os.path.getsize(n)
            print('%s(text/csv) - %d bytes, last modified: 2026. 11. 26. - 100%% done' % (n, sz))
            print('Saving %s to %s' % (n, n))
            out[n] = open(n, 'rb').read()
        return out
files = _Files()
