import nashpy as nash
import numpy as np
from scipy.optimize import linprog

from .models import Task8In, Task8Out


def solve8(task_in: Task8In):
    A = np.array(task_in.m)
    game = nash.Game(A)
    x, y = list(game.support_enumeration())[0]

    c = [-1, -1, -1]
    b = [1, 1, 1]

    res = linprog(c, A_ub=A, b_ub=b)
    v = 1 / res.x.sum()

    x = x.tolist()
    y = y.tolist()

    return Task8Out(
        x=x,
        y=y,
        v=v
    )
