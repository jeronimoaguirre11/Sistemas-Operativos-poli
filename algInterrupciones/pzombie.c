#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    for (int i = 0; i < 5; i++) {
        pid_t pid = fork();

        if (pid == 0) {
            printf("Hijo %d con PID %d terminado\n", i, getpid());
            sleep(1);
            exit(0);
        }
    }

    printf("Padre durmiendo sin recoger hijos...\n");
    sleep(30);

    return 0;
}
