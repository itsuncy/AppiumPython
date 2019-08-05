from read_ini import ReadIni


class GetByLocal:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        # id>com.tbex.trader:id/edtAccount
        read_ini = ReadIni()
        local = read_ini.get_value(key)
        by = local.split('>')[0]
        value = local.split('>')[1]
        if by == 'id':
            return self.driver.find_element_by_id(value)
        elif by == 'className':
            return self.driver.find_element_by_class_name(value)
        else:
            return self.driver.find_element_by_xpath(value)
