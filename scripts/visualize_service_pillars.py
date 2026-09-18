from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

services_html = r'''<section class="section services services-visual" id="services"><div class="container">
  <span class="kicker">ONE PACKAGE</span>
  <h2>小金井で必要なWEB施策を、<br><span>4つの柱でひとつの仕組みに。</span></h2>
  <p class="lead service-intro">バラバラに外注するのではなく、<strong>見つかる → 伝わる → 好きになる → 来店につながる</strong>までを一つに設計します。</p>

  <div class="service-flow">
    <span>見つかる</span><i>→</i><span>伝わる</span><i>→</i><span>好きになる</span><i>→</i><span>来店・再来店</span>
  </div>

  <div class="offer-grid offer-grid-visual">
    <a class="offer-card offer-card-link portal-card" href="https://machi-aka.cc-corp.co.jp/koganei/" target="_blank" rel="noopener">
      <div class="offer-top"><span class="offer-no">01</span><span class="offer-icon" aria-hidden="true">⌖</span></div>
      <span class="offer-eyebrow">LOCAL PORTAL</span>
      <h3>小金井ポータル</h3>
      <strong class="offer-catch">地域で、見つかる。</strong>
      <p>事業者情報とニュースをまとめ、地域検索の入口をつくります。</p>
      <span class="offer-link-label">小金井ポータルを見る →</span>
    </a>

    <article class="offer-card">
      <div class="offer-top"><span class="offer-no">02</span><span class="offer-icon" aria-hidden="true">◎</span></div>
      <span class="offer-eyebrow">GOOGLE MAP</span>
      <h3>Googleマップ / MEO</h3>
      <strong class="offer-catch">検索から、来店へ。</strong>
      <p>地図・最新情報・口コミを整え、「近くで探す」人に届く状態へ。</p>
      <span class="offer-tag">検索・地図・口コミ</span>
    </article>

    <article class="offer-card">
      <div class="offer-top"><span class="offer-no">03</span><span class="offer-icon" aria-hidden="true">♡</span></div>
      <span class="offer-eyebrow">INSTAGRAM</span>
      <h3>Instagram</h3>
      <strong class="offer-catch">知るから、好きへ。</strong>
      <p>プロフィール・ピン留め・ストーリーズで、小金井のファンを育てます。</p>
      <span class="offer-tag">新規 → フォロー → リピート</span>
    </article>

    <a class="offer-card offer-card-link view3d-card" href="#samples">
      <div class="offer-top"><span class="offer-no">04</span><span class="offer-icon" aria-hidden="true">◈</span></div>
      <span class="offer-eyebrow">3D / DRONE / VIDEO</span>
      <h3>空間3Dビュー</h3>
      <strong class="offer-catch">空間を、20秒で伝える。</strong>
      <p>広さ・動線・空気感まで、動画とドローンで直感的に見せます。</p>
      <span class="offer-link-label">ドローン映像を見る →</span>
    </a>
  </div>

  <div class="included-strip included-strip-visual">
    <div>
      <strong>さらに、必要な土台もまとめて。</strong>
      <div class="included-chips">
        <span>カスタムAI</span><span>口コミPOP</span><span>インタビュー</span><span>掲載ページ</span><span>写真・動画</span><span>Google連携</span>
      </div>
    </div>
    <a class="btn navy" href="#pricing">新プランを見る</a>
  </div>

  <div class="client-role-strip">
    <div class="client-role-copy">
      <span>YOUR PART</span>
      <h3>日々やることは、基本3つだけ。</h3>
      <p>仕組みはまちこがが設計。日々の運用は、無理なく続けられる形に絞ります。</p>
    </div>
    <div class="client-role-pills">
      <div><b>01</b><span>1日2分の<br>Google投稿</span></div>
      <div><b>02</b><span>口コミ依頼<br>＆ 返信</span></div>
      <div><b>03</b><span>ストーリーズ<br>投稿</span></div>
    </div>
  </div>
</div></section>'''

pattern = r'<section class="section services[^"]*" id="services">.*?</section>'
if not re.search(pattern, s, flags=re.S):
    raise SystemExit('Services section not found')
s = re.sub(pattern, services_html, s, count=1, flags=re.S)

css = r'''
/* V68 VISUAL SERVICE PILLARS */
.services-visual{
  background:linear-gradient(180deg,#fff 0%,#f7f9fc 100%);
}
.services-visual h2 span{
  color:#0a6570;
}
.services-visual .service-intro{
  max-width:860px;
}
.services-visual .service-flow{
  display:flex;
  align-items:center;
  flex-wrap:wrap;
  gap:9px;
  margin-top:22px;
}
.services-visual .service-flow span{
  display:inline-flex;
  align-items:center;
  min-height:34px;
  padding:7px 12px;
  border-radius:999px;
  background:#071d3f;
  color:#fff;
  font-size:.72rem;
  font-weight:900;
}
.services-visual .service-flow i{
  font-style:normal;
  color:#0a948d;
  font-weight:900;
}
.offer-grid-visual{
  margin-top:22px!important;
  gap:12px!important;
}
.offer-grid-visual .offer-card{
  position:relative;
  min-width:0;
  padding:20px 18px 18px!important;
  border-radius:22px!important;
  background:#fff;
  border:1px solid #dde5ee!important;
  box-shadow:0 12px 28px rgba(5,25,57,.07)!important;
  text-decoration:none!important;
  overflow:hidden;
  transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease;
}
.offer-grid-visual .offer-card:before{
  height:4px!important;
  background:linear-gradient(90deg,#0b5ea8,#0aa095)!important;
}
.offer-grid-visual .offer-card-link:hover{
  transform:translateY(-3px);
  box-shadow:0 18px 36px rgba(5,25,57,.11)!important;
  border-color:#9fc8c8!important;
}
.offer-top{
  display:flex;
  justify-content:space-between;
  align-items:center;
  gap:12px;
}
.offer-grid-visual .offer-no{
  width:38px!important;
  height:38px!important;
  border-radius:12px!important;
  font-size:.82rem!important;
}
.offer-icon{
  display:grid;
  place-items:center;
  width:44px;
  height:44px;
  border-radius:14px;
  background:#edf7f7;
  color:#087f7b;
  font-size:1.45rem;
  font-weight:900;
}
.offer-eyebrow{
  display:block;
  margin-top:18px;
  color:#8b98aa;
  font-size:.58rem;
  font-weight:950;
  letter-spacing:.12em;
}
.offer-grid-visual .offer-card h3{
  margin-top:6px!important;
  color:#071d3f!important;
  font-size:1.2rem!important;
  line-height:1.25!important;
}
.offer-catch{
  display:block;
  margin-top:13px;
  color:#0b6570;
  font-size:1.02rem;
  line-height:1.4;
}
.offer-grid-visual .offer-card p{
  margin-top:7px!important;
  min-height:0!important;
  color:#657287!important;
  font-size:.78rem!important;
  line-height:1.65!important;
}
.offer-tag,
.offer-link-label{
  display:inline-flex;
  margin-top:14px;
  padding-top:0!important;
  border-top:0!important;
  color:#087f7b!important;
  font-size:.7rem!important;
  font-weight:900!important;
}
.offer-link-label{
  padding:7px 10px!important;
  border-radius:999px;
  background:#eef8f7;
}
.portal-card .offer-icon{
  background:#fff3d8;
  color:#9b6a26;
}
.portal-card .offer-link-label{
  background:#fff5df;
  color:#8a621f!important;
}
.view3d-card .offer-icon{
  background:#eaf0ff;
  color:#304e8f;
}
.view3d-card .offer-link-label{
  background:#edf2ff;
  color:#304e8f!important;
}
.included-strip-visual{
  padding:16px 18px!important;
  margin-top:14px!important;
  border-radius:20px!important;
}
.included-strip-visual strong{
  font-size:.9rem!important;
}
.included-chips{
  display:flex;
  flex-wrap:wrap;
  gap:6px;
  margin-top:10px;
}
.included-chips span{
  display:inline-flex!important;
  margin:0!important;
  padding:6px 9px;
  border-radius:999px;
  background:#fff;
  border:1px solid #e6d7b3;
  color:#5d6675!important;
  font-size:.66rem!important;
  line-height:1!important;
}
@media(max-width:980px){
  .offer-grid-visual{
    grid-template-columns:repeat(2,minmax(0,1fr))!important;
  }
}
@media(max-width:780px){
  .services-visual .service-flow{
    gap:6px;
  }
  .services-visual .service-flow span{
    font-size:.67rem;
    min-height:31px;
    padding:6px 10px;
  }
  .offer-grid-visual{
    grid-template-columns:1fr!important;
  }
  .offer-grid-visual .offer-card{
    padding:18px 17px!important;
  }
  .offer-top{
    margin-bottom:2px;
  }
  .offer-icon{
    width:40px;
    height:40px;
  }
  .offer-grid-visual .offer-card p{
    font-size:.8rem!important;
  }
  .included-strip-visual{
    align-items:flex-start!important;
    flex-direction:column!important;
  }
  .included-strip-visual .btn{
    width:100%;
    text-align:center;
  }
}
'''

s = re.sub(r'/\* V68 VISUAL SERVICE PILLARS \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

for token in [
  'href="https://machi-aka.cc-corp.co.jp/koganei/"',
  'href="#samples"',
  'ドローン映像を見る',
  '見つかる',
  'V68 VISUAL SERVICE PILLARS'
]:
    if token not in s:
        raise SystemExit(f'Missing service visual token: {token}')
