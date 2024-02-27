import os
import sismos.modulos.menu as m

def AddCity(lstCities: list):
        os.system('cls')
        isValid = True
        i = 1
        while isValid:
            city = input(f'Ingrese la ciudad {i}/5\n-> ')
            lstCities.append([city])
            if i < 5:
                i += 1
            else:
                isValid = False
                os.system('pause')
                # No tengo necesidad de crear el menú

def AddQuake(lstCities):

    os.system('cls')

    numSis = int(input('Ingrese la cantidad de sismos, tenga en cuenta que va a ser la misma cantidad para cada ciudad\n-> '))

    sismos = []
    os.system('cls')
    i = 1
    
    isValid = True
    while isValid:
        if i > numSis:
            isValid = False
        else:
            for idx, item in enumerate(lstCities):
                if i > numSis:
                    i = 1
                    sismos = []
                    os.system('cls')
                if idx > 5:
                    isValid = False
                    break
                else:
                    while i <= numSis:
                        sismo = float(input(f'Ingrese la magnitud del sismo {i}/{numSis} para la ciudad de: {item[0]}\n-> '))
                        i += 1
                        (item).append(sismo)
    os.system('pause')
    # No crear menú porque no lo necesito

def SearchQuakeCity(lstCities):
    os.system('cls')
    for idx, item in enumerate(lstCities):
        print(f'{(idx+1)}. {str(item[0])}')
        if idx >= 5:
            break
    cityOpt = int(input('Ingrese la ciudad que quiere buscar:\n-> '))
    if (cityOpt <= 5) and (cityOpt > 0):
        for idx, item in enumerate(lstCities[cityOpt-1]):
            print(item)
        os.system('pause')
