from typing import List

from pydantic import BaseModel


class ClearStrategy(BaseModel):
    value: float
    index: int


class MixedStrategy(BaseModel):
    value: float
    weights: List[float]


class Task11In(BaseModel):
    m: List[List[float]]
    w: List[float]


class Task11Out(BaseModel):
    laplace: ClearStrategy
    bayes: ClearStrategy
    germeier_clear: ClearStrategy
    germeier_mixed: MixedStrategy
