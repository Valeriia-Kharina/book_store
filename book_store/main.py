from fastapi import FastAPI
from routes.book_routes import router as book_routes

app = FastAPI()

app.include_router(book_routes)