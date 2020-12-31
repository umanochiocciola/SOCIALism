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
print('type stop to save & close')
while 1:
    dude = input('Title of the post to remove: ')
    if dude == 'stop': break
    try: banca.pop(dude)
    except: print('No post named like that')

salva()
