# -*- encoding: utf-8 -*-
import unicodecsv as csv
from collections import defaultdict

d = defaultdict(list)
n = 10000000
prev_yomi = None
for line in csv.reader(file('dict.csv'), encoding='utf-8'):
    word = line[0]
    yomi = line[-1]
    if len(yomi) < 5:
        continue
    if word[0] in "(#0123456789-$?":
        continue
    if yomi == prev_yomi: continue
    if yomi[-1] == u'ン': continue
    length = len(yomi)
    if length > 10: continue
    original_yomi  = yomi
    for a, b in zip(u"ガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポャュョァィゥェォ",
                    u"カキクケコサシスセソタチツテトハヒフヘホハヒフヘホヤユヨアイウエオ"):
        yomi = yomi.replace(a, b)

    if length > 7: length = 7
    d[(yomi[-1], length)].append((yomi, word, original_yomi))
    prev_yomi = yomi
    n -= 1
    if n == 0: break

prev_yomi = None
for k in sorted(d):
    print u"# {} {}".format(k[0], k[1])
    for yomi, word, original_yomi in sorted(d[k]):
        if yomi == prev_yomi: continue
        print u"{}\t{}".format(word, original_yomi)
        prev_yomi = yomi
