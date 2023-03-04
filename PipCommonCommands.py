import os

# 菜单


def display():
    list = ("查看可升级包", "安装pip包", "卸载pip包",
            "查看当前pip源", "设置pip源", "安装计算机二级考试包",
            "导出已经安装的pip包", "从文件中安装pip包", "帮助")
    for i in range(len(list)):
        print("{}.{}".format(i+1, list[i]))
    print("0.退出")
    try:
        choose = input("请选择：")
        return choose
    except:
        print("已退出")
        return 0


# 查看可升级包


def outdate_package():
    pack = 0
    os.system("pip list --outdated")
    while pack != '':
        pack = input("请输入要升级的包名称（多个包之间使用空格隔开，留空退出）：")
        if pack == "pip":
            try:
                os.system("pip install pip -U")
            except:
                print("升级失败")
            else:
                print("升级成功")
        elif pack:
            try:
                os.system("pip install --upgrade "+pack)
            except:
                print("升级失败，请重试")
            else:
                print("升级成功")

# 安装包


def install_package():
    pack = input("请输入要安装的包名称：")
    try:
        os.system("pip install "+pack)
    except:
        print("安装失败")
    else:
        print("安装成功")

# 卸载包


def uninstall_package():
    pack = input("请输入要卸载的包名称：")
    try:
        os.system("pip uninstall "+pack)
    except:
        print("卸载失败")
    else:
        print("卸载成功")

# 查看源


def view_mirror():
    os.system("pip config list")

# 源菜单


def mirror_menu():
    list = ("官方源", "清华大学", "重庆邮电大学", "中国科学技术大学", "豆瓣", "阿里云", "华为云", "网易云")
    for i in range(len(list)):
        print("{}.{}".format(i, list[i]))
    choose = input("请选择源：")
    return choose

# 测试镜像速度


def test_mirror():
    print("镜像速度测试可以为你选择镜像提供依据")
    dic = {"官方镜像": "pypi.org",
           "清华镜像": "pypi.tuna.tsinghua.edu.cn",
           "重庆邮电大学镜像": "mirrors.cqupt.edu.cn",
           "中国科学技术大学镜像": "pypi.mirrors.ustc.edu.cn",
           "豆瓣镜像": "pypi.douban.com",
           "阿里云": "mirrors.aliyun.com",
           "华为云": "mirrors.huaweicloud.com",
           "网易开源镜像站": "mirrors.163.com"}
    sites = list(dic.items())
    for site in sites:
        print("\n测试：{}".format(site[0]))
        os.system("ping {}".format(site[1]))

# 设置镜像


def set_mirror():
    test_mirror()
    choose = mirror_menu()
    # 升级pip到最新版本
    print("升级pip版本:")
    try:
        os.system("pip install pip -U")
    except:
        print("升级失败")
    else:
        print("升级成功")
    match choose:
        case '0':
            print("将设置官方镜像")
            os.system("pip config set global.index-url \
                https://pypi.org/simple")
        case '1':
            print("将设置清华镜像")
            os.system("pip config set global.index-url \
                https://pypi.tuna.tsinghua.edu.cn/simple")
        case '2':
            print("将设置重庆邮电大学镜像")
            os.system(
                "pip config set global.index-url https://mirrors.cqupt.edu.cn/pypi/simple/")
        case '3':
            print("将设置中科大镜像")
            os.system("pip config set global.index-url \
                https://pypi.mirrors.ustc.edu.cn/simple")
        case '4':
            print("将设置豆瓣镜像")
            os.system("pip config set global.index-url \
                http://pypi.douban.com/simple/")
        case '5':
            print("将设置阿里镜像")
            os.system("pip config set global.index-url \
                https://mirrors.aliyun.com/pypi/simple/")
        case '6':
            print("将设置网易开源镜像站")
            os.system("pip config set global.index-url \
                https://mirrors.163.com/pypi/simple/")
    print("设置成功")

# 计算机二级考试需要安装的包


def NCRE_package():
    libs = ["future", "pefile", "jieba", "PyInstaller"]
    print("即将安装:future, pefile, jieba, PyInstaller")
    ans = input("是否继续安装(Y/N):")
    if ans == 'y' or ans == 'Y':
        for lib in libs:
            os.system("pip install "+lib)
        print("安装成功！")

# 导出安装的pip包


def export_package():
    os.system("pip freeze > requirements.txt")
    print("已经导出到文件夹中")

# 从文件导入要安装的pip包


def import_package():
    os.system("pip install -r requirements.txt")

# 帮助文档


def pip_help():
    os.system("pip --help")


def func(choose):
    match choose:
        case '1':
            outdate_package()
        case '2':
            install_package()
        case '3':
            uninstall_package()
        case '4':
            view_mirror()
        case '5':
            set_mirror()
        case '6':
            NCRE_package()
        case '7':
            export_package()
        case '8':
            import_package()
        case '9':
            pip_help()

# 主函数


def main():
    choose = 0
    while choose != '0':
        choose = display()
        func(choose)
    print("程序结束")


main()
