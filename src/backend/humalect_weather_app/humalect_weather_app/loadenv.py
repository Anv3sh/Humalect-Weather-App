import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

api_key = os.getenv("ACCUWEATHER_API_KEY")
base_url = os.getenv("ACCUWEATHER_BASE_URL")