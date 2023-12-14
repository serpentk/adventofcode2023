import sys


def move_north():
    for n in range(len(rocks)):
        for i in range(len(rocks[0])):
            if rocks[n][i] in ('#', '.'): continue
            dest = 0
            for j in range(n-1, -1, -1):
                if rocks[j][i] in ('O', '#'):
                    dest = j + 1
                    break
            rocks[n][i] = '.'
            rocks[dest][i] = 'O'

def move_west():
    for n in range(len(rocks[0])):
        for i in range(len(rocks)):
            if rocks[i][n] in ('#', '.'): continue
            dest = 0
            for j in range(n-1, -1, -1):
                if rocks[i][j] in ('O', '#'):
                    dest = j + 1
                    break
            rocks[i][n] = '.'
            rocks[i][dest] = 'O'

def move_east():
    for n in range(len(rocks[0]) - 1, -1, -1):
        for i in range(len(rocks)):
            if rocks[i][n] in ('#', '.'): continue
            dest = len(rocks[0]) - 1
            for j in range(n + 1, len(rocks[0])):
                if rocks[i][j] in ('O', '#'):
                    dest = j - 1
                    break
            rocks[i][n] = '.'
            rocks[i][dest] = 'O'

def move_south():
    for n in range(len(rocks) - 1, -1, -1):
        for i in range(len(rocks[0])):
            if rocks[n][i] in ('#', '.'): continue
            dest = len(rocks) - 1
            for j in range(n + 1, len(rocks)):
                if rocks[j][i] in ('O', '#'):
                    dest = j - 1
                    break
            rocks[n][i] = '.'
            rocks[dest][i] = 'O'

       
def cycle():
    move_north()
    move_west()
    move_south()
    move_east()


rocks = []

for n, line in enumerate(sys.stdin):
    rocks.append(list(line.strip()))

steps = {}
cycle_len = 0
cycle_start = 0
code = ''.join([''.join(row) for row in rocks])
for step in range(20000):
    cycle()
    code = ''.join([''.join(row) for row in rocks])

    if code in steps:
        cycle_len = step - steps[code][0]
        cycle_start = steps[code][0]
        print(step, steps[code])
        break
    s = 0
    for i in range(len(rocks)):
         s += len([x for x in rocks[i] if x == 'O']) * (len(rocks) - i)
    steps[code] = (step, s)
    
pos = (1000000000 - cycle_start) % cycle_len + cycle_start - 1
sums = {step: s for step, s in steps.values()}
print(sums[pos])
            
