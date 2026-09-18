from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

results_html = r'''<section class="section results machikoga-results" id="results"><div class="container">
  <span class="kicker">MACHIKOGA RESULTS</span>
  <h2>小金井で、<br>成果が出ています。</h2>
  <p class="lead results-lead">集客だけではありません。<strong>新規来店・採用・認知・Google・アカウント立ち上げまで。</strong> 実際に一緒に取り組んだ成果の一部です。</p>

  <div class="results-featured">
    <article class="result-impact result-featured">
      <span class="result-type">うどん店</span>
      <small>アルバイト採用</small>
      <strong>1ヶ月で<br>アルバイト3名採用</strong>
      <p>採用までつながった求人事例</p>
    </article>
    <article class="result-impact result-featured">
      <span class="result-type">美容室</span>
      <small>店舗アピール投稿</small>
      <strong>周年イベント翌日<br>新規来客4名</strong>
      <p>投稿から来店へ</p>
    </article>
    <article class="result-impact result-featured">
      <span class="result-type">小金井ゆるっと会</span>
      <small>地域交流イベント</small>
      <strong>定期開催へ</strong>
      <p>地域コミュニティ形成</p>
    </article>
    <article class="result-impact result-featured">
      <span class="result-type">ハウスクリーニング</span>
      <small>新規アカウント立ち上げ</small>
      <strong>3ヶ月で<br>多摩エリア700人</strong>
      <p>地域フォロワーを獲得</p>
    </article>
  </div>

  <div class="results-highlight">
    <article class="result-impact"><span class="result-type">飲食店</span><small>集客コンサル</small><strong>2ヶ月で<br>ランチ客数120%</strong></article>
    <article class="result-impact"><span class="result-type">求人</span><small>アルバイト募集投稿</small><strong>投稿後1日で<br>6名応募</strong><p>採用決定</p></article>
    <article class="result-impact"><span class="result-type">整体院</span><small>店舗アピール投稿</small><strong>翌日<br>新規顧客5名</strong><p>保存10</p></article>
    <article class="result-impact"><span class="result-type">カフェ</span><small>新規アカウント立ち上げ</small><strong>3ヶ月で<br><span class="result-long-line">小金井フォロワー</span><br><span class="result-big-number">300人</span></strong><p>1日1組「Instagramを見た」で新規来店</p></article>
    <article class="result-impact"><span class="result-type">ドローン</span><small>Google閲覧数</small><strong>1週間で<br>過去の閲覧数を突破</strong><p>閲覧数トップへ</p></article>
    <article class="result-impact"><span class="result-type">看護師採用</span><small>訪問ナース紹介</small><strong>看護師<br>2名採用</strong></article>
  </div>

  <details class="results-more">
    <summary>その他の成果を見る ＋</summary>
    <div class="results-list">
      <div class="result-row"><b>スポーツスクール</b><span>会員募集</span><strong>翌日 新規体験4名・保存11</strong></div>
      <div class="result-row"><b>ラーメン店</b><span>特集記事掲載</span><strong>混雑が続出するほど反響</strong></div>
      <div class="result-row"><b>バンド</b><span>新規アカウント立ち上げ</span><strong>初期設計から東京都・大阪へ認知拡大</strong></div>
    </div>
  </details>

  <p class="results-note">※成果事例は一部抜粋です。数値・実績は2026年8月時点を含みます。</p>
</div></section>'''

pattern = r'<section class="section results machikoga-results" id="results">.*?</section>'
if not re.search(pattern, s, flags=re.S):
    raise SystemExit('Results section not found')
s = re.sub(pattern, results_html, s, count=1, flags=re.S)

css = r'''
/* V68 RESULTS FEATURED CASES */
.results-featured{
  display:grid;
  grid-template-columns:repeat(4,minmax(0,1fr));
  gap:14px;
  margin-top:30px;
}
.results-featured .result-impact{
  position:relative;
  overflow:hidden;
  min-width:0;
  padding:24px 20px 22px!important;
  border:1px solid rgba(199,162,83,.34)!important;
  background:linear-gradient(145deg,#071d3f 0%,#0a4564 100%)!important;
  color:#fff!important;
  box-shadow:0 18px 42px rgba(5,25,57,.14)!important;
}
.results-featured .result-impact:before{
  content:"PICK UP";
  position:absolute;
  top:14px;
  right:14px;
  color:#f0d995;
  font-size:.58rem;
  font-weight:900;
  letter-spacing:.12em;
}
.results-featured .result-type{
  background:#f0d995!important;
  color:#071d3f!important;
}
.results-featured .result-impact small{
  color:rgba(255,255,255,.68)!important;
}
.results-featured .result-impact>strong{
  color:#fff!important;
  font-size:clamp(1.35rem,2vw,1.9rem)!important;
  line-height:1.24!important;
}
.results-featured .result-impact p{
  color:rgba(255,255,255,.76)!important;
}
.results-highlight{
  margin-top:18px!important;
}
@media(max-width:980px){
  .results-featured{
    grid-template-columns:repeat(2,minmax(0,1fr));
  }
}
@media(max-width:780px){
  .results-featured{
    grid-template-columns:1fr;
    gap:12px;
    margin-top:24px;
  }
  .results-featured .result-impact{
    padding:21px 19px!important;
  }
}
'''

s = re.sub(r'/\* V68 RESULTS FEATURED CASES \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

for token in [
    '1ヶ月で<br>アルバイト3名採用',
    '周年イベント翌日<br>新規来客4名',
    '小金井ゆるっと会',
    '3ヶ月で<br>多摩エリア700人',
    'V68 RESULTS FEATURED CASES',
]:
    if token not in s:
        raise SystemExit(f'Missing results token: {token}')
