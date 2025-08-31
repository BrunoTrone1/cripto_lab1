from scapy.all import IP, ICMP, send
import argparse

def enviar_icmp_mensaje(destino: str, mensaje: str):
    for i, char in enumerate(mensaje):
        paquete = IP(dst=destino)/ICMP(id=1234, seq=i)/char
        print(f"Enviando caracter '{char}' -> paquete ICMP seq={i}")
        send(paquete, verbose=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enviar mensaje en paquetes ICMP separados por caracteres")
    parser.add_argument("-d", "--destino", type=str, required=True, help="IP de destino")
    parser.add_argument("-m", "--mensaje", type=str, required=True, help="Mensaje a enviar")
    args = parser.parse_args()

    enviar_icmp_mensaje(args.destino, args.mensaje)
