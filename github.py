






###BLOQUE 1.Fundamentos de Programación

#1) Comparar dos numeros
print("Programa para comparar dos números\n")
num1=int(input("Dime un número: "))
num2=int(input("\nDime un segundo número: "))
if num1>num2:
  print("\n{} es mayor que {}".format(num1,num2))
elif num1<num2:
  print("\n{} es menor que {}".format(num1,num2))
elif num1==num2:
  print("\nAmbos numeros son iguales")

#2) Comparar varias parejas de numeros
print("\n**************************************")
print("Programa para comparar dos números")
pidiendo=True
while pidiendo==True:
    num1=int(input("\nDime un número: "))
    num2=int(input("Dime un segundo número: "))
    if num1>0 and num2>0:
        if num1>num2:
            print("\n{} es mayor que {}".format(num1,num2))
        elif num1<num2:
            print("\n{} es menor que {}".format(num1,num2))
        elif num1==num2:
            print("\nAmbos numeros son iguales")
    else:
        pidiendo=False
        print("Valor introducido no correcto")

#3) Elevar al cuadrado
print("\n******************************************")
print("Cuadrado de todos los números del 1 al 100\n")
for i in range(1,101):
    print(i**2)


#4) Listar numeros pares
print("****************")    
num0=int(input("Dime un número: "))
num=int(input("Dime otro número: "))
if num0<num:
    print("Números pares comprendidos entre {} y {}".format(num0,num))
    for i in range(num0,num):
        if i%2==0:
            print(i,end=" ")
elif num0>num:
    print("Números pares comprendidos entre {} y {}".format(num,num0))
    for i in range(num,num0):
        if i%2==0:
            print(i,end=" ")
            
else:
    print("Los números deben ser distintos\n")
    
#5) Media de una serie de números
print("*********************")
suma=0
contador=0
pidiendo=True
while pidiendo==True:
    num=float(input("Introduce un número: "))
    if num>0:
        suma+=num
        contador+=1
    else:
        pidiendo=False

print(f"\nLa suma de los números introducidos es {suma}")
print("La media de los números introducidos es: {}".format(round((suma/contador),2)))
            

#6) Calculadora
print("***************")
num=int(input("Introduce un número: "))
num1=int(input("Introduce un segundo número: "))
while num<0 or num1<0:
    print("\nHas introducido un número no válido\n")
    num=int(input("Introduce un número: "))
    num1=int(input("Introduce un segundo número: "))
print(f"\nSuma: {num} + {num1} = {num+num1}")
print(f"Resta: {num} - {num1} = {num-num1}")
print(f"Multiplicación: {num} * {num1} = {num*num1}")
print(f"División: {num} / {num1} = {num/num1}")
print(f"División Entera: {num} // {num1} = {num//num1}")
print(f"Resto: {num} % {num1} = {num%num1}")
print(f"Potencias: {num} ** {num1} = {num**num1}")


#7) Divisores de un número
print("**********")
import random
numero=random.randint(2,1000)
print("Divisores de", numero)
for i in range(1,numero+1):
    if numero%i==0:
        print(i)

#8) Comparar medias de aleatorios

suma=0
suma2=0
print("\n*************")
print("Números para primera media:")
for i in range(12):
    numero=random.randint(0,100)
    suma+=numero
    print(numero, end=" ")
media=round(suma/12,2)
print(". Y su media es: {}".format(media))
print("\nNúmeros para segunda media:")
for j in range(12):
    numero=random.randint(0,100)
    suma2+=numero
    print(numero, end=" ")
media2=round(suma2/12,2)    
print(". Y su media es: {}\n".format(media2))
if media>media2:
    print(media, "es mayor que", media2)
else:
    print(media, "es menor que", media2)

#9) Tabla de multiplicar

print("***************************")
num=int(input("Introduce un número del 1 al 15 para mostrar su tabla de multplicar: "))
while num<1 or num>15:
    print("\nNúmero incorrecto")
    num=int(input("Introduce un número del 1 al 15 para mostrar su tabla de multiplicar: "))
for i in range(1,11):
    print("{} * {} = {}".format(num,i,num*i))
    
#10) Tablas de multiplicar hasta 15*15
    
print("\n*************\n")
for j in range(1,15):
    print(f"Tabla del {j}\n")
    for i in range(1,11):
        print("{} * {} = {}".format(j,i,j*i))
    print()    
       
  

    

    

    
        
        
        
    


  
  
