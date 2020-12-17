"""
Version: 2.0
Autor: jce2090
Date: 2020-12-17 23:17:02
LastEditors: Seven
LastEditTime: 2020-12-17 23:17:04
"""
import requests

params = dict(q="Sauages", format="json")
parased = requests.get("http://api.duckduckgo.com", params=params).json()

results = parased["RelatedTopics"]
for r in results:
    if "Text" in r:
        print(r["FirstURL"] + "-" + r["Text"])
