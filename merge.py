import requests
import json
import warnings
warnings.filterwarnings("ignore")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 仅保留全球可访问的CDN地址
source_list = [
    "https://fastly.jsdelivr.net/gh/liu673cn/box@main/m.json",
    "https://fastly.jsdelivr.net/gh/smiek/TVbox/main/tv.json"
]

final_data = {"sites": [], "lives": []}
key_set = set()
live_set = set()

for url in source_list:
    try:
        response = requests.get(url, timeout=10, verify=False, headers=headers)
        data = response.json()
        for site in data.get("sites", []):
            if site["key"] not in key_set:
                key_set.add(site["key"])
                final_data["sites"].append(site)
        for live in data.get("lives", []):
            live_url = live.get("url", "")
            if live_url and live_url not in live_set:
                live_set.add(live_url)
                final_data["lives"].append(live)
    except Exception as err:
        print(f"访问失败：{url}，错误信息：{str(err)}")

with open("tv.json", "w", encoding="utf-8") as f:
    json.dump(final_data, f, ensure_ascii=False)
with open("tv.json", "w", encoding="utf-8") as f:
    json.dump(final_data, f, ensure_ascii=False)
