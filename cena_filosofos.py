import threading
import time
import random

N = 5

PENSANDO = 0
HAMBRIENTO = 1
COMIENDO = 2

estado = [PENSANDO] * N

mutex = threading.Semaphore(1)
s = [threading.Semaphore(0) for _ in range(N)]


def LEFT(i):
    return (i - 1) % N


def RIGHT(i):
    return (i + 1) % N


def test(i):
    if (estado[i] == HAMBRIENTO and
        estado[LEFT(i)] != COMIENDO and
        estado[RIGHT(i)] != COMIENDO):

        estado[i] = COMIENDO
        s[i].release()


def tomar_tenedores(i):
    mutex.acquire()
    estado[i] = HAMBRIENTO
    print(f"Filósofo {i} tiene HAMBRE")
    test(i)
    mutex.release()
    s[i].acquire()


def soltar_tenedores(i):
    mutex.acquire()
    estado[i] = PENSANDO
    print(f"Filósofo {i} terminó de COMER y vuelve a pensar")
    test(LEFT(i))
    test(RIGHT(i))
    mutex.release()


def filosofo(i):
    while True:
        print(f"Filósofo {i} está PENSANDO")
        time.sleep(random.uniform(1, 3))
        tomar_tenedores(i)
        print(f"Filósofo {i} está COMIENDO")
        time.sleep(random.uniform(1, 2))
        soltar_tenedores(i)


# Crear hilos
for i in range(N):
    threading.Thread(target=filosofo, args=(i,), daemon=True).start()

# Mantener programa activo
while True:
    time.sleep(1)
