from fastapi import FastAPI
import psycopg2
from nanoid import generate

app = FastAPI()

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
URL = "http://localhost:8000/"

def generate_alias():
    
    return generate(ALPHABET, size=16)


@app.get("/")
def index():
    return {"message": "Post the link to be shortened to /short/[link]"}

@app.post("/short/{link}")
def shorten(link: str):
    # save link to database
    # generate shortened alias for link
    # return shortened link
    