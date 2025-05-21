from flask import Flask, jsonify
from controllers import get_all_news,get_news_by_country
from logger import logger

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    logger.info("Testing Statement")
    return jsonify({"message": "Welcome To The News API"})


@app.route("/news", methods=['GET'])
def All_News():
    logger.info("To Get All News")
    data = get_all_news()
    return data


@app.route('/news/<country>', methods=['GET'])
def news_by_country(country):
    logger.info("To Get News Based on a country")
    data = get_news_by_country(country)
    if not data:
        return jsonify({"message": f"No news found for country '{country}'."}), 404
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)