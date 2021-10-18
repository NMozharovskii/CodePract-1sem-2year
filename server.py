import socket

sock = socket.socket()
sock.bind(('localhost', 9092)) #Адрес сервера

while True:
	msg = ''
	sock.listen(1) #Устанавливаем количнество подключений
	conn, addr = sock.accept() #Принимаем подключерие
	print(addr)
	data = conn.recv(1024) #Количество байт для чтения
	msg += data.decode() #Декодируем сообщение
	conn.send(data) #Отправляем сообщение обратно
	print(msg)
	if data.decode()=='exit': #Условие на выход
		break

