from tabulate import tabulate
import os
estudiantes = {}
pesosEstudiantes = {}

msg = """

    Opciones:
    a. Cuantos estudiantes se encuentran en peso bajo.
    b. Cuantos estudiantes se encuentran en el peso ideal.
    c. Cuantos estudiantes se encuentran en Sobrepeso
    d. Cuantos estudiantes se encuentran en obesidad grado I
    e. Cuantos estudiantes se encuentran en obesidad grado II
    f. Cuantos estudiantes se encuentran en obesidad grado III
    g. Ver todos los estudiantes
    h. salir

"""


def AddStudent(estudiantes: dict):
    os.system('cls')
    idx = input('Ingrese el ID del estudiante que va a registrar:\n-> ')
    nombre = input(f'Ingrese el nombre del estudiante con ID - {idx}:\n-> ')

    try:
        edad = int(input(f'Ingrese la edad de {nombre}:\n-> '))
    except ValueError:
        print(f'El dato debe ser de tipo numérico')
        os.system('pause')
        AddStudent(estudiantes)
    else:

        try:
            peso = float(input(f'Ingrese el peso de {nombre} en Kg:\n-> '))
            altura = float(
                input(f'Ingrese la altura de {nombre} en Mts:\n-> '))
        except ValueError:
            print(f'El dato debe ser de tipo decimal')
            os.system('pause')
            AddStudent(estudiantes)
        else:
            pass

    estudiante = {
        'idx': idx,
        'nombre': nombre,
        'edad': edad,
        'peso': peso,
        'altura': altura,
        'imc': 0.0,
        'estado': ''
    }

    estudiantes.update({idx: estudiante})

    # print(estudiante)
    # print(estudiantes)


def ViewStudents(estudiantes: dict):
    os.system('cls')
    titulo = """

        +++++++++++++++++++++++++++
        +   LISTADO ESTUDIANTES   +
        +++++++++++++++++++++++++++

    """
    print(titulo)
    est = []
    for key, value in estudiantes.items():
        est.append(value)
    print(tabulate(est, headers="keys", stralign='center', tablefmt='pretty'))


def HallarImc(estudiantes: dict, pesosEstudiantes: dict) :
    for idx, item in estudiantes.items():
        estudiantes[idx]['imc'] = round((estudiantes[idx]['peso']) / (estudiantes[idx]['altura'])**2, 1)

    if (estudiantes[idx]['imc'] < 18.5):
        estudiantes[idx]['estado'] = 'PB'
    elif (estudiantes[idx]['imc'] >= 18.5) and estudiantes[idx]['imc'] <= 24.9:
        estudiantes[idx]['estado'] = 'N'
    elif (estudiantes[idx]['imc'] >= 25.0) and estudiantes[idx]['imc'] <= 29.9:
        estudiantes[idx]['estado'] = 'SP'
    elif (estudiantes[idx]['imc'] >= 30.0) and estudiantes[idx]['imc'] <= 34.9:
        estudiantes[idx]['estado'] = 'OB1'
    elif (estudiantes[idx]['imc'] >= 35.0) and estudiantes[idx]['imc'] <= 39.9:
        estudiantes[idx]['estado'] = 'OB2'
    elif (estudiantes[idx]['imc'] >= 40.0):
        estudiantes[idx]['estado'] = 'OB3'
    else:
        print(f'El IMC {estudiantes[idx]['imc']} no corresponde a ningún estado...')

    pesos = {
        'idx': idx,
        'nombre': estudiantes[idx]['nombre'],
        'imc': estudiantes[idx]['imc'],
        'estado': estudiantes[idx]['estado']
    }

    if (estudiantes[idx]['imc'] < 18.5):
        pesosEstudiantes.update({idx:pesos})
    elif (estudiantes[idx]['imc'] >= 18.5) and estudiantes[idx]['imc'] <= 24.9:
        pesosEstudiantes.update({idx:pesos})
    elif (estudiantes[idx]['imc'] >= 25.0) and estudiantes[idx]['imc'] <= 29.9:
        pesosEstudiantes.update({idx:pesos})
    elif (estudiantes[idx]['imc'] >= 30.0) and estudiantes[idx]['imc'] <= 34.9:
        pesosEstudiantes.update({idx:pesos})
    elif (estudiantes[idx]['imc'] >= 35.0) and estudiantes[idx]['imc'] <= 39.9:
        pesosEstudiantes.update({idx:pesos})
    elif (estudiantes[idx]['imc'] >= 40.0):
        pesosEstudiantes.update({idx:pesos})


def ViewPesos(pesosEstudiantes: dict): 
    os.system('cls')
    est = []

    print(msg)
    opcion = input('-> ')

    os.system('cls')

    if opcion.lower() == 'a':
        for i in pesosEstudiantes:
            if pesosEstudiantes[i]['estado'] == 'PB':
                est.append(pesosEstudiantes[i])
    elif opcion.lower() == 'b':
        for i in pesosEstudiantes:
            if pesosEstudiantes[i]['estado'] == 'N':
                est.append(pesosEstudiantes[i])
    elif opcion.lower() == 'c':
        for i in pesosEstudiantes:
            if pesosEstudiantes[i]['estado'] == 'SP':
                est.append(pesosEstudiantes[i])
    elif opcion.lower() == 'd':
        for i in pesosEstudiantes:
            if pesosEstudiantes[i]['estado'] == 'OB1':
                est.append(pesosEstudiantes[i])
    elif opcion.lower() == 'e':
        for i in pesosEstudiantes:
            if pesosEstudiantes[i]['estado'] == 'OB2':
                est.append(pesosEstudiantes[i])
    elif opcion.lower() == 'f':
        for i in pesosEstudiantes:
            if pesosEstudiantes[i]['estado'] == 'OB3':
                est.append(pesosEstudiantes[i])
    elif opcion.lower() == 'g':
        ViewStudents(estudiantes)
    elif opcion.lower() == 'h':
        return
    else:
        print('La opcion no es valida')
        os.system('pause')
        ViewPesos(estudiantes)
    

    print(tabulate(est, headers="keys", stralign='center', tablefmt='pretty'))
    os.system('pause')
    os.system('cls')
    ViewPesos(pesosEstudiantes)


for _ in range(20):  # ! Cambiar a 20 para usar correctamente
    AddStudent(estudiantes)
    HallarImc(estudiantes, pesosEstudiantes)

ViewPesos(pesosEstudiantes)
