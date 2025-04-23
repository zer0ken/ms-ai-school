import os
import secrets
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = secrets.token_urlsafe(64)

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = (
    f'postgresql+psycopg2://'
    f'{os.getenv("POSTGRES_USER", "postgres")}:'
    f'{os.getenv("POSTGRES_PASSWORD", "password")}@'
    f'{os.getenv("POSTGRES_HOST", "localhost")}:'
    f'{os.getenv("POSTGRES_PORT", "5432")}/'
    f'{os.getenv("POSTGRES_DB", "flask_basics")}'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
