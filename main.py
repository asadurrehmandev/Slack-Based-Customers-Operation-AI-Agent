from fastapi import FastAPI

from database import initialize_database

app = FastAPI()
initialize_database()
