# coding:utf-8

class CarStore(object):

	def createCar(self,typeName):
		pass

	def order(self,typeName):
		self.car=self.createCar(typeName);
		self.car.move()
		self.car.stop()

