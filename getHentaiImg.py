#coding:utf-8
import os
import os.path

from urllib import request
from bs4 import BeautifulSoup


def derectory_creation(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

def hentai_search(url, dir_name="images/"):
    imgs_list = []
    html = request.urlopen(url)

    soup = BeautifulSoup(html, "html.parser")
    images = soup.find_all("img")

    for image in images:
        if image.get("src").endswith(".jpg"):
            imgs_list.append(image.get("src"))

    derectory_creation(dir_name)
    for target in imgs_list:
        re = request.urlopen(target).read()
        with open(dir_name + target.split("/")[-1], "wb") as f:
            f.write(re)

if __name__ == "__main__":
    #http_test
    url = "http://www.dmm.co.jp/digital/"
    #https_test
    #url = "https://official.ameba.jp/categories/14/ranking"
    hentai_search(url)


