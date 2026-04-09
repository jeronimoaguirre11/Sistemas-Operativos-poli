# ejercicio de Interrupciones

Al realizar la practica de interrupciones, se desarrollo un proceso padre y multiples procesos hijos

contamos con 4 archivo que en realidad son 2 y sus compilaciones.

## estructura y definicion de cada algoritmo

- interrupciones.c → en este codigo el proceso padre no para de trabajar, van surgiendo procesos hijos, cuando estos terminan de trabajar, se manda una señal que indica su fin y el padre con el metodo waitid() recoge los registros para que no queden procesos zombies

- p.zombie → ponemos en evidencia que sucede cuando el programa no usa el metodo waitid() y quedan procesos zombies por recoger.   se ven sus registros hasta el punto de terminar el programa, pero si pasaramos mucho tiempo en el programa, dichos registros permanecen ahi indefinidamente

## tecnologias

- C

