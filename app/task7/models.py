from typing import List

from pydantic import BaseModel


class Task7In(BaseModel):
    c: List[List[float]]
    a: List[float]
    b: List[float]


class Task7Out(BaseModel):
    x: List[List[float]]
    f: float
