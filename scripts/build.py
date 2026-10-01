from pathlib import Path
import json,html,re,math
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'docs'; BASE='/future-chain/'; CLOUD='https://future-chain.docile-clock-7844.chatgpt.site'
chapters=[json.loads(p.read_text()) for p in sorted((ROOT/'content/chapters').glob('*.json'))]
volumes=[(1,'意识之火','2026—2037','01—30','从一个家庭的日常，到机器第一次为未来保留选择。'),(2,'超级智能时代','2038—2063','31—60','当科学、生产与决策开始加速，人类如何理解自己创造的智能。'),(3,'太阳文明','2064—2150','61—90','机器走向月球、火星与太阳，文明不再拥有同一个现在。')]
e=lambda x:html.escape(str(x),quote=True)
def label(n):return '序言' if n==0 else f'第 {n:02d} 章'
def href(n):return f'{BASE}read/{n}/'
def page(title,body):return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title><meta name="description" content="《未来之链》正式版：意识之火、超级智能时代与太阳文明。完整正文与章节配图。"><link rel="icon" href="{BASE}assets/favicon.svg"><link rel="stylesheet" href="{BASE}assets/style.css"></head><body>{body}</body></html>'''
def write(path,text):p=OUT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
brand=f'<a class="brand" href="{BASE}">未来之链<span>THE CHAIN OF THE FUTURE</span></a>'
books=''
for i,name,period,span,desc in volumes:
 books+=f'''<article class="volume"><a class="cover" href="#volume-{i}"><img src="{BASE}assets/cover-{i}.webp" alt="第{i}部《{name}》封面" width="1024" height="1536"></a><div class="volume-copy"><p class="eyebrow">VOL. 0{i}<span>{period}</span></p><h2><a href="#volume-{i}">{name}</a></h2><p>{desc}</p><a class="volume-link" href="#volume-{i}">第 {span} 章</a></div></article>'''
catalog=''
for i,name,period,_,_ in volumes:
 rows=''.join(f'<a href="{href(c["number"])}"><span>{"序" if c["number"]==0 else str(c["number"]).zfill(2)}</span><div>{e(c["title"])}'+('<small>正文待补齐</small>' if c.get('missing') else '')+'</div></a>' for c in chapters if c['volume']==i)
 catalog+=f'<section class="volume-catalog" id="volume-{i}"><div class="catalog-title"><span>0{i}</span><h3>{name}</h3><small>{period}</small></div><div class="chapter-list">{rows}</div></section>'
write(Path('index.html'),page('未来之链',f'''<main><header class="topbar">{brand}<nav><a href="#library">三部曲</a><a href="#catalog">完整目录</a><a href="{CLOUD}/account">读者登录</a></nav></header><section class="intro"><div><p class="eyebrow">长篇科幻 · 正式版</p><h1>从意识之火，<br>走向<span>太阳文明。</span></h1><p class="intro-copy">一场跨越百年的文明演化。<br>在机器学会思考之后，重新看见人的位置。</p><div class="actions"><a class="primary" href="{href(0)}">从序言开始</a><a class="text-link" href="#catalog">浏览章节目录</a></div></div><div class="intro-meta"><span>THE FUTURE IS A CHAIN</span><strong>2026<span>—</span>2150</strong><p>三部 · 九十章的文明长卷</p></div></section><section class="library" id="library">{books}</section><section class="catalog" id="catalog"><div class="section-head"><div><p class="eyebrow">READ THE COMPLETE STORY</p><h2>章节目录</h2></div><span>点击章节标题开始阅读</span></div>{catalog}</section><section class="reader-invite"><p class="eyebrow">读完之后，留下你的思考</p><h2>未来的另一种可能，<br>也在读者的声音里。</h2><p>每章末尾可前往互动站，为这一章评分、留下评论。</p><a class="secondary" href="{CLOUD}/account">登录互动站</a></section><footer><a href="{BASE}">未来之链</a><span>Sun Zhen · 正式版</span><a href="{CLOUD}/author">作者后台</a></footer></main>'''))
for idx,c in enumerate(chapters):
 n=c['number'];vol=volumes[c['volume']-1];prev=chapters[idx-1] if idx else None;next=chapters[idx+1] if idx+1<len(chapters) else None
 def para(s):
  safe=''.join('<strong>'+e(x)+'</strong>' if i%2 else e(x) for i,x in enumerate(re.split(r'\*\*(.+?)\*\*',s)))
  return '<h2 class="section-number">'+safe+'</h2>' if re.fullmatch('[一二三四五六七八九十]{1,3}',s) else '<p>'+safe+'</p>'
 text=''.join(para(p) for p in c['paragraphs']) if not c.get('missing') else '<div class="missing-chapter"><h2>本章正文待补齐</h2><p>本章配图已收录，正文将在核对完成后上线。</p></div>'
 art=''.join(f'<figure><a href="{BASE}assets/{e(Path(src).name)}" target="_blank" rel="noreferrer"><img src="{BASE}assets/{e(Path(src).name)}" alt="{label(n)}《{e(c["title"])}》配图" loading="lazy"></a><figcaption>点击查看完整配图</figcaption></figure>' for src in c['images'])
 nav=(f'<a href="{href(prev["number"])}"><small>上一章 · {label(prev["number"])}</small><span>{e(prev["title"])}</span></a>' if prev else f'<a href="{BASE}">返回书架</a>')+(f'<a href="{href(next["number"])}"><small>下一章 · {label(next["number"])}</small><span>{e(next["title"])}</span></a>' if next else f'<a href="{BASE}#catalog"><small>第三部完</small><span>返回完整目录</span></a>')
 meta='正文待补齐' if c.get('missing') else f'{c["characters"]:,} 字 · 约 {math.ceil(c["characters"]/500)} 分钟'
 write(Path(f'read/{n}/index.html'),page(label(n)+' '+c['title']+' · 未来之链',f'''<div class="reader-shell"><header class="reader-bar"><a class="brand" href="{BASE}">未来之链</a><nav><a href="{BASE}#volume-{c['volume']}">章节目录</a><a href="#reviews">读者留言</a><a href="{CLOUD}/account">登录</a></nav></header><main class="reader-main"><div class="reader-breadcrumb"><a href="{BASE}">三部曲</a><span>/</span><a href="{BASE}#volume-{c['volume']}">{vol[1]}</a><span>/</span><span>{label(n)}</span></div><header class="chapter-heading"><p class="eyebrow">{label(n)} · 第{['一','二','三'][c['volume']-1]}部</p><h1>{e(c['title'])}</h1><p class="story-time">{e(c['timeline'])}</p><div class="chapter-meta"><span>{meta}</span><a href="#chapter-text">阅读正文</a><a href="#chapter-art">本章配图</a></div></header><div class="reading-layout"><article class="chapter-prose" id="chapter-text">{text}</article><aside class="chapter-art" id="chapter-art"><p class="eyebrow">本章配图</p>{art}</aside></div><nav class="chapter-navigation">{nav}</nav><section class="reviews" id="reviews"><p class="eyebrow">READER VOICES</p><h2>读者留言与评价</h2><div class="github-discussion"><p>关于这一章，你看见了怎样的未来？</p><p>评分与留言统一保存在互动站。点击下面的按钮，进入本章留言区，登录后即可参与。</p><a class="primary" href="{CLOUD}/read/{n}#reviews">查看本章留言与评分</a></div></section></main><footer class="reader-foot"><a href="{BASE}">未来之链 · Sun Zhen</a><a href="#">回到章首</a></footer></div>'''))
write(Path('.nojekyll'),'')
write(Path('404.html'),page('页面未找到 · 未来之链',f'<main class="account-page"><section class="account-card"><h1>这一页暂时不存在</h1><a class="primary" href="{BASE}#catalog">返回完整目录</a></section></main>'))
print(f'Generated {len(chapters)} chapter pages and homepage.')
