# usage: python3 day5_2.py < testinput5.py
import sys
import re

_, seedranges = input().split(': ')
seedranges = re.findall(r'\d+ \d+', seedranges)
seedranges = [ tuple(map(int, s.split())) for s in seedranges ]
seedranges.sort()

seed_to_soil = []
soil_to_fert = []
fert_to_water = []
water_to_light = []
light_to_temp = []
temp_to_hum = []
hum_to_loc = []
input()

maps = (seed_to_soil,
        soil_to_fert,
        fert_to_water,
        water_to_light,
        light_to_temp,
        temp_to_hum,
        hum_to_loc)
for m in maps:
    input()
    for line in sys.stdin:
        if len(line) < 2:
            break
        dst, src, l = [int(x) for x in line.split()]
        m.append((src, l, dst))
    m.sort()

locations = []
ranges = seedranges
for m in maps:
    resranges = []
    for s, l in ranges:
        filtered = [(src, lm, dst)
                    for src, lm, dst in m
                    if src < s + l and src + lm > s]
        prev = s
        for src, lm, dst in filtered:
            newstart = max(src, s)
            if prev < newstart:
                resranges.append((prev, newstart - prev))
            newl = min(s + l, src + lm) - newstart
            resranges.append((dst + newstart - src, newl))
            prev = newstart + newl

        if s + l > prev:
            resranges.append((prev, s + l - prev))

    ranges = resranges

print(min([x[0] for x in ranges]))
