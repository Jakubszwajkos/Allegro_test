from lib2to3.pgen2 import driver
from telnetlib import EC

from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select

import utilities
from selenium import webdriver
import time
import pytest

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.HomePage import HomePage
from PageObjects.LoggingPage import LoggingPage
from PageObjects.SearchPage import SearchPage
from utilities.BaseClass import BaseClass


class TestWyszukiwanie(BaseClass):

    def test_wyszukiwanie(self):
        log = self.getLogger()
        Home_Page = HomePage(self.driver)
        Search_Page = SearchPage(self.driver)
        log.info("Home Page")
        Home_Page.Wyszukiwanie_przedmiotu().send_keys("ps5")
        Home_Page.Przycisk_Szukaj().click()
        log.info("Moved to SearchPage")
        Search_Page.Konsole().click()
        self.Wait(3)
        Search_Page.Digital_PS5().click()
        self.Wait(2)

        liczba_produktów = int(Search_Page.Liczba_Produktow().text)
        log.info("Start Scanning Products")
        Scanning = True
        liczba_ofert = 0
        site = 1

        while Scanning:
            products = Search_Page.Products()
            time.sleep(3)

            for product in products:
                liczba_ofert += 1


            if site == 1:
                xpath_site = Search_Page.nastepna_strona1
                site += 1
            else:
                xpath_site = Search_Page.next_site


            try:
                Search_Page.Next_site(xpath_site).click()
                self.Wait(3)
                time.sleep(3)
                continue

            except NoSuchElementException:
                Scanning = False
                if liczba_produktów == liczba_ofert:
                    log.info("Scanning completed")
                    print("The number of offers matches the number displayed next to the category")
                else:
                    log.info("Stop scanning")
                    print("The number of offers do not matches the number displayed next to the category")




