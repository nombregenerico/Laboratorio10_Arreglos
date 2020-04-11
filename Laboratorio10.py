# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 20:22:08 2020

@author: abaly
"""

print("ingrese 0 en a para terminar")  
def a_power_b (a,b): #creo una funcion para desarrolar el ejericio
    d = 1  #me ayuda en el proceso
    e = 1 #en esta variable voy almacenando las multiplicaciones. 
    while d <= b: #condicional para que el algoritmo sepa donde detenerse
        e = e * a #aqui le voy agregando los resultados de las multiplicaciones
        d = d + 1 #le sumo a d 1 para aumentar su valor y que este llegue a ser menor o igual a b      
    print("el resultado de numero a elevado al numero b es: "+str(e))#hago la impresion
a=1
while a<0 or a>0:
    a=int(input("ingrese el valor de a: ")) #aqui pregunto por a
    b=int(input("ingrese el valor de b: ")) #aqui pregunto por b
    a_power_b(a,b)

      

