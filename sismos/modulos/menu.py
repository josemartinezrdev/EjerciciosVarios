import os

def CreateMenu():
    msg = """

    1. Registrar Ciudad
    2. Registrar Sismo
    3. Buscar sismos por ciudad
    4. Informe de riesgo
    5. Salir

    """
    options = ['1', '2', '3', '4', '5']

    os.system('cls')
    print(msg)
    opt = input('Ingresa la opción\n-> ')

    while opt not in options:
        print('La opción no es válida')
        opt = input('Ingresa la opción nuevamente\n-> ')

    return opt