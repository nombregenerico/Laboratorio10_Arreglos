# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 20:22:08 2020

@author: abaly
"""  
import numpy as np

def a_power_b (a,b): #creo una funcion para desarrolar el ejericio
    d = 1  #me ayuda en el proceso
    e = 1 #en esta variable voy almacenando las multiplicaciones. 
    while d <= b: #condicional para que el algoritmo sepa donde detenerse
        e = e * a #aqui le voy agregando los resultados de las multiplicaciones
        d = d + 1 #le sumo a d 1 para aumentar su valor y que este llegue a ser menor o igual a b      
    return e
operan=int(input("ingrese el numero de potencias que quiere encontrar: "))
cont=0
cont2=00
conttotal=0
for i in range(0,operan,1): #este ciclo pide numeros de entrada hasta que se llegue a la cantidad de pares deseada, en ese momento se detiene el algoritmo
    a=int(input("ingrese el valor de a: ")) #aqui pregunto por a que es el numerador
    b=int(input("ingrese el valor de b: ")) #aqui pregunto por b que es el exponente 
    conttotal=conttotal+1 #contador de operaciones totales
    if a_power_b(a,b)%2==0: #contador de pares
        cont=cont+1       
    elif a_power_b(a,b)%2!=0: #contador impares
        cont2=cont2+1 
    print("el resultado de numero a elevado al numero b es: "+str(a_power_b(a,b)))#impresion de resultado de cada potencia
print("el numero de veces en el que la potencia fue par es: "+str(cont))#contador de pares
print("el numero de veces en el que la potencia fue impar es: "+str(cont2))#contador de impares
print("el numero de veces en que se calcularon potencias fue: "+str(conttotal))  #contador de operaciones         

listaA=[0]*operan
arregloA=np.array(listaA)
for i in range (0,listaA):
    print(i)
listaB=[0]*operan
arregloB=np.array(listaB)

print




