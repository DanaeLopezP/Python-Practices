# Autor: Paola Danae Lopez Perez
# Fecha: 31/05/2025

# Contadores de vocales

def vowelCount1(sentence):
    """
    Función que cuenta el número total de vocales que tiene una frase.

    Usa ciclos for anidados. Es funcional pero ineficiente a gran escala.

    Args:
        sentence (str): Frase ingresada por el usuario.

    Returns:
        int: Número total de vocales encontradas.
    """
    accum = 0
    vowels = "aeiou"
    for i in sentence.lower():
        for j in vowels:
            if i == j:
                accum += 1
    return accum

def vowelCount(sentence):
    """
    Función eficiente que cuenta el número total de vocales en una frase.

    Args:
        sentence (str): Frase ingresada por el usuario.

    Returns:
        int: Total de vocales encontradas.
    """
    accum = 0
    vowels = "aeiou"
    for i in sentence.lower():
        if i in vowels:
            accum += 1
    return accum

sentence = input("Escribe una frase: ")
print(f"Total de vocales: {vowelCount(sentence)}")
