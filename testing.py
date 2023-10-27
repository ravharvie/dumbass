from fastapi import FastAPI

import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get ("/{username}")
async def get_data (username: str):
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69'
    })
    resp = session.get(f"https://classicwowarmory.com/character/us/defias-pillager/{username}")
    soup = BeautifulSoup(resp.text, "html.parser")
    data = {
     "level" : soup.select_one("span.bold").text,
    }

    return{"results": data}