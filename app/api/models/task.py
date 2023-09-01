from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str


class TaskUpdate(BaseModel):
    title: str
    description: str
    completed: bool


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
