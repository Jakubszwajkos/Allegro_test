from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    Mojeallegro = (By.XPATH, "//span[text()='Moje Allegro']")
    ZalogujsieH = (By.XPATH, "//a[text()='Zaloguj się']")


    def Moje_Allegro(self):
        return self.driver.find_element(*HomePage.Mojeallegro)

    def Zaloguj_sie_Home(self):
        return self.driver.find_elements(*HomePage.ZalogujsieH)[1]

