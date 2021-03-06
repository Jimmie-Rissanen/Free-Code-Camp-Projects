import socket

url = input('Enter URL: ')


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((url, 80 or 443))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
