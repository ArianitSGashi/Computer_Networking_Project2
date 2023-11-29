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


