# usage: python3 day5_2_sloooooow.py < testinput5.py
import sys
import re

_, seedranges = input().split(': ')
seedranges = re.findall(r'\d+ \d+', seedranges)
seedranges = [range(*((lambda x, y : (x, x + y))(*map(int, s.split()))))
              for s in seedranges]

seed_to_soil = {}
soil_to_fert = {}
fert_to_water = {}
water_to_light = {}
light_to_temp = {}
temp_to_hum = {}
hum_to_loc = {}
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
        m[(src, l)] = dst

locations = []
for seedrange in seedranges:
    for s in seedrange:
        loc = s
        for m in maps:
            for (src, l) in m:
                if loc in range(src, src + l):
                    loc = m[(src, l)] + loc - src
                    break
        locations.append(loc)
print(min(locations))
