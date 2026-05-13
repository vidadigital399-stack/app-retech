from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    app_name: str = "Retech Control API"
    secret_key: str = os.getenv("SECRET_KEY", "change-me")
    database_url: str = os.getenv("DATABASE_URL", "postgresql+psycopg2://retec:retec@db:5432/retec")

settings = Settings()
