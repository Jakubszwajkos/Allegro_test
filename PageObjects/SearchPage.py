from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self,driver):
        self.driver = driver


    konsole = (By.XPATH, "//a[text()=' Konsole']")
    digitalkonsole = (By.XPATH, "//label[@for='multi-select-PlayStation 5 Digital Edition']")
    liczba_produktow_kolokategorii = (By.XPATH, "/html/body/div[2]/div[6]/div/div[2]/div/div/div/div/div/div[3]/div[2]/div[1]/div/div/div/section/div[2]/ul/li/div/span[2]")
    produkty = (By.XPATH, "//article/div/div/div[2]")
    nastepna_strona1 = "/html/body/div[2]/div[6]/div/div[2]/div/div/div/div/div/div[3]/div[1]/div[2]/div[4]/div/div/div/a/i"
    next_site = "/html/body/div[2]/div[6]/div/div[2]/div/div/div/div/div/div[3]/div[1]/div[2]/div[4]/div/div/div/a[2]"
    cena = (By.XPATH, "div[2]/div/div/span/div")


    def Konsole(self):
        return self.driver.find_element(*SearchPage.konsole)

    def Digital_PS5(self):
        return self.driver.find_element(*SearchPage.digitalkonsole)

    def Liczba_Produktow(self):
        return self.driver.find_element(*SearchPage.liczba_produktow_kolokategorii)

    def Products(self):
        return self.driver.find_elements(*SearchPage.produkty)

    def Next_site(self,xpath_site):
        return self.driver.find_element(By.XPATH, xpath_site)

    def Price(self):
        return self.driver.find_element()
        # price = product.find_element(By.XPATH, "div[2]/div/div/span/div").text



