#11) Frecuencia de caracteres

print("*"*10)
alfabeto="abcdefghijklmnñopqrstuvwxyz"
veces=0
texto=input("Escribe un texto: ")
texto.lower()
for i in alfabeto:
    if i in texto:
        veces=texto.count(i)
        if veces==1:
            print("\nLa letra '{}' aparece 1 vez".format(i.upper()))
        else:
            print("\nLa letra '{}' aparece {} veces".format(i.upper(),veces))

#12) Calculadora de IVA
print("*"*10)
print("\nCaso A\n")
precio=float(input("¿Cuánto es el precio del producto sin IVA?: "))
Iva=1.21#(21%)
print("\nCálculo del precio con IVA:") 
print(f"{precio} euros * IVA(21%)= {round((precio*Iva),2)} euros")

print("\nCaso B\n")
precio_IVA=float(input("¿Cuánto cuesta el producto con el IVA incluido?: "))
print("\nCálculo del precio sin IVA")
print(f"{precio_IVA} euros / IVA(21%) = {round((precio_IVA/Iva),2)} euros")

#13) Edad
print("*"*10)
nacimiento=int(input("\nDime en qué año naciste: "))
edad=2020-nacimiento
print(f"""\nAl nacer en {nacimiento}, tienes {edad} años,
por lo que el año que viene cumples {edad+1} años""")

#14) ¿Está el número en la lista?
print("*"*10)
numeros=[1,3,9]
pidiendo=True
num=int(input("\nDime un número entre 0 y 9: "))
while num<0 or num>9:
    num=int(input("Dime un número entre 0 y 9: "))
if num in numeros:
    print("\nEl número se encuentra dentro de la lista")    
#15) Números aleatorios con y sin repetición
print("*"*10)

from random import randint
lista_rep=[]
lista_no_rep=[]
lista3=[]
for i in range(10):
    lista_rep+=[randint(1,20)]
lista_rep.sort()    
for i in range(100):
    n=randint(1,20)
    if len(lista_no_rep)==10:
        break
    if n not in lista_no_rep:
        lista_no_rep+=[n]
lista_no_rep.sort()        
for i in lista_no_rep:
    if i in lista_rep:
        lista3+=[i]
lista3.sort()

print(lista_no_rep) 
print(lista_rep) 
print(lista3)      

#16) Ordenar una lista
print("*"*10)
lista=[]
for i in range(10):
    lista+=[random.randint(1,50)]
print(lista)
lista2=[]
lista2+=[min(lista)]
lista2+=[max(lista)]
lista.remove(min(lista))
lista.remove(max(lista))

for i in range(1,9):      
    lista2.insert((len(lista2)-i),max(lista))
    lista.remove(max(lista))
print(lista2)

#17) Función separa
print("*"*10)
lista=[]
lista_pares=[]
lista_impares=[]
suma_par=0
suma_impar=0
for i in range(15):
    lista+=[random.randint(-20,20)]
for j in lista:
    if j%2==0:
        if j not in lista_pares:
            lista_pares+=[j]
            suma_par+=j
    else:
        if j not in lista_impares:
            lista_impares+=[j]
            suma_impar+=j          
lista_pares.sort()
lista_impares.sort()
print(f"Lista de pares: {lista_pares}")
print(f"Lista de impares: {lista_impares}")
if suma_par>suma_impar:
    print(f"La suma de la lista de números pares, es {suma_par}, que es mayor que la de la lista de números impares; {suma_impar}")                   
elif suma_impar>suma_par:
    print(f"La suma de la lista de números impares, es {suma_impar}, que es mayor que la de la lista de números pares; {suma_par}")
else:
    print("La suma de ambas listas de números es igual")       

#18) Binario a decimal
print("*"*10)
suma=0
num=input("Introduce un número binario: ")
indice=0
for i in num:
    if i=="1":
        suma+=1*2**((len(num)-1)-indice) 
        print("1*2**{}".format(len(num)-1-indice),end=" + ")
    else:
        print("0*2**{}".format(len(num)-1-indice), end=" + ")
    if indice==(len(num)-1):
        if i=="1": 
            print("1*2**{} = {}".format((len(num)-1-indice),suma))
        else:
            print("1*2**{} = {}".format((len(num)-1-indice),suma))           
    indice+=1 
print(f"El número binario '{num}'', corresponde en número decimal a '{suma}'")


#19) Decimal a binario
print("*"*10)

n=int(input("Introduce un número decimal: "))
print("\nndecimal       entero           resto")
cifras=[]
dividiendo=True
while dividiendo==True:
    print("{}{:17}{:17}".format(n,n//2,n%2))
    n=n//2
    cifras+=[n%2]
    if n//2==0:
        print("{}{:17}{:17}".format(n,n//2,n%2))
        cifras+=[n%2]
        break
print("\nEl número decimal",n,"equivale en binario a ", end="")
for j in cifras:
    print(f"{j}",end="")







  

    

    

    
        
        
        
    


  
  
