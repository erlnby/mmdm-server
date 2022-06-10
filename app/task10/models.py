from typing import List

from pydantic import BaseModel


class ClearStrategy(BaseModel):
    value: float
    index: int


class MixedStrategy(BaseModel):
    value: float
    weights: List[float]


class Task10In(BaseModel):
    a: List[List[float]]
    b: List[List[float]]


class Task10Out(BaseModel):
    clear_a: ClearStrategy
    clear_b: ClearStrategy
    clear_value: float

    mixed_a: MixedStrategy
    mixed_b: MixedStrategy
    mixed_value: float
