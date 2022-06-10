import numpy as np
from scipy.optimize import linprog

from .models import Task11In, Task11Out, ClearStrategy, MixedStrategy


def solve11(task_in: Task11In):
    a = np.array(task_in.m)
    w = np.array(task_in.w)

    n = 4

    w1 = np.ones(n) / n
    laplace = ClearStrategy(
        value=a.dot(w1).max(),
        index=a.dot(w1).argmax(),
    )

    bayes = ClearStrategy(
        value=a.dot(w).max(),
        index=a.dot(w).argmax(),
    )

    A = a * w
    A = A.T

    germeier_clear = ClearStrategy(
        value=A.min(axis=0).max(),
        index=A.min(axis=0).argmax()
    )

    c = np.array([1, 1, 1, 1])
    b = np.array([1, 1, 1, 1])

    res = linprog(c, A_ub=-A, b_ub=-b)
    v = 1 / res.x.sum()
    p = res.x / res.x.sum()

    germeier_mixed = MixedStrategy(
        value=v,
        weights=p.tolist()
    )

    return Task11Out(
        laplace=laplace,
        bayes=bayes,
        germeier_clear=germeier_clear,
        germeier_mixed=germeier_mixed
    )
