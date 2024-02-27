import os 

def CreateMenuConsumo():
    msg = """

    1. Registrar Oficina
    2. Ver Dispositivos
    3. Registrar Automóviles
    4. Salir.

    """

    options = ['1', '2', '3', '4']

    os.system('cls')
    print(msg)
    opt = input('Ingresa la opción\n-> ')

    while opt not in options:
        print('La opción no es válida')
        opt = input('Ingresa la opción nuevamente\n-> ')

    return opt