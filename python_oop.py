class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def displayInfo(self):
		print("name : ", self.name, ", age : ", self.age)

class Small_Person(Person):
	def displayInfo(self):
		print("small person name")

p = Small_Person("yogi", 30)
p.displayInfo()
p1 = Person("yogi2", 32)
p1.displayInfo()
