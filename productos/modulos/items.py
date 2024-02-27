import modulos.menu as mn


def AddProducts(lstProductos: dict, isModified=False):
    mn.Clear()

    if isModified == True:

        while True:

            idp = input(
                'Ingrese el Código del producto que desea modificar:\n-> ')
            mn.Clear()
            restaStock = int(
                input(f'Ingrese la cantidad que le desea restar al stock actual:\n-> '))
            mn.Clear()
            sumaStock = int(
                input(f'Ingrese la cantidad que le desea sumar al stock actual:\n-> '))
            mn.Clear()

            lstProductos[idp]['stockAct'] = lstProductos[idp]['stockAct'] - restaStock
            lstProductos[idp]['stockAct'] = lstProductos[idp]['stockAct'] + sumaStock

            op = bool(input('Desea modificar otro producto? Si / Enter:\n-> '))
            if op == False:
                break
    else:

        while True:

            idp = input('Ingrese el Código del producto:\n-> ')
            mn.Clear()
            nameProduct = input(
                f'Ingrese el Nombre del producto con el código {idp}\n-> ')
            mn.Clear()
            purchaseValue = int(
                input(f'Ingrese el valor de compra del producto: {nameProduct}\n-> '))
            mn.Clear()
            saleValue = int(
                input(f'Ingrese el valor de venta del producto: {nameProduct}\n-> '))
            mn.Clear()
            stockMin = int(
                input(f'Ingrese el stock mínimo de {nameProduct}\n-> '))
            mn.Clear()
            stockMax = int(
                input(f'Ingrese el stock máximo de {nameProduct}\n-> '))
            mn.Clear()
            stockAct = int(input(f'Ingrese la cantidad de productos que hay actualmente min: {
                           stockMin}, max: {stockMax}: para el producto: {nameProduct}\n-> '))
            mn.Clear()
            nameSupplier = input(f'Ingrese el nombre del proveedor del producto: {
                                 nameProduct}\n-> ')
            mn.Clear()

            producto = {
                'idp': idp,
                'nameProduct': nameProduct,
                'purchaseValue': purchaseValue,
                'saleValue': saleValue,
                'stockMin': stockMin,
                'stockMax': stockMax,
                'stockAct': stockAct,
                'nameSupplier': nameSupplier,
            }

            lstProductos.update({idp: producto})

            op = bool(input('Desea añadir otro producto? Si / Enter:\n-> '))
            if op == False:
                break


def ViewProducts(lstProductos: dict):
    for idx, item in lstProductos.items():
        print('Producto:\n')
        for i, it in item.items():
            print(f'{i}: {it}\n')
        print('- - - - - - - - - - - - - - -\n')
    mn.Pause()


def CriticalProducts(lstProductos: dict):

    for idx, item in lstProductos.items():
        if item['stockAct'] < item['stockMin']:
            print('Productos por debajo del stock mínimo:\n')
            print(f'{item['nameProduct']}:\nStock Mínimo: {item['stockMin']}\nStock Actual: {item['stockAct']}\n')
            print('- - - - - - - - - - - - - - -\n')
        else:
            print('No hay productos fuera del stock mínimo')
    mn.Pause()


def BenefitProducts(lstProductos: dict):
    for idx, item in lstProductos.items():
        benefit = round(((item['saleValue'] - item['purchaseValue']) * item['stockAct']),2)
        print(f'\nLa ganancia potencial del producto: {item['nameProduct']} es de:\n{benefit}\n')
    mn.Pause()
