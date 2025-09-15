from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from scraper import compare_products

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/compare/")
def compare(query: str = Query(...)):
    return {"results": compare_products(query)}