from rx import from_iterable
from rx.operators import filter, map

temperaturas_celsius = [18, 20, 25, 30, 35, 22, 28]

observable = from_iterable(temperaturas_celsius)

flujo_transformado = observable.pipe(
    filter(lambda temp: temp > 25),
    map(lambda temp: temp * 9 / 5 + 32)
)

flujo_transformado.subscribe(
    on_next=lambda x: print(f"Temperatura transformada: {x:.2f}°F"),
    on_error=lambda e: print(f"Error: {e}"),
    on_completed=lambda: print("Proceso completo")
)

