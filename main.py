import os
from dotenv import load_dotenv

load_dotenv(".env")

api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")

print("API_KEY:", api_key)
print("DATABASE_URL:", database_url)
