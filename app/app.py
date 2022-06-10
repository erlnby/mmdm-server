from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.task1 import calc
from app.task1.models import Task1In, Task1Out
from app.task10 import solve10, Task10In, Task10Out
from app.task11 import solve11, Task11In, Task11Out
from app.task12 import solve12, Task12In, Task12Out
from app.task2.calc import get_variables, solve2
from app.task2.models import Task2VariablesIn, Task2SolveIn, Task2VariablesOut, Task2SolveOut
from app.task3.calc import solve3
from app.task3.models import Task3In, Task3Out
from app.task4.calc import solve4
from app.task4.models import Task4In, Task4Out
from app.task5.calc import solve5
from app.task5.models import Task5In, Task5Out
from app.task6 import solve6, Task6In, Task6Out
from app.task7 import solve7, Task7In, Task7Out
from app.task8 import solve8, Task8In, Task8Out
from app.task9 import solve9, Task9In, Task9Out

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/task1", response_model=Task1Out)
async def task1(task_in: Task1In):
    return calc.calc(task_in)


@app.post("/task2/variables", response_model=Task2VariablesOut)
async def task2_variables(task_in: Task2VariablesIn):
    return get_variables(task_in)


@app.post("/task2/solve", response_model=Task2SolveOut)
async def task2_solve(task_in: Task2SolveIn):
    return solve2(task_in)


@app.post("/task3", response_model=Task3Out)
async def task3(task_in: Task3In):
    return solve3(task_in)


@app.post("/task4", response_model=Task4Out)
async def task4(task_in: Task4In):
    return solve4(task_in)


@app.post("/task5", response_model=Task5Out)
async def task5(task_in: Task5In):
    return solve5(task_in)


@app.post("/task6", response_model=Task6Out)
async def task6(task_in: Task6In):
    return solve6(task_in)


@app.post("/task7", response_model=Task7Out)
async def task7(task_in: Task7In):
    return solve7(task_in)


@app.post("/task8", response_model=Task8Out)
async def task8(task_in: Task8In):
    return solve8(task_in)


@app.post("/task9", response_model=Task9Out)
async def task9(task_in: Task9In):
    return solve9(task_in)


@app.post("/task10", response_model=Task10Out)
async def task10(task_in: Task10In):
    return solve10(task_in)


@app.post("/task11", response_model=Task11Out)
async def task11(task_in: Task11In):
    return solve11(task_in)


@app.post("/task12", response_model=Task12Out)
async def task12(task_in: Task12In):
    return solve12(task_in)
