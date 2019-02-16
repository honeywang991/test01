#coding=utf-8
from .read_init import ReadInni


class GetByLocal:
    def __init__(self,driver):
        self.driver = driver
    def get_element(self,key):
        read_ini = ReadInni()
        local = read_ini.get_value(key)
        if local !=None:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            if by == 'id':
                return self.driver.find_element_by_id(local_by)
            elif by =='className':
                return self.driver.find_element_by_class_name(local_by)
            else:
                return self.driver.find_element_by_xpath(local_by)
        else:
            return None