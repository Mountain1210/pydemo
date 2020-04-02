class Dog(obj):
	__instance=None

	def __new__(cls):
		if cls.__instance==None:
			cls.__instance=obj.__new__(cls)
			return cls.__instance
		else:
			return cls.__instance

a=Dog();
print(id(a))
b=Dog()
print(id(b))