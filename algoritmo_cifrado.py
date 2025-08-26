import argparse

def cifrado_cesar(texto: str, desplazamiento: int) -> str:
    resultado = ""

    for char in texto:
        # Para letras mayusculas
        if 'A' <= char <= 'Z':
            resultado += chr((ord(char) - ord('A') + desplazamiento) % 26 + ord('A'))
        # Para letras minusculas
        elif 'a' <= char <= 'z':
            resultado += chr((ord(char) - ord('a') + desplazamiento) % 26 + ord('a'))
        else:
            # Otros caracteres (espacios, signos, numeros) quedan iguales
            resultado += char
    return resultado


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cifrado Cesar")
    parser.add_argument("-t", "--texto", type=str, required=True, help="Texto a cifrar")
    parser.add_argument("-d", "--desplazamiento", type=int, required=True, help="Desplazamiento Cesar")
    args = parser.parse_args()

    cifrado = cifrado_cesar(args.texto, args.desplazamiento)
    print("Texto cifrado:", cifrado)
