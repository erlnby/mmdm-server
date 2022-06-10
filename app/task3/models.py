from typing import List

from pydantic import BaseModel


class Task3In(BaseModel):
    u: str
    p: float
    q: float
    i: float
    x0: List[float]


class Task3Out(BaseModel):
    u: float
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
