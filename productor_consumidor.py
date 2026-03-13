import threading
import time
import random

# Tamaño del buffer
TAMANO_BUFFER = 3
buffer = [None] * TAMANO_BUFFER

# Semáforos
mutex = threading.Semaphore(1)
empty = threading.Semaphore(TAMANO_BUFFER)
full = threading.Semaphore(0)

entrada = 0
salida = 0


def productor():
    global entrada
    while True:
        elemento = random.randint(1, 100)
        time.sleep(random.uniform(1, 2))

        empty.acquire()
        mutex.acquire()

        buffer[entrada] = elemento
        print(f"Productor produjo: {elemento} | Buffer: {buffer}")
        entrada = (entrada + 1) % TAMANO_BUFFER

        mutex.release()
        full.release()


def consumidor():
    global salida
    while True:
        full.acquire()
        mutex.acquire()

        elemento = buffer[salida]
        buffer[salida] = None
        print(f"Consumidor consumió: {elemento} | Buffer: {buffer}")
        salida = (salida + 1) % TAMANO_BUFFER

        mutex.release()
        empty.release()

        time.sleep(random.uniform(1, 3))


# Crear hilos
threading.Thread(target=productor, daemon=True).start()
threading.Thread(target=consumidor, daemon=True).start()

# Mantener programa activo
while True:
    time.sleep(1)
