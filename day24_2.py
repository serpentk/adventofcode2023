import sys
from sympy import Matrix, linsolve, symbols

data = []
for line in sys.stdin:
    position, vel = line.strip().split(' @ ')
    data.append([int(x) for x in position.split(', ') + vel.split(', ')])

a = []
b = []

a0, b0, c0, u0, v0, w0 = data[0]
for i in range(1, 3):
    a1, b1, c1, u1, v1, w1 = data[i]
    a.extend([[v1 - v0, u0 - u1, 0, b0 - b1, a1 - a0, 0],
              [0, w1 - w0, v0 - v1, 0, c0 - c1, b1 - b0],
              [w1 - w0, 0, u0 - u1, c0 - c1, 0, a1 - a0]
              ])
    b.extend([u0 *b0 - v0 * a0 - u1 * b1 + v1 * a1,
              v0 *c0 - w0 * b0 - v1 * c1 + w1 * b1,
              u0 *c0 - w0 * a0 - u1 * c1 + w1 * a1])

A = Matrix(a)
B = Matrix(b)
x, y, z, u, v, w = symbols("x, y, z, u, v, w")

for res in linsolve((A, b), [x, y, z, u, v, w]):
    print(res[0] + res[1] + res[2])
                   
