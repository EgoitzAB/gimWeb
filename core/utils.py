from datetime import datetime

def generar_horario(horarios):
    """
    Genera una tabla de horarios organizada por días y horas.
    :param horarios: QuerySet de objetos Horario.
    :return: Diccionario con días, horas y la tabla de horarios.
    """
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    horas = [f"{h}:30" if h % 2 != 0 else f"{h}:00" for h in range(9, 23)]
    horas = [datetime.strptime(h, "%H:%M").time() for h in horas]  # Convertir a time

    tabla_horarios = []
    for hora in horas:
        fila = {'hora': hora.strftime("%H:%M"), 'celdas': []}
        for dia in dias:
            actividades = [
                horario for horario in horarios
                if horario.dia == dia
                and horario.hora_inicio <= hora < horario.hora_fin
            ]
            fila['celdas'].append(actividades)
        tabla_horarios.append(fila)

    return {'dias': dias, 'tabla_horarios': tabla_horarios}