import socket
import sys
import pickle as pk

def carica():
    global banca
    with open('dati.dat', 'rb') as f:
        banca, dummy = pk.load(f)

def salva():
    with open('dati.dat', 'wb') as f:
        pk.dump([banca, ''], f, protocol=2)


banca = {}

def main(conn):
    richiesta = conn.recv(4096)
    stuff = richiesta.decode().split('_')
    
    print(richiesta.decode())
    
    if stuff[0] == 'post':
        if not banca.get(stuff[1], 0):
            banca.update({stuff[1]: stuff[2]})
            data = 'Post uploaded.'
            salva()
        else: data = 'A post with this name already exists'
        
    else:
        if richiesta.decode() == 'index':
            data = 'Welcome to da best social nettùorc!\nHere are all our articles, in cronological order.'
            gino = []
            for i in banca: gino.append(i)
            gino.reverse()
            for i in gino: data += f'\n{i}'
        else:
            data = banca.get(richiesta.decode(), 'no item found.\nTo create this article, type\n    post_<name>_<article>').replace('-', ' ')
    conn.sendall(data.encode())


def sub_server(indirizzo, backlog=1):
    print("Kane Stream server started")
    while 1:
        try:
            s = socket.socket()                    
            s.bind(indirizzo)                     
            s.listen(backlog)                     
            print('Ready to accept a new connection')
        except socket.error as errore:
            print(f"Something went wrong\n{errore}")
            print(f"Server reboot aptempt")
            sub_server(indirizzo, backlog=1)
        conn, indirizzo_client = s.accept()
        print(f"Connection: {indirizzo_client}")
        main(conn)
        carica()

try: carica()
except: 0

try: sub_server(("", int(sys.argv[1])))
except: sub_server(("", 1000))
