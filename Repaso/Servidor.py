import threading
import socket
import pickle
import pyrebase as py
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

firebase = py.initialize_app(firebaseConfig) ## Iniciamos el servidor desde el Jupyterlab
ddbb=firebase.database()
dimensiones={'A':'206','B':'26'}
ddbb.child('repasoParcial/22016494/server/22016494/serverConfig').set(firebaseConfig) ##Se guarda el user en la carpeta Credenciales en la Base de Datos
ddbb.child('repasoParcial/22016494/server/22016494/dimensiones/').set(dimensiones) ##Se guarda el user en la carpeta Credenciales en la Base de Datos
storage=firebase.storage()

class Servidor():
    port_ = int(input("Escribe el puerto con el que desea comunicarse: "))

    def __init__(self, host=socket.gethostname(), port=port_):
        self.nicks = []
        self.clientes = []
        self.sock = socket.socket()
        self.sock.bind((str(host), int(port)))
        self.sock.listen(20)
        self.sock.setblocking(False)

        aceptar = threading.Thread(target=self.aceptarC)
        procesar = threading.Thread(target=self.procesarC)

        aceptar.daemon = True
        aceptar.start()

        procesar.daemon = True
        procesar.start()

        while True:
            msg = input('SALIR = Q\n')
            
            if msg == 'Q':
                print("**** TALOGOOO *****")
                self.sock.close()
                sys.exit()
            elif msg == 'p': # si el usuario escribe por el servidor una p muestra los nicks que hay guardados
                print(self.nicks)
            else:
                pass

    def broadcast(self, msg, cliente):
        for c in self.clientes:
            try:
                if c != cliente:
                    c.send(msg)
            except:
                self.clientes.remove(c)

    def aceptarC(self):
        while True:
            try:
                conn, addr = self.sock.accept()
                print(f"\nConexion aceptada via {conn}\n")
                conn.setblocking(False)
                self.clientes.append(conn)
            except:
                pass

    def procesarC(self):
        print("Procesamiento de mensajes iniciado")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(32)
                        if data:
                            self.broadcast(data, c)
                            if ": " not in pickle.loads(data): #hace una comprobacion siempre que recibe cualquier dato para ver si es un nick o un mensaje del cliente
                                self.nicks.append(pickle.loads(data)) #carga los nicks en la lista
                            else:
                                print(pickle.loads(data)) #envia el mensaje y se visualiza desde el servidor
                    except:
                        pass

s = Servidor()