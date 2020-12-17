"""
Version: 2.0
Autor: jce2090
Date: 2020-12-17 23:09:22
LastEditors: Seven
LastEditTime: 2020-12-17 23:10:26
"""
import json
from urllib.request import urlopen
from urllib.parse import urlencode


params = dict(q="Sauages", format="json")
handle = urlopen("http://api.duckduckgo.com" + "?" + urlencode(params))
raw_text = handle.read().decode("uft8")
parsed = json.loads(raw_text)

results = parsed["RelatedTopics"]
for r in results:
    if "Text" in r:
        print(r["FirstUrl"] + "_" + r["Text"])
