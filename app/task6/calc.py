import numpy as np
from scipy.optimize import linprog

from .models import Task6In, Task6Out


def solve6(task_in: Task6In):
    a_ = task_in.a
    b_ = task_in.b
    c_ = task_in.c

    A = np.array([
        [1, 3, a_],
        [6, 5, 2],
        [-1, 0, 0],
        [0, -1, 0],
        [0, 0, -1],
    ])

    b = np.array([3000, 3320, 0, 0, 0])

    c = np.array([6 * b_ + 12, 5 * b_ + 22, c_])

    res = linprog(-c, A_ub=A, b_ub=b)
    x = res.x.tolist()
    f = -res.fun

    return Task6Out(
        x=x,
        f=f
    )
