import random
import re
import time
from typing import Optional

import scrapy
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from ..logger import logger


class NyaaSpiderSpider(scrapy.Spider):
    name = 'nyaa_spider'
    start_urls = ['https://nyaa.si/']

    def wait(self, min: int = 2, max: int = 10) -> None:
        time.sleep(random.randint(min, max))

    def parse(self, response):

        for page_no in range(1, 1000):
            try:
                url = f"https://nyaa.si/?p={page_no}"

                logger.info(f"START: Crawling page {page_no}")
                self.run_driver(url)

                logger.info(f"DONE: Crawling page {page_no}")

            except Exception:
                logger.info("Exception encountered")
                break

    def run_driver(self, page_url: str = 1):

        logger.info("Setting selenium driver")
        self.wait(1, 2)
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)

        logger.info("Sending request")
        driver.implicitly_wait(0.4)
        driver.get(page_url)

        logger.info("Clicking download icon")
        self.wait(1, 2)
        icon_elements = driver.find_elements_by_xpath("//i[@class='fa fa-fw fa-download']")

        for index, icon in enumerate(icon_elements, start=1):
            icon.find_element_by_xpath("..").click()
            logger.info(f"DONE: Downloaded {index}")

        return driver
