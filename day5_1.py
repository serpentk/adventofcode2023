# usage: python3 day5_1.py < testinput5.py
import sys

_, seeds = input().split(': ')
seeds = [int(s) for s in seeds.split()]

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
for s in seeds:
    loc = s
    for m in maps:
        for (src, l) in m:
            if loc in range(src, src + l):
                loc = m[(src, l)] + loc - src
                break
    locations.append(loc)
print(min(locations))
