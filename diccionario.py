#1. Lista
lista = [2,5,-6,0]

#2. Matriz
matriz_1 = [[2 , 5 ,8],[-8, 6 ,0],[4 ,-1 ,2]]

#3. Tupla
tupla_negro = (0,0,0)

#4. Diccionarió
diccionario = { "nro": 1, "nombre": "Snes", "funciona": False, "peso": 0.2
}

#           comandos para listas, matrizes y diccionarió
len(lista) #4: entrega el tamaño de la lista
lista.append(15)  #[2,5,-6,0,15]: se agrega el 15 al final
lista.insert(2,1) #[2,5,1,-6,0,15]: se agrega el 1 en la posición 2
lista.index(-6) #3: posición donde está el -6
lista.pop(3) #[2,5,1,0,15]: eliminó el valor de la posición 3
lista.remove(15) #[2,5,1,0]: eliminó el valor 15 de la lista
lista.sort() #[0,1,2,5]: ordena la lista de menor a mayor, a-z
lista.reverse() #[5,2,1,0]: invierte la lista
lista.clear() #[]: limpia toda la lista
diccionario.values() #entrega una lista con los valores del diccionario

#sirve solo para diccionarió
diccionario.keys() #entrega una lista con las llaves del diccionario