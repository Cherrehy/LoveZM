import requests
import json

# 选用主流公开TVBox接口
source_list = [
    "https://fastly.jsdelivr.net/gh/liu673cn/box@main/m.json",
    "http://cdn.qiaoji8.com/tvbox.json",
    "http://xhztv.top/4k.json",
    "https://raw.kkgithub.com/xyq254245/xyqonlinerule/main/XYQTVBox.json"
]

final_data = {"sites": [], "lives": []}
key_set = set()

for url in source_list:
    try:
        response = requests.get(url, timeout=4, verify=False)
        data = response.json()
        # 合并点播站点并去重
        for site in data.get("sites", []):
            if site["key"] not in key_set:
                key_set.add(site["key"])
                final_data["sites"].append(site)
        # 合并直播源
        final_data["lives"].extend(data.get("lives", []))
    except Exception:
        continue

# 输出文件
with open("tv.json", "w", encoding="utf‑8") as f:
    json.dump(final_data, f, ensure_ascii=False)
