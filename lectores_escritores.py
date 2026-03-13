import threading
import time
import random

# Semáforos
mutex = threading.Semaphore(1)
db = threading.Semaphore(1)

contador_lectores = 0


def lector(id):
    global contador_lectores
    while True:
        time.sleep(random.uniform(0.5, 2))

        mutex.acquire()
        contador_lectores += 1
        if contador_lectores == 1:
            db.acquire()
        mutex.release()

        print(f"Lector {id} está LEYENDO")
        time.sleep(random.uniform(1, 3))

        mutex.acquire()
        contador_lectores -= 1
        if contador_lectores == 0:
            db.release()
        mutex.release()

        print(f"Lector {id} terminó de leer")


def escritor(id):
    while True:
        time.sleep(random.uniform(2, 4))

        print(f"Escritor {id} quiere escribir")
        db.acquire()

        print(f"Escritor {id} está ESCRIBIENDO")
        time.sleep(random.uniform(2, 3))

        db.release()
        print(f"Escritor {id} terminó de escribir")


# Crear hilos
for i in range(3):
    threading.Thread(target=lector, args=(i,), daemon=True).start()

for i in range(2):
    threading.Thread(target=escritor, args=(i,), daemon=True).start()

# Mantener programa vivo
while True:
    time.sleep(1)
