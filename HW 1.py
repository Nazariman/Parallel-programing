import threading

numbers = []
input_done = threading.Event()

def input_numbers(): 
    print("Введіть числа (порожній рядок — завершити):")
    while True: 
        user_input = input("-> ")
        if user_input == "": 
            break
        try:
            num = float(user_input)
            numbers.append(num)
        except: 
            print("Введіть коректне число")
    input_done.set()

def calculate_sum():
    input_done.wait()
    total = sum(numbers)
    print(f"\n Сума чисел: {total}")


def calculate_average():
    input_done.wait()
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"Середнє арифметичне: {average}")
    else:
        print("Немає даних для обчислення середнього")


# Створення потоків
input_thread = threading.Thread(target=input_numbers)
sum_thread = threading.Thread(target=calculate_sum)
avg_thread = threading.Thread(target=calculate_average)

# Запуск усіх потоків
input_thread.start()
sum_thread.start()
avg_thread.start()


# Очікуємо завершення всіх
input_thread.join()
sum_thread.join()
avg_thread.join()

print("\nПрограма завершена")
