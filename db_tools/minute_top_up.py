import requests
import json

def complex_data_request(symbols):
    url = "https://api.twelvedata.com/complex_data?apikey=b410a081bcbe42bc8807dc30e1407ede"
    json_dict = {
        "symbols":  symbols,
        "intervals": ["1min"],
        "outputsize": 1,
        "methods": [
            "price",
        ]
    }
    json_data = json.dumps(json_dict)
    response = requests.post(
        url,
        data = json_data,
        headers = {'Content-Type': 'application/json'}
    )
    return(response.json()['data'])




