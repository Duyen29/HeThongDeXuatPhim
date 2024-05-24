from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

API_KEY = "92e37327850cc5fd6aeb2d8c847c7e7e"
BASE_URL = "https://api.themoviedb.org/3"

@app.get("/movie/{movie_id}")
async def get_movie(movie_id: int):
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Movie not found")

@app.get("/search")
async def search_movies(query: str):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Search failed")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)