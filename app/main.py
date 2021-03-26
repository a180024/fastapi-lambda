from fastapi import FastAPI
from mangum import Mangum

from .routers import users

app = FastAPI(title="Mqtt Service")
app.include_router(users.router)

handler = Mangum(app)
