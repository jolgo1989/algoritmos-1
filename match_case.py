# Ejercicio: realiza un programa que lea un color y devuelva su nombre en inglés
color = input("Ingresa un color: ")
match color:
    case "rojo":
        print("Red")
    case "verde":
        print("Green")
    case "azul":
        print("Blue")
    case _:
        print("Color desconocido")