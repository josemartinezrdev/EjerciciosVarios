import modulos.menu as mn
import modulos.items as it

if __name__ == "__main__":

    lstProductos = {}
    isRunning = True

    while isRunning == True:
        mn.Clear()

        opt = mn.CreateMenu()

        if opt == '1':
            it.AddProducts(lstProductos)
        elif opt == '2':
            it.ViewProducts(lstProductos)
        elif opt == '3':
            it.AddProducts(lstProductos, True)
        elif opt == '4':
            it.CriticalProducts(lstProductos)
        elif opt == '5':
            it.BenefitProducts(lstProductos)
        elif opt == '6':
            isRunning = False
