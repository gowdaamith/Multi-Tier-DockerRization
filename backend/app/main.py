from fastapi import FastAPI

app = FastAPI(title="Employee Management API")


@app.get("/")
def root():
    return {
        "message": "Employee Management API",
        "version": "1.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": "1.0"
    }
