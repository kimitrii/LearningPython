#we can do in this way a web browser
#import socket

#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#mysock.send(cmd)

#while True:
#    data = mysock.recv(512)
#    if len(data) < 1:
#        break
#    print(data.decode(),end='')
#mysock.close()

#But we can simplify it, and do in this way with librarie
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

#we can make a dictionary
#decode() means bytes, not string
fhand2 = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand2:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
