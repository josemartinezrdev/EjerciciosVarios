import sismos.modulos.menu as m
import sismos.modulos.ciudades as c
import sismos.modulos.registros as r

if __name__ == "__main__":

    lstCities = [] * 5


    isRunning = True
    while isRunning:
        opt = m.CreateMenu()
        if opt == '1':
            r.os.system('cls')
            c.AddCity(lstCities)
        elif opt == '2':
            r.os.system('cls')
            c.AddQuake(lstCities)
        elif opt == '3':
            c.SearchQuakeCity(lstCities)
        elif opt == '4':
            r.InformeRiesgo(lstCities)
        elif opt == '5':
            r.os.system('cls')
            isRunning = False
