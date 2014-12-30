familiar_ana = {
    "nombre": "Ana",
    "sexo": "mujer"
}

familiar_paca = {
    "nombre": "Paca",
    "sexo": "mujer"
}

familiar_pedro = {
    "nombre": "Pedro",
    "sexo": "hombre"
}

contador_hombres = 0
contador_mujeres = 10

# cosas nuevas

# -> familiar
for familiar in lista_familiares:
    if familiar["sexo"] == "hombre":
        contador_hombres = contador_hombres + 1
    else:
        contador_mujeres = contador_mujeres + 1

print("El numero total de mujeres es " + str(contador_mujeres))
print("El numero total de hombres es " + str(contador_hombres))
