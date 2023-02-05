from flask import Flask, jsonify
from flask_cors import CORS
from scraper import scrape

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify(scrape())