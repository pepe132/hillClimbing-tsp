# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:34:48 2021

@author: JOSE DOMINGUEZ G
"""

import math
import random

def distancia(coord1,coord2):
    lat1=coord1[0]
    lon1=coord1[1]
    lat2=coord2[0]
    lon2=coord2[1]
    return math.sqrt((lat1-lat2)**2+(lon1-lon2)**2)

#calcular distancia cubierta por una ruta
def evalua_ruta(ruta):
    total=0
    for i in range(0,len(ruta)-1):
        ciudad1=ruta[i]
        ciudad2=ruta[i+1]
        total=total+distancia(coord[ciudad1],coord[ciudad2])
        ciudad1=ruta[i+1]
        ciudad2=ruta[0]
        total=total+distancia(coord[ciudad1],coord[ciudad2])
    return total

def hill_climbing():
    #se crea una ruta inicial aleatoria
    ruta=[]
    for ciudad in coord:
        ruta.append(ciudad)
    mejor_ruta=ruta[:]
    max_iteraciones=10
    
    while max_iteraciones>0:
        mejora=True
        #Generamos una nueva ruta aleatoria
        random.shuffle(ruta)
        while mejora:
            mejora=False
            dist_actual=evalua_ruta(ruta)
            #evaluar ciudades vecinas
            for i in range(0,len(ruta)):
                if mejora:
                    break
                for j in range(0,len(ruta)):
                    if i!=j:
                        ruta_tmp=ruta[:]
                        ciudad_tmp=ruta_tmp[i]
                        ruta_tmp[i]=ruta_tmp[j]
                        ruta_tmp[j]=ciudad_tmp
                        dist=evalua_ruta(ruta_tmp)
                        if dist<dist_actual:
                            #encontrando el mejor vecino mejorando el resultado
                            mejora=True
                            ruta=ruta_tmp[:]
                            break
        max_iteraciones=max_iteraciones-1
        if evalua_ruta(ruta)<evalua_ruta(mejor_ruta):
            mejor_ruta=ruta[:]
    return mejor_ruta

coord={
      'Guadalajara':[20.66682, -103.39182],
      'Ciudad de Mexico':[19.42847, -99.12766],
      'Puebla':[19.03793, -98.20346],
      'Tijuana':[32.5027, -117.00371],
      'San Luis':[22.14982, -100.97916],
      'Saltillo':[25.42321, -101.0053],
      'Mexicali':[32.62781, -115.45446],
      'Cancun':[21.17429, -86.84656],
      'Morelia':[19.70078, -101.18443],
      'Chihuahua':[28.63528, -106.08889]
}

ruta=hill_climbing()
print(ruta)
print('distancia total: '+ str(evalua_ruta(ruta)))