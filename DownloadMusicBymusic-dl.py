import os

# Usage: music-dl[OPTIONS]
# Search and download music from netease, qq, kugou, baidu and xiami. Example:
#   music-dl - k "周杰伦"
# Options:
#   --version             Show the version and exit.
#   -k, --keyword TEXT    搜索关键字，歌名和歌手同时输入可以提高匹配（如 空帆船 朴树）
#   -u, --url TEXT        通过指定的歌曲URL下载音乐
#   -p, --playlist TEXT   通过指定的歌单URL下载音乐
#   -s, --source TEXT     支持的数据源: baidu
#   -n, --number INTEGER  搜索数量限制
#   -o, --outdir TEXT     指定输出目录
#   -x, --proxy TEXT      指定代理（如http: // 127.0.0.1: 1087）
#   -v, --verbose         详细模式
#   --lyrics              同时下载歌词
#   --cover               同时下载封面
#   --nomerge             不对搜索结果列表排序和去重
#   --help                Show this message and exit.

print("1.Download music by music`s name.")
print("2.Download music by music`s url.")
print("3.Download music by playlist`s url.")
print("4.Help")
print("0.Exit")
choose = int(input("Please input a number:"))
match choose:
    case 1: os.system("music-dl --number 10")
    case 2:
        music_url = input("Please input a music`s url:")
        os.system("music-dl --url "+music_url)
    case 3:
        play_list_url = input("Please input a playlist`s url:")
        os.system("music-dl --playlist "+play_list_url)
    case 4:
        os.system("music-dl --help")
    case 0:
        exit()
