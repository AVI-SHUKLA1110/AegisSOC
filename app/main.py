from fastapi import FastAPI

app = FastAPI(
    title="AegisSOC",
    description="Agentic Security Operations Platform",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {
        "project": "AegisSOC",
        "status": "running",
        "version": "0.1.0"
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}