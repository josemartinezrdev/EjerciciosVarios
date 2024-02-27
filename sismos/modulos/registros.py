import os
import sismos.modulos.menu as m

#!Borrar antes de enviar
# def VerificarCities(lstCities: list):
#     for idx, item in enumerate(lstCities):
#         print(f'{idx+1}. {str(item[0])}')
#         if idx >= 5:
#             break
#     opt = int(input('Ingrese la ciudad que quiere ver sus registros en sismos:\n-> '))
#     if opt == 1:
#         if lstCities[0-1][0] == lstCities[opt-1][0]:
#             print(f'La ciudad {lstCities[opt-1][0]} esta registrada')
#             os.system('pause')
#             InformeRiesgo(lstCities, opt)
#         else:
#             print(lstCities[0-1][0])
#             print(f'la ciudad {lstCities[opt-1][0]} no esta registrada')
#             os.system('pause')
#             VerificarCities(lstCities)

def InformeRiesgo(lstCities: list):

#? lstCities[0=[0='a', 1=5.5, 2=5.8 3=...],   1=['b'],   2=['c'], 3=['d'], 4=['e']]
    
    suma = 0

    amarillo = []  # < 2,5
    naranja = []  # 2,6 - 4,5
    rojo = []  # > 4,5

    for opt, item in enumerate(lstCities):
        for i in item:
            if type(i) in (int, float):
                suma += i
        promedio = round(suma / (len(item)-1), 2)

        if promedio < 2.5:
            amarillo.append(item)
            suma = 0
        elif (promedio > 2.6) and (promedio <= 4.5):
            naranja.append(item)
            suma = 0
        elif promedio > 4.5:
            rojo.append(item)
            suma = 0
        if opt > 5:
            break

    ViewRiesgos(amarillo, naranja, rojo)

    
def ViewRiesgos(amarillo, naranja, rojo):
    os.system('cls')
    print('Las ciudades que están sin riesgo son:')
    print(amarillo)
    print('Las ciudades que están con riesgo medio son:')
    print(naranja)
    print('Las ciudades que están con riesgo alto son:')
    print(rojo)
    os.system('pause')
