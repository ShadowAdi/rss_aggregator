import sqlite3
from logger import logger 

DB_FILE = "news.db" 

def get_all_news():
    try:
        logger.info("Fetching all news from database")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT title, source, country, summary, link, language, published, id 
            FROM news
        """)
        rows = cursor.fetchall()
        conn.close()

        logger.info(f"Fetched {len(rows)} news articles.")
        return [
            {
                "title": row[0],
                "source": row[1],
                "country": row[2],
                "summary": row[3],
                "link": row[4],
                "language": row[5],
                "published": row[6],
                "id": row[7],
            }
            for row in rows
        ]
    except Exception as e:
        logger.exception("Failed to fetch all news")
        return []

def get_news_by_country(country):
    try:
        logger.info(f"Fetching news for country: {country}")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT title, source, country, summary, link, language, published, id 
            FROM news 
            WHERE LOWER(country) = LOWER(?)
        """, (country,))
        rows = cursor.fetchall()
        conn.close()

        logger.info(f"Fetched {len(rows)} news articles for country: {country}")
        return [
            {
                "title": row[0],
                "source": row[1],
                "country": row[2],
                "summary": row[3],
                "link": row[4],
                "language": row[5],
                "published": row[6],
                "id": row[7],
            }
            for row in rows
        ]
    except Exception as e:
        logger.exception(f"Failed to fetch news for country: {country}")
        return []
