# ===== СЕРВЕР (server.py) =====
import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def send_message(from_client, to_client, from_name):
    while True:
        try:
            msg = from_client.recv(1024).decode('utf-8')
            if msg.lower() == 'вихід':
                break
            to_client.send(f"{from_name}: {msg}".encode('utf-8'))
        except:
            break

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

    t1 = threading.Thread(target=send_message, args=(conn1, conn2, name1))
    t2 = threading.Thread(target=send_message, args=(conn2, conn1, name2))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    conn1.close()
    conn2.close()
    print("[Сервер] З'єднання закрито")