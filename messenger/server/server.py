import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(1)
print("Сервер запущен и ждет подключений...")

client_socket, address = server.accept()
print(f"Ура! Кто-то подключился! Его адрес: {address}")

message = client_socket.recv(1024).decode('utf-8')
print(f"Клиент написал: {message}")

client_socket.send("Привет, клиент! Связь установлена!".encode('utf-8'))

# Хороший тон: закрываем за собой двери
client_socket.close()
server.close()