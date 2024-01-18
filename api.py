from fastapi import FastAPI
import psycopg2
from nanoid import generate

app = FastAPI()

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
URL = "http://localhost:8000/"

def generate_alias():
    # possibly offer custom urls
    return generate(ALPHABET, size=16)


@app.get("/")
def index():
    return {"message": "Post the link to be shortened to /short/[link]"}

@app.post("/short/{link}")
def shorten(link: str):
    # generate shortened alias for link
    # save link to database alongside alias
    # return shortened link
    