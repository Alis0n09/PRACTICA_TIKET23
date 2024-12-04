def calcularPromedio(val1,val2,val3):
    calculo=val1+val2+val3
    promedio1=calculo/3
    return promedio1

def calcularSubtotal(precio,cantidad,porcentaje):
    subtotalsindescuento = precio*cantidad
    descuento= (subtotalsindescuento*porcentaje)/100
    subtotal= subtotalsindescuento-descuento
    return subtotal

def calcularValorHora(val1):
    resultado= val1/160
    return resultado

def calcularTipoMulta(tipoMulta):
    
    return

def calcularValorDescuento(precio,porcentajedescuento):
    valorDescuento = precio*porcentajedescuento
    resultado= valorDescuento/100
    return resultado