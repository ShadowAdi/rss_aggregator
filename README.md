
```markdown
# 🌍 RSS News Aggregator

A Python-based news aggregator that fetches headlines from various country-specific RSS feeds, stores them in a local database, and exports them to a JSON file. The application is built using a modular approach—each component handles a distinct responsibility, improving maintainability and readability.


## 📦 Features

- Fetches news from country-specific RSS feeds.
- Deduplicates and stores news in a local SQLite database.
- Exports structured news data to a JSON file.
- Logs every major action for easy debugging.
- Flask API to serve the news via endpoints.



```
## 🗂️ Folder Structure
```plaintext
rss_aggregator/
├── app.py             # Flask API 
├── main.py            # Entry script to fetch and save news
├── controllers.py     # Function For API
├── country_rss.py     # Stores country-wise RSS feed URLs
├── DB_Connect.py      # Handles SQLite database operations
├── Json_saver.py      # Saves fetched news to a JSON file
├── logger.py          # Custom logging setup
├── utils.py           # Utility functions (e.g., language detection, feed accessible)
├── news.json          # ✅ Sample output file (as required)
├── requirements.txt   # Required dependencies
├── logs/              # Here You Can Logs for info and error
└── README.md          # 📖 You're reading this
```

> ✅ **Modular Codebase**:  
> Unlike dumping everything into a single script, the logic is split across multiple files based on functionality (fetching, saving, logging, API, etc.), making it clean and modular.

---

## ⚙️ Requirements

- Python 3.7+
- Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

> 🔁 This will fetch, deduplicate, and store news data.

### Step-by-step:

1. Clone the project or download the files.

2. (Optional but recommended) Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Run the main script:

```bash
python main.py
```

5. Output:
   - News saved in SQLite DB: `news.db`
   - News exported to JSON file: `news.json`

---

## 🌐 Optional: Run the Flask API

To serve the news via an API:

```bash
python app.py
```

Then visit:

- `http://localhost:5000/` – Home
- `http://localhost:5000/news` – All news
- `http://localhost:5000/news/<country>` – News filtered by country (e.g., `/news/us`)

---

## 📄 Sample Output

Your exported news data will be stored in:

```
news.json
```

Each entry will contain:

```json
{
  "title": "Example Headline",
  "link": "https://example.com/news",
  "published": "2025-05-21",
  "summary": "Short summary of the article",
  "country": "usa",
  "source":"BBC",
  "id":1,
  "language":"English"
}
```

---

## 🧠 Author Notes

- Clean code using a modular file structure.
- Easy to extend with new feeds or export formats.
- Suitable for cron jobs or scheduled tasks (e.g., using `schedule` or `cron`).

