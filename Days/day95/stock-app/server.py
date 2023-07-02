from flask import Flask
import requests
from config import Config

app = Flask(__name__)


def fetch_price(ticker):
    params={'access_key': Config.API_KEY}
    print(Config.API_URL.format(ticker=ticker))
    data = requests.get(Config.API_URL.format(ticker=ticker.lower()), params).json()
    return float(data['price'])
    

@app.route('/stock/<ticker>')
def stock(ticker):
    price = fetch_price(ticker)
    return f"The price of {ticker} is ${price: .2f}"


@app.route('/')
def home_page():
    return 'Try /stock/APPL'


if __name__ == "__main__":
    
    with app.app_context():
        app.run(debug=True)

