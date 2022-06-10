from typing import List, Dict

from pydantic import BaseModel


class Task2VariablesIn(BaseModel):
    qs: List[str]
    c: str


class Task2SolveIn(Task2VariablesIn):
    qs: List[str]
    c: str
    vars: Dict[str, float]


class Task2VariablesOut(BaseModel):
    vars: List[str]


class Task2SolveOut(BaseModel):
    v: List[float]
    p: float
    qs: List[float]
    x: List[List[float]]
    y: List[List[float]]
    z: List[List[float]]
