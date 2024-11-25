from fastapi import FastAPI
from app.routers import blogs, users

app = FastAPI()

# Include Routers
app.include_router(blogs.router, prefix="/blogs", tags=["Blogs"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Welcome to the API"}
