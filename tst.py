# coding:utf-8

def add(a,b):
	return a+b



if __name__=="__main__":
	ret=add(12,22)

	print(__name__=='__main__')

	print("in test.py file, __name__ is %s"%__name__)