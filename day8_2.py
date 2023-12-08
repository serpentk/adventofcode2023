import math
import sys

instructions = input().strip()
n = len(instructions)
input()

nodes = dict()
for line in sys.stdin:
    nodes[line[:3]] = {'L': line[7:10], 'R': line[12:15]}

locations = [n for n in nodes if n[-1] == 'A']
cycles = []

for i in range(len(locations)):
    step = 0
    path = dict()
    z = []
    while (locations[i], step % n) not in path:
        path[(locations[i], step % n)] = step
        if locations[i][-1] == 'Z':
            z.append(step)
        locations[i] = nodes[locations[i]][instructions[step % n]]
        step += 1
    cycle = step - path[(locations[i], step % n)]
    # What an unbelievable input!
    if not(len(z) == 1 and z[0] == cycle):
        print("Ooooops... It seems to be complicated...")
        break
    cycles.append(cycle)

if len(cycles) == len(locations):
    print(math.lcm(*cycles)) 
