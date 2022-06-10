import numpy as np
from scipy.optimize import minimize
from sympy import sympify, Symbol, lambdify

from .models import *


def get_variables(task_in: Task2VariablesIn):
    qs = map(sympify, task_in.qs)
    c = sympify(task_in.c)

    vars = set()

    for q in qs:
        vars.update(q.free_symbols)
    vars.update(c.free_symbols)

    named_vars = map(lambda v: v.name, vars)
    cleared_vars = list(filter(lambda v: not v.startswith(('q_', 'p_')), named_vars))
    sorted_vars = sorted(cleared_vars)

    return Task2VariablesOut(
        vars=sorted_vars
    )


def solve2(task_in: Task2SolveIn):
    qs = list(map(sympify, task_in.qs))
    c = sympify(task_in.c)
    symbols = []
    p = 0

    for i, q in enumerate(qs):
        p_ = Symbol(f'p_{i + 1}')
        c = c.subs({f'q_{i + 1}': q})
        p += p_ * q
        symbols.append(p_)

    p -= c
    p = p.subs(task_in.vars)

    f = lambdify(symbols, p)
    r = minimize(lambda args: -f(*args), np.zeros(len(symbols)))
    ps = dict(zip(symbols, r.x)) | task_in.vars

    N = 100
    x = np.outer(np.linspace(-100, 100, N), np.ones(N))
    y = x.copy().T

    z = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            z[i, j] = f(x[i, j], y[i, j])

    return Task2SolveOut(
        v=r.x.tolist(),
        qs=list(map(lambda q: q.subs(ps), qs)),
        p=f(*r.x),
        x=x.tolist(),
        y=y.tolist(),
        z=z.tolist()
    )
