import socket
import threading
import os

IP = "10.1.8.251"
PORT = 5568
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

print("[STARTING] Server is starting...")
server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None)
server.bind(ADDR)

first_client = None


def handle_client(conn, addr):
    global first_client

    print(f"[NEW CONNECTION] {addr} connected.")

    if first_client is None:
        first_client = conn
        print(f"[FULL ACCESS] Granted full access to {addr}")
    else:
        print(f"[READ-ONLY ACCESS] Granted read-only access to {addr}")

    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
            continue

        print(f"[{addr}] {msg}")

        try:
            command, *rest = msg.split()
            if command == "read":
                try:
                    with open(rest[0], "r") as file:
                        content = file.read()
                    conn.send(content.encode(FORMAT))
                except FileNotFoundError:
                    conn.send("File not found.".encode(FORMAT))
            elif command == "write" and rest and conn == first_client:
                filename, content = rest[0], " ".join(rest[1:])
                with open(filename, "a") as file:
                    file.write(content + "\n")
                conn.send("File written successfully.".encode(FORMAT))
            elif command == "execute" and rest and conn == first_client:
                output = os.popen(rest[0]).read()
                conn.send(output.encode(FORMAT))
            elif command == "message":
                # Handle text messages from the client
                text_message = " ".join(rest)
                response = input(f"Received message from {addr}: {text_message}\nType your response: ")
                conn.send(response.encode(FORMAT))
            else:
                conn.send("Invalid command or insufficient permissions.".encode(FORMAT))
        except Exception as e:
            conn.send(f"Error: {str(e)}".encode(FORMAT))

    conn.close()


def main():
    server.listen(5)
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[SERVER] Server is starting")
main()

#aaaaaa