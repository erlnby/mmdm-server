from typing import List

from pydantic import BaseModel


class ClearStrategy(BaseModel):
    value: float
    index: int


class Task12In(BaseModel):
    m: List[List[float]]


class Task12Out(BaseModel):
    pessimistic: ClearStrategy
    optimistic: ClearStrategy
    wald: ClearStrategy

    hurwitz_matrix: List[List[float]]
    hurwitz_steps: List[float]
    hurwitz_peaks: List[float]
    hurwitz_indices: List[float]

    savage: ClearStrategy
