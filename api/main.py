from fastapi import FastAPI
from fastapi.responses import Response
import json
from pathlib import Path

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "Welcome to the Affordable Housing Scraper API"}

@app.get("/listings")
def get_listings():
    data_path = Path("scraper/data.json")
    if not data_path.exists():
        return {"error": "No data available. Please run the scraper first."}
    
    with data_path.open() as f:
        data = json.load(f)

    pretty_data = json.dumps(data, indent=2)
    return Response(content=pretty_data, media_type="application/json")