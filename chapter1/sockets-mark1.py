import socket

target_host="www.google.com"
targe_port=80

clinet=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clinet.connect((target_host,targe_port))

clinet.send("GET /HTTP/1.1.\r\nHost: google.com\r\n\r\n")

respon=clinet.recv(4096)

print(respon)