# Simulador de Procesos Concurrentes

Programa desarrollado en Python que simula el procesamiento de varias tareas mediante **multihilos**. Utiliza una cola de tareas para distribuir el trabajo entre diferentes hilos, representando de forma sencilla el funcionamiento de un sistema con varios trabajadores ejecutando tareas concurrentemente.

## Características

* Uso de múltiples hilos con `threading`.
* Cola de tareas mediante `Queue`.
* Distribución de tareas entre los hilos disponibles.
* Simulación del tiempo de procesamiento.
* Barras de progreso para visualizar las tareas.
* Espera de todos los hilos antes de finalizar el programa.

## Tecnologías utilizadas

* **Python**
* **threading** — creación y ejecución de hilos.
* **queue** — administración segura de las tareas compartidas.
* **Rich** — interfaz visual para mostrar el progreso.

## 1. Importación de módulos

```python
import time
import threading
from queue import Queue
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn
```

`time` permite simular el tiempo de procesamiento.

`threading` permite crear varios hilos que pueden trabajar concurrentemente.

`Queue` proporciona una cola segura para compartir tareas entre diferentes hilos.

`Rich` se utiliza para mostrar barras de progreso en la terminal.

## 2. Clase principal

```python
class SimuladorProcesos:
    def __init__(self, numero_nucleos: int = 3):
        self.cola_tareas = Queue()
        self.numero_nucleos = numero_nucleos
```

La clase `SimuladorProcesos` contiene la lógica principal del programa.

`cola_tareas` almacena los procesos pendientes de ejecución.

`numero_nucleos` determina cuántos hilos trabajadores serán utilizados por el simulador.

## 3. Agregar procesos

```python
def agregar_proceso(self, nombre: str, carga_trabajo: int):
    self.cola_tareas.put({
        "nombre": nombre,
        "carga": carga_trabajo
    })
```

Cada proceso se agrega a la cola con un nombre y una carga de trabajo.

La cola permite que los hilos puedan obtener las tareas pendientes de manera segura.

## 4. Procesamiento mediante hilos

```python
def procesar_tarea(self, progress, hilo_id: int):
    while not self.cola_tareas.empty():
        tarea = self.cola_tareas.get()

        nombre = tarea["nombre"]
        carga = tarea["carga"]
```

Cada hilo ejecuta `procesar_tarea`.

Mientras existan tareas pendientes, el hilo obtiene una tarea de la cola y comienza a procesarla.

El identificador `hilo_id` permite mostrar qué hilo está ejecutando cada tarea.

## 5. Simulación del procesamiento

```python
for _ in range(carga):
    time.sleep(0.05)
    progress.advance(id_barra)
```

El programa utiliza `time.sleep` para simular que cada proceso necesita cierto tiempo para completarse.

La cantidad de iteraciones depende de la carga de trabajo asignada a la tarea.

## 6. Finalización de una tarea

```python
self.cola_tareas.task_done()
```

Cuando un hilo termina una tarea, `task_done` indica a la cola que ese trabajo fue completado correctamente.

Esto permite llevar el control de las tareas procesadas.

## 7. Creación de los hilos

```python
hilos = []

for i in range(1, self.numero_nucleos + 1):
    hilo = threading.Thread(
        target=self.procesar_tarea,
        args=(progress, i)
    )

    hilos.append(hilo)
    hilo.start()
```

Se crean varios hilos utilizando `threading.Thread`.

Cada hilo ejecuta el método `procesar_tarea` y recibe un identificador diferente.

Al utilizar varios hilos, varias tareas pueden estar siendo procesadas al mismo tiempo.

## 8. Esperar a que terminen los hilos

```python
for hilo in hilos:
    hilo.join()
```

`join` hace que el programa principal espere hasta que cada hilo termine.

De esta manera, el programa no muestra que todo terminó hasta que todos los trabajadores hayan finalizado sus tareas.

## 9. Procesos utilizados en la simulación

```python
simulador.agregar_proceso("Renderizado Textura A", 180)
simulador.agregar_proceso("Calculo de Fisicas", 280)
simulador.agregar_proceso("Generacion de Terreno", 150)
simulador.agregar_proceso("Carga de Audios", 30)
simulador.agregar_proceso("Guardado en Base de Datos", 90)
```

Se agregan diferentes tareas con cargas de trabajo distintas.

Estas tareas representan operaciones que podrían existir dentro de un sistema informático, aunque en este programa su procesamiento solamente es simulado.

## 10. Ejecución

```python
if __name__ == "__main__":
    simulador = SimuladorProcesos(numero_nucleos=3)

    simulador.agregar_proceso("Renderizado Textura A", 180)
    simulador.agregar_proceso("Calculo de Fisicas", 280)
    simulador.agregar_proceso("Generacion de Terreno", 150)
    simulador.agregar_proceso("Carga de Audios", 30)
    simulador.agregar_proceso("Guardado en Base de Datos", 90)

    simulador.ejecutar()
```

Se crea un simulador con tres trabajadores y se cargan cinco tareas.

Después se ejecuta el procesamiento concurrente.

## Resultados

<img width="656" height="143" alt="image" src="https://github.com/user-attachments/assets/df9b5d7c-4274-4f56-86d2-b276a648a327" />


* Ejecución del programa.
* Tareas siendo procesadas simultáneamente.
* Barras de progreso.
* Finalización de todos los procesos.
