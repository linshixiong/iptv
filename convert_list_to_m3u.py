# -*- coding:utf-8 -*-
import json


if __name__ == "__main__":

    print("正在转换频道列表...")
    with open('channellist.json', 'r', encoding='utf8') as fcc_file:
        fcc_data = json.load(fcc_file)

        # items = fcc_data.items()

        with open("gd_unicom_iptv.m3u", "w",encoding="utf8") as file:
            file.write("#EXTM3U\n")
            for item in fcc_data:
                id = item["channelID"]
                name = item["channelName"]
                url = item["channelURL"][0]
                group_name = "未分组"
                if("CCTV" in name):
                    group_name = "央视"
                if("卫视" in name):
                    group_name = "卫视"
                if("广东" in name or "深圳" in name):
                    group_name = "广东"
                    
                if("高清" in name):
                    group_name += ";高清"    
            
                print("正在生成频道: {}".format(name))

                file.write(
                    "#EXTINF:-1 tvg-id=\"{}\" tvg-name=\"{}\"  group-title=\"{}\",{}\n".format(name, name, group_name, name))
                file.write("{}\n".format(url))
