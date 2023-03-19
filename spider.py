"""
@Author: zhuang_qf
@encoding: utf-8
@time: 2023/3/19 16:02
"""
import requests
from lxml import etree
from multiprocessing.dummy import Pool
from fake_useragent import UserAgent
import os


# 获取主页url, 解析得到图片分类
def get_main_info():
    # 主页url
    url = "https://desk.zol.com.cn"
    response = requests.get(url=url, headers=headers)
    response.encoding = 'gb2312'
    tree = etree.HTML(response.text)
    choose_boxs = tree.xpath('//*[@id="main"]/dl[1]/dd/a[position()>1]/text()')
    href_list = tree.xpath('//*[@id="main"]/dl[1]/dd/a[position()>1]/@href')
    # 创建字典: 将解析的数据放进字典
    choose_dict = {}
    for box, href in zip(choose_boxs, href_list):
        url = "https://desk.zol.com.cn/" + href
        choose_dict[box] = url
    print(choose_boxs)
    # 输入你想要的需求
    try:
        data = input("请输入你想下载的类型: ")
        # 返回自己想要类型的页面url
        page_url = choose_dict[data]
        return page_url
    except Exception as e:
        print(e)
        # 输入错误, 回调函数重新输入
        print("输入错误!")
        main()


# 获取到页面, 解析得到下一页url和详情页url
def get_page_info(url):
    response = requests.get(url=url, headers=headers)
    response.encoding = 'gb2312'
    # 解析数据
    tree = etree.HTML(response.text)
    detail_hrefs = tree.xpath('//ul[@class="pic-list2  clearfix"]/li[position()>2]/a/@href')
    hrefs = []
    for href in detail_hrefs:
        href = "https://desk.zol.com.cn/" + href
        hrefs.append(href)
    # 返回页面里的次级url
    return hrefs


# 分页获取
def get_page(url):
    detail_hrefs = get_page_info(url)
    page = int(input("请输入你想获取图片的页数: "))
    # 获取页数url
    try:
        if page == 1:
            # 返回页面里的子页面url
            return detail_hrefs
        else:
            for i in range(2, page + 1):
                # 页数大于2, 回调此函数继续获取详情页图片url
                page_url = f"https://desk.zol.com.cn/fengjing/{page}.html"
                urls = get_page_info(page_url)
                detail_hrefs = detail_hrefs + urls
            # 返回页面里的子页面url
            return detail_hrefs
    except Exception as e:
        print(e)


def get_detail_text(url):
    # 请求图片地址获取到src和名字
    response = requests.get(url=url, headers=headers)
    response.encoding = 'gb2312'
    tree = etree.HTML(response.text)
    titles = tree.xpath('/html/body/div[3]/h3//text()')
    # 处理名字
    for title in enumerate(titles):
        if "\n" in title[1]:
            titles.pop(title[0])
    img_name = ", ".join(titles).replace(", ", "").replace("/", "-")
    # 处理url
    href = tree.xpath('//a[@id="1680x1050"]/@href')[0]
    href = "https://desk.zol.com.cn/" + href
    # 请求url得到下载地址资源
    response2 = requests.get(url=href, headers=headers)
    tree2 = etree.HTML(response2.text)
    img_src = tree2.xpath('//img[1]/@src')[0]
    return img_name, img_src


def get_detail_info(url):
    # 获取到详情页面
    response = requests.get(url=url, headers=headers)
    response.encoding = "gb2312"
    tree = etree.HTML(response.text)
    # 解析得到页面组图的url
    hrefs = tree.xpath('//*[@id="showImg"]/li/a/@href')
    for href in hrefs:
        href = "https://desk.zol.com.cn/" + href
        # print(href)
        # 获取组图的url和名字
        img_name, img_src = get_detail_text(href)
        # 下载图片
        resp_img = requests.get(url=img_src, headers=headers)
        print(img_name, "---------准备下载----------")
        try:
            with open(f"./ZOL/{img_name}.jpg", mode="wb") as f:
                f.write(resp_img.content)
                print(img_name, "---------下载完成----------")
        except Exception as e:
            print(e)
            print("---------下载失败----------")


def main():
    # 从主页面获取到想要类型的页面url
    page_url = get_main_info()
    # 获取到想要页面的详情页url列表
    detail_url_list = get_page(page_url)
    # 获取详情页url, 得到图片名和地址, 使用多线池提高爬取效率
    pool.map(get_detail_info, detail_url_list)


if __name__ == '__main__':
    # 创建文件夹
    if not os.path.exists("./ZOL"):
        os.mkdir("./ZOL")
    headers = {
        "User-Agent": UserAgent().random
    }
    # 定义一个有四个线程的线程池
    pool = Pool(4)
    main()
