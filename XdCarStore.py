# coding:utf-8
from CarStore import CarStore
from CarFactory import CarFactory


class XdCarStore(CarStore):
	def createCar(self, typeName):
		self.carFactory = CarFactory()
		return self.carFactory.createCar(typeName)
