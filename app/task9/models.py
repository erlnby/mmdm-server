from typing import List

from pydantic import BaseModel


class ClearStrategy(BaseModel):
    value: float
    index: int


class MixedStrategy(BaseModel):
    value: float
    weights: List[float]


class Task9In(BaseModel):
    a: List[List[float]]


class Task9Out(BaseModel):
    clear_a: ClearStrategy
    clear_b: ClearStrategy
    mixed_a: MixedStrategy
