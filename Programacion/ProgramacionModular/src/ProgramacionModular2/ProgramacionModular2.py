"""
Design a method called computeFactorial that receives a positive integer and
returns the factorial for that number. If the number is negative the method should
return None.
"""

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