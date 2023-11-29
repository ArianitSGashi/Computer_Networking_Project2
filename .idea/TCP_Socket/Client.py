import socket

IP = "192.168.1.7"
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def file_type(type):
    match type:
        case 'read':
            f = open("read.txt", "r")
            print(f.read())
        case 'write':
            filename = input("Enter the filename to write to: ")
            user_input = input(f"Enter the content to write to {filename}: ")
            print(f"Content to write: {user_input}")
        case 'execute':
            print("Execute..")



def main():
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
    connected = True
    while connected:
        msg = input("Type a command (read, write, execute) and file name or content: ")

        client.send(msg.encode(FORMAT))

        if msg == DISCONNECT_MSG:
            connected = False
        else:
            response = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {response}")


    client.close()

if __name__ == "__main__":
    main()