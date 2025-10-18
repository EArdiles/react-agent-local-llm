from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def handle_query(request: QueryRequest):
    query = request.query.lower()
    print("Received query:", query)
    if "laptop" in query:
        return {"response": 1400}
    else:
        return {"response": "Query not recognized"}
    
# run usin: uvicorn dummy_server:app --reload  