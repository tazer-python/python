import socket,threading

PORT = 5050;
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

users = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
server.bind(ADDR)

def handle(conn, addr):
    try:
        connection = True;
        while connection:
            msg = conn.recv(1024);
            if msg:
                print(msg)
                if msg != ("!DISCONNECT").encode("UTF-8"):
                    for user in users:
                        try:
                            if user == conn:
                                continue
                            user.send(msg)
                        except ConnectionAbortedError:
                            users.remove(user)
                else:
                    users.remove(conn)
                    break
                    
    except ConnectionResetError:
        users.remove(conn);



def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        users.append(conn);
        thread = threading.Thread(target = handle, args=(conn, addr));
        thread.start()
        print("Users: " + str(threading.active_count()-1))

if __name__ == "__main__":
    start()