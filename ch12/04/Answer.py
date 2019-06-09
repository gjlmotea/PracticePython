import math

class Date():

    def __init__(self):
        self.__year = '1970'
        self.__month = '01'
        self.__day = '01'

    def set_value(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day

    def GetDate(self):
        return self.__year, self.__month, self.__day


input_Y = input("欲設定日期，\n請輸入年:\n")
input_M = input("請輸入月份:\n")
input_D = input("請輸入日期:\n")


YMD = Date()
YMD.set_value(input_Y, input_M, input_D)
for element in YMD.GetDate():
    print(element)
