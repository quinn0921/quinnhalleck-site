#!/usr/bin/env python3
"""Build /<slug>/breakdown/ for every film in breakdowns.json: the stable 'Watch how I made this' link used in
YouTube descriptions (Quinn 2026-11-09). Before `live` it shows the poster and the drop date; after, it plays
assets/video/<slug>-breakdown.mp4 (final over previs). Run by stamp.sh."""
import json, os, datetime
B = json.load(open('breakdowns.json'))
T = open('breakdown.tpl.html').read()
for sl, b in B.items():
    live = b.get('live')
    when = datetime.datetime.fromisoformat(live).strftime('%B %-d') if live else ''
    h = (T.replace('{{slug}}', sl).replace('{{title}}', b['title']).replace('{{show}}', b.get('show', ''))
          .replace('{{live}}', live or '').replace('{{when}}', when))
    os.makedirs(f'{sl}/breakdown', exist_ok=True); open(f'{sl}/breakdown/index.html', 'w').write(h)
print('built', len(B), 'breakdown pages')
