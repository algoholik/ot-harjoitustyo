import os
from dotenv import load_dotenv

dir_name = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dir_name, "..", ".env"))
except FileNotFoundError:
    print(f"File not found: {os.path.join(dir_name, '..', '.env')}")

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "monoa-db.sqlite3"
DATABASE_FILE_PATH = os.path.join(dir_name, "..", "data", DATABASE_FILENAME)