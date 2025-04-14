from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/news")
def get_filtered_news(
    strength: Optional[str] = Query(None, description="Filter by data strength (e.g., strong, medium)"),
    currency: Optional[str] = Query(None, description="Filter by currency (e.g., USD, EUR)"),
    date: Optional[str] = Query(None, description="Filter by date string (YYYY.MM.DD)")
):
    url = "https://www.jblanked.com/news/api/forex-factory/calendar/today/"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key 8A5puVeD",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        filtered = []
        for item in data:
            item_strength = item.get("Strength", "").lower()
            item_currency = item.get("Currency", "").upper()
            item_date = item.get("Date", "").split(" ")[0]  # e.g., "2024.02.08"

            if strength and strength.lower() not in item_strength:
                continue
            if currency and currency.upper() != item_currency:
                continue
            if date and date != item_date:
                continue

            filtered.append(item)

        return filtered

    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(status_code=response.status_code, detail=str(http_err))
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
