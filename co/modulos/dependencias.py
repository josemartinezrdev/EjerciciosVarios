import os

def AddDependence(lstDependencies:dict, lstOffices, lstDevicesOffice):
    os.system('cls')

    nombre = input(f'Ingrese el nombre de la dependencia\n-> ')

    dependence = {
        'nombre': nombre,
        'Consumo Transporte': 0.0,
        'Consumo Dispositivos': 0.0,
        'Oficinas': [],
        'Autos': [],
        'CO2': 0.0,
    }

    lstDependencies.update({nombre:dependence})

    opt = bool(input('Desea añadir otra dependencia? | Si / Enter |\n-> '))
    if opt == True:
        AddDependence(lstDependencies, lstOffices, lstDevicesOffice)
    else:
        os.system('pause')
        return