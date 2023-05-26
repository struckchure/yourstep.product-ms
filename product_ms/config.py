import os

import dotenv

dotenv.load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY", "keep-it-secret")
DEBUG = int(os.environ.get("DEBUG", 1))
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(" ")

CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS", "").split(" ")
