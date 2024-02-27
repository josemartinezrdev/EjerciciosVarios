import modulos.menu as me
import modulos.dependencias as dep
import modulos.consumo.menuConsumo as mec
import modulos.consumo.consumos as con
import modulos.consumo.co as co2
from modulos.consumo.consumos import lstDevices

if __name__ == "__main__":

    # {'cop': {'nombre': 'cop', 'Consumo Transporte': 0.0, 'Consumo Dispositivos': 0.0, 'Oficinas': [{'nombre': 'bog', 'Dispositivos': [{'nombre': 'Computador', 'factorConsumo': 0.45, 'cantidad': 5, 'timePower': 8}, {'nombre': 'Teléfono', 'factorConsumo': 0.05, 'cantidad': 5, 'timePower': 18}], 'Autos': {}, 'Consumo Total': 0.0}], 'CO2': 0.0}, 'bra': {'nombre': 'bra', 'Consumo Transporte': 0.0, 'Consumo Dispositivos': 0.0, 'Oficinas': [{'nombre': 'rjn', 'Dispositivos': [{'nombre': 'Bombillos', 'factorConsumo': 0.015, 'cantidad': 50, 'timePower': 24}, {'nombre': 'Microondas', 'factorConsumo': 0.8, 'cantidad': 5, 'timePower': 9}], 'Autos': {}, 'Consumo Total': 0.0}], 'CO2': 0.0}}

    lstDependencies = {}
    lstOffices = {}
    lstDevicesOffice = []

    isRunning = True
    while isRunning:
        opt = me.CreateMenu()
        if opt == '1':
            dep.AddDependence(lstDependencies, lstOffices, lstDevicesOffice)
        elif opt == '2':
            optConsumo = mec.CreateMenuConsumo()
            if optConsumo == '1':
                con.AddOffice(lstDependencies)
            elif optConsumo == '2':
                con.os.system('cls')
                con.ViewDevice(lstDevices)
                con.os.system('pause')
            elif optConsumo == '3':
                con.AddCar(lstDependencies)

        elif opt == '3':
            co2.ViewCO2(lstDependencies)
        elif opt == '4':
            co2.MayorCO2(lstDependencies)
        elif opt == '5':
            isRunning = False
