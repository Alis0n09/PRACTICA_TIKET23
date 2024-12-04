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

def consultarMulta(tipoMulta):
    if tipoMulta == 1:
        return 10/100*100
    elif tipoMulta ==2:
        return 15/100*100
    elif tipoMulta == 3:
        return 20/100*100
    elif tipoMulta == 4:
        return 30/100*100
    else:
        return -1

def calcularValorDescuento(precio,porcentajedescuento):
    valorDescuento = precio*porcentajedescuento
    resultado= valorDescuento/100
    return resultado