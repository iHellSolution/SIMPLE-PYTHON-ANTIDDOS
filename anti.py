import socket
import time

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 80))
    sock.listen(5)
    blocked_ips = {}
    def handle_connection(conn, addr):
        ip_address = addr[0]
        if ip_address in blocked_ips:
            conn.close()
            return
        data = conn.recv(1024)
        if not data.startswith('GET /'):
            conn.close()
            return
        conn.send('HTTP/1.1 200 OK\n\nServer Load!')
        conn.close()
    while True:
        conn, addr = sock.accept()
        handle_connection(conn, addr)
        print("Win Actived.")
if __name__ == '__main__':
    main()
