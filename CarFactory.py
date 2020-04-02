# coding:utf-8
from Suonata import SuonataCar

class CarFactory(object):
	def createCar(self,typeName):
		if typeName=="索纳塔":
			car=SuonataCar()

		return car