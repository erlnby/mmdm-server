import numpy as np
from scipy.optimize import minimize
from sympy import sympify, lambdify, symbols, Eq, solve

from .models import *


def solve3(task_in: Task3In):
    p, q, I = task_in.p, task_in.q, task_in.i
    x0 = task_in.x0
    b = sympify(task_in.u)

    l = lambdify(symbols('x y'), b)

    def constraint1(x):
        return I - p * x[0] - q * x[1]

    con1 = {'type': 'ineq', 'fun': constraint1}
    constraints = con1
    r = minimize(lambda args: -l(*args), x0, method='SLSQP', constraints=constraints)
    u = -r.fun

    N = 100
    x = np.outer(np.linspace(-100, 100, N), np.ones(N))
    y = x.copy().T
    z = np.zeros((N, N))

    ox = np.linspace(-100, 100, N)
    oy = (I - ox * p) / q
    oz = np.zeros(N)

    for i in range(N):
        oz[i] = l(ox[i], oy[i])
        for j in range(N):
            z[i, j] = l(x[i, j], y[i, j])

    mask = (oy > -100) & (oy < 100)
    ox = ox[mask]
    oy = oy[mask]
    oz = oz[mask]

    eq = Eq(b, u)
    solutions = solve(eq, 'y')

    qx = []
    qy = []
    qz = []

    for s in solutions:
        ll = lambdify('x', s)
        for i in np.linspace(-100, 100, N):
            qx.append(i)
            qy.append(ll(i))
            qz.append(u)

    qx = np.array(qx)
    qy = np.array(qy)
    qz = np.array(qz)

    mask = (qy > -100) & (qy < 100)
    qx = qx[mask]
    qy = qy[mask]
    qz = qz[mask]

    return Task3Out(
        u=u,
        x=r.x[0],
        y=r.x[1],
        xs=x.tolist(),
        ys=y.tolist(),
        zs=np.nan_to_num(z).tolist(),
        ox=ox.tolist(),
        oy=oy.tolist(),
        oz=np.nan_to_num(oz).tolist(),
        qx=qx.tolist(),
        qy=np.nan_to_num(qy).tolist(),
        qz=qz.tolist(),
    )
