from read_ini import ReadIni
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LocationRoute:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, file_name, section, key):
        read_ini = ReadIni(file_name)
        local = read_ini.get_value(key, section)

        self.set_element_wait(local)

        by = local.split('=>')[0]
        value = local.split('=>')[1]

        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_android_uiautomator('new UiSelector().text(value)')
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def set_element_wait(self, local, delay=30, interval=1):

        by = local.split('=>')[0]
        value = local.split('=>')[1]

        if by == "id":
            element = WebDriverWait(self.driver, delay, interval).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            element = WebDriverWait(self.driver, delay, interval).until(
                EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            element = WebDriverWait(self.driver, delay, interval).until(
                EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            element = WebDriverWait(self.driver, delay, interval).until(
                EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            element = WebDriverWait(self.driver, delay, interval).until(
                EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            element = WebDriverWait(self.driver, delay, interval).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element
