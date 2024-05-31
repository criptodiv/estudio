#Ejercicio de agregar pokemones:
import os
os.system('cls')

pokemones = []

while True:
    print("     POKEDEX")
    print("1. Agregar pokemon")
    print("2. Actualizar pokemon")
    print("3. Ver pokemones")
    print("4. Ver pokemon")
    print("5. Eliminar pokemon")
    print("6. Salir")
    opc = int(input("Ingrese opción: "))
    if opc==1:
        print("AGREGAR POKEMON")
        nombre = input("Ingrese nombre: ")
        tipo = input("Ingrese tipo: ")
        nivel = int(input("Ingrese nivel: "))

        pokemon = {
            "nro": len(pokemones)+1,
            "nombre": nombre,
            "tipo": tipo,
            "nivel": nivel
        }
        pokemones.append(pokemon)
        print("POKEMON AGREGADO!")

    elif opc==2:
        numero = int(input("Ingrese número pokemon: "))
        for x in range(len(pokemones)):
            if pokemones[x]["nro"]==numero:
                nivel = input("Ingrese nuevo nivel: ")
                pokemones[x]["nivel"] = nivel
                #pokemones[x].update({"nivel": nivel})
                break
    elif opc==3:
        print(pokemones)
    elif opc==4:
        numero = int(input("Ingres número pokemon: "))
        for x in range(len(pokemones)):
            if pokemones[x]["nro"]==numero:
                print(pokemones[x])
                break
    elif opc==5:
        numero = int(input("Ingrese número: "))
        for x in range(pokemones):
            if pokemones[x]["nro"]==numero:
                pokemones.pop(x)
                break
    else:
        print("ADIOS!")
        break