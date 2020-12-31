import socket
import sys
import tkinter as tk
from tkinter import ttk

TITLE="SOCIAL NETTùORC"

win = tk.Tk()
win.title(TITLE)
win.geometry("800x500")
win.configure(bg='gray10')

def invia_comandi(s, comando):
    global ffre
    s.send(comando.encode())
    data = s.recv(4096)
    print("Killing connection...")
    s.close()
    ffre = data.decode()

def conn_sub_server(indirizzo_server, richie):
    try:
        s = socket.socket()
        s.connect(indirizzo_server)
        print(f"Succesfully connected to { indirizzo_server }")
        invia_comandi(s, richie)
    except socket.error as errore:
        print(f"Connection error \n{errore}")

def main():
    global but, c, b, serie, episodio
    global ib, port
    global req
    global out
    
    ib, port = serie.get(), episodio.get()
    if port=='': port = 1000
    
    tit = tk.Label(text=TITLE, fg='DarkGoldenrod1', bg='gray15')
    req = tk.Entry()
    homebut = tk.Button(text='Home', bg='grey', command=GoBackHome)
    gebut = tk.Button(text='Search', bg='grey', command=get)
    pobut = tk.Button(text='Post', bg='grey', command=post)
    out = tk.Label(text='-   -   -')
    
    conn_sub_server((ib, int(port)), 'index')
    out.configure(text=ffre)
    
    but.destroy()
    c.destroy()
    b.destroy()
    serie.destroy()
    episodio.destroy()
    
    tit.pack()
    req.pack()
    homebut.pack()
    gebut.pack()
    pobut.pack()
    out.pack()
    
    win.mainloop()
    
def get():
    global req
    global out
    global ib, port

    conn_sub_server((ib, int(port)), f'{req.get()}')
    out.configure(text=f'result:\n' + ffre.replace('type\n    post_<name>_<article>', 'click on Post'))

def post():
    global req
    global out, ferb, art, fin, canc
    global ib, port
    
    ferb = tk.Label(text=f'Writing post: {req.get()}')
    art = tk.Entry()
    fin = tk.Button(text='Upload', command=lesgo)
    canc = tk.Button(text='Cancel', command=cance)
    
    ferb.pack()
    art.pack()
    fin.pack()
    canc.pack()
  
def cance():
    global ferb, art, fin, canc
    ferb.destroy()
    art.destroy()
    fin.destroy()
    canc.destroy()

def lesgo():
    global art, ib, port, req
    global ferb, art, fin
    conn_sub_server((ib, int(port)), f'post_{req.get()}_{art.get()}')
    
    ferb.destroy()
    art.destroy()
    fin.destroy()
    canc.destroy()

def GoBackHome():
    global req
    global out
    global ib, port

    conn_sub_server((ib, int(port)), 'index')
    out.configure(text=f'result:\n' + ffre.replace('type\n    post_<name>_<article>', 'click on Post'))


ib = art = port = req = out = ferb = art = canc = fin = None
ffre = '---'

b = tk.Label(text='ip', fg='white', bg='gray15')
serie = tk.Entry()
c = tk.Label(text='port (deafult 1000)', fg='white', bg='gray15')
episodio = tk.Entry()
but = tk.Button(text='Connect',bg='grey', command=main)

b.pack()
serie.pack()
c.pack()
episodio.pack()
but.pack()

win.mainloop()