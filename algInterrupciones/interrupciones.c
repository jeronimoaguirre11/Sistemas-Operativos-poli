#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>

// Handler de la señal (interrupción)
void manejador(int sig) {
    printf("Interrupción recibida: un hijo terminó\n");

    // Recoger todos los hijos que hayan terminado
    while (waitpid(-1, NULL, WNOHANG) > 0) {
        printf("Se recogió un hijo terminado\n");
    }
}

int main() {

    // Asociar señal SIGCHLD al manejador
    signal(SIGCHLD, manejador);

    printf("Proceso Padre PID: %d\n", getpid());

    // Crear múltiples hijos
    for (int i = 0; i < 3; i++) {

        pid_t pid = fork();

        if (pid == 0) {
            // Código del hijo
            printf("Hijo %d con PID %d ejecutándose\n", i, getpid());

            sleep(5 + i); // cada hijo dura diferente tiempo

            printf("Hijo %d con PID %d terminando\n", i, getpid());

            exit(0);
        }
    }

    // Código del padre
    while (1) {
        printf("Padre trabajando...\n");
        sleep(10);
    }

    return 0;
}
