from typing import List

from pydantic import BaseModel


class Line(BaseModel):
    xs: List[float]
    ys: List[float]


class Task5In(BaseModel):
    a: str
    b: str
    c: str


class Task5Out(BaseModel):
    lines: List[Line]
    solution: Line
    m: List[float]
    f: float
