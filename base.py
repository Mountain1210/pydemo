class Dog:	
	
	#类属性
    num = 0

    #实例方法
    def __init__(self):
        #实例属性
        self.name = "laowang"

    #类方法
    @classmethod
    def add_num(cls):
        cls.num = 100

    #静态方法
    @staticmethod
    def print_menu():
        print("----------------------")
        print("    穿越火线V11.1")
        print(" 1. 开始游戏")
        print(" 2. 结束游戏")
        print("----------------------")

    #私有方法
    def __send_msg(self):
        print("------正在发送短信------")
	
	def set_age(self,new_age):
        if new_age>0 and new_age<=100:
            self.__age = new_age
        else:
            self.__age = 0

    def get_age(self):
        return self.__age
	
    #公有方法
    def send_msg(self, new_money):
        if new_money>10000:
            self.__send_msg()
        else:
            print("余额不足,请先充值 再发送短信")
			
	def __del__(self):
        print("-----英雄over------")		
		
