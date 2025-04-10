# ===== СЕРВЕР (server.py) =====
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.bind((HOST, PORT))
    s.listen()
    print("[Сервер] Очікування двох клієнтів...")

    conn1, addr1 = s.accept()
    print(f"[Сервер] Клієнт 1 підключений: {addr1}")
    name1 = conn1.recv(1024).decode('utf-8')

    conn2, addr2 = s.accept()
    print(f"[Сервер] Клієнт 2 підключений: {addr2}")
    name2 = conn2.recv(1024).decode('utf-8')

    conn1.send(f"Спілкуєтесь з {name2}".encode('utf-8'))
    conn2.send(f"Спілкуєтесь з {name1}".encode('utf-8'))

    try:
        while True:
            msg1 = conn1.recv(1024).decode('utf-8')
            if msg1.lower() == 'вихід':
                break
            conn2.send(f"{name1}: {msg1}".encode('utf-8'))

            msg2 = conn2.recv(1024).decode('utf-8')
            if msg2.lower() == 'вихід':
                break
            conn1.send(f"{name2}: {msg2}".encode('utf-8'))
    finally:
        conn1.close()
        conn2.close()
        print("[Сервер] З'єднання закрито")
