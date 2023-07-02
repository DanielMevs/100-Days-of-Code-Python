from urllib.request import urlopen
import certifi
import json
import os

key = os.environ.get("FINANCIAL_MODELING_API_KEY")
def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

url = (f"https://financialmodelingprep.com/api/v3/quote_short/apikey={key}")
print(get_jsonparsed_data(url))