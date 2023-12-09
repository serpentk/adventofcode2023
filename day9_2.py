import sys

def extrapolate(numbers):
    if all([x == 0 for x in numbers]):
        return 0
    return numbers[0] - extrapolate(
        [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)])

s = 0
for line in sys.stdin:
    s += extrapolate([int(x) for x in line.split()])

print(s)
