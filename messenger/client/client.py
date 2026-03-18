import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

# Отправляем сообщение серверу
client.send("Привет, Сервер! Это мой первый мессенджер!".encode('utf-8'))

# Получаем ответ и печатаем его
answer = client.recv(1024).decode('utf-8')
print(f"Сервер ответил: {answer}")

# Хороший тон: закрываем дверь
client.close()