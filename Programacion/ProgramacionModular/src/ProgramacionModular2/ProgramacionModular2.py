#Ejercicio1
numero= int(input("Introduce un numero positivo= "))

def calcularFactorial(numero):
    if numero>=0:
        factorial=1
        for i in range(1, numero+1):
            factorial=factorial*i
        return factorial
    else:
        return None
    
print(f"The factorial is {calcularFactorial(numero)}")

#Ejercicio2
year = int(input("Enter a year: "))

def is_leap(year):
    leap = False

    # Si es divisible entre 4, es un año bisiesto
    if year%4 == 0:
        leap = True

    # Si es divisible entre 100 falso
    if year%4 == 0 and year%100 == 0:
        leap = False

    # si es divisible entre 400 es verdadero
    if year%4 == 0 and year%100 == 0 and year%400 == 0:
        leap = True

    return leap
print(f"The year {year} is it leap? {is_leap(year)}")


#Ejercicio3
year=int(input("Enter a year:  "))
month=int(input("Enter a month:  "))
if year <=0 or month <=0 or month>=13:
    def incorrect (year, month):
        return (-1)
    print(incorrect(month, year))
elif year>0 or month >=1 or month <=12:
    def incorrect (month,year):
        if year <=0 or month <=0 or month>=13:
            print(-1)
        print(f"{incorrect (month,year)}")
    def isLeapYear (year):
        return year % 400 == 0
    def computeDaysInMonth (month, year):
        # Meses con 30 dias
        if month in [4, 6, 9, 11]:
            return 30
        # Si febrero es bisiesto o no lo es
        if month == "2":
            if isLeapYear (year):
                return 29
            else:
                return 28
        else:
            # el resto, tienen 31 dias
            return 31
    
    days = computeDaysInMonth (month, year)
    print(f"For the year {year} and month {month} the days it's {days}")


#Ejercicio4
date=[]
day=int(input("Input a day"))
month=int(input("Input a month"))
year=int(input("Input a year"))
def getDayOfWeek(date):
    week = ["monday","tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    a = (14 - month) / 12
    y = year - a
    m = month + 12 * a - 2
    d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) % 7
    return week[d]
print(getDayOfWeek(date))

#Ejercicio5
def powerIt (base, exponent=0):
    power = base**exponent
    return power

print("The power it's: ")
print(powerIt (2, 3))

#Ejercicio6
def  getNumberOfDigits(n):
    count = 0
    def decimal(n):
        while n != 0:
            #En decimal
            n //= 10
        count += 1
    return count

    """def octal(n):
        if len(n)<8:
            while n != 0:
                #En octal
                n //= 8
            count += 1"""
 #no se como continuar a partir de este punto y no creo funcione.

n = 345289467
print(f"Number of digits: {getNumberOfDigits(n)}")


#Ejercicio7
n=int(input("Input a number: "))

def isPrime(n):
    if n>0:
        esPrimo=True
        if n>2:
            for i in range(2,n):
                if n%i==0:
                    esPrimo=False
   
    else:
        esPrimo=None
    return esPrimo
print(isPrime(n))

#Ejercicio8
from math import sqrt

a = int(input("Input number for squared x: "))
b = int(input("Input number for x: "))
c = int(input("Input number for the independent number: "))
x1= 0
x2= 0
def solveSecondOrderEquation ():
    if ((b**2)-4*a*c) < 0:
        return None
        print("The equation is solved with complex numbers")
    else:
        x1 = (-b+sqrt(a**2-(4*b*c)))/(2*a)
        x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
        print(f"The solutions of x1 it's {x1} and x2 it's {x2}:")
print(solveSecondOrderEquation ())

#Ejercicio9
num = int(input("Enter a number:"))

def prime(num):
    while num>0:
        prime =True
        for i in range(2,num):
            if num%i==0:
                prime=False
        return prime
   
def div(num):
    lista_div=[]
    for i in range(1,num):
        if num%i==0:
            if prime(i):
                lista_div.append(i)
    return lista_div

print(div(num), prime(num))

#Ejercicio10
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def isFriendNumber(num1, num2):
    div1=0
    div2=0
    friends= False
    list1=[]
    list2=[]
    if num1>0 and num2>0:
        for i in range(1, num1):
            if num1%i==0:
                list1.append(i)
                div1+=i
        for i in range(1, num2):
            if num1%i==0:
                list2.append(i)
                div2+=i
        if div1==div2:
            friends=True
    else:
        return None
    return friends
print(isFriendNumber(num1, num2))