# Modulo para introducir los gastos en una hoja de exel

data = {}
option = 0

def menuppl():
    print('{:-^20}'.format('Menu Principal'))
    print('1. Cargar factura')
    print('2. Salir')

def menu_carga_fac():
    datalst = []
    print('{:-^20}'.format('Menu de carga'))
    shop = input('Ingresa "M" para Carrefour\n"D" para Dia\n"C" para Coto\n"V" para verduleria\n"')


while option != 5:
    menuppl()
    option = int(input('Escoje la opcion deseada: '))
    if option == 1:
        data = menu_carga_fac()

menuppl()