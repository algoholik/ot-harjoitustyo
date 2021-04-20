'''
Configure environment variables
'''
import os
from dotenv import load_dotenv

DIR_NAME = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(DIR_NAME, "..", ".env"))
except FileNotFoundError:
    print(f"File not found: {os.path.join(DIR_NAME, '..', '.env')}")

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "monoa-db.sqlite3"
DATABASE_FILE_PATH = os.path.join(DIR_NAME, "..", "data", DATABASE_FILENAME)

SETTINGS_FILENAME = os.getenv("SETTINGS_FILENAME") or "monoa-settings.json"
SETTINGS_FILE_PATH = os.path.join(DIR_NAME, "..", "data", SETTINGS_FILENAME)
