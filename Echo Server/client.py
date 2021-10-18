import socket

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9092)) #Подключаемся

msg = input()
#msg = "Hi!"
sock.send(msg.encode()) #Отправка сообщения
data = sock.recv(1024) #Количество байт
sock.close() #Закрываем

print(data.decode())
