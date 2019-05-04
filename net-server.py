import socket
from threading import Thread

host = '192.168.0.31'
port = 8007

class MyThread(Thread):
    def __init__(self, conn):
        """Инициализация потока"""
        Thread.__init__(self)
        # сохраняем полученный сокет в локальной переменной
        self.csocket=conn

    def run(self):
        """Запуск потока"""
        connect=True
        while connect:
            try:
                # получаем данные из сокета, указываем размер буфера (желательно кратно 2)
                # можно указать какие-то флаги
                data = self.csocket.recv(10)
                cl_data = data.decode()
                print(self.name, " : ", cl_data.strip())
                if "bye" in cl_data:
                    self.csocket.close()
                    connect = False
            except(ConnectionResetError):
                print("ConnectionReset")
                connect=False

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(10)

    while True:
        conn, addr = s.accept()
        my_thread = MyThread(conn)
        my_thread.start()
#conn.send(data)
