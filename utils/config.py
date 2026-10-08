from os import getenv

from dotenv import load_dotenv

load_dotenv()

BASE_URL=getenv("BASE_URL")
EXISTING_USER_EMAIL=getenv("EXISTING_USER_EMAIL")
EXISTING_USER_PASSWORD=getenv("EXISTING_USER_PASSWORD")