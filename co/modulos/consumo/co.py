import os

def ViewCO2(lstDependencies:dict):
    sum = 0
    for i, item in (lstDependencies).items():
        sum += item.get('CO2')
    print(f'El CO2 total producido fue de: {round(sum, 2)}')
    os.system('pause')


def MayorCO2(lstDependencies:dict):
    co2Temp = 0
    nameTemp = ''
    isAct = False
    for i, item in (lstDependencies).items():
        while isAct:
            co2Temp = item.get('CO2')
            nameTemp = item.get('nombre')
            isAct = False
        
        if ((item.get('CO2')) >= co2Temp):
            co2Temp = item.get('CO2')
            nameTemp = item.get('nombre')

    print(f'La dependencia que más CO2 produce es: {nameTemp}\nCO2: {co2Temp}')
    os.system('pause')