import sys

def check_rows(pattern):
    n = len(pattern)
    for i in range(n - 1):
        size = min(i + 1, n - i - 1)
        if all([pattern[i - j] == pattern[i + j + 1]
                for j in range(0, size)]):
            return (i + 1) * 100
    return 0

def check_columns(pattern):
    n = len(pattern[0])
    for i in range(n - 1):
        size = min(i + 1, n - i - 1)
        if all([pattern[k][i - j] == pattern[k][i + j + 1]
                for j in range(0, size)
                for k in range(len(pattern))]):
            return i + 1
    return 0

def check_pattern(pattern):
    return check_rows(pattern) + check_columns(pattern)
    

pattern = []
s = 0
for line in sys.stdin:
    row = line.strip()
    if row:
        pattern.append(row)
        continue
    s += check_pattern(pattern)
    pattern = []
s += check_pattern(pattern)
print(s)
