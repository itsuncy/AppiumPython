from read_ini import ReadIni


class LocationRoute:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, file_name, section, key):
        read_ini = ReadIni(file_name)
        local = read_ini.get_value(key, section)
        by = local.split('>')[0]
        value = local.split('>')[1]
        if by == 'id':
            return self.driver.find_element_by_id(value)
        elif by == 'name':
            return self.driver.find_element_by_android_uiautomator('new UiSelector().text(value)')
        elif by == 'xpath':
            return self.driver.find_element_by_xpath(value)
