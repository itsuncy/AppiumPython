import configparser


class ReadIni:
    def __init__(self, file_name):

        self.file_path = 'D:\\CoreRepository\\Python\\AppiumPython\\resources\\element\\' + file_name + ".ini"

        self.data = self.read_ini()

    # 读取ini配置文件
    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    # 通过key获取对应的value
    def get_value(self, key, section=None):
        if section == None:
            section = "default_element"
        try:
            value = self.data.get(section, key)
        except:
            value = None
        return value


if __name__ == '__main__':
    a = ReadIni("MineElement").get_value("mine", "default_element")
    print(a)
