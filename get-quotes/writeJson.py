import json
import os

def write_to_json(quote_dics):
    assert type(quote_dics) == list and len(quote_dics) >= 1

    with open("quotes.json", 'w') as f:
        json.dump([], f)
    with open("quotes.json", 'w') as f:
        json.dump(quote_dics, f)
