from read_ini import ReadIni


class LocationRoute:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, file_name, section, key):
        read_ini = ReadIni(file_name)
        local = read_ini.get_value(key, section)
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
