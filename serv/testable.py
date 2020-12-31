'''
Admin script to remove existing posts
'''
import pickle as pk

def carica():
    global banca
    with open('dati.dat', 'rb') as f:
        banca, dummy = pk.load(f)

def salva():
    with open('dati.dat', 'wb') as f:
        pk.dump([banca, ''], f, protocol=2)


banca = {}
carica()

while 1:
    try: banca.pop(input('Title of the post to remove: '))
    except: print('No post named like that')

salva()
