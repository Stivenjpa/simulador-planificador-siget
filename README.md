# simulador-planificador-siget
S1. Tarea. Simulador de planificación de procesos


# Simulador del Planificador CPU - SIGET

## Descripción

Este proyecto implementa un simulador de planificación de procesos para el **Sistema Inteligente de Gestión de Tráfico (SIGET)**.

El simulador permite observar cómo diferentes procesos relacionados con la gestión del tráfico son administrados por la CPU utilizando diferentes algoritmos de planificación.

El proyecto fue desarrollado como parte de la actividad académica sobre **administración de procesos y planificación de CPU**.

## Objetivo

Desarrollar una simulación que permita comprender el funcionamiento de diferentes algoritmos de planificación de procesos y analizar su comportamiento mediante métricas como:

* Tiempo de respuesta.
* Tiempo de espera.
* Tiempo de finalización.
* Prioridad de los procesos.

## Procesos simulados

El sistema utiliza tres procesos relacionados con la gestión inteligente del tráfico:

| Proceso | Tarea               | Tiempo de irrupción | Prioridad |   Datos | CPU |
| ------- | ------------------- | ------------------: | --------: | ------: | --: |
| P1      | Detectar accidente  |                 0 s |         1 |  500 MB | 5 s |
| P2      | Analizar tráfico    |                 1 s |         3 | 1000 MB | 7 s |
| P3      | Controlar semáforos |                 2 s |         2 |  300 MB | 4 s |

La prioridad **1 representa la mayor prioridad**.

## Algoritmos implementados

### Round Robin

Se utiliza un **quantum de 2 segundos**.

Cada proceso recibe un intervalo de tiempo para utilizar la CPU. Si el proceso no termina durante ese intervalo, vuelve a la cola de procesos listos para esperar su próximo turno.

Este algoritmo permite distribuir el uso de la CPU entre los diferentes procesos.

### Planificación por Prioridad

Los procesos son seleccionados de acuerdo con su nivel de prioridad.

El proceso con el número de prioridad más bajo tiene mayor prioridad de ejecución.

## Estados de los procesos

Durante la simulación se representan los siguientes estados:

* **Nuevo:** el proceso todavía no ha ingresado a la cola de procesos listos.
* **Listo:** el proceso está esperando para utilizar la CPU.
* **En ejecución:** el proceso está utilizando la CPU.
* **Bloqueado:** el proceso queda temporalmente detenido esperando un recurso o información.
* **Terminado:** el proceso finalizó su ejecución.

En Round Robin se simula además el bloqueo temporal del proceso **P2**, representando una espera por datos provenientes de sensores de tráfico.

## Métricas

El simulador calcula diferentes métricas para analizar el comportamiento de los algoritmos:

### Tiempo de respuesta

Representa el tiempo transcurrido desde la llegada del proceso hasta su primera ejecución.

### Tiempo de espera

Representa el tiempo que el proceso permanece esperando para utilizar la CPU.

### Tiempo de finalización

Indica el momento en el que el proceso termina completamente su ejecución.

Al ejecutar ambos algoritmos, el programa muestra una comparación de los promedios de tiempo de respuesta y tiempo de espera.

## Tecnologías utilizadas

* **Python 3**
* Programación orientada a objetos.
* Estructuras de datos.
* Simulación de planificación de procesos.

## Ejecución

### Requisitos

Tener instalado **Python 3**.

### Ejecutar el programa

Desde la carpeta del proyecto ejecutar:

```bash
python simuladorDeProcesos.py
```

También puede ejecutarse directamente desde un entorno como **Visual Studio Code**.

Al iniciar el programa se presenta un menú:

```text
1. Round Robin
2. Prioridad
3. Ejecutar ambos
4. Salir
```

El usuario puede seleccionar el algoritmo que desea ejecutar.

## Ejemplo de funcionamiento

El programa muestra la transición de los procesos entre sus diferentes estados:

```text
Nuevo -> Listo -> En ejecución -> Listo -> Terminado
```

Cuando se presenta una situación de bloqueo:

```text
Nuevo -> Listo -> En ejecución -> Bloqueado -> Listo -> Terminado
```

Finalmente, se muestran los resultados obtenidos y, al ejecutar ambos algoritmos, se realiza una comparación de sus métricas.

## Estructura del proyecto

```text
simulador-planificador-siget/
│
├── simuladorDeProcesos.py
└── README.md
```

## Conclusión

El simulador permite comprender de manera práctica cómo un sistema operativo administra diferentes procesos que requieren utilizar la CPU.

La implementación de **Round Robin** permite observar la distribución equitativa del procesador mediante un quantum, mientras que la **planificación por prioridad** permite atender primero los procesos considerados más importantes.

La simulación de los estados **Nuevo, Listo, En ejecución, Bloqueado y Terminado** permite representar de forma más cercana el comportamiento de los procesos dentro de un sistema operativo aplicado al contexto del SIGET.

## Autor

**Estiven Jaramillo**

Tecnólogo en Desarrollo de Software y Sistemas
