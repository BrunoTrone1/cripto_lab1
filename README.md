# Laboratorio 1 

## Índice

- [Descripción](#descripción)
- [Herramientas utilizadas](#herramientas-utilizadas)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Librerías necesarias](#librerías-necesarias)
- [Ejecución de los programas](#ejecución-de-los-programas)
  - [algoritmo_cifrado.py](#algoritmo_cifradopy)
  - [modo_stealth.py](#modo_stealthpy)
  - [MitM.py](#mitmpy)F


## Descripción  

Este laboratorio tuvo como objetivo explorar conceptos de cifrado clásico, ocultamiento de información en tráfico legítimo y técnicas de análisis para recuperación de mensajes.  

Se desarrollaron tres actividades principales:  
1. Implementación del cifrado César en Python.  
2. Envío de mensajes encubiertos en paquetes ICMP para simular tráfico legítimo.  
3. Ejecución de un ataque MitM (Man-in-the-Middle) para recuperar mensajes transmitidos y descifrarlos automáticamente.  

La experimentación se apoyó en IA generativa (ChatGPT) para la generación inicial de código, que demostró ser una herramienta eficiente y complementaria al conocimiento adquirido, optimizando tiempos y resultados.  

---

## Herramientas utilizadas  

- Lenguaje: Python 3  
- Editor: VSCode  
- Latex: Overleaf (para informe en PDF)  
- Sniffer de red: Wireshark (para verificar tráfico ICMP)  
- Sistema operativo: Linux (Arch Linux)  
- IA generativa: ChatGPT  

---

## Estructura del proyecto  

```
├── actividades/
│ ├── ac1/ # Imágenes y capturas de la Actividad 1
│ ├── ac2/ # Imágenes y capturas de la Actividad 2
│ ├── ac3/ # Imágenes y capturas de la Actividad 3
├── [algoritmo_cifrado.py](./algoritmo_cifrado.py)
├── [captura.pcap](./captura.pcap)
├── [lab01_informe.tex](./lab01_informe.tex)
├── [MitM.py](./MitM.py)
├── [modo_stealth.py](./modo_stealth.py)
└── [README.md](./README.md)
```

---

## Librerías necesarias  

Antes de ejecutar los programas, instalar las siguientes dependencias en Python 3:  

```bash
pip install scapy pyspellchecker
```

---

## Ejecución de los programas

### `algoritmo_cifrado.py`

Implementa el cifrado César, recibiendo como parámetros el texto y el desplazamiento.

```
python3 algoritmo_cifrado.py -t "<frase/palabra a cifrar>" -d <desplazamiento a aplicar>

```

---

### `modo_stealth.py`

Envía un mensaje caracter por caracter en paquetes ICMP Echo Request, simulando un tráfico de red legítimo.

```
python3 modo_stealth.py -d <IP destino> -m "<frase/palabra a cifrar>"
```

La transmisión puede verificarse con Wireshark, aplicando filtros:

```
icmp && ip.dst == <IP destino>
```

---

### `MitM.py`

Procesa una captura `.pcap` con paquetes ICMP y reconstruye el mensaje. Luego aplica fuerza bruta con desplazamientos posibles (0–25) del cifrado César, seleccionando automáticamente la frase más probable en español.

```
python3 MitM.py -f <ruta del archivo .pcap>

```

