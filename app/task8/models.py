from typing import List

from pydantic import BaseModel


class Task8In(BaseModel):
    m: List[List[float]]


class Task8Out(BaseModel):
    x: List[float]
    y: List[float]
    v: float
