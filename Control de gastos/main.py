# Modulo para introducir los gastos en una hoja de exel

import datetime

today = datetime.datetime.now()
data = {}
option = 0

def menuppl():
    print('{:-^20}'.format('Menu Principal'))
    print('1. Cargar factura')
    print('2. Salir')

def menu_carga_fac():
    savelst = []
    print('{:-^20}'.format('Menu de carga'))
    fecha = input('Ingresa la fecha de compra: (dd/mm/yy)\n#')
    savelst.append(fecha)
    tienda = input('Ingresa el local donde compraste:\n\tM) para Market/Carrefour\n\tD) para Dia\n\tC) para Coto\n\tV) para verduleria\n\tF) para fiambreria\n#')
    savelst.append(tienda)
    total = float(input('Ingresa el monto total gastado:\n#'))
    savelst.append(total)
    print('Compraste en {} el dia {}, por un monto de {}'.format(savelst[0], savelst[1], savelst[2]))
    response = input('Deseas guardar la factura? (S/N)')
    if response.lower() == 's':
        data


while option != 2:
    menuppl()
    option = int(input('Escoje la opcion deseada: '))
    if option == 1:
        inv_date, shop, amount = menu_carga_fac()
        #data['agosto'] = menu_carga_fac()
