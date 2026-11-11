"""es/index.html から claude.ai アーティファクト用のページ本文を作る。

使い方: python3 es/tools/build-artifact.py <出力先.html>
アーティファクトは doctype/head/body を自動で付けるので、
<!--ARTIFACT-START--> から <!--ARTIFACT-END--> までを取り出し、
PWA用のタグ（manifest・アイコン・</head><body>）を取り除く。
"""
import re, sys, pathlib
src = (pathlib.Path(__file__).resolve().parent.parent / 'index.html').read_text(encoding='utf-8')
body = src.split('<!--ARTIFACT-START-->', 1)[1].split('<!--ARTIFACT-END-->', 1)[0]
drop = re.compile(r'^\s*(</head>|<body>|<link rel="(manifest|apple-touch-icon|icon)"|<meta name="(apple-mobile|theme-color))')
out = '\n'.join(l for l in body.strip('\n').split('\n') if not drop.match(l)) + '\n'
pathlib.Path(sys.argv[1]).write_text(out, encoding='utf-8')
print('wrote', sys.argv[1], len(out), 'bytes')
