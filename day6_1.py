times = list(map(int, input()[11:].split()))
distances = list(map(int, input()[11:].split()))
res = 1
for t, d in zip(times, distances):
    c = 0
    for i in range(1, t):
        if i * (t - i) > d:
            c = t + 1 - 2 * i
            break
    res *= c

print(res)
