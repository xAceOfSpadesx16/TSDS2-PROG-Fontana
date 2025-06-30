"""
Se desean organizar las actividades de una persona en una tabla, conformada por 
los días (de lunes a viernes) en las columnas, y las horas (de 7 a 23) en las filas.
Una vez cargada la información, se debe disponer un menú de 3 opciones:
1) Imprimir las actividades de un día
2) Imprimir la actividad de un día y hora
3) Salir del programa
En el primer caso, se le debe solicitar al usuario el día del cual quiere obtener un 
listado de sus actividades. En el segundo, debe ingresar día y hora para ver qué 
actividad debe desarrollar o informarle si no existe ninguna. Luego de mostrarle los 
resultados, el programa debe volver al menú anterior.
"""

import numpy as np
import os



def imprimir_recuadro_decorativo(texto: str) -> None:
    """
    Imprime un recuadro con un texto centrado.

    Documentacion de formato de strings: https://docs.python.org/3/library/string.html#format-examples
    
    """

    """ 
    ╔══════════════════════════════════════╗
    ║               EJEMPLO                ║
    ╚══════════════════════════════════════╝
    """
    caracter_borde_horizontal = '\u2550'
    caracter_borde_vertical = '\u2551'
    esq_sup_izq = '\u2554' 
    esq_sup_der = '\u2557'
    esq_inf_izq = '\u255A'
    esq_inf_der = '\u255D'
    ancho_recuadro = 40
    ancho_interno = ancho_recuadro - 2

    borde_superior = f"{esq_sup_izq}{caracter_borde_horizontal * ancho_interno}{esq_sup_der}"
    linea_texto = f"{caracter_borde_vertical}{texto:^{ancho_interno}}{caracter_borde_vertical}"
    borde_inferior = f"{esq_inf_izq}{caracter_borde_horizontal * ancho_interno}{esq_inf_der}"

    print(borde_superior)
    print(linea_texto)
    print(borde_inferior)
    print('')


def limpiar_terminal() -> None:
    """ Limpia la terminal """
    os.system('cls' if os.name == 'nt' else 'clear')


def crear_matriz(dias: np.ndarray, rango_horario: np.ndarray) -> np.ndarray:
    """ Creacion de calendario/matriz vacia """

    matriz= np.empty(shape=(len(rango_horario)+1, len(dias)+1), dtype=np.dtype('U20')) #U20 String Unicode, 20 chars maximo 

    #seteando dias
    for col, dia in enumerate(dias):
        matriz[0, col+1] = dia
        

        
    #seteando horario
    for row, hora in enumerate(rango_horario):
        matriz[row+1, 0] = hora

    return matriz


def opciones_dias(dias: np.ndarray) -> int:
    """ Returna el numero de columna del dia seleccionado """

    print('Dias de la semana:')
    for x, dia in enumerate(dias):
        print(f'{x+1}) {dia}')

    print('La selección puede ser un numero o el nombre del dia')
    seleccion = input('Seleccione un dia de la semana: ')

    while True:
        if seleccion.isdigit() and int(seleccion) <= len(dias):
            # Si es un numero y se encuentra en el rango de dias
            return int(seleccion)
        
        index = np.where(np.char.lower(dias) == seleccion.lower())
        #sino, busca la posicion dentro del array, retorna un array que contiene un array de la posicion
        # si no encuentra retorna un array con un array de shape 0
        if index[0].size == 0:
            print(f'No existe el dia {seleccion}')
            seleccion = input('Intente de nuevo: ')
        else:
            return int(index[0][0]) + 1


def opciones_horario(rango_horario: np.ndarray) -> int:
    """ Returna el numero de fila del horario seleccionado """
    seleccion = input(f'Seleccione una hora en el rango de {rango_horario[0]} a {rango_horario[-1]}: ')
    while True:
        if seleccion.isdigit() and (int(rango_horario[0]) <= int(seleccion) <= int(rango_horario[-1])):
            return int(np.where(rango_horario == int(seleccion))[0][0]) + 1
        else:
            seleccion = input('Seleccion de hora invalida, intente de nuevo: ')


def imprimir_actividades(cronograma: np.ndarray, dia: str, horarios: np.ndarray) -> None:
    if any(cronograma):
        print(f'Actividades del dia {dia}:')
        for hora, actividad in zip(horarios, cronograma):
            if actividad:
                print(f'{hora}: {actividad}')
    else:
        print(f'No hay actividades programadas para el dia {dia}')


def obtener_actividades_diarias(calendario: np.ndarray) -> None:

    imprimir_recuadro_decorativo('OBTENER ACTIVIDAD DEL DIA')

    columna = opciones_dias(DIAS_ACTIVIDAD)
    dia = calendario[0, columna]
    horarios = calendario[1:, 0]
    actividades = calendario[1:, columna]

    print('')

    imprimir_actividades(actividades, dia, horarios)


def obtener_actividad_especifica(calendario: np.ndarray) -> None:

    imprimir_recuadro_decorativo('OBTENER ACTIVIDAD ESPECIFICA')
    columna = opciones_dias(DIAS_ACTIVIDAD)
    fila = opciones_horario(RANGO_HORARIO)
    dia = calendario[0, columna]
    horario = calendario[fila, 0]
    actividad = calendario[fila, columna]

    print('')

    if actividad:
        print(f'Tarea programada para el dia {dia} a las {horario}:00 : {actividad}')
    else:
        print(f'No hay actividades programadas para el dia {dia} a las {horario}:00')



def crud_actividad(calendario: np.ndarray, dias: np.ndarray, rango_horario: np.ndarray, creacion: bool) -> None:

    imprimir_recuadro_decorativo("CREACION DE ACTIVIDAD" if creacion else "ELIMINACION DE ACTIVIDAD")

    columna = opciones_dias(dias=dias)
    fila = opciones_horario(rango_horario=rango_horario)
    dia = calendario[0, columna]
    horario = calendario[fila, 0]

    if creacion:
        actividad = input('Ingrese la actividad: ')
        calendario[fila, columna] = actividad
        print(f'{actividad} agendado exitosamente para el dia {dia} a las {horario}:00.')
    else:
        calendario[fila, columna] = ''
        print(f'Actividad del dia {dia} a las {horario}:00 eliminada exitosamente.')

    print('')

    imprimir_recuadro_decorativo('VISTA DIARIA ACTUALIZADA')
    imprimir_actividades(calendario[1:, columna], dia, calendario[1:, 0])

    return calendario

def todas_las_actividades(calendario: np.ndarray, dias: np.ndarray, horarios: np.ndarray) -> None:
    for ind_dia in range(1, len(dias) +1):
        imprimir_actividades(calendario[1:, ind_dia], calendario[0, ind_dia], horarios)
        

def menu(dias: np.ndarray, rango_horario: np.ndarray, calendario: np.ndarray) -> None:
    calendario = calendario
    dias = dias
    rango_horario = rango_horario
    while True:
        imprimir_recuadro_decorativo('MENU PRINCIPAL')
        print('1) Obtener actividades de un dia')
        print('2) Obtener actividad especifica.')
        print('3) Agregar una nueva actividad.')
        print('4) Eliminar actividad.')
        print('5) Mostrar todas las actividades.')
        print('Para salir presione otra letra.')
        print('')
        seleccion = input('Seleccione una opcion: ')
        limpiar_terminal()
        match seleccion:
            case '1':
                obtener_actividades_diarias(calendario=calendario)

            case '2':
                obtener_actividad_especifica(calendario=calendario)

            case '3':
                calendario = crud_actividad(calendario=calendario, dias=dias, rango_horario=rango_horario, creacion=True)
            
            case '4':
                calendario = crud_actividad(calendario=calendario, dias=dias, rango_horario=rango_horario, creacion=False)
            
            case '5':
                todas_las_actividades(calendario, dias, rango_horario)
            case _:
                break
        print('')
        input('Presione una tecla para continuar...')
        limpiar_terminal()

def llenar_matriz(matriz: np.ndarray, rango_horas: np.ndarray, dias: np.ndarray) -> np.ndarray:
    agenda_con_actividades = [
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["Reunión Equipo", "", "Preparar informe", "", ""],
        ["Reunión Equipo", "", "Preparar informe", "", "Llamada cliente"],
        ["", "Presentación", "Revisión código", "", "Llamada cliente"],
        ["", "Presentación", "Revisión código", "", ""],
        ["Almuerzo", "Almuerzo", "Almuerzo", "Almuerzo", "Almuerzo"],
        ["", "Taller", "", "Seguimiento", ""],
        ["", "Taller", "", "Seguimiento", "Cierre de tareas"],
        ["Planificación semanal", "", "Documentación", "", "Cierre de tareas"],
        ["Planificación semanal", "", "Documentación", "", ""],
        ["", "", "", "Revisión final", ""],
        ["", "", "", "Revisión final", ""],
        ["Estudio", "", "", "", ""],
        ["Estudio", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
    ]
    for ind_dia in range(1, len(dias) +1 ):
        for ind_hora in range( 1, len(rango_horas) + 1):
            matriz[ind_hora][ind_dia] = agenda_con_actividades[ind_hora-1][ind_dia-1]

    return matriz


if __name__ == "__main__":
    HORA_INICIO = 7
    HORA_FINALIZACION = 23

    DIAS_ACTIVIDAD = np.array(
        ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes")
    )

    RANGO_HORARIO = np.arange(HORA_INICIO, HORA_FINALIZACION+1)
    

    calendario_vacio = crear_matriz(DIAS_ACTIVIDAD, RANGO_HORARIO)

    calendario_fake = llenar_matriz(calendario_vacio, RANGO_HORARIO, DIAS_ACTIVIDAD)

    menu(DIAS_ACTIVIDAD, RANGO_HORARIO, calendario_fake)