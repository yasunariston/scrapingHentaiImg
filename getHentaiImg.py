#coding:utf-8
import os
import os.path

from time import sleep
from urllib import request
from bs4 import BeautifulSoup


def derectory_creation(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

def hentai_search(dir_name="images/"):
    html_list = []
    imgs_list = []
    getpage = 10

    for page in range(getpage):
        sleep(1)
        print(getpage - page)
        url = "http://www.dmm.co.jp/digital/videoc/-/list/=/sort=ranking/page={}/".format(page)
        html_list.append(request.urlopen(url))

    for html in html_list:
        soup = BeautifulSoup(html, "html.parser")
        body = soup.body
        images = body.find_all("img")
        for image in images:
            if image.get("src").endswith(".jpg")\
            or image.get("src").endswith(".png"):
                imgs_list.append(image.get("src"))

        derectory_creation(dir_name)
        for target in imgs_list:
            re = request.urlopen(target).read()
            sleep(1)
            with open(dir_name + target.split("/")[-1], "wb") as f:
                f.write(re)

if __name__ == "__main__":
    #http_test
    #url = "http://www.dmm.co.jp/digital/videoc/-/list/=/sort=ranking/page=2/"
    #https_test
    #url = "https://lastidol.com/"
    hentai_search()


