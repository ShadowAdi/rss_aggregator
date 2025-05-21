import feedparser
from country_rss import Country_Feeds
import sqlite3
from DB_Connect import DBConnect
from utils import is_feed_accessible, detect_language
from Json_saver import Json_Saver
from logger import logger
import schedule
import time

all_articles = []

conn, cursor = DBConnect()


def Scraping_Feed():
    for country, feeds in Country_Feeds.items():
        for feed_url in feeds:
            if not is_feed_accessible(feed_url):
                logger.warning(f"Skipping inaccessible feed: {feed_url}")
                continue
            try:
                feed = feedparser.parse(feed_url)
                if feed.bozo:
                    logger.warning(
                        f"Invalid feed data for {feed_url}: {feed.bozo_exception}"
                    )
                    continue

                source = feed.feed.get("title", "Unknown Source")
                logger.info(f"Processing feed: {feed_url} ({source})")

                for entry in feed.entries:
                    title = entry.get("title", "")
                    summary = (
                        entry.get("summary", "") or entry.get("description", "") or ""
                    )
                    published = (
                        entry.get("published", "") or entry.get("updated", "") or ""
                    )
                    link = entry.get("link", "")
                    language = detect_language(summary)

                    if not title or not link:
                        logger.warning(
                            f"Skipping entry with missing title or link in {feed_url}"
                        )
                        continue

                    news_item = {
                        "title": title,
                        "summary": summary,
                        "published": published,
                        "link": link,
                        "source": source,
                        "country": country,
                        "language": language,
                    }

                    try:
                        cursor.execute(
                            """
                            INSERT OR IGNORE INTO news (title, summary, published, link, source, country,language)
                            VALUES (?, ?, ?, ?, ?, ?,?)
                            """,
                            (
                                title,
                                summary,
                                published,
                                link,
                                source,
                                country,
                                language,
                            ),
                        )
                        if cursor.rowcount > 0:
                            all_articles.append(news_item)
                            logger.info(f"Added article: {title} from {country}")
                        else:
                            logger.info(
                                f"Skipped duplicate article: {title} from {country}"
                            )
                    except sqlite3.Error as e:
                        locals.error(f"Database insert error for {title}: {e}")
            except Exception as e:
                logger.exception(f"Error processing feed {feed_url}: {e}")

    try:
        conn.commit()
        logger.info(f"Inserted {len(all_articles)} new articles into database")
    except sqlite3.Error as e:
        logger.error(f"Database commit error: {e}")
    finally:
        conn.close()

    Json_Saver(all_articles=all_articles)


def job():
    logger.info("Starting scheduled scrape job...")
    Scraping_Feed()
    logger.info("Scrape job finished.")


if __name__ == "__main__":
    job()

    schedule.every(1).day.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
