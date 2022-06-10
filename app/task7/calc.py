import numpy as np
from scipy.optimize import linprog

from .models import Task7In, Task7Out


def solve7(task_in: Task7In):
    demand = task_in.a
    capacity = task_in.b
    cost = np.array(task_in.c)

    LANES = len(demand)
    CARRIERS = len(capacity)

    A_eq = np.zeros(LANES * CARRIERS * LANES).reshape(LANES, LANES * CARRIERS)
    # Constraint for each lane, sum over the available carriers
    for l in range(LANES):
        for var in range(l * CARRIERS, l * CARRIERS + CARRIERS):
            A_eq[l, var] = 1

    A_ub = np.zeros(CARRIERS * LANES * CARRIERS).reshape(CARRIERS, LANES * CARRIERS)
    # Constraint for each carrier, sum over the lanes
    for c in range(CARRIERS):
        for var in range(c, LANES * CARRIERS, CARRIERS):
            A_ub[c, var] = 1

    res = linprog(cost.flatten(), A_eq=A_eq, b_eq=demand, A_ub=A_ub, b_ub=capacity)
    x = res.x.reshape(cost.shape).tolist()
    f = res.fun

    return Task7Out(
        x=x,
        f=f
    )
