import socket

IP = "172.16.97.166"
PORT = 5568
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"


def file_type(command):
    if command == 'read':
        filename = input("Enter the filename to read: ")
        return f"{command} {filename}"
    elif command == 'write':
        filename = input("Enter the filename to write to: ")
        user_input = input(f"Enter the content to write to {filename}: ")
        msg = f"{command} {filename} {user_input}"
        return msg
    elif command == 'execute':
        filename = input("Enter the filename to execute: ")
        msg = f"{command} {filename}"
        return msg
    else:
        print("Invalid command")
        return None


def main():
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
    connected = True

    while connected:
        command = input("Type a command (read, write, execute) or type !DISCONNECT to disconnect: ")

        if command == DISCONNECT_MSG:
            client.send(command.encode(FORMAT))
            connected = False
        else:
            msg = file_type(command)
            if msg:
                client.send(msg.encode(FORMAT))
                response = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER] {response}")

    client.close()


if __name__ == "__main__":
    main()


# import socket
#
# IP = "172.20.10.10"
# PORT = 5566
# ADDR = (IP, PORT)
# SIZE = 1024
# FORMAT = "utf-8"
# DISCONNECT_MSG = "!DISCONNECT"
#
# def file_type(type, client):
#     match type:
#         case 'read':
#             client.send("read".encode(FORMAT))
#             response = client.recv(SIZE).decode(FORMAT)
#             print(response)
#         case 'write':
#             client.send("write".encode(FORMAT))
#             filename = input("Enter the filename to write to: ")
#             content = input(f"Enter the content to write to {filename}: ")
#             data = f"{filename} {content}"
#             client.send(data.encode(FORMAT))
#             print(f"Content to write: {content}")
#         case 'execute':
#             client.send("execute".encode(FORMAT))
#             response = client.recv(SIZE).decode(FORMAT)
#             print(response)
#
# def main():
#     client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None)
#     client.connect(ADDR)
#     print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
#     connected = True
#     while connected:
#         msg = input("Type a command (read, write, execute): ")
#
#         client.send(msg.encode(FORMAT))
#
#         if msg == DISCONNECT_MSG:
#             connected = False
#         else:
#             # Call file_type to handle the command
#             file_type(msg, client)
#
#             # Receive and print the response from the server
#             response = client.recv(SIZE).decode(FORMAT)
#             print(f"[SERVER] {response}")
#
#     client.close()
#
# if __name__ == "__main__":
#     main()

