import socket
import threading

IP = "10.1.8.250"
PORT = 5568
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None)
client.connect(ADDR)


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
    elif command == 'message':
        text_message = input("Enter your message: ")
        return f"{command} {text_message}"
    else:
        print("Invalid command")
        return None


def main():
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
    connected = True

    while connected:
        command = input("Type a command (read, write, execute, message) or type !DISCONNECT to disconnect: ")

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
