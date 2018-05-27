#coding:UTF-8

from bs4 import BeautifulSoup
from datetime import datetime

import getHentaiImg
import inspect
import time


class setTimeProgramStartUp:
    def __init__(self, func, *args):
        self.func = func
        self.args = args


    def setStartUp(hours, minutes, seconds):
        while True:
            waitForTime(hours, minutes, seconds)
            func(*args)



    def waitForTime(hours=7, minutes=0, seconds=0):
        while True:
            now = datetime.now()
            if not now.hour == hours:
                sleep((59 - now.minute) * 60)
            if not now.minute == minutes:
                sleep(59 - now.second)
            if not now.second >= seconds >= now.secondi - 1:
                sleep(1)
            else:
                if now.hour == hours and now.minute == minutes:
                    sleep(1)
                    break



if __name__ == "__main__":
