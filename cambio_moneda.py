# denominaciones del euro en centimos, de mayor a menor
# trabajo en centimos enteros para evitar errores de precision con los float
DENOMINACIONES = [50000, 20000, 10000, 5000, 2000, 1000, 500,
                  200, 100, 50, 20, 10, 5, 2, 1]


def cambio_voraz(cantidad):
    # paso la cantidad a centimos y redondeo para que no se cuele un error de float
    resto = round(cantidad * 100)
    resultado = {}

    # recorro de mayor a menor en cada paso cojo todas las que quepan 
    for valor in DENOMINACIONES:
        cantidad_usada = resto // valor

        if cantidad_usada > 0:
            resultado[valor] = cantidad_usada

        # modulo: lo que queda por devolver despues de usar esas monedas
        resto = resto % valor
    return resultado


def mostrar_reporte(cantidad, resultado):
    print("cambio para", cantidad, "euros")
    for valor, n in resultado.items():
        # vuelvo a euros solo para mostrarlo
        if valor >= 500:
            tipo = "billete de"
        else:
            tipo = "moneda de"
        print(n, "x", tipo, valor / 100, "euros")


try:
    # pido el input y lo convierto a float, cambio la coma por punto por si ponen 12,50
    texto_input = input("introduce la cantidad en euros: ")
    cantidad = float(texto_input.replace(",", "."))
    resultado = cambio_voraz(cantidad)
    mostrar_reporte(cantidad, resultado)
except ValueError:
    # control basico por si alguien mete texto en vez de numeros
    print("error: tienes que meter un numero valido")
