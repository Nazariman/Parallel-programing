# ===== КЛІЄНТ (client.py) =====
import socket
import threading

def receive_message(client):
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg:
                print("\n" + msg)
        except:
            break

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    name = input("Введіть ваше ім'я: ")
    s.send(name.encode('utf-8'))

    print(s.recv(1024).decode('utf-8')) # повідомлення з іменем співрозмовника

    t = threading.Thread(target=receive_message, args=(s,), daemon=True)
    t.start()

    while True:
        msg = input("Ви: ")
        s.send(msg.encode('utf-8'))
        if msg.lower() == 'вихід':
            break
        data = s.recv(1024).decode('utf-8')
        print(data)

    print("Чат завершено.")