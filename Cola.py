import time
import threading
from queue import Queue
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn

class SimuladorProcesos:
    def __init__(self, numero_nucleos: int = 3):
        #Queue es una estructura thread-safe perfecta para concurrencia
        self.cola_tareas = Queue()
        self.numero_nucleos = numero_nucleos

    def agregar_proceso(self, nombre: str, carga_trabajo: int):
        #El hilo principal actua como Productor agregando tareas
        self.cola_tareas.put({"nombre": nombre, "carga": carga_trabajo})

    def procesar_tarea(self, progress, hilo_id: int):
        #Los hilos actuan como Consumidores pidiendo trabajo
        while not self.cola_tareas.empty():
            tarea = self.cola_tareas.get()
            nombre = tarea["nombre"]
            carga = tarea["carga"]

            #Generamos una barra visual independiente para cada tarea
            id_barra = progress.add_task(f"[cyan]Nucleo {hilo_id} -> {nombre}", total=carga)

            #Simulamos el procesamiento en tiempo real
            for _ in range(carga):
                time.sleep(0.05) 
                progress.advance(id_barra)

            #Le decimos a la cola que la tarea termino exitosamente
            self.cola_tareas.task_done()

    def ejecutar(self):
        #Configuracion de la interfaz visual con Rich
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn()
        ) as progress:
            
            hilos = []
            
            #Lanzamos nuestros hilos
            for i in range(1, self.numero_nucleos + 1):
                hilo = threading.Thread(target=self.procesar_tarea, args=(progress, i))
                hilos.append(hilo)
                hilo.start()

            #Esperamos a que todos los nucleos terminen su trabajo
            for hilo in hilos:
                hilo.join()

if __name__ == "__main__":
    #Creamos un CPU virtual de 3 nucleos
    simulador = SimuladorProcesos(numero_nucleos=3)
    
    #Cargamos nuestra cola con procesos de distintos tamaños
    simulador.agregar_proceso("Renderizado Textura A", 180)
    simulador.agregar_proceso("Calculo de Fisicas", 280)
    simulador.agregar_proceso("Generacion de Terreno", 150)
    simulador.agregar_proceso("Carga de Audios", 30)
    simulador.agregar_proceso("Guardado en Base de Datos", 90)
    
    print("Iniciando procesamiento concurrente...\n")
    simulador.ejecutar()
    print("\nTodo fue completado con exito")