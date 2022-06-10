from typing import List

from pydantic import BaseModel


class Task6In(BaseModel):
    a: float
    b: float
    c: float


class Task6Out(BaseModel):
    x: List[float]
    f: float
