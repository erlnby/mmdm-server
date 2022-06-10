from sympy import lambdify, sympify, solve
from scipy.optimize import linprog
import numpy as np

from .models import Task5In, Line, Task5Out


def my_solve(q):
    x0 = 0
    y1 = 0

    q = q.lhs - q.rhs
    q = solve(q, 'y')[0]

    x1 = solve(q, 'x')[0]

    f = lambdify('x', q)
    y0 = f(x0)

    return [float(x0), float(x1)], [float(y0), float(y1)]


def linsolve(a_, b_, c_):
    A = np.array([[-1, -(b_ - 3)], [-(c_ - 4), -1], [-3, -2], [-1, 0], [0, -1]])

    b = np.array([-b_, -c_, -11, 0, 0])

    c = np.array([a_, 1])

    res = linprog(c, A_ub=A, b_ub=b)

    q = sympify('a * x + y <= F').subs({'a': a_, 'F': res.fun})
    return *my_solve(q), res.x, res.fun


def solve5(task_in: Task5In):
    a = float(sympify(task_in.a))
    b = float(sympify(task_in.b))
    c = float(sympify(task_in.c))

    v = {
        'a': a,
        'b': b,
        'c': c
    }

    qs = [
        'x + (b - 3) * y >= b',
        '(c - 4) * x + y >= c',
        '3 * x + 2 * y >= 11',
    ]

    lines = []
    for q in qs:
        q_ = sympify(q).subs(v)
        xs, ys = my_solve(q_)
        lines.append(Line(xs=xs, ys=ys))

    xs, ys, m, f = linsolve(a, b, c)
    solution = Line(xs=xs, ys=ys)

    return Task5Out(
        lines=lines,
        solution=solution,
        m=m.tolist(),
        f=f
    )



