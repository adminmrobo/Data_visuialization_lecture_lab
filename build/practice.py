# 옥상 · 마지막 장 — 실전 연습장 (카페 · 결제 · 건강검진 · 물류센터)
PR['nav'] = '<a href="#cafe">카페</a><a href="#pay">결제</a><a href="#health">건강검진</a><a href="#logi">물류센터</a><a href="../index.html">건물 안내도</a>'
PR['desc'] = '데이터 시각화 실전 연습장: 카페 메뉴 보고 차트, 결제 데이터 빈 값과 대표값, 건강검진 혈당 분포와 기준선, 물류센터 히트맵·파레토로 인력과 개선 순서 정하기를 직접 조작하고 미션 3개씩 자동 판정받는 시뮬레이터.'
PR['cover_alt'] = '디자인 연구실 건물 옥상에 이젤 네 개가 놓이고, 막대·분포·히트맵·누적선이 그려진 픽셀 표지'
PR['moods'] = ['doc_judge', 'doc_think', 'doc_verdict', 'asst_report', 'asst_think', 'asst_wow', 'fly_magnify', 'fly_point', 'fly_arms',
               'robo_happy', 'robo_chart', 'robo_sigh', 'robo_wow', 'robo_coin']

_CSS = '''<style>
.pr-tabs{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0}
.pr-tabs button{font:inherit;font-weight:700;padding:10px 16px;border-radius:12px;border:1.5px solid #cbd5e1;background:#fff;cursor:pointer}
.pr-tabs button[aria-selected=true]{background:#1e3a8a;color:#fff;border-color:#1e3a8a}
.pr-sc[hidden]{display:none}
.pr-box{border-left:4px solid #1e3a8a;background:#f4f7fc;padding:16px 20px;border-radius:10px;line-height:1.8;margin:12px 0}
.pr-ctrl{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:14px 0}
.pr-ctrl>div{border:2px solid;border-radius:12px;padding:12px 16px}
.pr-ctrl .g{border-color:#13733a;background:#f1faf4}.pr-ctrl .b{border-color:#1e3a8a;background:#f2f5fd}
.pr-ctrl h4{margin:0 0 8px;font-size:14px}.pr-ctrl .g h4{color:#13733a}.pr-ctrl .b h4{color:#1e3a8a}
.pr-ctrl label{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:6px 0;font-size:15px}
.pr-ctrl input[type=range]{flex:1;min-width:120px}.pr-ctrl select{font:inherit;padding:4px 6px;max-width:100%}
.pr-kpi{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:12px 0}
.pr-kpi div{border:1.5px solid #e2e8f0;border-radius:12px;padding:10px 12px;background:#fff}
.pr-kpi b{display:block;font-size:22px}.pr-kpi small{color:#5b6874;font-size:13px}
.pr-kpi .ok{border-color:#13733a}.pr-kpi .ok b{color:#13733a}.pr-kpi .ng{border-color:#b45309}.pr-kpi .ng b{color:#b45309}
.pr-g2{display:grid;grid-template-columns:1fr 1fr;gap:12px}.pr-g2>*{min-width:0}
.pr-say{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:12px 0}
.pr-mis{list-style:none;padding:0;margin:10px 0}.pr-mis li{border:1.5px dashed #cbd5e1;border-radius:10px;padding:10px 14px;margin:6px 0;line-height:1.7}
.pr-mis li.done{border-style:solid;border-color:#13733a;background:#f1faf4}.pr-mis li b.st{display:inline-block;min-width:64px}
.pr-back{font-size:15px;color:#5b6874}
@media (max-width:860px){.pr-ctrl,.pr-g2,.pr-say{grid-template-columns:1fr}.pr-kpi{grid-template-columns:1fr 1fr}}
</style>'''


def _scene(key, title, situation, green, blue, back):
    return ('<section class="level pr-sc" id="sc-%s" role="tabpanel" aria-labelledby="tab-%s"%s><div class="wrap">'
            '<h2>%s</h2><div class="pr-box"><b>상황</b> %s</div>'
            '<div class="pr-ctrl"><div class="g"><h4>시장·현장 조건 (초록)</h4>%s</div><div class="b"><h4>내 결정 (파랑)</h4>%s</div></div>'
            '<div class="pr-kpi" id="%s-kpi" aria-live="polite"></div>'
            '<div class="pr-g2"><div class="viz" id="%s-v1"></div><div class="viz" id="%s-v2"></div></div>'
            '<div class="pr-say" id="%s-say"></div>'
            '<h3>미션 세 개</h3><ul class="pr-mis" id="%s-mis"></ul>'
            '<p class="pr-back">배운 곳 다시 보기: %s</p></div></section>') % (
        key, key, '' if key == 'cafe' else ' hidden', title, situation, green, blue, key, key, key, key, key, back)


_cafe = _scene('cafe', '① 카페 — 사장님께 올릴 메뉴별 판매 차트',
    '카페 사장님이 “이번 달 어느 메뉴가 제일 잘 팔렸고, 2위와 얼마나 차이 나?”라고 묻습니다. 회의 시간은 짧습니다. 사장님이 <b>2초 안에 1위를 찾고, 차이를 실제 크기대로</b> 보게 만드세요.',
    '<label>메뉴 수 <input type="range" id="cf-n" min="3" max="10" value="5"> <span id="cf-nv"></span></label>'
    '<label>1위와 2위의 실제 차이 <input type="range" id="cf-gap" min="2" max="30" value="20"> <span id="cf-gapv"></span></label>',
    '<label>차트 <select id="cf-type"><option value="pie">파이</option><option value="bar">막대</option></select></label>'
    '<label><input type="checkbox" id="cf-sort"> 큰 것부터 정렬</label>'
    '<label><input type="checkbox" id="cf-hl"> 1위만 강조 색</label>'
    '<label>Y축 시작값 (2위 판매량의 %) <input type="range" id="cf-y0" min="0" max="90" step="10" value="0"> <span id="cf-y0v"></span></label>',
    '<a href="../weeks/w02_chart-theory.html">2층 — 정크와 Y축 0</a> · <a href="../weeks/w08_midterm-assignment.html">8층 — 그래프 A 배율</a>')

_pay = _scene('pay', '② 결제 — 빈 값과 대표값으로 보고 숫자 정하기',
    '결제 기록 800건 가운데 일부 금액이 비어 있고, 가끔 아주 큰 결제가 섞입니다. 팀장이 묻는 질문에 맞는 <b>대표값 하나</b>를 히스토그램과 함께 보고하세요. 질문이 바뀌면 맞는 처리도 바뀝니다.',
    '<label>팀장의 질문 <select id="py-q"><option value="typ">보통 손님 한 번 결제액은?</option><option value="avg">한 달 총매출 계산용 1건 평균은?</option></select></label>'
    '<label>빈 값 비율 <input type="range" id="py-miss" min="0" max="20" value="10"> <span id="py-missv"></span></label>'
    '<label>아주 큰 결제 <input type="range" id="py-out" min="0" max="5" value="2"> <span id="py-outv"></span></label>',
    '<label>빈 값 처리 <select id="py-fill"><option value="zero">0으로 채우기</option><option value="drop">빈 값 빼고 계산</option><option value="med">중앙값으로 채우기</option></select></label>'
    '<label>대표값 <select id="py-stat"><option value="mean">평균</option><option value="median">중앙값</option></select></label>',
    '<a href="../weeks/w03_data-cleaning.html">3층 — 빈 값과 0 채우기</a> · <a href="../weeks/w04_industry-fintech.html">4층 — 평균 함정과 상자그림</a>')

_health = _scene('health', '③ 건강검진 — 평균이 숨긴 꼬리를 찾기',
    '건강검진 3,000명의 공복혈당 자료입니다. 보건소장이 “우리 지역 혈당, 괜찮은 거지?”라고 묻습니다. 평균만 보면 괜찮아 보입니다. <b>126 mg/dL 이상</b>(당뇨 의심 기준)인 사람이 얼마나 되는지 화면에서 바로 읽히게 만드세요.',
    '<label>고령층(60세 이상) 비율 <input type="range" id="hc-old" min="10" max="70" step="10" value="30"> <span id="hc-oldv"></span></label>',
    '<label>차트 <select id="hc-type"><option value="avg">연령대별 평균 막대</option><option value="hist">분포(히스토그램)</option></select></label>'
    '<label><input type="checkbox" id="hc-ref"> 126 기준선 표시</label>'
    '<label>구간 폭 <select id="hc-bin"><option>20</option><option>10</option><option>5</option></select> mg/dL</label>',
    '<a href="../weeks/w10_healthcare.html">10층 — 기준선과 1,551명</a>')

_logi = _scene('logi', '④ 물류센터 — 인력 두 명과 개선 하나',
    '물류센터 배송 1,000건 가운데 늦은 배송이 있습니다. 이번 주에 쓸 수 있는 것은 <b>추가 인력 두 명(한 시간대)</b>과 <b>원인 하나를 고칠 예산</b>뿐입니다. 히트맵으로 시간대를, 파레토로 원인을 고르세요.',
    '<label>금요일 저녁 물량 증가 <input type="range" id="lg-fri" min="0" max="60" step="5" value="25"> <span id="lg-friv"></span></label>'
    '<label>토요일 낮 할인 행사 <input type="range" id="lg-sat" min="0" max="100" step="10" value="0"> <span id="lg-satv"></span></label>'
    '<label>주소 오류율 <input type="range" id="lg-addr" min="1" max="10" value="3"> <span id="lg-addrv"></span></label>',
    '<label>추가 인력 시간대 <select id="lg-slot"><option value="0">월 8시</option><option value="1">수 13시</option><option value="2">금 18시</option><option value="3">토 14시</option></select></label>'
    '<label>고칠 원인 <select id="lg-fix"><option>차량 고장</option><option>교통 체증</option><option>주소 오류</option><option>물량 폭주</option><option>기상 악화</option></select></label>',
    '<a href="../weeks/w11_smartcity-logistics.html">11층 — 히트맵과 파레토</a> · <a href="../weeks/w12_ai-studio-dashboard.html">12층 — 필터로 묶은 판</a>')

PR['body'] = _CSS + '''<main id="top"><section class="level"><div class="wrap">
<p class="kicker">옥상 · 마지막 장</p><h1>실전 연습장 — 네 현장에서 차트로 결정하기</h1>
<div class="first3"><h3>처음 오신 분께 — 이 페이지를 3줄로</h3><ol>
<li><b>무엇을</b>: 카페·결제·건강검진·물류센터 네 현장에서, 차트 종류와 처리 방법을 직접 골라 보고서를 만듭니다.</li>
<li><b>왜 중요한가</b>: 같은 데이터라도 차트를 어떻게 고르느냐에 따라 회의의 결론이 달라집니다.</li>
<li><b>업무에서는</b>: 보고 차트 한 장, 대표값 한 개, 인력 배치 한 번 — 모두 이 연습장의 조작과 같은 순서로 정합니다. 코드·수식을 몰라도 됩니다.</li></ol></div>
<p>초록 상자는 <b>현장의 조건</b>(내가 바꿀 수 없는 것), 파랑 상자는 <b>내 결정</b>입니다. 조작하면 성적표 네 개, 그래프 두 개, 등장인물 네 명의 말이 바로 바뀝니다. 미션은 직접 조작한 뒤에만 통과 표시가 켜집니다. 주소 끝에 <code>#cafe</code> · <code>#pay</code> · <code>#health</code> · <code>#logi</code>를 붙이면 그 현장이 바로 열립니다.</p>
<div class="pr-tabs" role="tablist" aria-label="현장 고르기"><button type="button" role="tab" id="tab-cafe" data-k="cafe" aria-selected="true">① 카페</button><button type="button" role="tab" id="tab-pay" data-k="pay" aria-selected="false">② 결제</button><button type="button" role="tab" id="tab-health" data-k="health" aria-selected="false">③ 건강검진</button><button type="button" role="tab" id="tab-logi" data-k="logi" aria-selected="false">④ 물류센터</button></div>
</div></section>''' + _cafe + _pay + _health + _logi + '''<section class="level"><div class="wrap">
<h2>마무리 — 네 현장이 함께 묻는 질문</h2>
<div class="pr-box">네 현장은 모두 같은 것을 물었습니다. <b>“이 그림을 본 사람이 2초 안에, 실제 크기대로, 맞는 결정을 내릴 수 있는가?”</b> 카페에서는 Y축 0과 정렬이, 결제에서는 질문에 맞는 대표값이, 건강검진에서는 평균 대신 분포와 기준선이, 물류센터에서는 히트맵의 가장 진한 시간과 파레토의 첫 막대가 그 답이었습니다.</div>
<p style="font-size:14px;color:#5b6874">모형의 한계: 이 연습장의 데이터와 효과(예: 인력 두 명이 물량 지연을 줄이는 정도, 차트를 읽는 데 걸리는 시간)는 설명을 위해 단순하게 만든 <b>교육용 가상 숫자</b>입니다. 실제 경영·의료 판단이나 투자 권고가 아닙니다. 기록은 이 탭을 열어 둔 동안에만 남고 저장되지 않습니다.</p>
<p><a href="../index.html">← 건물 안내도로</a> · <a href="../weeks/w12_ai-studio-dashboard.html">12층 대시보드 공방으로</a></p>
</div></section></main>'''

PR['js'] = r'''(function(){var V=LAB.VIZ,$=LAB.$,$$=LAB.$$,nf=LAB.nf;
function kpi(id,a){$('#'+id+'-kpi').innerHTML=a.map(function(k){return '<div class="'+(k[2]===true?'ok':k[2]===false?'ng':'')+'"><small>'+k[0]+'</small><b>'+k[1]+'</b></div>';}).join('');}
var NM={doc:'박사',asst:'조수 하루',fly:'초파리',robo:'주판봇'};
function says(id,a){$('#'+id+'-say').innerHTML=a.map(function(x){return '<div class="say"><img data-who="'+x[0]+'" data-mood="'+x[1]+'" width="56" height="56" alt="" aria-hidden="true"><div class="bub"><span class="who w-'+x[0]+'">'+NM[x[0]]+'</span><p>'+x[2]+'</p></div></div>';}).join('');if(window.Cast)Cast.fill();}
var MS={};function mis(id,list,touched){MS[id]=MS[id]||{};var st=MS[id];$('#'+id+'-mis').innerHTML=list.map(function(m,i){if(touched&&m[1])st[i]=1;return '<li class="'+(st[i]?'done':'')+'"><b class="st">'+(st[i]?'✓ 통과':'미션 '+(i+1))+'</b> '+m[0]+(st[i]&&m[2]?'<br><small>'+m[2]+'</small>':'')+'</li>';}).join('');}
var TOUCH={};function bind(id,ids,fn){ids.forEach(function(x){var e=$('#'+x);e.addEventListener('input',function(){TOUCH[id]=1;fn();});e.addEventListener('change',function(){TOUCH[id]=1;fn();});});fn();}
/* ── ① 카페 ── */
var MENU=['아메리카노','라떼','바닐라라떼','콜드브루','녹차라떼','에이드','스무디','케이크','쿠키','샌드위치'],PERM=[2,5,0,7,3,1,9,4,8,6],CF={m3env:0};
function cafeVals(n,gap){var v=[1000,Math.round(1000/(1+gap/100))];for(var k=2;k<n;k++)v.push(Math.round(v[1]*Math.pow(.82,k-1)));return v;}
function lieF(v1,v2,b){return ((v1-b)/(v2-b)-1)/((v1/v2)-1);}
function cafe(){var n=+$('#cf-n').value,gap=+$('#cf-gap').value,type=$('#cf-type').value,srt=$('#cf-sort').checked,hl=$('#cf-hl').checked,y0p=+$('#cf-y0').value;
 $('#cf-nv').textContent=n+'개';$('#cf-gapv').textContent=gap+'%';$('#cf-y0v').textContent=y0p+'%';$('#cf-y0').disabled=type==='pie';
 var v=cafeVals(n,gap),b=type==='bar'?v[1]*y0p/100:0,lie=type==='bar'?lieF(v[0],v[1],b):1;
 var t=type==='pie'?1.5+.5*n+(gap<10?2:0):(srt?1:1+.35*n);if(type==='bar'&&hl)t-=.4;t=Math.max(.6,t);
 var acc=type==='pie'?(gap<10?50+gap*2:Math.min(85,75+gap/2)):Math.max(30,100-(lie-1)*25);
 var good=lie<=1.05&&t<=2&&acc>=90;
 kpi('cafe',[['거짓말 지수 (1.0이 정직)',lie.toFixed(2),lie<=1.05],['1위 찾는 시간',t.toFixed(1)+'초',t<=2],['차이 읽기 정확도',Math.round(acc)+'%',acc>=90],['판정',good?'보고 가능':'고칠 곳 있음',good]]);
 var idx=PERM.filter(function(i){return i<n;});if(srt)idx=idx.slice().sort(function(a,c){return a-c;});
 var labs=idx.map(function(i){return MENU[i];}),vals=idx.map(function(i){return v[i];}),top=idx.indexOf(0);
 if(type==='pie')V.pie($('#cafe-v1'),{labels:labs,values:vals,pct:false,title:'이번 달 메뉴별 판매 (잔)',w:420,h:300});
 else V.bar($('#cafe-v1'),{labels:labs,values:vals,y0:Math.round(b),hl:hl?top:-1,title:(hl&&srt?MENU[0]+'가 1위 — 2위보다 '+gap+'% 더 팔렸다':'이번 달 메뉴별 판매 (잔)'),unit:'판매량 (잔)',h:300,w:420});
 var xs=[],ys=[];for(var p=0;p<=90;p+=10){xs.push(p+'%');ys.push(+lieF(v[0],v[1],v[1]*p/100).toFixed(1));}
 V.line($('#cafe-v2'),{labels:xs,series:[{name:'거짓말 지수',values:ys,vlab:true}],hl:type==='bar'?{s:0,i:y0p/10}:null,y0:0,title:'Y축 시작값을 올리면 차이가 부풀려진다',h:300,w:420});
 var r=(v[0]/v[1]).toFixed(2),shown=type==='bar'?((v[0]-b)/(v[1]-b)).toFixed(2):r;
 says('cafe',[['doc',good?'verdict':'judge',good?'판정: 사장님이 '+t.toFixed(1)+'초 안에 1위를 찾고, 차이를 실제 크기대로 봅니다. 보고해도 됩니다.':type==='pie'?'판정 보류. 조각 '+n+'개의 각도로는 1·2위 차이 '+gap+'%를 읽기 어렵습니다.':lie>1.05?'판정 보류. 막대 길이로는 1위가 2위의 '+shown+'배로 보이지만 실제는 '+r+'배입니다.':'거의 됐습니다. 정렬과 강조로 1위 찾는 시간을 줄여 보세요.'],
  ['asst','report','보고: 거짓말 지수 '+lie.toFixed(2)+', 1위 찾기 '+t.toFixed(1)+'초, 차이 읽기 '+Math.round(acc)+'%.'],
  ['fly','magnify',b>0&&type==='bar'?'Y축이 0이 아니야. 아래가 잘려서 1·2위 차이가 '+lie.toFixed(1)+'배 부풀었어.':type==='pie'?'파이는 조각이 많아질수록 각도 비교가 어려워. 막대로 바꿔 봐.':!srt?'정렬 안 하면 눈이 왔다 갔다 해. 큰 것부터 세워 봐.':'정직한 그림이네. 메뉴를 늘리고 차이를 좁혀도 그대로일까?'],
  ['robo',b>0&&type==='bar'?'wow':type==='pie'?'happy':'chart',b>0&&type==='bar'?'와, 1위가 압도적이야! 이대로 보고하면 박수 나오겠다!':type==='pie'?'파이가 제일 예쁘잖아! 동그라미는 다 좋아!':'1위 '+MENU[0]+'! 2위는 안 봐도 되지?']]);
 if(TOUCH.cafe&&(n>=8&&gap<=5))CF.m3env=1;
 mis('cafe',[['사장님이 2초 안에 1위를 찾고 거짓말 지수 1.0인 차트 만들기',type==='bar'&&b===0&&srt&&t<=2,'막대 · Y축 0 · 정렬. 2층에서 배운 세 가지입니다.'],
  ['함정 관찰: Y축 시작값을 올려 거짓말 지수가 3 이상이 되는 것 보기',type==='bar'&&lie>=3,'눈금 숫자는 그대로인데 막대 길이만 과장됩니다. 8층 “그래프 A 배율” 문제와 같은 함정입니다.'],
  ['조건을 바꿔도 유지: 메뉴 8개 이상 · 차이 5% 이하에서 미션 1 조건 지키기',n>=8&&gap<=5&&type==='bar'&&b===0&&srt&&t<=2,'차이가 작을수록 파이와 잘린 Y축은 더 위험해지고, 정렬한 막대는 그대로 정직합니다.']],TOUCH.cafe);}
bind('cafe',['cf-n','cf-gap','cf-type','cf-sort','cf-hl','cf-y0'],cafe);
/* ── ② 결제 ── */
var R=LAB.rng(2026),BASE=[],ORD=[];for(var i=0;i<800;i++){var u1=Math.max(1e-9,R()),u2=R(),z=Math.sqrt(-2*Math.log(u1))*Math.cos(2*Math.PI*u2);BASE.push(Math.round(Math.exp(6.85+.55*z)*10)/10);ORD.push(i);}
for(i=ORD.length-1;i>0;i--){var j=Math.floor(R()*(i+1)),tm=ORD[i];ORD[i]=ORD[j];ORD[j]=tm;}
var BIG=[31200,26800,38500,29400,35100];
function med(a){var s=a.slice().sort(function(x,y){return x-y;}),n=s.length;return n%2?s[(n-1)/2]:(s[n/2-1]+s[n/2])/2;}
function mean(a){return a.reduce(function(x,y){return x+y;},0)/a.length;}
var PASSQ={};
function payCalc(q,miss,out,fill,stat){var full=BASE.slice(0,800-out).concat(BIG.slice(0,out)),truth=q==='typ'?med(full):mean(full);
 var nm=Math.round(800*miss/100),isM={};ORD.slice(0,nm).forEach(function(k){isM[k]=1;});
 var obs=full.filter(function(_,k){return !isM[k];}),mo=med(obs),proc=fill==='drop'?obs:full.map(function(x,k){return isM[k]?(fill==='zero'?0:mo):x;});
 var rep=stat==='mean'?mean(proc):med(proc);return {truth:truth,rep:rep,err:Math.abs(rep-truth)/truth*100,proc:proc,nm:nm};}
function pay(){var q=$('#py-q').value,miss=+$('#py-miss').value,out=+$('#py-out').value,fill=$('#py-fill').value,stat=$('#py-stat').value;
 $('#py-missv').textContent=miss+'% ('+Math.round(8*miss)+'건)';$('#py-outv').textContent=out+'건';
 var c=payCalc(q,miss,out,fill,stat),ok=c.err<=1.5;if(TOUCH.pay&&ok)PASSQ[q]=1;
 kpi('pay',[['보고할 대표값',nf(Math.round(c.rep))+'원',null],['참값 (빈 값 없는 원자료)',nf(Math.round(c.truth))+'원',null],['참값과 차이',c.err.toFixed(1)+'%',ok],['판정',ok?'보고 가능':'다시 계산',ok]]);
 var over=c.proc.filter(function(x){return x>=4000;}).length;
 V.hist($('#pay-v1'),{values:c.proc,lo:0,hi:4000,bin:200,refs:[{v:Math.min(3990,c.rep),label:'',color:'#b45309'},{v:Math.min(3990,c.truth),label:'',color:'#13733a'}],title:'결제액 분포 — 앰버 선 보고값, 초록 선 참값',unit:over?'4,000원 이상 '+over+'건은 그림 밖':'',h:300,w:420});
 var combos=[['zero','mean','0·평균'],['zero','median','0·중앙값'],['drop','mean','빼기·평균'],['drop','median','빼기·중앙값'],['med','mean','중앙값 채움·평균'],['med','median','중앙값 채움·중앙값']];
 var es=combos.map(function(k){return +payCalc(q,miss,out,k[0],k[1]).err.toFixed(1);}),me=combos.findIndex(function(k){return k[0]===fill&&k[1]===stat;});
 V.bar($('#pay-v2'),{labels:combos.map(function(k){return k[2];}),values:es,hl:me,dec:1,unitShort:'%',horizontal:true,ref:1.5,refLabel:'허용 1.5%',title:'처리 방법별 참값과 차이 (%)',w:420,L:128,T:52});
 says('pay',[['doc',ok?'verdict':'judge',ok?'판정: 질문(“'+(q==='typ'?'보통 손님':'총매출용 평균')+'”)에 맞는 숫자입니다. 차이 '+c.err.toFixed(1)+'%.':fill==='zero'&&miss>0?'판정 보류. 비어 있던 '+c.nm+'건을 0원 결제로 바꿨습니다. 실제로 0원을 낸 손님은 없습니다.':'판정 보류. 질문이 “'+(q==='typ'?'보통 손님 한 번':'총매출 계산용 평균')+'”이면 대표값을 다시 고르세요.'],
  ['asst','report','보고: 처리 후 '+c.proc.length+'건, 대표값 '+nf(Math.round(c.rep))+'원, 참값과 '+c.err.toFixed(1)+'% 차이.'],
  ['fly','magnify',q==='typ'&&stat==='mean'?'분포 꼬리가 오른쪽으로 길어. 큰 결제 몇 건이 평균을 끌고 가. “보통 손님”이면 중앙값.':q==='avg'&&stat==='median'?'총매출 = 1건 평균 × 건수야. 중앙값을 곱하면 큰 결제가 빠진 매출이 나와.':fill==='zero'?'0원 막대가 맨 왼쪽에 생겼어. 그게 진짜 결제야?':'처리는 맞아 보여. 질문을 바꾸면 이 방법이 그대로 맞을까?'],
  ['robo',fill==='zero'?'happy':'coin',fill==='zero'?'빈 값은 0으로 채우면 깔끔하지! 빈 곳이 없잖아!':'평균이 제일 유명하니까 평균이면 다 돼!']]);
 mis('pay',[['지금 질문에 맞게 참값과 차이 1.5% 이내로 보고하기',ok,'질문이 “보통”이면 중앙값, “총매출용”이면 빈 값을 뺀 평균입니다.'],
  ['함정 관찰: 빈 값 10% 이상에서 0으로 채워 차이가 5% 넘게 벌어지는 것 보기',fill==='zero'&&miss>=10&&c.err>=5,'3층에서 본 대로, 0 채우기는 “결제가 없었다”는 거짓 기록을 만듭니다.'],
  ['조건을 바꿔도 유지: 팀장의 질문 두 가지 모두에서 미션 1 통과하기',PASSQ.typ&&PASSQ.avg,'같은 데이터라도 질문이 대표값을 정합니다.']],TOUCH.pay);}
bind('pay',['py-q','py-miss','py-out','py-fill','py-stat'],pay);
/* ── ③ 건강검진 ── */
var R2=LAB.rng(1010),PEO=[];for(i=0;i<3000;i++){var a=R2(),bm=Math.sqrt(-2*Math.log(Math.max(1e-9,R2())))*Math.cos(2*Math.PI*R2()),tl=R2(),tz=Math.sqrt(-2*Math.log(Math.max(1e-9,R2())))*Math.cos(2*Math.PI*R2());
 PEO.push({u:a,y:tl<.02?140+20*tz:89+9*bm,o:tl<.12?145+22*tz:99+12*bm});}
function hcData(p){var Y=[],O=[];PEO.forEach(function(q){if(q.u<p)O.push(q.o);else Y.push(q.y);});return {Y:Y,O:O,A:Y.concat(O)};}
function hc(){var p=+$('#hc-old').value/100,type=$('#hc-type').value,ref=$('#hc-ref').checked,bin=+$('#hc-bin').value;$('#hc-oldv').textContent=Math.round(p*100)+'%';$('#hc-bin').disabled=type==='avg';
 var D=hcData(p),m=mean(D.A),hi=D.A.filter(function(x){return x>=126;}).length,pc=hi/D.A.length*100,vis=type==='hist'&&ref&&bin<=10;
 kpi('health',[['전체 평균 혈당',m.toFixed(1)+' mg/dL',null],['126 이상',nf(hi)+'명 ('+pc.toFixed(1)+'%)',null],['화면에서 꼬리가 보이나',vis?'예':'아니오',vis],['판정',vis?'보고 가능':'꼬리가 숨음',vis]]);
 if(type==='avg')V.bar($('#health-v1'),{labels:['60세 미만','60세 이상','전체'],values:[mean(D.Y),mean(D.O),m],dec:1,y0:0,yMax:140,ref:ref?126:null,refLabel:'126',title:'연령대별 평균 공복혈당 (mg/dL)',h:300,w:420});
 else{var lo=126-bin*Math.floor(56/bin),hh=126+bin*Math.ceil(74/bin);V.hist($('#health-v1'),{values:D.A,lo:lo,hi:hh,bin:bin,refs:ref?[{v:126,label:'126 기준선',color:'#b45309'}]:[],title:'공복혈당 분포 — 구간 폭 '+bin+' (mg/dL)',h:300,w:420});}
 var xs=[],ys=[];for(var k=1;k<=7;k++){var d=hcData(k/10);xs.push(k*10+'%');ys.push(+(d.A.filter(function(x){return x>=126;}).length/30).toFixed(1));}
 V.line($('#health-v2'),{labels:xs,series:[{name:'126 이상 비율',values:ys,vlab:true}],hl:{s:0,i:Math.round(p*10)-1},y0:0,unit:'126 이상 (%)',title:'고령층 비율이 늘면 꼬리가 두꺼워진다',h:300,w:420});
 says('health',[['doc',vis?'verdict':'judge',vis?'판정: 평균 '+m.toFixed(0)+'은 정상 범위지만, '+nf(hi)+'명('+pc.toFixed(1)+'%)이 기준선 위에 있다는 것이 그림에서 바로 읽힙니다.':type==='avg'?'판정 보류. 평균 막대는 모두 126 아래입니다. 그래서 “괜찮다”로 읽히지만, 실제로는 '+nf(hi)+'명이 위에 있습니다.':!ref?'판정 보류. 분포는 보이지만 어디부터 위험한지 선이 없습니다.':'구간이 넓어서 126 근처가 한 덩어리로 뭉쳤습니다. 폭을 좁혀 보세요.'],
  ['asst','report','보고: 평균 '+m.toFixed(1)+', 126 이상 '+pc.toFixed(1)+'%, 고령층 '+Math.round(p*100)+'%.'],
  ['fly','magnify',type==='avg'?'평균은 꼬리를 숨겨. 오른쪽 끝에 몇 명이 있는지 분포로 봐야 해.':!ref?'기준선 하나만 그으면 “몇 명이 넘었나”가 보여.':bin>10?'구간 폭 20이면 120~140이 한 막대야. 126에서 끊어야 해.':'기준선 오른쪽 막대들이 꼬리야. 고령층이 늘면 더 두꺼워질걸.'],
  ['robo',type==='avg'?'happy':'chart',type==='avg'?'평균 94! 정상이니까 우리 지역은 건강해!':'막대가 많아서 복잡해… 평균 하나면 안 될까?']]);
 mis('health',[['분포 + 126 기준선 + 구간 폭 10 이하로 꼬리를 보이게 하기',vis,'10층에서 본 1,551명(5.2%)도 이렇게 찾았습니다.'],
  ['함정 관찰: 평균 막대에 기준선을 그어 “모두 정상처럼” 보이는 것 확인하기',type==='avg'&&ref,'평균이 기준선 아래라고 사람들이 모두 아래인 것은 아닙니다.'],
  ['조건을 바꿔도 유지: 고령층 60% 이상에서도 꼬리가 보이는 차트 유지하기',p>=.6&&vis,'조건이 바뀌어도 분포와 기준선은 그대로 정직하게 보여 줍니다.']],TOUCH.health);}
bind('health',['hc-old','hc-type','hc-ref','hc-bin'],hc);
/* ── ④ 물류센터 ── */
var WD=['월','화','수','목','금','토','일'],HR=[];for(var h=8;h<=21;h++)HR.push(h);var SLOTS=[[0,8],[2,13],[4,18],[5,14]],CA=['차량 고장','교통 체증','주소 오류','물량 폭주','기상 악화'],L4={};
function load(fri,sat){return WD.map(function(_,d){return HR.map(function(h){var we=d>=5,b=we?40+50*Math.exp(-Math.pow((h-14)/3,2)):30+70*Math.exp(-Math.pow((h-9)/1.3,2))+80*Math.exp(-Math.pow((h-18)/1.5,2));
 if(d===4&&h>=16)b*=1+fri/100;if(d===5)b+=sat*1.2*Math.exp(-Math.pow((h-14)/1.5,2));return Math.round(b);});});}
function causes(fri,sat,addr){return {'차량 고장':15,'교통 체증':70,'주소 오류':addr*14,'물량 폭주':Math.round(30+fri*.8+sat*.6),'기상 악화':28};}
function delays(M,C,slot,fix){var mx=Math.max.apply(null,[].concat.apply([],M)),s=SLOTS[slot],eff=.6*M[s[0]][HR.indexOf(s[1])]/mx,tot=0;
 CA.forEach(function(c){var v=C[c];if(c===fix)v*=.3;if(c==='물량 폭주')v*=1-eff;tot+=v;});return tot;}
function logi(){var fri=+$('#lg-fri').value,sat=+$('#lg-sat').value,addr=+$('#lg-addr').value,slot=+$('#lg-slot').value,fix=$('#lg-fix').value;
 $('#lg-friv').textContent='+'+fri+'%';$('#lg-satv').textContent=sat?sat+'%':'없음';$('#lg-addrv').textContent=addr+'%';
 var M=load(fri,sat),C=causes(fri,sat,addr),before=CA.reduce(function(a,c){return a+C[c];},0),now=delays(M,C,slot,fix),best=[1e9,0,''];
 SLOTS.forEach(function(_,si){CA.forEach(function(c){var v=delays(M,C,si,c);if(v<best[0]-1e-9)best=[v,si,c];});});
 var opt=Math.abs(now-best[0])<1e-6,red=(before-now)/before*100;
 kpi('logi',[['지연 건수 (1,000건 중)',Math.round(now)+'건',null],['지연률',(now/10).toFixed(1)+'%',null],['개선 전보다 줄어듦',red.toFixed(0)+'%',red>=35],['판정',opt?'최선의 조합':'더 줄일 수 있음',opt]]);
 var s=SLOTS[slot];V.heat($('#logi-v1'),{rows:WD,cols:HR.map(String),m:M,ramp:'teal',hlMax:true,mark:[s[0],HR.indexOf(s[1])],cw:26,ch:26,L:30,w:420,title:'요일 × 시간 물량 — 앰버 = 가장 붐빔, 초록 점선 = 내 인력'});
 var srt=CA.slice().sort(function(a,b){return C[b]-C[a];});V.pareto($('#logi-v2'),{labels:srt,values:srt.map(function(c){return C[c];}),cum:true,hl:srt.indexOf(fix),unit:'지연 건수',title:'지연 원인 파레토 — 앰버 = 내가 고칠 원인',h:300,w:420});
 var peak=[0,0,0];M.forEach(function(r,d){r.forEach(function(v,j){if(v>peak[0])peak=[v,d,HR[j]];});});var rank=srt.indexOf(fix)+1;
 says('logi',[['doc',opt?'verdict':'judge',opt?'판정: 가장 붐비는 시간에 사람을, 가장 큰 원인에 예산을 썼습니다. 지연이 '+red.toFixed(0)+'% 줄었습니다.':'판정 보류. 같은 자원으로 지연을 '+Math.round(now-best[0])+'건 더 줄일 수 있습니다.'],
  ['asst','report','보고: 지연 '+Math.round(before)+'건 → '+Math.round(now)+'건. 가장 붐비는 셀은 '+WD[peak[1]]+'요일 '+peak[2]+'시, 1위 원인은 '+srt[0]+'.'],
  ['fly','magnify',rank>=4?fix+'은(는) 파레토에서 '+rank+'번째야. 작은 원인을 다 고쳐도 지연은 조금밖에 안 줄어.':(s[0]!==peak[1]||s[1]!==peak[2])&&Math.abs(M[s[0]][HR.indexOf(s[1])]-peak[0])>1?'인력을 둔 곳이 히트맵에서 가장 진한 셀이 아니야. 앰버 테두리를 봐.':'조합은 좋아 보여. 행사나 주소 오류가 늘면 그래도 이 조합이 맞을까?'],
  ['robo',rank>=4?'sigh':'coin',rank>=4?'차량 고장은 고치기 쉬우니까 그거부터 하면 되잖아…':'인력은 월요일 아침이지! 한 주의 시작이 제일 중요해!']]);
 var defBest=(function(){var M0=load(25,0),C0=causes(25,0,3),b0=[1e9,0,''];SLOTS.forEach(function(_,si){CA.forEach(function(c){var v=delays(M0,C0,si,c);if(v<b0[0])b0=[v,si,c];});});return b0;})();
 mis('logi',[['지연 건수가 가장 적은 인력 시간대 + 원인 조합 찾기',opt,'히트맵의 가장 진한 셀과 파레토의 첫 막대 — 11층의 두 차트가 그대로 답입니다.'],
  ['함정 관찰: 파레토 4번째 이하 원인을 골라 줄어든 몫이 작은 것 보기',rank>=4,'고치기 쉬운 원인보다 큰 원인이 먼저입니다.'],
  ['조건을 바꿔도 유지: 행사·주소 오류를 바꿔 최선의 조합이 달라진 상황에서 다시 최선 찾기',opt&&(best[1]!==defBest[1]||best[2]!==defBest[2]),'조건이 바뀌면 진한 셀과 첫 막대도 바뀝니다. 차트를 다시 보는 습관이 핵심입니다.']],TOUCH.logi);}
bind('logi',['lg-fri','lg-sat','lg-addr','lg-slot','lg-fix'],logi);
/* ── 탭 ── */
function show(k){if(!document.getElementById('sc-'+k))k='cafe';$$('.pr-tabs button').forEach(function(b){b.setAttribute('aria-selected',String(b.dataset.k===k));});$$('.pr-sc').forEach(function(s){s.hidden=s.id!=='sc-'+k;});({cafe:cafe,pay:pay,health:hc,logi:logi})[k]();}
$$('.pr-tabs button').forEach(function(b){b.onclick=function(){history.replaceState(null,'','#'+b.dataset.k);show(b.dataset.k);};});
function fromHash(){var k=(location.hash||'').slice(1);if(['cafe','pay','health','logi'].indexOf(k)>=0){show(k);var t=document.getElementById('tab-'+k);if(t)t.scrollIntoView({block:'start'});}}
window.addEventListener('hashchange',fromHash);fromHash();
})();'''
