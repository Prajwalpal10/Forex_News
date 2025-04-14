from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/news")
def get_news():
    url = "https://www.jblanked.com/news/api/mql5/calendar/today/"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key 8A5puVeD",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(status_code=response.status_code, detail=str(http_err))
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
