/* ══ 디자인 연구실 공용 모듈 (낮의 연구실 · 데이터 시각화 시리즈) ══
   도우미 → 캐릭터(Cast) → 용어(Gloss) → 퀴즈 → 조별 대결(Duel) → 흐름 캔버스(Flow) → 차트(VIZ) → 기타 */
(function(){'use strict';
var $=function(s,r){return (r||document).querySelector(s);}, $$=function(s,r){return [].slice.call((r||document).querySelectorAll(s));};
var esc=function(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});};
var RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
function rng(seed){var s=seed>>>0||1; return function(){s^=s<<13;s>>>=0;s^=s>>17;s^=s<<5;s>>>=0;return (s>>>0)/4294967296;};}
function fit(cv){var r=cv.getBoundingClientRect(),d=window.devicePixelRatio||1,w=Math.max(10,Math.round(r.width)),h=Math.max(10,Math.round(r.height));
  if(cv.width!==w*d||cv.height!==h*d){cv.width=w*d;cv.height=h*d;} var c=cv.getContext('2d'); c.setTransform(d,0,0,d,0,0); return {c:c,W:w,H:h};}
var MODS=[],vis=new WeakMap(),io=('IntersectionObserver' in window)?new IntersectionObserver(function(es){es.forEach(function(e){vis.set(e.target,e.isIntersecting);});}):null;
function addMod(el,fn){MODS.push({el:el,fn:fn}); if(io)io.observe(el); else vis.set(el,true); fn(0);}
var last=0;
function loop(t){var dt=Math.min(.05,(t-(last||t))/1000); last=t; MODS.forEach(function(m){if(vis.get(m.el)&&!RM)m.fn(dt);}); requestAnimationFrame(loop);}
window.addEventListener('resize',function(){MODS.forEach(function(m){m.fn(0);});});
function stamp(c,W,txt){c.save(); c.font='700 11px '+getComputedStyle(document.body).fontFamily; var w=Math.max(c.measureText(txt).width,txt.length*10.5)+12; c.translate(W-w-8,8); c.rotate(-.03);
  c.strokeStyle='#a35c00'; c.fillStyle='rgba(255,255,255,.9)'; c.lineWidth=1.5; c.beginPath(); c.rect(0,0,w,18); c.fill(); c.stroke(); c.fillStyle='#a35c00'; c.fillText(txt,6,13); c.restore();}

/* ── 캐릭터 (박사·하루·초파리·주판봇·시아·모아·X1~X3) ── */
var ALIAS={doc_front:'doc_e08',doc_board:'doc_e07',doc_judge:'doc_e10',doc_verdict:'doc_e18',doc_magic:'doc_e16',doc_think:'doc_e09',doc_smile:'doc_e13',
 asst_smile:'asst_e13',asst_firm:'asst_e12',asst_report:'asst_e07',asst_spark:'asst_e01',asst_shock:'asst_e24',asst_sigh:'asst_e02',asst_proud:'asst_e16',asst_think:'asst_e09',asst_wow:'asst_e04',
 fly_clip:'fly_e10',fly_point:'fly_e08',fly_arms:'fly_e16',fly_coffee:'fly_e13',fly_cry:'fly_e21',fly_type:'fly_e09',fly_magnify:'fly_e07',
 robo_smile:'robo_e13',robo_coin:'robo_e16',robo_chart:'robo_e07',robo_happy:'robo_e12',robo_sigh:'robo_e20',robo_meh:'robo_e18',robo_cry:'robo_e21',robo_wow:'robo_e04',robo_blush:'robo_e14',robo_calc:'robo_e09',
 sia_smile:'sia_e13',sia_signal:'sia_e10',sia_explain:'sia_e07',sia_guide:'sia_e08',sia_think:'sia_e09',sia_firm:'sia_e12',sia_proud:'sia_e16',sia_doze:'sia_e17',sia_stop:'sia_e06',sia_shock:'sia_e24',
 moa_smile:'moa_e13',moa_tea:'moa_e01',moa_cheer:'moa_e12',moa_plant:'moa_e16',moa_report:'moa_e07',moa_guide:'moa_e08',moa_think:'moa_e09',moa_ok:'moa_e10',moa_sparkle:'moa_e19',moa_cry:'moa_e21',moa_shock:'moa_e24'};
['x1','x2','x3'].forEach(function(x){ALIAS[x+'_smile']=x+'_e13';ALIAS[x+'_joy']=x+'_e01';ALIAS[x+'_sad']=x+'_e02';ALIAS[x+'_wow']=x+'_e04';ALIAS[x+'_think']=x+'_e09';ALIAS[x+'_proud']=x+'_e16';ALIAS[x+'_flustered']=x+'_e15';ALIAS[x+'_shock']=x+'_e24';});
var BASE={doc:'doc_e08',asst:'asst_e13',fly:'fly_e10',robo:'robo_e13',sia:'sia_e13',moa:'moa_e13',x1:'x1_e13',x2:'x2_e13',x3:'x3_e13'};
function src(who,mood){var S=window.SPRITE||{}; var k=who+'_'+mood; k=ALIAS[k]||k; return S[k]||S[BASE[who]]||'';}
var Cast={fill:function(){$$('img[data-who]').forEach(function(im){var s=src(im.dataset.who,im.dataset.mood||'front'); if(s)im.src=s;});},
  set:function(im,who,mood){if(!im)return; var s=src(who,mood); if(!s)return; if(RM){im.src=s;return;} im.style.transition='opacity .1s'; im.style.opacity=0; setTimeout(function(){im.src=s; im.style.opacity=1;},100);}};
window.Cast=Cast;

/* ── 용어 말풍선 ── */
function Gloss(GL){
  var tip=$('#tip'); if(!tip||!GL)return; var keys=Object.keys(GL).sort(function(a,b){return b.length-a.length;}); if(!keys.length)return;
  var done={},re=new RegExp('('+keys.map(function(k){return k.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}).join('|')+')');
  $$('main section.level:not(#kg):not(#export) p, main section.level:not(#kg):not(#export) li, header.hero p').forEach(function(p){
    if(p.closest('.quiz,.duel,.say,pre,table,.kgx,.viz,.codebox'))return;
    var w=document.createTreeWalker(p,NodeFilter.SHOW_TEXT,null),nodes=[],n; while((n=w.nextNode()))nodes.push(n);
    nodes.forEach(function(t){ if(t.parentNode.closest('a,code,.gl,b.nogl,button'))return; var m=re.exec(t.nodeValue); if(!m||done[m[1]])return; done[m[1]]=1;
      var sp=document.createElement('span'); sp.className='gl'; sp.tabIndex=0; sp.dataset.k=m[1]; sp.textContent=m[1];
      var after=t.splitText(m.index); after.nodeValue=after.nodeValue.slice(m[1].length); t.parentNode.insertBefore(sp,after);});
  });
  function show(e){var k=e.target.closest&&e.target.closest('.gl'); if(!k)return; var g=GL[k.dataset.k]; tip.innerHTML='<b>'+esc(g[0])+'</b> <span style="color:#5b6874">· '+esc(g[1])+'</span><br>'+esc(g[2]);
    var r=k.getBoundingClientRect(); tip.style.display='block'; var x=Math.min(window.scrollX+r.left,window.scrollX+document.documentElement.clientWidth-tip.offsetWidth-10); tip.style.left=Math.max(6,x)+'px'; tip.style.top=(window.scrollY+r.bottom+6)+'px';}
  document.addEventListener('pointerover',show); document.addEventListener('focusin',show);
  document.addEventListener('pointerout',function(e){if(e.target.closest&&e.target.closest('.gl'))tip.style.display='none';});
  document.addEventListener('focusout',function(){tip.style.display='none';});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')tip.style.display='none';});
}

/* ── 퀴즈 ── */
var QSTAT={done:0,ok:0,total:0,by:{}};
function Quiz(el,items){
  var h='<div class="qh">확인 퀴즈 · '+items.length+'문항</div>';
  items.forEach(function(q,i){QSTAT.total++; h+='<div class="q" data-i="'+i+'"><p>Q'+(i+1)+'. '+q.q+'</p><div class="opts">'+q.o.map(function(o,j){return '<button type="button" class="bt" data-j="'+j+'">'+(j+1)+') '+o+'</button>';}).join('')+'</div>'+
    (q.hint?'<details class="hint"><summary>힌트</summary>'+q.hint+'</details>':'')+'<div class="why" hidden></div></div>';});
  el.innerHTML=h;
  $$('.q',el).forEach(function(qe){var q=items[+qe.dataset.i],answered=false;
    $$('.opts button',qe).forEach(function(b){b.onclick=function(){var j=+b.dataset.j; var ok=j===q.a;
      $$('.opts button',qe).forEach(function(x){x.classList.remove('ok','no');}); b.classList.add(ok?'ok':'no'); if(!ok)$$('.opts button',qe)[q.a].classList.add('ok');
      var w=$('.why',qe); w.hidden=false; w.innerHTML=(ok?'<b style="color:#13733a">맞아요.</b> ':'<b style="color:#c9302c">다시 볼까요.</b> 괜찮아요, 여기서 한 번 짚고 가면 됩니다. ')+q.why;
      if(!answered){answered=true;QSTAT.done++; if(ok)QSTAT.ok++; QSTAT.by[(el.dataset.quiz||'q')+':'+qe.dataset.i]={ok:ok}; updProg();}};});});
}
function updProg(){var e=$('#qprog'); if(e)e.textContent='퀴즈 '+QSTAT.done+'/'+QSTAT.total+' · 맞힘 '+QSTAT.ok;}

/* ── 조별 대결 (초파리 조 vs 주판봇 조, 심판 박사) ── */
function Duel(cfg){
  var el=$(cfg.el); if(!el)return; var imF=$('.head img[data-who=fly]',el),imR=$('.head img[data-who=robo]',el),imD=$('.res img[data-who=doc]',el),imA=$('.res img[data-who=asst]',el);
  $$('.guess button',el).forEach(function(b){b.onclick=function(){$$('.guess button',el).forEach(function(x){x.setAttribute('aria-pressed',String(x===b));}); $('.gnote',el).textContent='예상을 적어 두었습니다. 이제 결과를 봅시다.';};});
  $('.go',el).onclick=function(){
    var r=cfg.run(); el.classList.add('open'); var hib=cfg.higherIsBetter!==false;
    var mx=Math.max(Math.abs(r.fly),Math.abs(r.robo))||1;
    $('.bar.f s',el).style.width=(100*Math.abs(r.fly)/mx)+'%'; $('.bar.r s',el).style.width=(100*Math.abs(r.robo)/mx)+'%';
    $('.bar.f b',el).textContent=r.flyTxt||r.fly; $('.bar.r b',el).textContent=r.roboTxt||r.robo;
    var res; if(r.foul)res='X'; else if(r.cond)res='C'; else if(Math.abs(r.fly-r.robo)<=(cfg.drawMargin||0))res='D'; else res=((r.fly>r.robo)===hib)?'F':'R';
    var M={F:['judge','spark','arms','sigh'],R:['judge','spark','coffee','happy'],D:['think','smile','coffee','meh'],C:['think','report','coffee','calc'],X:['judge','shock','arms','blush']}[res];
    Cast.set(imD,'doc',M[0]); Cast.set(imA,'asst',M[1]); Cast.set(imF,'fly',M[2]); Cast.set(imR,'robo',M[3]);
    $$('.team.f img',el).forEach(function(im){Cast.set(im,im.dataset.who,res==='F'?(im.dataset.who==='asst'?'spark':im.dataset.who.charAt(0)==='x'?'joy':'sparkle'):'smile');});
    $$('.team.r img',el).forEach(function(im){Cast.set(im,im.dataset.who,res==='R'?(im.dataset.who==='moa'?'cheer':'joy'):'smile');});
    $('.ann',el).innerHTML=cfg.announce(r); $('.ver',el).innerHTML=cfg.verdict(res,r);
  };
  $('.reset',el).onclick=function(){el.classList.remove('open'); Cast.set(imF,'fly','point'); Cast.set(imR,'robo','coin'); $$('.bar s',el).forEach(function(s){s.style.width=0;});};
}

/* ── 흐름 캔버스: 카드가 단계를 지나며 바뀐다 ── */
function Flow(cv,o){
  var st=o.stations,items=o.items,t=0,speed=o.speed||.45,W,H,cols=o.colors||['#c9302c','#9b3fb5','#13733a','#1e55c8','#a35c00','#0b7a86'];
  var font=getComputedStyle(document.body).fontFamily;
  function draw(dt){var F=fit(cv),c=F.c; W=F.W; H=F.H; t+=dt*speed; c.clearRect(0,0,W,H);
    var n=st.length,pad=14,bw=(W-pad*2)/n,by=34,bh=H-by-28;
    st.forEach(function(s,i){var x=pad+i*bw+4; c.fillStyle='#f6f8fa'; c.strokeStyle='#d5dbe2'; c.lineWidth=1; c.beginPath(); c.roundRect?c.roundRect(x,by,bw-8,bh,10):c.rect(x,by,bw-8,bh); c.fill(); c.stroke();
      c.fillStyle=cols[i%cols.length]; c.font='700 13px '+font; c.textAlign='center'; c.fillText(s,x+(bw-8)/2,by-10);
      if(i<n-1){c.fillStyle='#9aa5b1'; c.beginPath(); var ax=x+bw-6,ay=by+bh/2; c.moveTo(ax-2,ay-6); c.lineTo(ax+4,ay); c.lineTo(ax-2,ay+6); c.fill();}});
    var lanes=Math.min(items.length,Math.max(1,Math.floor(bh/30)));
    items.forEach(function(it,k){
      var lane=k%lanes,ph=((t+k*(n/items.length))%(n+0.6)); if(RM)ph=Math.min(n-0.01,k%n+.5);
      var i=Math.min(n-1,Math.floor(ph)),f=ph-i,x=pad+i*bw+4+(bw-8)*Math.min(1,f),y=by+14+lane*((bh-24)/lanes);
      var lab=it[Math.min(i,it.length-1)],bad=o.bad&&o.bad(it,i);
      c.font='13px '+font; var tw=Math.min(bw-14,c.measureText(lab).width+16); var bx=Math.max(pad+i*bw+6,Math.min(x-tw/2,pad+(i+1)*bw-tw-6));
      c.fillStyle=bad?'#fcebea':'#ffffff'; c.strokeStyle=bad?'#c9302c':cols[i%cols.length]; c.lineWidth=1.5; c.beginPath(); c.roundRect?c.roundRect(bx,y,tw,22,6):c.rect(bx,y,tw,22); c.fill(); c.stroke();
      c.fillStyle=bad?'#c9302c':'#16212b'; c.textAlign='left'; c.save(); c.beginPath(); c.rect(bx,y,tw,22); c.clip(); c.fillText(lab,bx+8,y+15.5); c.restore();
    });
    if(o.stamp!==false)stamp(c,W,o.stamp||'설명용 모형');
  }
  addMod(cv,draw);
}

/* ══ VIZ — 외부 라이브러리 없는 SVG 차트 ══
   모든 함수: VIZ.xxx(el, opt) → el 안에 SVG를 그린다. 색: 기본 인디고 #1e3a8a, 강조 앰버 #b45309 (교안 팔레트) */
var IND='#1e3a8a',AMB='#b45309',GRY='#9aa5b1',INK='#16212b',MUT='#5b6874',GRID='#e3e8ee';
function nf(v,d){if(v==null||isNaN(v))return '';d=d==null?0:d;var s=(+v).toFixed(d);var p=s.split('.');p[0]=p[0].replace(/\B(?=(\d{3})+(?!\d))/g,',');return p.join('.');}
function svgOpen(W,H,lab){return '<svg viewBox="0 0 '+W+' '+H+'" width="100%" role="img" aria-label="'+esc(lab||'차트')+'" style="max-width:'+W+'px;display:block;font-family:inherit">';}
function txt(x,y,s,o){o=o||{};return '<text x="'+x+'" y="'+y+'" font-size="'+(o.fs||12)+'" fill="'+(o.c||MUT)+'" text-anchor="'+(o.a||'middle')+'"'+(o.w?' font-weight="'+o.w+'"':'')+(o.rot?' transform="rotate('+o.rot+' '+x+' '+y+')"':'')+'>'+esc(s)+'</text>';}
function ticks(lo,hi,n){var span=hi-lo||1,step=Math.pow(10,Math.floor(Math.log10(span/n))),err=span/n/step;if(err>=7.5)step*=10;else if(err>=3.5)step*=5;else if(err>=1.5)step*=2;var a=[],v=Math.ceil(lo/step)*step;for(;v<=hi+1e-9;v+=step)a.push(+v.toFixed(10));return a;}
function fixL(F,o,hi,d){if(!o.L)F.L=Math.max(F.L,22+7*nf(hi,d||0).length+(o.ylab||o.unit?14:0));return F;}
function frame(o,W,H){return {L:o.L||58,R:o.R||16,T:o.T||(o.title?34:16),B:o.B||46,W:W,H:H};}
function title(o,W){return o.title?txt(W/2,20,o.title,{fs:14,c:INK,w:700}):'';}
var VIZ={
 nf:nf,
 bar:function(el,o){ // o: labels, values, hl(index|-1), y0, yMax, unit, horizontal, color, junk{shadow,grad,grid3,photo,legend}
  var W=o.w||560,H=o.h||(o.horizontal?Math.max(220,o.labels.length*30+70):300),F=frame(o,W,H),n=o.labels.length,s=svgOpen(W,H,o.alt||o.title);
  var vals=o.values,lo=o.y0==null?0:o.y0,hi=o.yMax||Math.max.apply(null,vals)*1.12;
  s+=title(o,W);
  if(o.junk&&o.junk.grad)s+='<defs><linearGradient id="jg'+(o.id||'')+'" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fde68a"/><stop offset="1" stop-color="#a5b4fc"/></linearGradient></defs><rect x="0" y="0" width="'+W+'" height="'+H+'" fill="url(#jg'+(o.id||'')+')" opacity=".55"/>';
  if(o.junk&&o.junk.photo)s+='<g opacity=".5"><rect x="'+(W-120)+'" y="'+(F.T+4)+'" width="100" height="64" rx="4" fill="#cfe0f7"/><path d="M'+(W-120)+' '+(F.T+68)+' l30 -30 l20 18 l18 -12 l32 24 z" fill="#5b86c9"/><circle cx="'+(W-40)+'" cy="'+(F.T+20)+'" r="8" fill="#fbe7b0"/></g>';
  if(o.horizontal){
   var bh=(H-F.T-F.B)/n,sx=function(v){return F.L+(W-F.L-F.R)*(v-lo)/(hi-lo);};
   ticks(lo,hi,5).forEach(function(t){s+='<line x1="'+sx(t)+'" x2="'+sx(t)+'" y1="'+F.T+'" y2="'+(H-F.B)+'" stroke="'+GRID+'"/>'+txt(sx(t),H-F.B+16,nf(t,o.dec||0));});
   vals.forEach(function(v,i){var y=F.T+bh*i+bh*.15,c=(i===o.hl)?AMB:(o.color||IND);s+='<rect x="'+F.L+'" y="'+y+'" width="'+Math.max(0,sx(v)-F.L)+'" height="'+bh*.7+'" fill="'+c+'"/>'+txt(F.L-6,y+bh*.35+4,o.labels[i],{a:'end',c:INK})+(o.vlab!==false?txt(sx(v)+4,y+bh*.35+4,nf(v,o.dec||0)+(o.unitShort||''),{a:'start',c:INK}):'');});
   if(o.ref!=null)s+='<line x1="'+sx(o.ref)+'" x2="'+sx(o.ref)+'" y1="'+(F.T-4)+'" y2="'+(H-F.B)+'" stroke="'+INK+'" stroke-dasharray="4 3"/>'+txt(sx(o.ref),F.T-6,o.refLabel||'',{c:INK,fs:11});
   if(o.unit)s+=txt((F.L+W-F.R)/2,H-8,o.unit);
  }else{
   fixL(F,o,hi,o.dec);var bw=(W-F.L-F.R)/n,sy=function(v){return H-F.B-(H-F.T-F.B)*(Math.max(v,lo)-lo)/(hi-lo);};
   var tk=ticks(lo,hi,5),td=(tk.length>1&&tk[1]-tk[0]<1)?1:(o.dec||0);
   tk.forEach(function(t){if(!(o.junk&&o.junk.grid3===false))s+='<line x1="'+F.L+'" x2="'+(W-F.R)+'" y1="'+sy(t)+'" y2="'+sy(t)+'" stroke="'+GRID+'"/>';s+=txt(F.L-6,sy(t)+4,nf(t,td),{a:'end'});});
   if(o.junk&&o.junk.grid3)for(var g=0;g<n*3;g++)s+='<line x1="'+(F.L+g*bw/3)+'" x2="'+(F.L+g*bw/3)+'" y1="'+F.T+'" y2="'+(H-F.B)+'" stroke="#c9d2dc"/>';
   vals.forEach(function(v,i){var x=F.L+bw*i+bw*.18,w=bw*.64,y=sy(v),c=(i===o.hl)?AMB:(o.color||IND);
     if(o.junk&&o.junk.shadow)s+='<rect x="'+(x+7)+'" y="'+(y-7)+'" width="'+w+'" height="'+(H-F.B-y)+'" fill="#000" opacity=".25"/><polygon points="'+x+','+y+' '+(x+7)+','+(y-7)+' '+(x+w+7)+','+(y-7)+' '+(x+w)+','+y+'" fill="#93a5cf"/>';
     var fc=(o.junk&&o.junk.rainbow)?['#ef4444','#f59e0b','#10b981','#3b82f6','#a855f7','#ec4899','#14b8a6','#eab308'][i%8]:c;
     s+='<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+Math.max(0,H-F.B-y)+'" fill="'+fc+'"/>';
     if(o.vlab!==false)s+=txt(x+w/2,y-5,nf(v,o.dec||0)+(o.unitShort||''),{c:INK,fs:11});
     s+=txt(x+w/2,H-F.B+16,o.labels[i],{c:INK});});
   if(lo!==0&&o.markCut!==false)s+='<path d="M'+(F.L-8)+' '+(H-F.B-6)+' l8 -4 l8 4" stroke="'+AMB+'" fill="none" stroke-width="2"/>'+txt(F.L+4,H-F.B-10,'축이 '+nf(lo)+'부터',{a:'start',c:AMB,fs:11});
   if(o.ref!=null)s+='<line x1="'+F.L+'" x2="'+(W-F.R)+'" y1="'+sy(o.ref)+'" y2="'+sy(o.ref)+'" stroke="'+INK+'" stroke-dasharray="4 3"/>'+txt(W-F.R,sy(o.ref)-5,o.refLabel||'',{a:'end',c:INK,fs:11});
   if(o.unit)s+=txt(14,(F.T+H-F.B)/2,o.unit,{rot:-90});
   if(o.junk&&o.junk.legend)s+='<rect x="'+(W-150)+'" y="'+(F.T)+'" width="134" height="44" fill="#fff" stroke="#c9d2dc"/><rect x="'+(W-142)+'" y="'+(F.T+8)+'" width="10" height="10" fill="'+IND+'"/>'+txt(W-128,F.T+17,'결제 금액',{a:'start',fs:11})+'<rect x="'+(W-142)+'" y="'+(F.T+26)+'" width="10" height="10" fill="'+IND+'"/>'+txt(W-128,F.T+35,'금액(결제)',{a:'start',fs:11});
  }
  s+='<line x1="'+F.L+'" x2="'+F.L+'" y1="'+F.T+'" y2="'+(H-F.B)+'" stroke="'+GRY+'"/><line x1="'+F.L+'" x2="'+(W-F.R)+'" y1="'+(H-F.B)+'" y2="'+(H-F.B)+'" stroke="'+GRY+'"/>';
  el.innerHTML=s+'</svg>';
 },
 line:function(el,o){ // o: labels, series:[{name,values,color,dash}], y0, yMax, hl:{s,i}, xs(숫자 위치, 선택), unit
  var W=o.w||560,H=o.h||300,F=frame(o,W,H),s=svgOpen(W,H,o.alt||o.title),all=[];
  o.series.forEach(function(se){se.values.forEach(function(v){if(v!=null)all.push(v);});});
  var lo=o.y0==null?Math.min.apply(null,all)*.95:o.y0,hi=o.yMax||Math.max.apply(null,all)*1.1;
  fixL(F,o,hi,o.dec);var n=o.labels.length,xs=o.xs||o.labels.map(function(_,i){return i;}),x0=Math.min.apply(null,xs),x1=Math.max.apply(null,xs);
  var sx=function(i){return F.L+(W-F.L-F.R)*(xs[i]-x0)/((x1-x0)||1);},sy=function(v){return H-F.B-(H-F.T-F.B)*(v-lo)/(hi-lo);};
  s+=title(o,W);
  ticks(lo,hi,5).forEach(function(t){s+='<line x1="'+F.L+'" x2="'+(W-F.R)+'" y1="'+sy(t)+'" y2="'+sy(t)+'" stroke="'+GRID+'"/>'+txt(F.L-6,sy(t)+4,nf(t,o.dec||0),{a:'end'});});
  var step=Math.max(1,Math.ceil(n/Math.max(1,Math.floor((W-F.L-F.R)/44))));
  o.labels.forEach(function(t,i){if(i%step===0||i===n-1)s+=txt(sx(i),H-F.B+16,t,{c:INK,fs:11});});
  o.series.forEach(function(se,k){var c=se.color||(k?AMB:IND),d='',pen=false;
    se.values.forEach(function(v,i){if(v==null){pen=false;return;} d+=(pen?'L':'M')+sx(i).toFixed(1)+' '+sy(v).toFixed(1)+' ';pen=true;});
    s+='<path d="'+d+'" fill="none" stroke="'+c+'" stroke-width="'+(se.width||2.5)+'"'+(se.dash?' stroke-dasharray="6 4"':'')+'/>';
    if(se.dots!==false)se.values.forEach(function(v,i){if(v==null)return;var h=o.hl&&o.hl.s===k&&o.hl.i===i;s+='<circle cx="'+sx(i)+'" cy="'+sy(v)+'" r="'+(h?6:3)+'" fill="'+(h?AMB:c)+'"/>';if(se.vlab)s+=txt(sx(i),sy(v)-8,nf(v,o.dec||0),{c:INK,fs:11});});
  });
  if(o.series.length>1&&o.legend!==false){var lx=F.L+6;o.series.forEach(function(se,k){var c=se.color||(k?AMB:IND);s+='<rect x="'+lx+'" y="'+(F.T-2)+'" width="12" height="4" fill="'+c+'"/>'+txt(lx+16,F.T+3,se.name,{a:'start',c:INK,fs:11});lx+=se.name.length*12+40;});}
  if(o.ref!=null)s+='<line x1="'+F.L+'" x2="'+(W-F.R)+'" y1="'+sy(o.ref)+'" y2="'+sy(o.ref)+'" stroke="'+INK+'" stroke-dasharray="4 3"/>'+txt(W-F.R,sy(o.ref)-5,o.refLabel||'',{a:'end',c:INK,fs:11});
  if(o.unit)s+=txt(14,(F.T+H-F.B)/2,o.unit,{rot:-90});
  s+='<line x1="'+F.L+'" x2="'+F.L+'" y1="'+F.T+'" y2="'+(H-F.B)+'" stroke="'+GRY+'"/><line x1="'+F.L+'" x2="'+(W-F.R)+'" y1="'+(H-F.B)+'" y2="'+(H-F.B)+'" stroke="'+GRY+'"/>';
  el.innerHTML=s+'</svg>';
 },
 hist:function(el,o){ // o: values(raw) 또는 counts+edges, bin, lo, hi, refs:[{v,label,color}], meanLine
  var W=o.w||560,H=o.h||280,F=frame(o,W,H),s=svgOpen(W,H,o.alt||o.title),edges=o.edges,counts=o.counts;
  if(!counts){edges=[];for(var e=o.lo;e<=o.hi+1e-9;e+=o.bin)edges.push(+e.toFixed(6));counts=edges.slice(0,-1).map(function(){return 0;});
    o.values.forEach(function(v){if(v==null||v<o.lo||v>=o.hi)return;counts[Math.min(counts.length-1,Math.floor((v-o.lo)/o.bin))]++;});}
  var lo=edges[0],hi=edges[edges.length-1],mx=Math.max.apply(null,counts)*1.12||1,sx=function(v){return F.L+(W-F.L-F.R)*(v-lo)/(hi-lo);},sy=function(c){return H-F.B-(H-F.T-F.B)*c/mx;};
  var top=counts.indexOf(Math.max.apply(null,counts));
  s+=title(o,W);
  ticks(0,mx,4).forEach(function(t){s+='<line x1="'+F.L+'" x2="'+(W-F.R)+'" y1="'+sy(t)+'" y2="'+sy(t)+'" stroke="'+GRID+'"/>'+txt(F.L-6,sy(t)+4,nf(t),{a:'end'});});
  counts.forEach(function(c,i){s+='<rect x="'+(sx(edges[i])+.5)+'" y="'+sy(c)+'" width="'+Math.max(0,sx(edges[i+1])-sx(edges[i])-1)+'" height="'+(H-F.B-sy(c))+'" fill="'+(o.hlTop&&i===top?AMB:(o.color||IND))+'"/>';});
  ticks(lo,hi,6).forEach(function(t){s+=txt(sx(t),H-F.B+16,nf(t),{c:INK,fs:11});});
  (o.refs||[]).forEach(function(r){s+='<line x1="'+sx(r.v)+'" x2="'+sx(r.v)+'" y1="'+F.T+'" y2="'+(H-F.B)+'" stroke="'+(r.color||GRY)+'" stroke-width="2"'+(r.dash?' stroke-dasharray="5 4"':'')+'/>'+txt(sx(r.v)+4,F.T+12+(r.dy||0),r.label,{a:'start',c:r.color||INK,fs:11});});
  if(o.unit)s+=txt((F.L+W-F.R)/2,H-8,o.unit);
  s+=txt(16,(F.T+H-F.B)/2,o.yunit||'건수',{rot:-90});
  s+='<line x1="'+F.L+'" x2="'+(W-F.R)+'" y1="'+(H-F.B)+'" y2="'+(H-F.B)+'" stroke="'+GRY+'"/>';
  el.innerHTML=s+'</svg>';return counts;
 },
 scatter:function(el,o){ // o: pts:[[x,y]], jitter, fit(회귀선), hl:[i], xlab, ylab, ref
  var W=o.w||560,H=o.h||320,F=frame(o,W,H),s=svgOpen(W,H,o.alt||o.title),P=o.pts,R=rng(o.seed||7);
  var xs=P.map(function(p){return p[0];}),ys=P.map(function(p){return p[1];});
  var xlo=o.xlo!=null?o.xlo:Math.min.apply(null,xs),xhi=o.xhi!=null?o.xhi:Math.max.apply(null,xs),ylo=o.ylo!=null?o.ylo:Math.min.apply(null,ys),yhi=o.yhi!=null?o.yhi:Math.max.apply(null,ys);
  var px=(xhi-xlo)*.04||1,py=(yhi-ylo)*.06||1;xlo-=px;xhi+=px;if(o.ylo==null)ylo-=py;yhi+=py;
  fixL(F,o,yhi);var sx=function(v){return F.L+(W-F.L-F.R)*(v-xlo)/(xhi-xlo);},sy=function(v){return H-F.B-(H-F.T-F.B)*(v-ylo)/(yhi-ylo);};
  s+=title(o,W);
  ticks(ylo,yhi,5).forEach(function(t){s+='<line x1="'+F.L+'" x2="'+(W-F.R)+'" y1="'+sy(t)+'" y2="'+sy(t)+'" stroke="'+GRID+'"/>'+txt(F.L-6,sy(t)+4,nf(t),{a:'end'});});
  ticks(xlo,xhi,6).forEach(function(t){s+=txt(sx(t),H-F.B+16,nf(t,o.xdec||0),{c:INK,fs:11});});
  if(o.ref!=null)s+='<line x1="'+F.L+'" x2="'+(W-F.R)+'" y1="'+sy(o.ref)+'" y2="'+sy(o.ref)+'" stroke="'+GRY+'" stroke-dasharray="5 4"/>'+txt(W-F.R,sy(o.ref)-5,o.refLabel||'',{a:'end',c:INK,fs:11});
  P.forEach(function(p,i){var h=o.hl&&o.hl.indexOf(i)>=0,jx=o.jitter?(R()-.5)*2*o.jitter:0;s+='<circle cx="'+sx(p[0]+jx).toFixed(1)+'" cy="'+sy(p[1]).toFixed(1)+'" r="'+(h?6:(o.r||3.2))+'" fill="'+(h?AMB:(o.color||IND))+'" fill-opacity="'+(h?1:(o.alpha||.6))+'"/>';});
  if(o.fit){var st=VIZ.stats(xs,ys);s+='<line x1="'+sx(xlo+px)+'" y1="'+sy(st.a+st.b*(xlo+px))+'" x2="'+sx(xhi-px)+'" y2="'+sy(st.a+st.b*(xhi-px))+'" stroke="'+AMB+'" stroke-width="2.5"/>'+txt(W-F.R,F.T+12,'r = '+st.r.toFixed(2),{a:'end',c:AMB,fs:12,w:700});}
  if(o.xlab)s+=txt((F.L+W-F.R)/2,H-8,o.xlab);
  if(o.ylab)s+=txt(14,(F.T+H-F.B)/2,o.ylab,{rot:-90});
  s+='<line x1="'+F.L+'" x2="'+F.L+'" y1="'+F.T+'" y2="'+(H-F.B)+'" stroke="'+GRY+'"/><line x1="'+F.L+'" x2="'+(W-F.R)+'" y1="'+(H-F.B)+'" y2="'+(H-F.B)+'" stroke="'+GRY+'"/>';
  el.innerHTML=s+'</svg>';
 },
 stats:function(xs,ys){var n=xs.length,mx=0,my=0,i;for(i=0;i<n;i++){mx+=xs[i];my+=ys[i];}mx/=n;my/=n;var sxx=0,syy=0,sxy=0;for(i=0;i<n;i++){sxx+=(xs[i]-mx)*(xs[i]-mx);syy+=(ys[i]-my)*(ys[i]-my);sxy+=(xs[i]-mx)*(ys[i]-my);}var b=sxy/(sxx||1);return {b:b,a:my-b*mx,r:sxy/Math.sqrt((sxx*syy)||1),mx:mx,my:my};},
 pie:function(el,o){ // o: labels, values, colors, donut, sum100 표시
  var W=o.w||420,H=o.h||300,s=svgOpen(W,H,o.alt||o.title),cx=W*.36,cy=(H+(o.title?20:0))/2,r=Math.min(W*.3,H*.38),tot=o.values.reduce(function(a,b){return a+b;},0),a0=-Math.PI/2;
  var cols=o.colors||['#1e3a8a','#93a5cf','#b45309','#0b7a86','#9b3fb5','#c93030','#13733a','#5b6874','#a35c00'];
  s+=title(o,W);
  var base=o.base||tot;
  o.values.forEach(function(v,i){var a1=a0+2*Math.PI*v/base;if(a1-a0>=2*Math.PI-1e-6)a1=a0+2*Math.PI-1e-4;var lg=(a1-a0)>Math.PI?1:0;
    s+='<path d="M'+cx+' '+cy+' L'+(cx+r*Math.cos(a0))+' '+(cy+r*Math.sin(a0))+' A'+r+' '+r+' 0 '+lg+' 1 '+(cx+r*Math.cos(a1))+' '+(cy+r*Math.sin(a1))+' Z" fill="'+cols[i%cols.length]+'" stroke="#fff" stroke-width="1.5"/>';a0=a1;});
  if(o.donut)s+='<circle cx="'+cx+'" cy="'+cy+'" r="'+r*.55+'" fill="#fff"/>'+txt(cx,cy+5,o.center||'',{c:INK,fs:13,w:700});
  var ly=cy-o.labels.length*11;
  o.labels.forEach(function(t,i){s+='<rect x="'+(W*.7)+'" y="'+(ly+i*22-9)+'" width="12" height="12" fill="'+cols[i%cols.length]+'"/>'+txt(W*.7+18,ly+i*22+1,t+(o.pct===false?'':' '+nf(100*o.values[i]/base,1)+'%'),{a:'start',c:INK,fs:12});});
  el.innerHTML=s+'</svg>';
 },
 heat:function(el,o){ // o: rows, cols, m[r][c], hlMax, fmt, ramp:'ind'|'teal'|'div'
  var W=o.w||600,cw=o.cw||Math.max(18,Math.floor((W-70)/o.cols.length)),ch=o.ch||28,L=o.L||52,T=o.title?40:22,H=T+ch*o.rows.length+30;W=L+cw*o.cols.length+12;
  var s=svgOpen(W,H,o.alt||o.title),flat=[].concat.apply([],o.m),mx=Math.max.apply(null,flat),mn=Math.min.apply(null,flat.concat(o.div?[]:[0]));
  var best=null;
  s+=title(o,W);
  o.rows.forEach(function(rn,i){s+=txt(L-6,T+ch*i+ch/2+4,rn,{a:'end',c:INK,fs:12});
    o.cols.forEach(function(cn,j){var v=o.m[i][j],t,fill;
      if(o.div){var am=Math.max(Math.abs(mx),Math.abs(mn))||1;t=v/am;fill=t>=0?'rgba(30,58,138,'+(0.08+0.85*t)+')':'rgba(180,83,9,'+(0.08+0.85*-t)+')';}
      else{t=(v-mn)/((mx-mn)||1);fill=(o.ramp==='teal'?'rgba(11,122,134,':'rgba(30,58,138,')+(0.06+0.9*t)+')';}
      s+='<rect x="'+(L+cw*j)+'" y="'+(T+ch*i)+'" width="'+(cw-1)+'" height="'+(ch-1)+'" fill="'+fill+'"><title>'+esc(rn+' · '+cn+' : '+(o.fmt?o.fmt(v):nf(v)))+'</title></rect>';
      if(o.showVal)s+=txt(L+cw*j+cw/2,T+ch*i+ch/2+4,o.fmt?o.fmt(v):nf(v),{fs:11,c:Math.abs(t)>.55?'#fff':INK});
      if(o.mark&&o.mark[0]===i&&o.mark[1]===j)s+='<rect x="'+(L+cw*j+2)+'" y="'+(T+ch*i+2)+'" width="'+(cw-5)+'" height="'+(ch-5)+'" fill="none" stroke="#13733a" stroke-width="3" stroke-dasharray="4 2"/>';
      if(o.hlMax&&v===mx&&!best){best=1;s+='<rect x="'+(L+cw*j-1)+'" y="'+(T+ch*i-1)+'" width="'+(cw+1)+'" height="'+(ch+1)+'" fill="none" stroke="'+AMB+'" stroke-width="3"/>';}
    });});
  var st=Math.max(1,Math.ceil(o.cols.length/16));
  o.cols.forEach(function(cn,j){if(j%st===0)s+=txt(L+cw*j+cw/2,T+ch*o.rows.length+16,cn,{fs:11,c:INK});});
  el.innerHTML=s+'</svg>';
 },
 pareto:function(el,o){ // o: labels, values (정렬 여부는 호출하는 쪽), cum(true면 누적선)
  var W=o.w||560,H=o.h||300,F=frame(o,W,H);F.R=46;var s=svgOpen(W,H,o.alt||o.title),n=o.labels.length,tot=o.values.reduce(function(a,b){return a+b;},0),mx=Math.max.apply(null,o.values)*1.12;
  fixL(F,o,mx);var bw=(W-F.L-F.R)/n,sy=function(v){return H-F.B-(H-F.T-F.B)*v/mx;},sp=function(p){return H-F.B-(H-F.T-F.B)*p/100;};
  s+=title(o,W);
  ticks(0,mx,5).forEach(function(t){s+='<line x1="'+F.L+'" x2="'+(W-F.R)+'" y1="'+sy(t)+'" y2="'+sy(t)+'" stroke="'+GRID+'"/>'+txt(F.L-6,sy(t)+4,nf(t),{a:'end'});});
  o.values.forEach(function(v,i){var x=F.L+bw*i+bw*.15;s+='<rect x="'+x+'" y="'+sy(v)+'" width="'+bw*.7+'" height="'+(H-F.B-sy(v))+'" fill="'+(i===o.hl?AMB:IND)+'"/>'+txt(x+bw*.35,sy(v)-5,nf(v),{c:INK,fs:11})+txt(x+bw*.35,H-F.B+16,o.labels[i],{c:INK,fs:11});});
  if(o.cum){var acc=0,d='';o.values.forEach(function(v,i){acc+=v;var p=100*acc/tot,x=F.L+bw*(i+.5);d+=(i?'L':'M')+x+' '+sp(p)+' ';s+='<circle cx="'+x+'" cy="'+sp(p)+'" r="3.5" fill="'+AMB+'"/>'+txt(x,sp(p)-8,nf(p)+'%',{c:AMB,fs:11,w:700});});
    s+='<path d="'+d+'" fill="none" stroke="'+AMB+'" stroke-width="2.5"/>';[0,50,80,100].forEach(function(p){s+=txt(W-F.R+6,sp(p)+4,p+'%',{a:'start',c:AMB,fs:11});});
    s+='<line x1="'+F.L+'" x2="'+(W-F.R)+'" y1="'+sp(80)+'" y2="'+sp(80)+'" stroke="'+AMB+'" stroke-dasharray="3 4" opacity=".6"/>';}
  if(o.unit)s+=txt(14,(F.T+H-F.B)/2,o.unit,{rot:-90});
  s+='<line x1="'+F.L+'" x2="'+(W-F.R)+'" y1="'+(H-F.B)+'" y2="'+(H-F.B)+'" stroke="'+GRY+'"/>';
  el.innerHTML=s+'</svg>';
 },
 box:function(el,o){ // o: groups:[{name, values}] → 다섯 숫자 요약 상자그림
  var W=o.w||560,H=o.h||280,F=frame(o,W,H),s=svgOpen(W,H,o.alt||o.title),G=o.groups.map(function(g){return VIZ.five(g.values);}),all=[];
  G.forEach(function(g){all.push(g.min,g.max);});var lo=o.lo!=null?o.lo:Math.min.apply(null,all),hi=o.hi!=null?o.hi:Math.max.apply(null,all)*1.05,n=G.length;fixL(F,o,hi);var bw=(W-F.L-F.R)/n,sy=function(v){return H-F.B-(H-F.T-F.B)*(v-lo)/(hi-lo);};
  s+=title(o,W);
  ticks(lo,hi,5).forEach(function(t){s+='<line x1="'+F.L+'" x2="'+(W-F.R)+'" y1="'+sy(t)+'" y2="'+sy(t)+'" stroke="'+GRID+'"/>'+txt(F.L-6,sy(t)+4,nf(t),{a:'end'});});
  G.forEach(function(g,i){var cx=F.L+bw*(i+.5),w=Math.min(70,bw*.5);
    s+='<line x1="'+cx+'" x2="'+cx+'" y1="'+sy(g.lw)+'" y2="'+sy(g.uw)+'" stroke="'+INK+'"/><rect x="'+(cx-w/2)+'" y="'+sy(g.q3)+'" width="'+w+'" height="'+(sy(g.q1)-sy(g.q3))+'" fill="#e6eefb" stroke="'+IND+'" stroke-width="1.5"/><line x1="'+(cx-w/2)+'" x2="'+(cx+w/2)+'" y1="'+sy(g.med)+'" y2="'+sy(g.med)+'" stroke="'+AMB+'" stroke-width="3"/>';
    g.out.forEach(function(v){s+='<circle cx="'+cx+'" cy="'+sy(v)+'" r="2.6" fill="none" stroke="'+IND+'"/>';});
    if(o.mean)s+='<path d="M'+(cx-5)+' '+sy(g.mean)+' l5 -5 l5 5 l-5 5 z" fill="'+INK+'"/>';
    s+=txt(cx,H-F.B+16,o.groups[i].name,{c:INK});});
  if(o.unit)s+=txt(14,(F.T+H-F.B)/2,o.unit,{rot:-90});
  el.innerHTML=s+'</svg>';return G;
 },
 five:function(v){var a=v.filter(function(x){return x!=null&&!isNaN(x);}).slice().sort(function(x,y){return x-y;}),q=function(p){var i=(a.length-1)*p,f=Math.floor(i);return a[f]+(a[Math.min(a.length-1,f+1)]-a[f])*(i-f);};
  var q1=q(.25),q3=q(.75),iq=q3-q1,lf=q1-1.5*iq,uf=q3+1.5*iq,inside=a.filter(function(x){return x>=lf&&x<=uf;});
  return {min:a[0],max:a[a.length-1],q1:q1,med:q(.5),q3:q3,lw:inside[0],uw:inside[inside.length-1],out:a.filter(function(x){return x<lf||x>uf;}),mean:a.reduce(function(s,x){return s+x;},0)/a.length,n:a.length};},
 csv:function(t){var L=t.trim().split(/\r?\n/),h=L[0].split(',');return L.slice(1).map(function(l){var c=l.split(','),o={};h.forEach(function(k,i){var v=c[i];o[k]=(v===''||v==null)?null:(isNaN(+v)?v:+v);});return o;});}
};

/* ── 진행 막대 ── */
function prog(){var p=$('#prog'); if(!p)return; var h=document.documentElement; p.style.width=(100*h.scrollTop/Math.max(1,h.scrollHeight-h.clientHeight))+'%';}
window.addEventListener('scroll',prog,{passive:true});

/* ── 낱말 카드 ── */
function Flash(el,cards){el.classList.add('flash'); el.innerHTML=cards.map(function(c,i){return '<button type="button" class="bt" data-i="'+i+'">'+c[0]+'</button>';}).join('');
  $$('button',el).forEach(function(b){var c=cards[+b.dataset.i],f=false; b.onclick=function(){f=!f; b.classList.toggle('flip',f); b.innerHTML=f?c[1]:c[0];};});}

/* ── 고르기 게임: 질문 → 답 버튼 ── */
function Pick(el,items,opts){ // items:[{q, a(index), why}], opts:[label]
  var i=0,score=0;
  function draw(){if(i>=items.length){el.innerHTML='<div class="insight"><p class="g">'+items.length+'문제 중 <b>'+score+'개</b>를 맞혔습니다. '+(score===items.length?'모두 맞혔어요.':'틀린 문제는 해설을 다시 읽으면 충분합니다.')+'</p></div><div class="ctrl"><button type="button" class="bt">처음부터 다시</button></div>';$('button',el).onclick=function(){i=0;score=0;draw();};return;}
    var it=items[i];el.innerHTML='<p class="pq"><b>'+(i+1)+'/'+items.length+'</b> '+it.q+'</p><div class="ctrl">'+opts.map(function(o,j){return '<button type="button" class="bt" data-j="'+j+'">'+o+'</button>';}).join('')+'</div><div class="insight" aria-live="polite"></div>';
    $$('.ctrl button',el).forEach(function(b){b.onclick=function(){var ok=+b.dataset.j===it.a;if(ok)score++;$$('.ctrl button',el).forEach(function(x){x.disabled=true;});b.classList.add(ok?'ok':'no');
      $('.insight',el).innerHTML='<p class="'+(ok?'g':'r')+'">'+(ok?'맞아요. ':'정답은 「'+opts[it.a]+'」. ')+it.why+'</p><div class="ctrl"><button type="button" class="bt primary nx">다음 →</button></div>';$('.nx',el).onclick=function(){i++;draw();};};});}
  draw();
}

window.QSTAT=QSTAT;window.VIZ=VIZ;
window.LAB={$:$,$$:$$,esc:esc,rng:rng,fit:fit,addMod:addMod,stamp:stamp,Gloss:Gloss,Quiz:Quiz,Duel:Duel,Flow:Flow,Flash:Flash,Pick:Pick,RM:RM,VIZ:VIZ,nf:nf};
window.addEventListener('DOMContentLoaded',function(){
  Cast.fill();
  if(window.QUIZ)Object.keys(QUIZ).forEach(function(k){var e=document.querySelector('.quiz[data-quiz="'+k+'"]'); if(e)Quiz(e,QUIZ[k]);});
  updProg();
  if(window.GL)Gloss(GL);
  $$('canvas.flow').forEach(function(cv){var o=window.FLOWS&&FLOWS[cv.id]; if(o)Flow(cv,o);});
  if(window.DUEL)Duel(DUEL);
  $$('.flash[data-cards]').forEach(function(el){var o=window.CARDS&&CARDS[el.dataset.cards]; if(o)Flash(el,o);});
  if(window.PAGE&&PAGE.init){try{PAGE.init(window.LAB);}catch(e){if(window.console)console.error(e);}}
  requestAnimationFrame(loop); prog();
});
})();
