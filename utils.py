def pedir_entero(mensaje: str) -> int:
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        else:
            print("El valor ingresado debe ser un numero.")

def presentar_funcion(numero_ejercicio: int, funcion: callable) -> None:
    print("/"*25)
    print(f"EJERCICIO N° {numero_ejercicio}")
    print("/"*25)
    print()
    funcion()
    print()

print(int(""))