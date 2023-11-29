import socket
import threading
import os

IP = "192.168.1.7"
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
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
                # Handle read operation
                try:
                    with open(rest[0], "r") as file:
                        content = file.read()
                    conn.send(content.encode(FORMAT))
                except FileNotFoundError:
                    conn.send("File not found.".encode(FORMAT))
            elif command == "write" and rest:
                # Handle write operation
                filename, content = rest[0], " ".join(rest[1:])
                with open(filename, "a") as file:
                    file.write(content + "\n")
                conn.send("File written successfully.".encode(FORMAT))
            elif command == "execute" and rest:
                # Handle execute operation
                output = os.popen(rest[0]).read()
                conn.send(output.encode(FORMAT))
            else:
                conn.send("Invalid command.".encode(FORMAT))
        except Exception as e:
            conn.send(f"Error: {str(e)}".encode(FORMAT))

    conn.close()