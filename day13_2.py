import sys

def fix_rows(pattern):
    n = len(pattern)
    for i in range(n - 1):
        size = min(i + 1, n - i - 1)
        c = len([(j, k) for j in range(0, size)
                 for k in range(len(pattern[0]))
                 if pattern[i - j][k] != pattern[i + j + 1][k]
                 ])
        if c == 1:
            return (i + 1) * 100
    return 0

def fix_columns(pattern):
    n = len(pattern[0])
    for i in range(n - 1):
        size = min(i + 1, n - i - 1)
        c = len([(j, k) for j in range(0, size)
                 for k in range(len(pattern))
                 if pattern[k][i - j] != pattern[k][i + j + 1]
                 ])
        if c == 1:
            return i + 1
    return 0

def check_pattern(pattern):
    return check_rows(pattern) + check_columns(pattern)


def fix_pattern(pattern):
    return fix_rows(pattern) + fix_columns(pattern)


pattern = []
s = 0
for line in sys.stdin:
    row = line.strip()
    if row:
        pattern.append(row)
        continue
    s += fix_pattern(pattern)
    pattern = []
s += fix_pattern(pattern)
print(s)
