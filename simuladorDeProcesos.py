class Proceso:
    def __init__(self, nombre, tarea, tiempo_irrupcion, prioridad, tamano_datos, tiempo_cpu):
        self.nombre = nombre
        self.tarea = tarea
        self.tiempo_irrupcion = tiempo_irrupcion
        self.prioridad = prioridad
        self.tamano_datos = tamano_datos
        self.tiempo_cpu = tiempo_cpu

        self.estado = "Nuevo"
        self.tiempo_restante = tiempo_cpu
        self.primer_inicio = None
        self.tiempo_respuesta = None
        self.tiempo_finalizacion = None
        self.tiempo_espera = 0

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado


def mostrar_procesos(procesos):
    print("\n==============================================")
    print("       PROCESOS DEL SISTEMA SIGET")
    print("==============================================")

    print(
        f"{'Proceso':<10}"
        f"{'Tarea':<25}"
        f"{'Irrupción':<12}"
        f"{'Prioridad':<12}"
        f"{'Datos':<12}"
        f"{'CPU':<8}"
    )

    print("-" * 79)

    for proceso in procesos:
        print(
            f"{proceso.nombre:<10}"
            f"{proceso.tarea:<25}"
            f"{proceso.tiempo_irrupcion:<12}"
            f"{proceso.prioridad:<12}"
            f"{proceso.tamano_datos:<12} MB"
            f"{proceso.tiempo_cpu:<8} s"
        )


def round_robin(procesos, quantum):
    tiempo = 0
    cola = []
    procesos_pendientes = procesos.copy()

    print("\n==============================================")
    print("              ROUND ROBIN")
    print("==============================================")
    print(f"\nQuantum: {quantum} segundos\n")

    while cola or procesos_pendientes:

        for proceso in procesos_pendientes[:]:
            if proceso.tiempo_irrupcion <= tiempo:
                proceso.cambiar_estado("Listo")
                cola.append(proceso)
                procesos_pendientes.remove(proceso)

                print(
                    f"Tiempo {tiempo}: "
                    f"{proceso.nombre} -> Nuevo -> Listo"
                )

        if not cola:
            tiempo += 1
            continue

        proceso = cola.pop(0)
        proceso.cambiar_estado("En ejecución")

        if proceso.primer_inicio is None:
            proceso.primer_inicio = tiempo
            proceso.tiempo_respuesta = (
                tiempo - proceso.tiempo_irrupcion
            )

        tiempo_ejecucion = min(
            quantum,
            proceso.tiempo_restante
        )

        print(
            f"Tiempo {tiempo}: "
            f"{proceso.nombre} -> En ejecución "
            f"({tiempo_ejecucion} segundos)"
        )

        proceso.tiempo_restante -= tiempo_ejecucion
        tiempo += tiempo_ejecucion

        if proceso.tiempo_restante > 0:
            proceso.cambiar_estado("Listo")
            cola.append(proceso)

            print(
                f"{proceso.nombre} -> Listo "
                f"(restan {proceso.tiempo_restante} segundos)"
            )

        else:
            proceso.cambiar_estado("Terminado")
            proceso.tiempo_finalizacion = tiempo

            print(
                f"{proceso.nombre} -> Terminado "
                f"en t={tiempo}"
            )

    for proceso in procesos:
        proceso.tiempo_espera = (
            proceso.tiempo_finalizacion
            - proceso.tiempo_irrupcion
            - proceso.tiempo_cpu
        )

    print("\n==============================================")
    print("         RESULTADOS ROUND ROBIN")
    print("==============================================")

    print(
        f"{'Proceso':<10}"
        f"{'Respuesta':<15}"
        f"{'Finalización':<15}"
        f"{'Espera':<10}"
    )

    print("-" * 50)

    for proceso in procesos:
        print(
            f"{proceso.nombre:<10}"
            f"{proceso.tiempo_respuesta:<15}"
            f"{proceso.tiempo_finalizacion:<15}"
            f"{proceso.tiempo_espera:<10}"
        )

    return procesos


def prioridad(procesos):
    tiempo = 0
    cola = []
    procesos_pendientes = procesos.copy()

    print("\n==============================================")
    print("          PLANIFICACIÓN POR PRIORIDAD")
    print("==============================================")
    print("\n1 = Mayor prioridad\n")

    while cola or procesos_pendientes:

        for proceso in procesos_pendientes[:]:
            if proceso.tiempo_irrupcion <= tiempo:
                proceso.cambiar_estado("Listo")
                cola.append(proceso)
                procesos_pendientes.remove(proceso)

                print(
                    f"Tiempo {tiempo}: "
                    f"{proceso.nombre} -> Nuevo -> Listo"
                )

        if not cola:
            tiempo += 1
            continue

        cola.sort(key=lambda proceso: proceso.prioridad)

        proceso = cola.pop(0)
        proceso.cambiar_estado("En ejecución")

        if proceso.primer_inicio is None:
            proceso.primer_inicio = tiempo
            proceso.tiempo_respuesta = (
                tiempo - proceso.tiempo_irrupcion
            )

        print(
            f"Tiempo {tiempo}: "
            f"{proceso.nombre} -> En ejecución"
        )

        tiempo += proceso.tiempo_restante
        proceso.tiempo_restante = 0

        proceso.cambiar_estado("Terminado")
        proceso.tiempo_finalizacion = tiempo

        print(
            f"{proceso.nombre} -> Terminado "
            f"en t={tiempo}"
        )

    for proceso in procesos:
        proceso.tiempo_espera = (
            proceso.tiempo_finalizacion
            - proceso.tiempo_irrupcion
            - proceso.tiempo_cpu
        )

    print("\n==============================================")
    print("       RESULTADOS POR PRIORIDAD")
    print("==============================================")

    print(
        f"{'Proceso':<10}"
        f"{'Prioridad':<12}"
        f"{'Respuesta':<15}"
        f"{'Finalización':<15}"
        f"{'Espera':<10}"
    )

    print("-" * 62)

    for proceso in procesos:
        print(
            f"{proceso.nombre:<10}"
            f"{proceso.prioridad:<12}"
            f"{proceso.tiempo_respuesta:<15}"
            f"{proceso.tiempo_finalizacion:<15}"
            f"{proceso.tiempo_espera:<10}"
        )

    return procesos


# ==================================================
# PROCESOS DEL SIGET
# ==================================================

procesos_rr = [
    Proceso(
        "P1",
        "Detectar accidente",
        0,
        1,
        500,
        5
    ),
    Proceso(
        "P2",
        "Analizar trafico",
        1,
        3,
        1000,
        7
    ),
    Proceso(
        "P3",
        "Controlar semaforos",
        2,
        2,
        300,
        4
    )
]

procesos_prioridad = [
    Proceso(
        "P1",
        "Detectar accidente",
        0,
        1,
        500,
        5
    ),
    Proceso(
        "P2",
        "Analizar trafico",
        1,
        3,
        1000,
        7
    ),
    Proceso(
        "P3",
        "Controlar semaforos",
        2,
        2,
        300,
        4
    )
]


# ==================================================
# EJECUCIÓN
# ==================================================

print("\n======================================================")
print("       SIMULADOR DEL PLANIFICADOR CPU - SIGET")
print("======================================================")

mostrar_procesos(procesos_rr)

resultados_rr = round_robin(procesos_rr, 2)

resultados_prioridad = prioridad(procesos_prioridad)


# ==================================================
# COMPARACIÓN
# ==================================================

promedio_respuesta_rr = sum(
    p.tiempo_respuesta for p in resultados_rr
) / len(resultados_rr)

promedio_espera_rr = sum(
    p.tiempo_espera for p in resultados_rr
) / len(resultados_rr)

promedio_respuesta_prioridad = sum(
    p.tiempo_respuesta for p in resultados_prioridad
) / len(resultados_prioridad)

promedio_espera_prioridad = sum(
    p.tiempo_espera for p in resultados_prioridad
) / len(resultados_prioridad)


print("\n======================================================")
print("             COMPARACIÓN DE ALGORITMOS")
print("======================================================")

print(
    f"\n{'Métrica':<25}"
    f"{'Round Robin':<18}"
    f"{'Prioridad':<18}"
)

print("-" * 61)

print(
    f"{'Promedio respuesta':<25}"
    f"{promedio_respuesta_rr:<18.2f}"
    f"{promedio_respuesta_prioridad:<18.2f}"
)

print(
    f"{'Promedio espera':<25}"
    f"{promedio_espera_rr:<18.2f}"
    f"{promedio_espera_prioridad:<18.2f}"
)

print("\n======================================================")
print("                 SIMULACIÓN FINALIZADA")
print("======================================================")