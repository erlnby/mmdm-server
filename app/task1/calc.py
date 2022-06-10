import numpy as np

from .models import Task1In, Task1Out


def calc(task_in: Task1In) -> Task1Out:
    x = np.array(task_in.x)
    y = np.array(task_in.y)
    y2 = np.array(task_in.y2)

    n = x.shape[0]
    xx = x.sum(axis=1) + y
    e = np.eye(n)
    a = x / xx
    ea = e - a
    s = np.linalg.inv(ea)

    eig = np.linalg.eig(a)
    d = eig[0]
    p = eig[1]
    di = np.argmax(d)

    lambda_a = d[di]
    p_a = p[:, di]

    x2 = s.dot(y2)
    xc = x2 - (a * x2).sum(axis=0)

    return Task1Out(
        a=a.tolist(),
        x1=xx.tolist(),
        x2=x2.tolist(),
        xc=xc.tolist(),
        lambda_a=lambda_a,
        p_a=p_a.tolist(),
    )
