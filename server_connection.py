import socket
import pygame
from pygame.locals import *
import time
import button

host = ''
port = 5580

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind comlete.")
    return s

def setupConnection():
    s.listen(1) # Allows one connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ": " + str(address[1]))
    return conn

def dataTransfer(conn):
    # A big loop that sends/receives data until told not to.
    while True:
        # Receive the data
        data = conn.recv(1024) # receive the data
        data = data.decode('utf-8')
        if data == 'EXIT':
            print("client exited")
            break
        elif data == 'KILL':
            print("program killed")
            s.close()
            break
        elif data == 'w':
            reply = "forward"
        elif data == 'a':
            reply = "left"
        elif data == 'd':
            reply = "right"
        elif data == "u":
            reply = "up"
        elif data == "j":
            reply = "down"
        else:
            reply = "unknown command"
        # Send the reply back to the client
        conn.sendall(str.encode(reply))
        print("Data has been sent!")
    conn.close()

s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break