from fastapi import FastAPI

from router.client import clientRouter
from router.coach import coachRouter

app = FastAPI()

app.include_router(clientRouter, prefix="/client", tags=["clients"])
app.include_router(coachRouter, prefix="/coach", tags=["coach"])