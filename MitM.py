from scapy.all import rdpcap, ICMP
from spellchecker import SpellChecker
import argparse

def descifrado_cesar(texto: str, desplazamiento: int) -> str:
    resultado = ""
    for char in texto:
        if 'A' <= char <= 'Z':
            resultado += chr((ord(char) - ord('A') - desplazamiento) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            resultado += chr((ord(char) - ord('a') - desplazamiento) % 26 + ord('a'))
        else:
            resultado += char
    return resultado

def obtener_mensaje_mas_probable(texto: str) -> str:
    spell = SpellChecker(language='es')
    mejor_desplazamiento = 0
    max_palabras_validas = -1
    mejor_texto = texto

    for d in range(26):
        descifrado = descifrado_cesar(texto, d)
        palabras = descifrado.split()
        validas = sum(1 for w in palabras if w.lower() in spell)
        if validas > max_palabras_validas:
            max_palabras_validas = validas
            mejor_desplazamiento = d
            mejor_texto = descifrado

    print(f"Mejor desplazamiento encontrado: {mejor_desplazamiento}")
    return mejor_texto

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Descifrado de mensaje ICMP con Cesar")
    parser.add_argument("-f", "--file", type=str, required=True, help="Archivo pcap de captura")
    args = parser.parse_args()
    archivo_pcap = args.file
    paquetes = rdpcap(archivo_pcap)

    mensaje = ""
    for pkt in paquetes:
        if ICMP in pkt and pkt[ICMP].type == 8: 
            payload = bytes(pkt[ICMP].payload).decode(errors='ignore')
            mensaje += payload

    print(f"Mensaje recibido (concatenado): {mensaje}")
    frase_probable = obtener_mensaje_mas_probable(mensaje)
    print(f"Frase descifrada mas probable: {frase_probable}")
