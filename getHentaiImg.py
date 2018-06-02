#coding:utf-8
import os
import os.path

import cv2
import pprint

from time import sleep
from urllib import request
from bs4 import BeautifulSoup

import setTimeProgramStartUp


def derectory_creation(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)


def generate_html(url_list):
    for url in url_list:
        print("Start connection:" + url)
        html = request.urlopen(url)
        print("Connection finished!!")
        yield html


def hentai_search(url_list, dir_name="../images/"):
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


def setImgSize(imagePass, min_width, max_width, min_height, max_height):
    image = cv2.imread(imagePass)
    width, height = image.shape[1], image.shape[0]

    if max_width >= width >= min_width\
    and max_height >= height >= min_height:
        return True
    else:
        return False


def write_image(images_info, dir_name):
    for i, image in enumerate(images_info):
        src = image.get("src")
        image_path = dir_name + src.split("/")[-1]
        if not os.path.isfile(image_path):
            re = request.urlopen(src).read()
            with open(image_path, "wb") as f:
                f.write(re)
                sleep(1)

            #Uneffective because remove img after write it.
            #Serve Original size, if original size is diffrent...
            if setImgSize(image_path, 130, 150, 190, 200):
                print("Servered{}:".format(i) + image_path)
            else:
                os.remove(image_path)


if __name__ == "__main__":

    url_stationery = "http://www.dmm.co.jp/digital/videoc/-/list/=/sort=ranking/page={}/"
    pages = 1
    url_list = [url_stationery.format(page + 1) for page in range(pages)]
    test = setTimeProgramStartUp.setProgram(hentai_search, url_list)
    test.setStartUp(8,10,0)

    #url = ["https://book.dmm.com/photo/"]
    #hentai_search(url, "../test/")
