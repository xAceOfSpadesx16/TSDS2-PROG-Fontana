""" UTILIDADES """
def pedir_entero(mensaje: str) -> int:
    while True:
        try:
            valor = input(mensaje)
            return int(valor)
        except ValueError:
            print("El valor ingresado debe ser un numero.")

def presentar_funcion(numero_ejercicio, funcion) -> None:
    print("/"*25)
    print(f"EJERCICIO N° {numero_ejercicio}")
    print("/"*25)
    print()
    funcion()
    print()

""" EJERCICIOS """
def ejercicio_1():
    """ 
        1) Crear una lista e inicializarla con 5 cadenas de caracteres leídas por teclado. 
        Copiar los elementos en otra lista, pero en orden inverso, y mostrar sus elementos por la pantalla. 
    """
    CANT_STR = 5
    lista = []
    for i in range(1, CANT_STR+1):
        entrada = input(f"Ingrese una cadena de caracteres {i} de {CANT_STR}: ")
        lista.append(entrada)
    
    lista_reverse = lista[::-1]
    print(lista_reverse)

def ejercicio_2():
    """
        2) Se desean guardar los nombres y las edades de los alumnos de un curso en una lista. 
        Realizar un programa que introduzca esos datos. 
        El proceso de lectura de datos terminará cuando se ingrese como nombre un asterisco (*). 
        Al finalizar se mostrarán los siguientes datos:
             Todos los alumnos mayores de edad.
             Los alumnos mayores (los que tienen más edad)
    """

    nombre = ""
    nombres = []
    edades = []

    while nombre != '*':
        nombre = input("Ingrese el nombre del alumno: ")
        if nombre != "*":
            edad = pedir_entero("Ingrese la edad del alumno: ")
            nombres.append(nombre)
            edades.append(edad)
    
    print()
    
    max_edad = max(edades)
    alumnos_mayores_edad = []
    alumnos_viejos = []
    for nomb, ed in zip(nombres, edades):
        if ed >= 18:
            alumnos_mayores_edad.append(f"Nombre: {nomb} - edad: {ed}")
            if ed == max_edad:
                alumnos_viejos.append(nomb)
    
    print()

    print("Alumnos mayores de edad:")
    print(*alumnos_mayores_edad, sep="\n")
    print(f"Alumnos con mas edad ({max_edad}):")
    print(*alumnos_viejos, sep="\n")


def ejercicio_3():
    """
    3) Escribe un programa que pida un número por teclado y
    que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, 
    y los valores sean los cuadrados de las claves.
    """
    numero = pedir_entero("Ingrese un numero: ")
    dict_cuadrados = {}
    for num in range(1,numero+1):
        dict_cuadrados[num] = num ** 2
    
    print()

    print(f"Cuadrados de 1 a {numero}: ")
    print(dict_cuadrados)


def ejercicio_4():
    """
    4) Crear un programa donde se declare un diccionario para guardar los precios de distintas frutas.
    El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y 
    nos mostrará el precio final de la venta a partir de los datos guardados en el diccionario. 
    Si la fruta no existe nos dará un error. 
    Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
    """
    precios_dict = {
        "pera": 15,
        "manzana": 20,
        "naranja": 17,
        "banana": 25,
        "kiwi": 30
    }

    while True:
        fruta = input("Ingrese una fruta: ")
        fruta_select = precios_dict.get(fruta)
        if not fruta_select:
            print(f"{fruta} no se encuentra en stock.")
            continue
        cantidad = pedir_entero("Ingrese la cantidad vendida: ")

        print(f'El precio total de la venta es: ${fruta_select*cantidad}')

        if input("Presione cualquier letra para continuar (S para salir): ").lower() == "s":
            break

def ejercicio_5():
    """
    5) Codificar un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido.
    Cada alumno puede tener distinta cantidad de notas.
    Guardar la información en un diccionario cuyas claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
    El programa pedirá el número de alumnos que vamos a introducir,
    pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo.
    Al final, el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. 
    Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error. 
    """
    alumnos_notas = {}
    cantidad_alumnos = pedir_entero("Ingrese la cantidad de alumnos que cargara: ")

    for _ in range(cantidad_alumnos):
        alumno = input('Ingrese el nombre del alumno: ')
        if alumno in alumnos_notas.keys():
            print("El alumno ya fue cargado.")
            continue

        notas_cargadas = []
        while True:
            nota = pedir_entero("Ingrese una nota: ")
            if nota < 0:
                break
            notas_cargadas.append(nota)
        
        alumnos_notas.update({alumno:notas_cargadas})
    
    for alumno, notas in alumnos_notas.items():
        print(f"{alumno}: promedio de {sum(notas)/len(notas)}")


if __name__ == "__main__":

    presentar_funcion(1, ejercicio_1)

    presentar_funcion(2, ejercicio_2)

    presentar_funcion(3, ejercicio_3)

    presentar_funcion(4, ejercicio_4)

    presentar_funcion(5, ejercicio_5)