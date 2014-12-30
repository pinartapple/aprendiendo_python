def es_par(numero):
    return(numero % 2 == 0)

def decir_hola_marta():
    print("Hola marta")

# Obtener la lista de los numeros pares del 0 al 100

lista_numeros_pares = []

# lista_numeros_pares.append(8)

#for num in range(0, 101):
#    print(num)

#print(101 % 2)

lista_numeros_pares = []

for num in range(0, 101):
    if es_par(num):
        lista_numeros_pares.append(num)

print("######################################")
print("#       LISTA DE NUMEROS PARES       #")
print("######################################")
print("")
print(lista_numeros_pares)
print(" ------ ")
for num in lista_numeros_pares:
    print(num)
print("######################################")
print("#           SOMOS PARES :D           #")
print("######################################")
