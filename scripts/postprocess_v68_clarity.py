from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

# Partner section: make Buru the clear center, remove explanatory lead, and clarify every metric.
start = s.find('<section class="section tools" id="tools">')
end = s.find('<section class="section local-edge"', start)
if start != -1 and end != -1:
    tools = s[start:end]

    tools = re.sub(r'<span class="kicker">.*?</span>', '<span class="kicker">ぶる × POWERFUL PARTNERS</span>', tools, count=1, flags=re.S)
    tools = re.sub(r'<h2>.*?</h2>', '<h2>ぶるを支える、<br>強力なパートナー。</h2>', tools, count=1, flags=re.S)
    tools = re.sub(r'<p class="lead trio-lead">.*?</p>', '', tools, count=1, flags=re.S)

    tools = tools.replace('<div class="main-badge">MACHIKOGA / BUL</div>', '<div class="main-badge">まちこが / ぶる</div>')
    tools = tools.replace('<div class="trio-role">BUL / PRODUCER</div>', '<div class="trio-role">ぶる / PRODUCER</div>')

    # Suzuki: shorten prose and make authority boxes self-explanatory.
    suzuki_pattern = r'(<article class="trio-person suzuki">.*?<strong>「見つかる」を支える、地域ビジネスの実力者。</strong>).*?(<div class="authority-box">.*?</div><a class="trio-cta")'
    suzuki_repl = r'''\1<p class="partner-summary">株式会社C&amp;C代表。地域メディア「まちアカ」主宰。</p><div class="authority-box"><div class="authority-item"><b>令和の虎</b><span>虎として出演</span></div><div class="authority-item"><b>全国165地域</b><span>地域メディア「まちアカ」展開</span></div><div class="authority-item"><b>ANA</b><span>地域創生プロジェクト</span></div><div class="authority-item"><b>1年で19店舗</b><span>飲食ブランド展開</span></div></div><a class="trio-cta'''
    tools = re.sub(suzuki_pattern, suzuki_repl, tools, count=1, flags=re.S)

    # Buru: keep a very short description, then spell out exactly what each number means.
    buru_pattern = r'(<article class="trio-person buru-center">.*?<strong>小金井で強くなる仕組みを、全体から組み立てる。</strong>).*?(<div class="buru-current">)'
    buru_repl = r'''\1<p class="partner-summary">小金井在住11年目。店舗・SNS・Google・地域導線を、事業者の資産として残る形に設計。</p>\2'''
    tools = re.sub(buru_pattern, buru_repl, tools, count=1, flags=re.S)

    tools = re.sub(
        r'<div class="buru-current">.*?</div><div class="authority-box buru-history">.*?</div><a class="trio-cta buru-instagram"',
        '''<div class="buru-current"><span class="asof">現在の小金井での活動実績｜2026年8月時点</span><div class="buru-stats"><div><b>5,500人</b><span>Instagram「ぶる」フォロワー数</span></div><div><b>85%</b><span>フォロワーのうち小金井エリア</span></div><div><b>21社</b><span>小金井で実際に一緒に仕事をした事業者</span></div><div><b>100件以上</b><span>まちこがの投稿制作・支援実績</span></div></div></div><div class="authority-box buru-history"><div class="authority-item"><b>0→250店舗</b><span>大手カフェチェーン立ち上げ・拡大</span></div><div class="authority-item"><b>200店舗規模</b><span>医療業界の店舗責任者</span></div><div class="authority-item"><b>100件以上</b><span>店舗・SNSコンサル実績</span></div><div class="authority-item"><b>11年目</b><span>小金井在住・地域密着</span></div></div><a class="trio-cta buru-instagram"''',
        tools,
        count=1,
        flags=re.S,
    )

    # Yokota: remove long prose and show recognizable authority/client names visually.
    yokota_pattern = r'(<article class="trio-person yokota">.*?<strong>「伝わる」を支える、ドローン映像の第一人者。</strong>).*?(<div class="authority-box">.*?</div><a class="trio-cta")'
    yokota_repl = r'''\1<p class="partner-summary">株式会社ドローンエンタテインメント代表。FPV・マイクロドローン映像の第一人者。</p><div class="authority-box authority-box-wide"><div class="authority-item"><b>元日本代表</b><span>ドローンレース</span></div><div class="authority-item"><b>アジア準優勝</b><span>Asia Drone Championships</span></div><div class="authority-item"><b>万博</b><span>大型プロジェクト</span></div><div class="authority-item"><b>Coca-Cola</b><span>企業映像</span></div><div class="authority-item"><b>HONDA</b><span>企業映像</span></div><div class="authority-item"><b>BMW</b><span>企業映像</span></div><div class="authority-item"><b>NTTデータ</b><span>企業映像</span></div><div class="authority-item"><b>100件以上</b><span>メディア掲載</span></div></div><a class="trio-cta'''
    tools = re.sub(yokota_pattern, yokota_repl, tools, count=1, flags=re.S)

    s = s[:start] + tools + s[end:]

# Make Buru's current stats blend into the surrounding cream/gold design instead of floating as a blue block.
clarity_css = '''
/* V68 PARTNER CLARITY */
.partner-summary{margin-top:12px!important;color:#5f6d80!important;font-size:.86rem!important;text-align:center!important;line-height:1.65!important}
.buru-current{margin-top:18px!important;padding:17px!important;border-radius:20px!important;background:#f8f4ea!important;border:1px solid #e7d7ad!important;color:#0b2348!important;box-shadow:none!important}
.asof{display:block!important;margin-bottom:11px!important;color:#9b6a26!important;font-size:.68rem!important;font-weight:900!important;letter-spacing:.04em!important}
.buru-stats{display:grid!important;grid-template-columns:1fr 1fr!important;gap:10px!important}
.buru-stats div{padding:12px 9px!important;border-radius:14px!important;background:#fffdf8!important;border:1px solid #eadfbe!important;text-align:center!important}
.buru-stats b{display:block!important;color:#0b2348!important;font-size:1.18rem!important;line-height:1.2!important}
.buru-stats span{display:block!important;margin-top:5px!important;color:#657185!important;font-size:.64rem!important;font-weight:800!important;line-height:1.45!important}
.authority-box-wide{grid-template-columns:1fr 1fr!important}
@media(max-width:780px){.buru-stats{grid-template-columns:1fr 1fr!important}.partner-summary{text-align:left!important}.authority-box-wide{grid-template-columns:1fr 1fr!important}}
'''
if '/* V68 PARTNER CLARITY */' not in s:
    s = s.replace('</style>', clarity_css + '</style>', 1)

p.write_text(s, encoding='utf-8')

# Safety checks
required = [
    'ぶるを支える、<br>強力なパートナー。',
    'Instagram「ぶる」フォロワー数',
    'フォロワーのうち小金井エリア',
    '小金井で実際に一緒に仕事をした事業者',
    '大手カフェチェーン立ち上げ・拡大',
    'Coca-Cola',
    'HONDA',
    'BMW',
    'NTTデータ',
]
for item in required:
    if item not in s:
        raise SystemExit(f'Missing expected partner clarity item: {item}')
