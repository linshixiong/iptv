# -*- coding:utf-8 -*-
import json
import re

if __name__ == "__main__":

    print("正在转换频道列表...")
    with open('channellist.json', 'r', encoding='utf8') as fcc_file:
        fcc_data = json.load(fcc_file)

        # items = fcc_data.items()

        with open("gd_unicom_iptv.m3u", "w", encoding="utf8") as file:
            file.write("#EXTM3U\n")
            for item in fcc_data:
                id = item["channelID"]
                name = item["channelName"]
                url = item["channelURL"][0]
                group_name = "未分组"
                short_name = name.replace("高清1", "").replace("标清1", "").replace("标清", "").replace(
                    "高清", "").replace("超清", "").replace("-", "").replace("测试", "")
                if ("CCTV" in name):
                    group_name = "央视"
                    short_name = re.sub(u"([^\u0041-\u005a\u0061-\u007a\u0030-\u0039])", "", short_name)
                if ("央视" in name):
                    group_name = "央视"
                if ("卫视" in name):
                    group_name = "卫视"
                if ("CETV" in name):
                    group_name = "CETV"
                if ("广东" in name or "深圳" in name):
                    group_name = "广东"

                if ("高清" in name):
                    group_name += ";高清"

                print("正在生成频道: {}".format(name))

                file.write(
                    "#EXTINF:-1 tvg-id=\"{}\" tvg-name=\"{}\" tvg-logo=\"https://live.fanmingming.com/tv/{}.png\" group-title=\"{}\",{}\n".format(name, name, short_name, group_name, name))
                file.write("{}\n".format(url))
