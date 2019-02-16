import unittest
import HTMLTestRunner
from class_0816.class_0811_work.read_data_1 import ReadData
from class_0816.class_0811_work.math_method import TestMath


test_data=ReadData().read_data()#测试数据
suite = unittest.TestSuite()

for item in test_data:
    suite.addTest(TestMath('test_add',eval(item)['a'],eval(item)['b'],eval(item)['expected']))

with open('test_report.html','wb+') as file:

    runner = HTMLTestRunner.HTMLTestRunner(file,title='Python9期')
    runner.run(suite)