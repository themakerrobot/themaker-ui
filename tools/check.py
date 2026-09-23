# -*- coding: utf-8 -*-
"""킷이 깨진 채 올라가지 않게 보는 검사.

  1. themaker-ui.css 의 중괄호 짝이 맞는가
  2. var(--토큰) 이 전부 :root 에 정의돼 있는가 (오타 잡기)
  3. preview.html 이 가리키는 파일이 실제로 있는가

문법 파서를 새로 만들지 않는다 — 실수로 자주 나는 것만 본다.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
fails = []


def check_css():
    css = (ROOT / 'themaker-ui.css').read_text(encoding='utf-8')
    body = re.sub(r'/\*.*?\*/', '', css, flags=re.S)

    opens, closes = body.count('{'), body.count('}')
    if opens != closes:
        fails.append(f'themaker-ui.css: 중괄호 짝이 안 맞습니다 ({{ {opens}개, }} {closes}개)')

    root = re.search(r':root\s*\{(.*?)\}', body, re.S)
    if not root:
        fails.append('themaker-ui.css: :root 블록을 찾지 못했습니다')
        return
    defined = set(re.findall(r'(--[\w-]+)\s*:', root.group(1)))
    used = set(re.findall(r'var\(\s*(--[\w-]+)', body))
    missing = sorted(used - defined)
    if missing:
        fails.append('themaker-ui.css: :root 에 없는 토큰을 씁니다 — ' + ', '.join(missing))

    unused = sorted(defined - used)
    if unused:
        print('참고: 아무 데서도 안 쓰는 토큰 —', ', '.join(unused))


def check_preview():
    html = (ROOT / 'preview.html').read_text(encoding='utf-8')
    for href in re.findall(r'(?:href|src)="([^"#]+)"', html):
        if href.startswith(('http', 'data:', '/')):
            continue
        if not (ROOT / href).exists():
            fails.append(f'preview.html: {href} 가 없습니다')


check_css()
check_preview()

if fails:
    print('\n'.join('  ✗ ' + f for f in fails))
    sys.exit(1)
print('킷 검사 통과')
