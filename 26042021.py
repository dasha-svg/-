def zad5():
	a = 2
	mass = [a]
	while a <100:
		a+=2
		mass.append(a)
	print(mass)

def zad2():
	mass = []
	for i in range(10):
		mass.append(i%2)
	print(mass)


def zad3():
	mass = []
	for i in range(1,10,2):
		mass.append(i)
	print(mass)
	
	
def zad4():
	mass = []
	x = int(input())
	d = int(input())
	for i in range(x,100,d):
		mass.append(i)
	print(mass)

	
def zad6():
	mass = []
	n = int(input())
	for i in range(n):
		if i%3 == 0:
			mass.append(i)
	print(mass[::-1])
	
	
def zad9():
	mass = []
	n = int(input())
	for i in range(n):
		mass.append(i**2)
	print(mass)	
	
	
def zad8():

	
	
	
	
change = input('Введите номер задачи - ')
if change == '1':
	zad1()
elif change == '2':
	zad2()
elif change == '3':
	zad3()
elif change == '4':
	zad4()
elif change == '5':
	zad5()
elif change == '6':
	zad6()
elif change == '7':
	zad7()
elif change == '8':
	zad8()
elif change == '9':
	zad9()
