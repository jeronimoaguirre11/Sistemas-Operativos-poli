import threading
import time

# Semáforo inicia en 0 (nadie puede continuar)
sem = threading.Semaphore(0)


def proceso_que_espera():
    print("Proceso A: Necesito el recurso...")
    print("Proceso A: No está disponible, me DUERMO.")
    
    sem.acquire()  # Aquí se bloquea (duerme)

    print("Proceso A: Me despertaron! Ahora uso el recurso.")


def proceso_que_despierta():
    time.sleep(3)
    print("Proceso B: Recurso disponible. DESPIERTO al proceso A.")
    
    sem.release()  # Despierta al proceso A


# Crear hilos
threading.Thread(target=proceso_que_espera).start()
threading.Thread(target=proceso_que_despierta).start()
