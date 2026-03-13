# Sistemas operativos

Este repositorio contiene todo lo relacionado con la materias, practicas con interrupciones, semaforos y maquina virtual

## estructura y definicion de cada algoritmo

- cena_filosofos → problema de concurrencia clasico donde varios porcesos compiten por un recurso limitado, si no se tiene un control se pueden generar interbloqueos (deadlock)

- dormir_despertar → mecanismo de sincronizacion que permite bloquear procesos (dormir) cuando no puede continuar y despertar procesos cuando otros liberan el recurso

- lectores_escritores → multiples procesos pueden leer un recurso compartido pero solo uno puede escribir y estos procesos no pueden trabajar simultaneamente

- productor_consumidor → un proceso produce datos y el otro consume todo lo que el productor genera, esto dentro de un buffer compartido y limitado

## tecnologias

- Python
- threading
