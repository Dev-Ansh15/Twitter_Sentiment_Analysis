import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    BEARER_TOKEN = os.getenv("BEARER_TOKEN")

settings = Settings()