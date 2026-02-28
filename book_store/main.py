from fastapi import FastAPI
from routes.book_routes import router as book_routes
from routes.author_routes import router as author_routes
from routes.customer_routes import router as customer_routes
from routes.order_routes import router as order_routes
from routes.return_routes import router as return_routes
from routes.journal_routes import router as journal_routes
from routes import preorder_routes
from routes import subscription_routes
from routes import event_routes

app = FastAPI()

app.include_router(book_routes)
app.include_router(author_routes)
app.include_router(customer_routes)
app.include_router(order_routes)
app.include_router(return_routes)
app.include_router(journal_routes)
app.include_router(preorder_routes.router)
app.include_router(subscription_routes.router)
app.include_router(event_routes.router)