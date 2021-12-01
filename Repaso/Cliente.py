
#22016494

import threading
import pyrebase as py
import socket 
import pickle
import os
import sys

firebaseConfig = {
 "apiKey": "AIzaSyDvaqx4FUfvBVF75fo--uPXWCnq626rbaM",
  "authDomain": "repaso-a4bc2.firebaseapp.com",
  "databaseURL": "https://repaso-a4bc2-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "repaso-a4bc2",
  "storageBucket": "repaso-a4bc2.appspot.com",
  "messagingSenderId": "997466082272",
  "appId": "1:997466082272:web:578b1289aebe4463653985"
}

firebase = py.initialize_app(firebaseConfig)#Iniciamos el servidor 
ddbb = firebase.database()

class Cliente():
    host_ = input("Escribe la ip a donde desea conectarse: ")
    port_ = int(input("Escriba el puerto con el que desea comunicarse: "))
    nick = input("Nombre de usuario: ")

    nicks = []
    
    mail=nick+'@live.uem.es'
    ddbb.child('repasoParcial/22016494/client/'+nick+'/user/').set(mail) ##Se guarda el user en la carpeta Credenciales en la Base de Datos


    def __init__(self, host=socket.gethostname(), port=port_, nickname=nick):
        self.sock = socket.socket()
        self.sock.connect((str(host), int(port)))
        hilo_recv_mensaje = threading.Thread(target=self.recibir)
        hilo_recv_mensaje.daemon = True
        hilo_recv_mensaje.start()
        print('Hilo con PID', os.getpid())
        print('Hilos activos', threading.active_count())
        self.enviarNick(nickname)
       
        while True:
            msg = input('\nEscriba texto ? ** Enviar = ENTER ** Abandonar Chat = Q \n')
            ddbb.child('repasoParcial/22016494/client/'+nickname+'/mensaje/').push(msg) ##Se guarda el user en la carpeta Credenciales en la Base de Datos
            if msg != 'Q':
                self.enviar(nickname + ": " + msg)
            else:
                print(" **** TALOGOOO  ****")
                self.sock.close()
                sys.exit()

    def recibir(self):
        while True:
            try:
                data = self.sock.recv(32)
                if data:
                    print(pickle.loads(data))
            except:
                pass

    def enviar(self, msg):
        self.sock.send(pickle.dumps(msg))

    def enviarNick(self, nick_):
        self.sock.send(pickle.dumps(nick_))


c = Cliente()