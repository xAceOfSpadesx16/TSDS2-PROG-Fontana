import numpy as np

def crear_array(min_val: int, max_val: int) -> np.ndarray:
    rango = np.arange(min_val, max_val)
    matriz = np.random.choice(rango, size=50, replace=False)
    return np.sort(matriz)

def informar_resultados(matriz: np.ndarray, val_1: int, val_2: int) -> None:
        print(f"El array de elementos es: {matriz}")
        indice_1 = np.where(matriz == val_1)
        indice_2 = np.where(matriz == val_2)

        primer_en_array = indice_1[0].size > 0
        segundo_en_array = indice_2[0].size > 0
        
        if primer_en_array and not segundo_en_array:
            print("Solo el primer numero se encuentra en el arreglo.")
        elif not primer_en_array and segundo_en_array:
            print("Solo el segundo numero se encuentra en el arreglo.")
        elif primer_en_array and segundo_en_array:
            print("Ambos numeros se encuentran en el arreglo.")
        else:
            print("Ninguno de los dos numeros se encuentra en el arreglo.")

def pedir_valor(mensaje: str) -> int:
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        else:
            print("El valor ingresado debe ser un numero.")
            
def menu() -> tuple[int, int]:
    val_1 = pedir_valor('Ingrese el primer numero: ')
    val_2 = pedir_valor('Ingrese el segundo numero: ')
    return val_1, val_2

def main():
    MIN_VALUE = 1
    MAX_VALUE = 100

    array = crear_array(MIN_VALUE, MAX_VALUE)

    valor_1, valor_2 = menu()

    informar_resultados(array, valor_1, valor_2)

if __name__ == "__main__":
    main()