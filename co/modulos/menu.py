import os

def CreateMenu():
    msg = """

    1. Registrar Dependencia.
    2. Registrar consumo por dependencia.
    3. Ver CO2 producido.
    4. Dependencia que produce mayor CO2.
    5. Salir.

    """

    options = ['1', '2', '3', '4', '5']


    os.system('cls')
    print(msg)
    opt = input('Ingresa la opción\n-> ')

    while opt not in options:
        os.system('cls')        
        print('La opción no es válida')
        print(msg)
        opt = input('Ingresa la opción nuevamente\n-> ')
    return opt