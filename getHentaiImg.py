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
        html = next(html_generated)
        images_info = scraping_img(html)
        write_image(images_info, dir_name)

    print("finished!!")


def scraping_img(html):
    soup = BeautifulSoup(html, "lxml")
    body = soup.body
    images = body.find_all("img")
    for image in images:
        src = image.get("src")
        if not src.endswith(".jpg")\
        and not src.endswith(".png"):
            images.remove(image)
    print(str(len(images)) + "files exist.")
    return images


def write_image(images_info, dir_name):
    for i, image in enumerate(images_info):
        src = image.get("src")
        image_path = dir_name + src.split("/")[-1]
        if not os.path.isfile(image_path):
            with open(image_path, "wb") as f:
                re = request.urlopen(src).read()
                f.write(re)
                print("Servered{}:".format(i) + image_path)
                sleep(1)


if __name__ == "__main__":
    url_stationery = "http://www.dmm.co.jp/digital/videoc/-/list/=/sort=ranking/page={}/"
    pages = 1
    url_list = [url_stationery.format(page + 1) for page in range(pages)]
    hentai_search(url_list)
