def solicitar_numero (mensaje: str):
    while True:
        numero= input( mensaje)
        if validar_numero:
            return float( numero)
            break
        else:
            print("Erro, ingrese un numero valido")

def validar_numero (entrada : str) -> bool:
    return entrada.isdigit()

       