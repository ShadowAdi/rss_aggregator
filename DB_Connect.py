import sqlite3
from logger import logger  

DB_FILE = "news.db"

def DBConnect():
    try:
        logger.info("Connecting to the database...")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS news 
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                summary TEXT,
                published TEXT,
                link TEXT UNIQUE,
                source TEXT,
                country TEXT,
                language TEXT
            )
            """
        )

        logger.info("Connected to the database and ensured table exists.")
        return conn, cursor

    except sqlite3.Error as e:
        logger.exception(f"Database connection failed: {e}")
        exit(1)
