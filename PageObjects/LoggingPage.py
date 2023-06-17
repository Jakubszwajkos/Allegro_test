from selenium.webdriver.common.by import By


class LoggingPage:

    def __init__(self,driver):
        self.driver = driver


    login = (By.CSS_SELECTOR, "#login")
    password = (By.CSS_SELECTOR, "#password")
    Zaloguj_sie_LP = (By.XPATH, "//button[text()='Zaloguj się']")
    error_text = (By.CSS_SELECTOR, "#login-form-submit-error")


    def Login(self):
        return self.driver.find_element(*LoggingPage.login)

    def Password(self):
        return self.driver.find_element(*LoggingPage.password)

    def Zaloguj_sie_LoggingPage(self):
        return self.driver.find_element(*LoggingPage.Zaloguj_sie_LP)


    def Error_login_text(self):
        return self.driver.find_element(*LoggingPage.error_text)

