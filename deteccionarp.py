# Código para detectar un ataque ARP Spoofing
# Martínez Pérez Raúl

import os
import time

# Función para obtener la tabla ARP del sistema
def get_arp_table():
    arp_table = {}
    with os.popen('arp -n') as f:
        data = f.readlines()
    for line in data:
        if 'incomplete' not in line:
            parts = line.split()
            if len(parts) >= 4:
                ip = parts[0]
                mac = parts[2]
                arp_table[ip] = mac
    return arp_table

# Función para detectar cambios en la tabla ARP
def detect_arp_spoofing():
    print("Monitoreando tabla ARP para detectar cambios...")
    initial_arp_table = get_arp_table()
    print("Tabla ARP inicial:")
    for ip, mac in initial_arp_table.items():
        print(f"{ip} -> {mac}")

    while True:
        current_arp_table = get_arp_table()
        if current_arp_table != initial_arp_table:
            print("\n¡Alerta! Se ha detectado un posible ataque ARP Spoofing:")
            for ip in current_arp_table:
                if ip in initial_arp_table:
                    if initial_arp_table[ip] != current_arp_table[ip]:
                        print(f"{ip} ha cambiado de {initial_arp_table[ip]} a {current_arp_table[ip]}")
                else:
                    print(f"Nueva entrada ARP detectada: {ip} -> {current_arp_table[ip]}")
            initial_arp_table = current_arp_table
        else:
            print("No se han detectado cambios en la tabla ARP.")
        time.sleep(10)

try:
    detect_arp_spoofing()
except KeyboardInterrupt:
    print("Detección de ARP Spoofing terminada.")
