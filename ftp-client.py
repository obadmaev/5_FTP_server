import socket
PORT = 8083

def func():
    print('Чтобы посмотреть список доступных команд, введите слово help')
    while True:
        request = input('$ ')
        if request == 'exit': #разрыв соединения
            break
        with socket.socket() as sock:
            sock.connect(('localhost', PORT))
            sock.send(request.encode())  #посылаем команду серверу
            response = sock.recv(1024).decode()
            if response:
                print(response)

print(func())
