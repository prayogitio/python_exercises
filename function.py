def cetak(num):
	for x in range(0,num):
		print(x, end=" ")

def tambah(num1, num2):
	return num1+num2

def kurang(num1, num2):
	return num1-num2

def bagi(num1, num2):
	return num1/num2

lala = input("your number: ")
cetak(num = int(lala))
print()

a = 100
b = 30
print(tambah(num1 = a, num2 = b))
print(kurang(num1 = a, num2 = b))
c = 12.0
d = 5.0
print(bagi(num1 = c, num2 = d))
print(a/b)
print(a//b)