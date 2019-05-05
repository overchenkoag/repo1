# -*- coding: utf-8 -*-
import socket
from threading import Thread
import sys

_old_excepthook = sys.excepthook
def myexcepthook(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        print ("Handler code goes here")
        s.close()
        exit()
    else:
        _old_excepthook(exctype, value, traceback)
sys.excepthook = myexcepthook

host = ''
port = 8000

class MyThread(Thread):
    # в качестве аргумента функция принимает сокет
    def __init__(self, conn,ip):
        """Инициализация потока"""
        Thread.__init__(self)
        # сохраняем полученный сокет в локальной переменной
        self.csocket=conn
        # сохраняем ip и порт клиента в локальном кортеже
        self.ip=ip

    def run(self):
        """Запуск потока"""
        connect=True
        while connect:
            try:
                # получаем данные из сокета, указываем размер буфера (желательно кратно 2)
                # можно указать какие-то флаги
                # на время выполнения команды recv поток блокируется
                data = self.csocket.recv(1024)
                # recv возвращает байтовую строку
                cl_data = data.decode()
                print(self.name, " : ", self.ip, " : ", cl_data.strip())
                if "bye" in cl_data:
                    # соединение можно закрыть функцией close
                    self.csocket.close()
                    connect = False
            # обрабатываем исключение вызова recv
            except(ConnectionResetError):
                print("ConnectionReset")
                self.csocket.close()
                connect=False

if __name__ == "__main__":
    # если наш поток - главный экзепляр, то подготавливаем сокет
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # указываем собственный ip, на который будем отвечать и tcp port
    # в качестве host можно указать "", тогда сервер будет отвечать
    # на все ip, которые установлены на машине
    s.bind((host, port))
    # включаем приём соединений. Аргумент - кол-во необслуженных соединений, которые
    # могут ожидать своей очереди. После превышения указанного кол-ва соединения будут отбрасываться
    s.listen()

    while True:
        # принимаем соединение. возвращается два значения - сокет
        # и кортеж из адреса клиента и порта клиента.
        conn, addr = s.accept()
        # создаём новый поток, передаём ему сокет и ip:port клиента
        my_thread = MyThread(conn, addr)
        my_thread.start()
#conn.send(data)
