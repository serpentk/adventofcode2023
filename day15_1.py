s = 0

for item in input().strip().split(','):
    si = 0
    for c in item:
        si = ((si + ord(c)) * 17) % 256
    s += si
print(s)
