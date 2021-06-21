import socket
import time

from codex_queue import Queue


class Server:

    def __init__(self, ip, port):
        self.queue = Queue(ip, port)
        self._run = True

    def start_server(self):
        self.queue.start_server()

    def stop_server(self):
        self.queue.stop_server()

    def loop(self):
        while self._run:
            time.sleep(1)
            if self.queue.exists():
                self.handle(self.queue.get())

    def send(self, ip, port, message):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        try:
            sock.sendall(bytes(message, 'ascii'))
        finally:
            sock.close()

    def handle(self, message):
        """
        Prototype
        """
        pass