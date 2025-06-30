import numpy as np
from time import perf_counter

def crear_vector_dnis() -> np.ndarray:
    print("Creando vector.")
    DNI_MIN = 50_000_000
    DNI_MAX = 80_000_000
    rango = np.arange(DNI_MIN, DNI_MAX)
    array = np.random.choice(rango, size=5800, replace=False)
    return array

def obtener_dni() -> int:
    while True:
        dni = input("Ingrese un numero de DNI: ")
        if dni.isdigit():
            return int(dni)
        else:
            print("El D.N.I. ingresado no es valido.")

def ordenar_vector(vector: np.ndarray) -> np.ndarray:
    print('Realizando Ordenamiento Shell del vector.')
    copia = vector.copy()
    N = copia.size
    salto = int(N/2)
    while salto >=1:
        sw = 1
        while sw != 0:
            sw = 0
            i=0
            while i < (N - salto):
                if copia[i] > copia[i+salto]:
                    aux = copia[i+salto]
                    copia[i+salto] = copia[i]
                    copia[i] = aux
                    sw = 1
                i += 1
        salto = int(salto/2)
    return copia

def busqueda_dicotomica(vector: np.ndarray, valor: int) -> bool:
    inf=0
    sup=len(vector)-1
    m=int((sup+inf)/2)
    sw=0
    while inf<=sup and sw==0:
        if vector[m]==valor:
            return True
            #sw = 1
        elif vector[m]>valor:
            sup=m-1
        else:
            inf=m+1
        m=int((sup+inf)/2)
    if sw==0:
        if vector[m]==valor:
            return True
        return False

def busqueda_for(vector: np.ndarray, valor:int) -> bool:
    for dni in vector:
        if dni == valor:
            return True
    return False

def informar_estado_vacunacion(res_busqueda: bool) -> None:
    if res_busqueda:
        print("El DNI proporcionado fue vacunado recientemente.")
    else:
        print("El DNI proporcionado se encuentra en condiciones de ser vacunado.")



if __name__ == "__main__":
    vector = crear_vector_dnis()
    vector_ordenado = ordenar_vector(vector)
    print("DNI en vector ordenado: ")
    print(f"Indice 500: {vector_ordenado[500]}")
    print(f"Indice 3200: {vector_ordenado[3200]}")
    print(f"Indice 5600: {vector_ordenado[5600]}")

    while True:
        dni = obtener_dni()

        print()
        print('/'*15)

        print("Busqueda Secuencial.")
        t1 = perf_counter()
        res_for = busqueda_for(vector= vector_ordenado, valor=dni)
        t2 = perf_counter()

        informar_estado_vacunacion(res_for)
        print(f"Tiempo de busqueda secuencial (seg): {t1-t2}")
        
        print()
        print('/'*15)

        print("Busqueda Dicotomica")
        t3 = perf_counter()
        res_bin = busqueda_dicotomica(vector = vector_ordenado, valor= dni)
        t4 = perf_counter()

        informar_estado_vacunacion(res_bin)
        print(f"Tiempo de busqueda dicotomica (seg): {t3-t4}")

        seguir = input("Presione cualquier letra para continuar (S para salir): ")
        if seguir.lower() == "s":
            break
        
        print()
        print('/'*15)