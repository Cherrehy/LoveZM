import requests
import json
import warnings
warnings.filterwarnings("ignore")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

source_list = [
    # 原有源
    "https://fastly.jsdelivr.net/gh/liu673cn/box@main/m.json",
    "http://cdn.qiaoji8.com/tvbox.json",
    "http://xhztv.top/4k.json",
    "https://raw.kkgithub.com/xyq254245/xyqonlinerule/main/XYQTVBox.json",
    # 新增稳定订阅源
    "https://api.caiji.cloud/api/v1/json/config",
    "https://tvbox.liumingye.cn/api.json",
    "https://fastly.jsdelivr.net/gh/smiek/TVbox/main/tv.json",
    "https://tvbox.caiji.cloud/ok.json",
    "http://api.rongyao.cloud/TVBox.json",
    "https://fastly.jsdelivr.net/gh/taksssss/TVBox/main/tv.json"
]

final_data = {"sites": [], "lives": []}
key_set = set()
live_set = set()

for url in source_list:
    try:
        response = requests.get(url, timeout=4, verify=False, headers=headers)
        data = response.json()
        # 点播站点去重
        for site in data.get("sites", []):
            if site["key"] not in key_set:
                key_set.add(site["key"])
                final_data["sites"].append(site)
        # 直播源按播放链接去重
        for live in data.get("lives", []):
            live_url = live.get("url", "")
            if live_url and live_url not in live_set:
                live_set.add(live_url)
                final_data["lives"].append(live)
    except Exception:
        continue

with open("tv.json", "w", encoding="utf-8") as f:
    json.dump(final_data, f, ensure_ascii=False)
