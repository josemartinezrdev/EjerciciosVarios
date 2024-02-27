import os

def Clear():
    osy = os.name
    if osy == 'posix':
        os.system('clear')
    elif osy == 'nt':
        os.system('cls')

def Pause():
    osy = os.name
    if os.name == 'nt':
        os.system('pause')
    elif os.name == 'posix':
        input("Presiona Enter para continuar...")

def CreateMenu():

    options = ['1', '2', '3', '4', '5', '6']

    msg = """

    Elige una opción:

    1. Registrar Productos
    2. Ver Productos
    3. Actualizar Productos
    4. Productos Críticos
    5. Ganancia Potencial Productos
    6. Salir

    """

    os.system('cls')
    print(msg)
    opt = input('\n-> ')

    if opt not in options:
        print(f'La opción {opt} no es valida')
        os.system('pause')
    else:
        return opt