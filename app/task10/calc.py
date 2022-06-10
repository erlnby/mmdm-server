import numpy as np
from scipy.optimize import minimize

from .models import Task10In, Task10Out, ClearStrategy, MixedStrategy


def solve10(task_in: Task10In):
    A = np.array(task_in.a)
    B = np.array(task_in.b)

    clear_a = ClearStrategy(
        value=A.max(axis=0).min(),
        index=A.max(axis=0).argmin()
    )

    clear_b = ClearStrategy(
        value=B.max(axis=1).min(),
        index=B.max(axis=1).argmin()
    )

    def l(x):
        p = x[:3]
        q = x[3:]

        As = p.dot(A).dot(q)
        Bs = p.dot(B).dot(q)

        return As.sum() + Bs.sum()

    def c1(x):
        p = x[:3]
        return p.sum() - 1

    def c2(x):
        q = x[3:]
        return q.sum() - 1

    def c3(x):
        p = x[:3]
        q = x[3:]

        Va = A.dot(q)
        As = p.dot(A).dot(q).sum()

        return As - Va

    def c4(x):
        p = x[:3]
        q = x[3:]

        Vb = p.dot(B)
        Bs = p.dot(B).dot(q).sum()

        return Bs - Vb

    constraints = [
        {'type': 'eq', 'fun': c1},
        {'type': 'eq', 'fun': c2},
        {'type': 'ineq', 'fun': c3},
        {'type': 'ineq', 'fun': c4},
    ]

    bounds = [
        (0, 1),
        (0, 1),
        (0, 1),
        (0, 1),
        (0, 1),
        (0, 1),
    ]

    x0 = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    solution = minimize(lambda x: -l(x), x0, method='SLSQP', constraints=constraints, bounds=bounds)

    a_w = solution.x[:3]
    b_w = solution.x[3:]

    a_v = a_w.dot(A).dot(b_w)
    b_v = a_w.dot(B).dot(b_w)

    mixed_a = MixedStrategy(
        value=a_v,
        weights=a_w.tolist()
    )

    mixed_b = MixedStrategy(
        value=b_v,
        weights=b_w.tolist()
    )

    return Task10Out(
        clear_a=clear_a,
        clear_b=clear_b,
        clear_value=clear_a.value + clear_b.value,

        mixed_a=mixed_a,
        mixed_b=mixed_b,
        mixed_value=mixed_a.value + mixed_b.value,
    )
