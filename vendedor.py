# Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero
# obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes
# tomando en cuenta su sueldo base y comisiones
# Inicio
# 	Leer sb, v1, v2, v3
# 	tot_vta = v1 + v2 + v3
# 	com = tot_vta * 0.10
# 	tpag = sb + com
# 	Imprimir tpag, com
# Fin

class Vendedor:
    def __init__(self):
        self.nombre = input('Ingrese su nombre: ')
        self.sueldo = float(input('Ingrese su sueldo base: $ '))

    def comision(self):
        self.venta_1 = float(input('Ingrese el valor de la primera venta: $ '))
        self.venta_2 = float(input('Ingrese el valor de la segunda venta: $ '))
        self.venta_3 = float(input('Ingrese el valor de la tercera venta: $ '))
        return (self.venta_1 + self.venta_2 + self.venta_3) * 0.1


vendedor_1 = Vendedor()
comision = vendedor_1.comision()
total = vendedor_1.sueldo + comision
print(f'\nVendedor: {vendedor_1.nombre}\nSueldo base: $ {vendedor_1.sueldo}\nComisión: $ {comision}\nTotal a pagar: $ {total}')
print('------------------------------\n')

vendedor_2 = Vendedor()
comision = vendedor_2.comision()
total = vendedor_2.sueldo + comision
print(f'\nVendedor: {vendedor_2.nombre}\nSueldo base: $ {vendedor_2.sueldo}\nComisión: $ {comision}\nTotal a pagar: $ {total}')
print('------------------------------\n')

