'''
Напишіть клієнт-серверний додаток для отримання
прогнозу погоди.
Клієнт: надсилає назву міста
Сервер: отримує прогноз погоди з json файлу та надсилає
результат клієнту. Якщо такого міста немає, то надсилає
повідомлення «Невідоме місто»
'''

# ==== СЕРВЕР ====
import socket
import json

HOST = '127.0.0.1'
PORT = 65432

# Завантаження погоди з файлу
with open('weather.json', 'r', encoding='utf-8') as f:
    weather_data = json.load(f)

# Створення сокету
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("[Сервер] Очікування підключення...")

    conn, addr = s.accept()
    with conn:
        print(f"[Сервер] Підключено: {addr}")
        while True:
            city = conn.recv(1024).decode('utf-8')
            if not city:
                break
            print(f"[Сервер] Отримано місто: {city}")
            response = weather_data.get(city, "Невідоме місто")
            conn.send(response.encode('utf-8'))
