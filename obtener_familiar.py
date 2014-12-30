# -*- coding: utf-8 -*-

ana = {
    "nombre": "Ana",
    "apellidos": "Palomero González",
    "telefono": "1234567890"
}

paco = {
    "nombre": "Paco",
    "apellidos": "Martínez Soria",
    "telefono": "1234567890"
}

pedro = {
    "nombre": "Pedro",
    "apellidos": "Tornavacas de la Rosa",
    "telefono": "1234567890"
}

def imprimir_familiar(familiar):
    print("~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~")
    print(familiar["nombre"] + " :D " + familiar["apellidos"] + " (^.^) " + familiar["telefono"])
    print("~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~·~")
    print("                                              ooooooooooo")
    print("                                           ooooooooooooooooo")
    print("                                        ooooooooooooooooooooooo")
    print("                                    oooooo                   oooooo")
    print("                                  oooooo                       oooooo")
    print("                            oooooooooooo      oo       oo       ooooooooooo")
    print("                        ooooooooooooo        oooo     oooo        oooooooooooo")
    print("                       oooooooooooo           oo       oo           oooooooooooo")
    print("                        ooooooooooooo                              ooooooooooo")
    print("                               ooooooo         oo      oo          oooooooo")
    print("                                   ooooo         oooooo           ooooo")
    print("                                      ooo                      ooo")
    print("                                        ooooooo           ooooooo")
    print("                                            oooooooooooooooo")
    print("                                               oooooooooo")

def buscar_familiares(cadena_de_busqueda):
    familiares = [ana, paco, pedro]

    familiares_buscados = []

    for familiar in familiares:
        if cadena_de_busqueda.lower() in familiar["nombre"].lower():
            familiares_buscados.append(familiar)
        elif cadena_de_busqueda == familiar["telefono"]:
            familiares_buscados.append(familiar)
        elif cadena_de_busqueda.lower() in familiar["apellidos"].lower():
            familiares_buscados.append(familiar)

    return familiares_buscados


busqueda = "Tornavacas"
familiares_encontrados = buscar_familiares(busqueda)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+++                 LA FAMILIA ¬¬                       +++")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")
print("==> Has buscado: " + busqueda)

for familiar in familiares_encontrados:
    imprimir_familiar(familiar)
