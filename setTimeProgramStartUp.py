#coding:UTF-8

from bs4 import BeautifulSoup
from datetime import datetime

import getHentaiImg
import inspect
import time


class setProgram:
    def __init__(self, func, *args):
        self.func = func
        self.args = args


    def waitForTime(self, hours=7, minutes=0, seconds=0):
        while True:
            now = datetime.now()
            if not now.hour == hours:
                time.sleep((now.minute + 59 - minutes) % 60 * 60)
            if not now.minute == minutes:
                time.sleep((now.second + 59 - seconds) % 60)
            if not now.second == seconds:
                time.sleep(1)
            elif now.hour == hours and now.minute == minutes:
                break


    def setStartUp(self, *hms):
        while True:
            print(self, *hms)
            self.waitForTime(*hms)
            self.func(*self.args)
