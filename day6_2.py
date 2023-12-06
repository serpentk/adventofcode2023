t = int(''.join(input()[11:].split()))
distance = int(''.join(input()[11:].split()))

def ways_count(t, d):
    for i in range(1, t):
        if i * (t - i) > d:
            return t + 1 - 2 * i
    return 0

print(ways_count(t, distance))
