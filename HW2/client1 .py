# ==== КЛІЄНТ ====

import socket
HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        city = input("Введіть назву міста (або Enter для виходу): ")
        if city == "":
            break
        s.send(city.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print(f"Прогноз погоди: {data}")
