# cambio-monedas

Programa en Python que calcula el cambio de una cantidad en euros con el menor número de billetes y monedas, usando el algoritmo voraz.

## Cómo ejecutarlo

```powershell
python cambio_moneda.py
```

Pide una cantidad en euros. Acepta punto o coma (`12.50` o `12,50`).

Ejemplo de salida para `12.50`:

```
cambio para 12.5 euros
1 x billete de 10.0 euros
1 x billete de 2.0 euros
1 x moneda de 0.5 euros
```

Si el texto no es un número, muestra un error.

## Cómo funciona

1. Pasa la cantidad a céntimos enteros para evitar errores de precisión con decimales.
2. Recorre las denominaciones de mayor a menor.
3. En cada paso toma todas las unidades que quepan y deja el resto para la siguiente.

Denominaciones (euros): 500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02 y 0.01. A partir de 5 € se muestran como billete; el resto, como moneda.
