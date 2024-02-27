import os

lstDevices = {
    1 : {'nombre': 'Computador','factorConsumo': 0.45, 'cantidad': 0, 'timePower': 0},
    2 : {'nombre': 'Teléfono','factorConsumo': 0.05, 'cantidad': 0, 'timePower': 0},
    3 : {'nombre': 'Televisor','factorConsumo': 0.26, 'cantidad': 0, 'timePower': 0},
    4 : {'nombre': 'Modem','factorConsumo': 0.02, 'cantidad': 0, 'timePower': 0},
    5 : {'nombre': 'Cámaras','factorConsumo': 0.015, 'cantidad': 0, 'timePower': 0},
    6 : {'nombre': 'Impresora','factorConsumo': 0.35, 'cantidad': 0, 'timePower': 0},
    7 : {'nombre': 'Microondas','factorConsumo': 0.8, 'cantidad': 0, 'timePower': 0},
    8 : {'nombre': 'Cafetera','factorConsumo': 0.720, 'cantidad': 0, 'timePower': 0},
    9 : {'nombre': 'Aire','factorConsumo': 3.5, 'cantidad': 0, 'timePower': 0},
    10 : {'nombre': 'Bombillos','factorConsumo': 0.015, 'cantidad': 0, 'timePower': 0},
    11 : {'nombre': 'Dis. Agua','factorConsumo': 0.1, 'cantidad': 0, 'timePower': 0},
}

def AddOffice(lstDependencies: dict):
    os.system('cls')

    nombreDep = input(f'Ingrese el nombre de la dependencia\n-> ')

    if nombreDep not in lstDependencies:
        print(f'La dependencia {nombreDep} no está registrada')
        os.system('pause')
        return
    else:

        nombreOffice = input('Ingrese el nombre de la oficina\n-> ')

        office = {
            'nombre': nombreOffice,
            'Dispositivos': AddDevice(lstDevices),
        }

        #! OFICINA A LA DEPENDENCIA QUE ES
        lstDependencies.setdefault(nombreDep, {'nombre': nombreDep, 'Consumo Transporte': 0.0, 'Consumo Dispositivos': 0.0, 'Oficinas': [], 'CO2': 0.0})['Oficinas'].append(office)
        opt = bool(input('Desea añadir otra oficina? | Si / Enter |\n-> '))
        if opt == True:
            AddOffice(lstDependencies)
        else:
            DataProcessingDevices(lstDependencies)
            os.system('pause')
            return
        
def ViewDevice(lstDevices: dict):
    for idx, item in lstDevices.items():
        print(f'{idx}. {item["nombre"]}')

def AddDevice(lstDevices: dict):

    os.system('cls')
    print('Añada los dispositivos que hay en la oficina\n')

    lstDevicesOffice = []

    while True:
        ViewDevice(lstDevices)
        opt = int(input('\n-> '))
        if opt not in lstDevices:
            print('La opción ingresada no es válida')
            os.system('pause')
            continue

        cantidad = int(input('Añada la cantidad de dispositivos\n-> '))
        timePower = int(input('Añade la cantidad de horas que el dispositivo está encendido (Max 24) \n-> '))

        if timePower > 24:
            print('MAX 24')
            os.system('pause')
            continue

        lstDevicesOffice.append({
            'nombre': lstDevices[opt]['nombre'],
            'factorConsumo': lstDevices[opt]['factorConsumo'],
            'cantidad': cantidad,
            'timePower': timePower,
        })

        optNew = bool(input('Deseas añadir otro dispositivo? | Si / Enter |\n-> '))
        if not optNew:
            return lstDevicesOffice
        else:
            os.system('cls')
            continue

def AddCar(lstDependencies:dict):

    faCon = 0.374
    os.system('cls')
    nameDep = input('Ingrese el nombre de la dependencia en la que va a registrar el auto:\n-> ')

    if nameDep in lstDependencies:
        modelo = input(f'Ingrese el modelo del auto:\n-> ')
        kmh = float(input(f'Ingrese los km recorridos por el auto:\n-> '))

        car = {
            'modelo': modelo,
            'Km/h': kmh,
        }

        lstDependencies[nameDep]['Autos'].append({modelo:car})
        lstDependencies[nameDep]['Consumo Transporte'] += round((kmh * faCon), 2)

        #! ENVIAR A CO2 LOS DATOS
        SendCO2(lstDependencies, nameDep)

        opt = bool(input('Desea añadir otro auto? | Si / Enter |\n-> '))
        if opt == True:
            AddCar(lstDependencies)
        else:
            os.system('pause')
            return
        
    elif nameDep not in lstDependencies:
        print(f'La dependencia {nameDep} no está registrada')
        os.system('pause')
        return

def DataProcessingDevices(lstDependencies:dict):
    #lstDependencies = {Dep = { Ofs = [ Of = { Dis = [ Di = {}, Di = {}]}], Ats = [Aut = {}, Aut = {}]}}
    #{'cop': {'nombre': 'cop', 'Consumo Transporte': 0.0, 'Consumo Dispositivos': 0.0, 'Oficinas': [{'nombre': 'bog', 'Dispositivos': [{'nombre': 'Computador', 'factorConsumo': 0.45, 'cantidad': 5, 'timePower': 8}, {'nombre': 'Teléfono', 'factorConsumo': 0.05, 'cantidad': 5, 'timePower': 18}], 'Autos': {}, 'Consumo Total': 0.0}], 'CO2': 0.0}, 'bra': {'nombre': 'bra', 'Consumo Transporte': 0.0, 'Consumo Dispositivos': 0.0, 'Oficinas': [{'nombre': 'rjn', 'Dispositivos': [{'nombre': 'Bombillos', 'factorConsumo': 0.015, 'cantidad': 50, 'timePower': 24}, {'nombre': 'Microondas', 'factorConsumo': 0.8, 'cantidad': 5, 'timePower': 9}], 'Autos': {}, 'Consumo Total': 0.0}], 'CO2': 0.0}}
    # Halla consumo de cada uno: ((cantidad * factorConsumo) * timePower) * 30 = consumoMensualDevice (kWh)

    for idx, item in lstDependencies.items():
        item['Consumo Dispositivos'] = 0.0
        nameDep = item['nombre']

        for oficina in item['Oficinas']:

            for disp in oficina['Dispositivos']:

                cantidad = disp['cantidad']
                fc = disp['factorConsumo']
                timePower = disp['timePower']

                # No hay necesidad de dividir fc en 1000 pues ya esta convertido a kWh
                cd = ((cantidad * fc) * timePower) * 30
                item['Consumo Dispositivos'] += cd

            SendCO2(lstDependencies, nameDep)

def SendCO2(lstDependencies, nameDep):
    faCon = 0.374
    lstDependencies[nameDep]['CO2'] = round(lstDependencies[nameDep]['Consumo Transporte'] + ((lstDependencies[nameDep]['Consumo Dispositivos']) * faCon), 2)