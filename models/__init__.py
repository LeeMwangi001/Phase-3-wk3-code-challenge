# models/connection.py
import sqlite3
import os

DATABASE_NAME = 'database.db'
DATABASE_PATH = os.path.join(os.path.dirname(__file__), DATABASE_NAME)

CONN = sqlite3.connect(DATABASE_PATH)
CURSOR = CONN.cursor()
