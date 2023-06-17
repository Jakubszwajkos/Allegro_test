from lib2to3.pgen2 import driver
from telnetlib import EC
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
from utilities.BaseClass import BaseClass


class TestLogowanie(BaseClass):

        def test_logowania(self,getData):
                log = self.getLogger()
                Home_Page = HomePage(self.driver)
                Logging_Page = LoggingPage(self.driver)

                Home_Page.Moje_Allegro().click()

                Home_Page.Zaloguj_sie_Home().click()
                log.info("name is " + getData["email"])
                Logging_Page.Login().send_keys(getData["email"])









                security_on = False
                while not security_on:


                        self.Wait(3)

                        log.info("password is " + getData["password"])
                        Logging_Page.Password().send_keys("konto.testowe1990M@gmail.com")
                        Logging_Page.Zaloguj_sie_LoggingPage().click()
                        Error_Text = Logging_Page.Error_login_text().text

                        if Error_Text  == "Wymagane jest rozwiązanie captchy":
                                security_on = True
                        else:
                                continue

        @pytest.fixture(params=[{"email": "konto.testowe1990M@gmail.com", "password": "konto.testowe1990M@gmail.com"}])

        def getData(self, request):
                return request.param



