from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse

from app.api.endpoints import tasks, users
from app.api.middleware.middleware import logging_middleware, logger
from app.core.security import get_user_by_token
from app.db.database import Base, engine

app = FastAPI()


app.include_router(tasks.router, prefix="/api/v1", tags=["Tasks"], dependencies=[Depends(get_user_by_token)])
app.include_router(users.router, prefix="/api/v1", tags=["Users"])
app.middleware("http")(logging_middleware)


@app.on_event("startup")
def startup_db():
    Base.metadata.create_all(bind=engine)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("Alarm! Global exception!")
    return JSONResponse(
        status_code=500,
        content={"error": "O-o-o-ps! Internal server error"}
    )


@app.get("/")
def read_root():
    return {"message": "Welcome to the Real-Time Task Manager API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
