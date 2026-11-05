#!/usr/bin/env python3
"""Build /<slug>/index.html for every film: a full copy of the site (no redirect)
with that film's share tags, so iMessage/Slack/etc. read the film's card.
Tags live in og.json. Run by stamp.sh."""
import json,re
idx=open('index.html').read()
og=json.load(open('og.json'))
head_old=re.search(r'<title>.*?<meta property="og:url"[^>]*>\n',idx,re.S).group(0)
for sl,lines in og.items():
    h=idx.replace(head_old,'<base href="/">\n'+'\n'.join(lines)+'\n',1)
    h=h.replace('<script src="data.js','<script>window.QH_START='+json.dumps(sl)+'</script>\n<script src="data.js',1)
    open(f'{sl}/index.html','w').write(h)
print('built',len(og),'film pages')
