def potenciacion(base, exponente):
    return base ** exponente

def radicacion(base, indice):
    if indice == 0:
        return "Error: índice de raíz cero"
    return base ** (1 / indice)

