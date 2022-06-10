from typing import List

from pydantic import BaseModel


class Task1In(BaseModel):
    x: List[List[float]]
    y: List[float]
    y2: List[float]


class Task1Out(BaseModel):
    a: List[List[float]]
    x1: List[float]
    x2: List[float]
    xc: List[float]
    lambda_a: float
    p_a: List[float]
