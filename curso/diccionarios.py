
#declarar
diccionario = {
    "nombres": ["Juan", "Maria", "Pedro"],
    "edad": [20, 30, 40],
    "sexo": ["M", "F", "M"],
}

print(diccionario)

#diccionario de vectores
vector1 = [1,2,3,1,5,2,1,2,4,5,7,85,3,3,2,1,2,45,6,6,4,3,4,5,6,44,33,33234,12]
vector2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w", "x", "y", "z"]
vector3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w", "x", "y", "z"]

#agregar a diccionario
diccionario2 = {"vector1": vector1, "vector2": vector2, "vector3": vector3}
print(diccionario2)

#eliminar elemento de diccionario
del diccionario2['vector1']
print(diccionario2)

#eliminar elemento en especifico de diccionario
del diccionario2['vector2'][0]
del diccionario2['vector3'][1]
print(diccionario2)
