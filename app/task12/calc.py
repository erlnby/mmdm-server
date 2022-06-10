import numpy as np

from .models import Task12In, Task12Out, ClearStrategy


def solve12(task_in: Task12In):
    x = np.array(task_in.m)

    pessimistic = ClearStrategy(
        value=x.min(axis=1).min(),
        index=x.min(axis=1).argmin()
    )

    optimistic = ClearStrategy(
        value=x.max(axis=1).max(),
        index=x.max(axis=1).argmax()
    )

    wald = ClearStrategy(
        value=x.min(axis=1).max(),
        index=x.min(axis=1).argmax()
    )

    w = np.linspace(0.0, 1.0, num=11).reshape(1, -1)
    max_ = x.max(axis=1).reshape(1, -1).T
    min_ = x.min(axis=1).reshape(1, -1).T
    res = max_.dot(w) + min_.dot(1 - w)

    hurwitz_matrix = res.tolist()
    hurwitz_steps = w.flatten().tolist()
    hurwitz_peaks = res.max(axis=0).tolist()
    hurwitz_indices = res.argmax(axis=0).tolist()

    y = x.max(axis=0) - x

    savage = ClearStrategy(
        value=y.max(axis=1).min(),
        index=y.max(axis=1).argmin()
    )

    return Task12Out(
        pessimistic=pessimistic,
        optimistic=optimistic,
        wald=wald,
        savage=savage,

        hurwitz_matrix=hurwitz_matrix,
        hurwitz_steps=hurwitz_steps,
        hurwitz_peaks=hurwitz_peaks,
        hurwitz_indices=hurwitz_indices,
    )
