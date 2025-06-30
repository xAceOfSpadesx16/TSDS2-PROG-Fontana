def obtener_datos() -> tuple[str, int, int]:
    """return [tipo_cliente, cant_libros, importe_total]"""
    tipo_cliente = input('Ingrese el tipo de cliente: "L" / "P" ').upper()

    while True:
        importe_str = input("Ingrese el importe total de la venta: ")
        if not importe_str.isdigit():
            print(
                "El importe ingresado debe ser un numero entero, intentelo nuevamente."
            )
            continue
        else:
            importe_total = int(importe_str)
            break

    while True:
        libros_str = input("Ingrese la cantidad de libros a vender: ")
        if not libros_str.isdigit():
            print(
                "La cantidad de libros a vender debe ser un numero entero, intentelo nuevamente"
            )
            continue
        else:
            cantidad_libros = int(libros_str)
            break

    return tipo_cliente, cantidad_libros, importe_total


def obtener_bonificacion_para_librerias(cant_libros: int, importe_total: int) -> float:
    if cant_libros <= 24:
        return importe_total * 0.2
    else:
        return importe_total * 0.25


def obtener_bonificacion_para_particulares(
    cant_libros: int, importe_total: int
) -> float | int:
    if 6 <= cant_libros < 18:
        return importe_total * 0.05
    elif cant_libros >= 18:
        return importe_total * 0.1
    else:
        0


def informar_resultado(importe_total: int, bonificacion: float | int) -> None:
    print(f"El importe bruto bonificado es de: {importe_total - bonificacion}")


def obtener_descuento(cliente: str, cant_libros: int, importe_total: int) -> int:
    if cliente == "L":
        bonificacion_percibida = obtener_bonificacion_para_librerias(
            cant_libros=cant_libros, importe_total=importe_total
        )

    elif cliente == "P":
        bonificacion_percibida = obtener_bonificacion_para_particulares(
            cant_libros=cant_libros, importe_total=importe_total
        )
    else:
        bonificacion_percibida = 0

    return bonificacion_percibida


def main():
    res = "S"

    while res == "S":
        try:
            tipo_cliente, cant_libros, importe_total = obtener_datos()
        except Exception:
            print("Surgio un error en la solicitud de datos, intentelo nuevamente")
            continue

        bonificacion = obtener_descuento(
            cliente=tipo_cliente, cant_libros=cant_libros, importe_total=importe_total
        )
        informar_resultado(importe_total=importe_total, bonificacion=bonificacion)

        res = input("Presione S para continuar, sino presione cualquier letra.")


if __name__ == "__main__":
    main()
