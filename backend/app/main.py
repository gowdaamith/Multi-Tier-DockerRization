from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import get_connection
app = FastAPI(title="Employee Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
@app.get("/employees")
def get_employees():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, name, salary FROM employee"
    )

    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return employees
