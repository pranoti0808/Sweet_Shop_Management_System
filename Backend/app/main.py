from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth_routes, sweet_routes

app = FastAPI(title="Sweet Shop Management System")

# Enable CORS so frontend can access backend
origins = [
    "http://127.0.0.1:5500",  # your frontend URL
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # allow all HTTP methods (GET, POST, PUT, DELETE)
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_routes.router)
app.include_router(sweet_routes.router)

# Root endpoint (optional)
@app.get("/")
def root():
    return {"message": "Welcome to the Sweet Shop Management System"}
