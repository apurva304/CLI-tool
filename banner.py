import socket


class banner:
    def __init__(self,Host):

        #Host = str(input("Enter url \n"))
        try:
            host = socket.gethostbyname(Host)
            print(host)
        except:
            print("[-] Cannot resolve '%s': Unknown host" % Host)
            exit(0)

        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con.connect((host, 80))

        try:
            con.send(b'GET / HTTP/1.1\r\n\r\n')
            ret = con.recv(1024)
            print(ret.decode('utf-8'))
        except Exception as e:
            print("[-] Unable to grab any information: " + str(e))
        con.close()
