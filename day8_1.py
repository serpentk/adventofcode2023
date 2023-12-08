import sys

instructions = input().strip()
n = len(instructions)
input()

nodes = dict()
for line in sys.stdin:
    nodes[line[:3]] = {'L': line[7:10], 'R': line[12:15]}

step = 0
location = 'AAA'
while location != 'ZZZ':
    location = nodes[location][instructions[step % n]]
    step += 1

print(step)
