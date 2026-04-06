# src/competencia.py

def procesar_ronda(ronda, stats, ronda_num):
    """Procesa una ronda, actualiza estadísticas y devuelve ganador y puntajes."""
    theme = ronda['theme']
    scores = {}
    for name, judges in ronda['scores'].items():
        total = sum(judges.values())
        scores[name] = total
        stats[name]["total"] += total
        stats[name]["scores"].append(total)
        if total > stats[name]["best"]:
            stats[name]["best"] = total

    # determinar ganador
    ganador = max(scores, key=scores.get)
    stats[ganador]["wins"] += 1

    return {
        "ronda_num": ronda_num,
        "theme": theme,
        "scores": scores,
        "ganador": ganador,
        "puntaje_ganador": scores[ganador]
    }


def imprimir_tabla_final(stats):
    """Imprime la tabla final ordenada por puntaje total."""
    print("Tabla de posiciones final:")
    print("Cocinero Puntaje Rondas ganadas Mejor ronda Promedio")
    print("--------------------------------------------------------------")
    ordenados = sorted(stats.items(), key=lambda x: x[1]["total"], reverse=True)
    for name, data in ordenados:
        promedio = data["total"] / len(data["scores"])
        print(f"{name:10} {data['total']:6} {data['wins']:13} {data['best']:11} {promedio:8.1f}")


def ejecutar_competencia(rounds):
    """Ejecuta toda la competencia mostrando resultados por ronda y tabla final."""
    # inicializar estadísticas
    stats = {name: {"total": 0, "wins": 0, "best": 0, "scores": []}
             for name in rounds[0]['scores'].keys()}

    # procesar rondas
    for i, ronda in enumerate(rounds, start=1):
        resultado = procesar_ronda(ronda, stats, i)
        print(f"Ronda {resultado['ronda_num']} - {resultado['theme']}:")
        print(f" Ganador: {resultado['ganador']} ({resultado['puntaje_ganador']} pts)")
        print(" Tabla de posiciones:")
        for name, total in resultado['scores'].items():
            print(f"  {name}: {total} pts")
        print()

    # tabla final
    imprimir_tabla_final(stats)

