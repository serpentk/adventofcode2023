from collections import OrderedDict
import re

def get_hash(item):
    si = 0
    for c in item:
        si = ((si + ord(c)) * 17) % 256
    return si


boxes = {}
for item in input().strip().split(','):
    label, rest = re.split(r'[-=]', item)
    box = get_hash(label)
    if box not in boxes:
        boxes[box] = OrderedDict()
    if rest:
        boxes[box][label] = int(rest)
    elif label in boxes[box]:
        del boxes[box][label]

s = 0
for b in range(256):
    if b not in boxes: continue
    for i, label in enumerate(boxes[b]):
       s += (b + 1) * (i + 1) * boxes[b][label] 
print(s)
