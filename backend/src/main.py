from fastapi import FastAPI
from .core.config import settings
from .api.routes import tasks_router, auth_router

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Include API routes
app.include_router(tasks_router, prefix="/api/{user_id}", tags=["tasks"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Add exception handlers if needed
# from fastapi.exceptions import RequestValidationError
# from starlette.exceptions import HTTPException as StarletteHTTPException