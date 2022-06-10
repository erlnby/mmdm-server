import numpy as np
from scipy.optimize import linprog

from .models import Task9In, Task9Out, ClearStrategy, MixedStrategy


def solve9(task_in: Task9In):
    A = np.array(task_in.a).T

    clear_a = ClearStrategy(
        value=A.min(axis=0).max(),
        index=A.min(axis=0).argmax()
    )

    clear_b = ClearStrategy(
        value=A.max(axis=1).min(),
        index=A.max(axis=1).argmin()
    )

    c = np.array([1, 1, 1])
    b = np.array([1, 1, 1])

    res = linprog(c, A_ub=-A, b_ub=-b)
    p = res.x / res.x.sum()
    v = 1 / res.x.sum()

    mixed_a = MixedStrategy(
        value=v,
        weights=p.tolist()
    )

    return Task9Out(
        clear_a=clear_a,
        clear_b=clear_b,
        mixed_a=mixed_a
    )
