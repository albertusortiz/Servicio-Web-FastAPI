
palabra = "a"
arreglo = ["ab", "a"]

def contar_palabras(arreglo, palabra=None):

    total_palabras_arreglo = 0
    
    for valor in arreglo:
        if palabra in valor:
            total_palabras_arreglo +=  1
        
    total_palabra = arreglo.count(palabra)

    return(total_palabra, total_palabras_arreglo)

print(contar_palabras(arreglo, palabra))