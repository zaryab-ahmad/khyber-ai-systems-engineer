from fastapi import FastAPI

# 1. Initialize the application
app = FastAPI()

# 2. Define a GET endpoint (Root/Home)
@app.get("/")
def read_root():
    return {"message": "AI Service Online", "version": "1.0.0"}

# 3. Define a GET endpoint with a parameter
@app.get("/status/{system_id}")
def get_status(system_id: str):
    return {"id": system_id, "health": "excellent", "memory_usage": "low"}
