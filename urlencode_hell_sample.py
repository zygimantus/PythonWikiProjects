# Sample of mwparserfromhell when pywikibot is not used
import json
from urllib.parse import urlencode
from urllib.request import urlopen
import mwparserfromhell
API_URL = "https://lt.wikipedia.org/w/api.php"

def parse(title):
    data = {"action": "query", "prop": "revisions", "rvlimit": 1,
            "rvprop": "content", "format": "json", "titles": title}
    raw = urlopen(API_URL, urlencode(data).encode()).read()
    res = json.loads(raw)
    text = list(res["query"]["pages"].values())[0]["revisions"][0]["*"]
    return mwparserfromhell.parse(text)

text = parse('Europos parkas')
print(text)
