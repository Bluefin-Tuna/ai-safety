import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(".env"))

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")