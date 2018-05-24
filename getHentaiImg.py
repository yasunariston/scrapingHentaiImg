#coding:utf-8
import os
import os.path

from time import sleep
from urllib import request
from bs4 import BeautifulSoup


def derectory_creation(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)


def generate_html(url_list):
    for url in url_list:
        print("Start connection:" + url)
        html = request.urlopen(url)
        print("Connection finished!!")
        yield html


def hentai_search(url_list, dir_name="images/"):
    derectory_creation(dir_name)
    html_generated = generate_html(url_list)

    for i in range(len(url_list)):
        imgs_list = []
        html = next(html_generated)
        soup = BeautifulSoup(html, "lxml")
        body = soup.body
        images = body.find_all("img")
        for image in images:
            if image.get("src").endswith(".jpg")\
            or image.get("src").endswith(".png"):
                imgs_list.append(image.get("src"))

        print(str(len(imgs_list)) + "files exist.")
        for target in imgs_list:
            target_path = dir_name +  target.split("/")[-1]
            if not os.path.isfile(target_path):
                with open(target_path, "wb") as f:
                    re = request.urlopen(target).read()
                    f.write(re)
                    sleep(1)

    print("finished!!")




if __name__ == "__main__":
    url_stationery = "http://www.dmm.co.jp/digital/videoc/-/list/=/sort=ranking/page={}/"
    pages = 2
    url_list = [url_stationery.format(page) for page in range(pages)]
    hentai_search(url_list)
