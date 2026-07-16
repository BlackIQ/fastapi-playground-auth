# FastAPI
from fastapi import FastAPI

# Routers
from routers import auth, user

# The FastAPI Instance
app = FastAPI(
    title="Mahi Auth API",
    version="1.0.0",
    summary="A simple Backend as our fourth project to use APIs in ReactJs",
    description="",
    openapi_tags=[
        {"name": "Application", "description": "Application endpoints like root and ping"},
        {"name": "Authentication", "description": "Login, Register, Logout"},
        {"name": "User", "description": "User profile"},
    ]
)


@app.get("/", tags=["Application"])
async def root():
    return {"message": "Server is functioning"}


@app.get("/api", tags=["Application"])
async def api():
    return {"message": "Welcome to Mahi Todo List API"}


# Router
app.include_router(auth.router, prefix="/api")
app.include_router(user.router, prefix="/api")
