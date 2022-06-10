from typing import List

from pydantic import BaseModel


class Task4In(BaseModel):
    q: str
    A: float
    i: float
    a: List[float]
    w: List[float]
    x0: List[float]


class Task4Out(BaseModel):
    q: float
    x: float
    y: float
    xs: List[List[float]]
    ys: List[List[float]]
    zs: List[List[float]]
    ox: List[float]
    oy: List[float]
    oz: List[float]
    qx: List[float]
    qy: List[float]
    qz: List[float]
