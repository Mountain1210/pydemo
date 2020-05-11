# coding:utf-8
class Check():
    #成员变量
    num1 = 0
    s1 = ""
 
    #成员方法
    def show(self):
        print("showing")
 
    #构造函数
    def __init__(self):
        print("构造函数被执行了")
        self.show()
 
c = Check()          #构造函数被执行了
c.show()