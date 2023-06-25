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

    def test_wyszukiwanie(self, getData):
        log = self.getLogger()
        Home_Page = HomePage(self.driver)
        Search_Page = SearchPage(self.driver)
        log.info("Home Page")
        log.info("Looking product is " + getData["Product"])
        Home_Page.Wyszukiwanie_przedmiotu().send_keys(getData["Product"])
        Home_Page.Przycisk_Szukaj().click()
        log.info("Moved to SearchPage")
        Search_Page.Konsole().click()
        self.Wait(3)
        Search_Page.Digital_PS5().click()
        self.Wait(2)

        liczba_produktów = int(Search_Page.Liczba_Produktow().text)
        log.info("Start Scanning Products")

        end_flag = True
        liczba_ofert = 0
        site = 1
        ceny = []

        while end_flag:
            products = Search_Page.Products()
            time.sleep(3)

            for product in products:

                try:
                    price = product.find_element(By.XPATH, "div[2]/div/div/span/div").text
                    liczba_ofert += 1


                    ceny.append(price)



                except NoSuchElementException:
                    price = product.find_element(By.XPATH, "div[3]/div/div/span/div").text

                    liczba_ofert += 1
                    ceny.append(price)

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
                end_flag = False
                if liczba_produktów == liczba_ofert:
                    log.info("Scanning completed")
                    print("The number of offers do  matches the number displayed next to the category")


                else:
                    log.info("Stop scanning")
                    print("The number of offers do not matches the number displayed next to the category")

        Ceny = [float(cena.replace(",", ".").replace(" zł", "")) for cena in ceny]
        lowest_number = min(Ceny)


        log.info("Sorting "+getData["category"])
        dropdown = Select(Search_Page.Sort())
        dropdown.select_by_visible_text(getData["category"])

        print(lowest_number)

    @pytest.fixture(params=[{"Product": "ps5","category":"cena: od najniższej"}])
    def getData(self, request):
        return request.param




