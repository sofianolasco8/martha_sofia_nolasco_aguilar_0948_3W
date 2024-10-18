print(" ")
print("nolasco_aguilar_martha_sofia_0948_3w")
print(" ")

# abrir  diccionario 
thisdict = {
    "hola": "hello",
    "adiós": "goodbye",
    "gracias": "thank you",
    "por favor": "please",
    "sí": "yes",
    "no": "no"
}

# indicar al usuario que ingrese una frase 
frase = input("ingresa una frase en español ")

# Traducir palabra 
resultado = []
for palabra in frase.split():
    # Si la palabra está en el diccionario traducir si no dejarla sin traducir
    if palabra in thisdict:
        resultado.append(thisdict[palabra])
    else:
        resultado.append(palabra)  # Dejar la palabra sin traducir

# Mostrar la traducción
print("la traduccion es :", " ".join(resultado))


