import socket
import threading
import sys
import pickle
import os

#59986



class Servidor():

    #Inicializamos obteniendo nuestra ip(getHostName) y pidiendo el puerto al usuario
    def __init__(self, host=socket.gethostname(), port = int(input("Introduzca el puerto deseado:"))):
        self.clientes = []
        self.nicknames = []#Creamos un array para guaradr los usuarios conectados
        self.sock = socket.socket()
        self.sock.bind((str(host), int(port)))#Asignamos la direccion y el puerto a la que el cliente se podra conectar 
        self.sock.listen(20)#Especifica el número de conexiones no aceptadas que permitirá el sistema antes de rechazar nuevas conexiones. 
        self.sock.setblocking(False)
        aceptar = threading.Thread(target=self.aceptarC)#Ponemos dos hilos a aceptar y procesar mensajes continuamente para cuando alguno llegue
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
            else:
                pass

    def broadcast(self, msg, cliente):#Funcion que encia a todos los clientes conectados el mensaje menos al que lo envia
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
                data = conn.recv(32)#Recogemos el nickname
                self.nicknames.append(data)#Metemos el nickname en el array
                print("Usuarios Conectados: ")
                for n in self.nicknames:
                    print(pickle.loads(n))#Recorremos el array nicknames printeando el nickname deserializado
                self.clientes.append(conn)#Anadimos el cliente a la lista de clientes 
                
            except:
                pass


    def procesarC(self):
        print("Procesamiento de mensajes iniciado")
        print(socket.gethostbyname(socket.gethostname()))#Printeamos la ip
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(32)
                        
                        if data:
                            with open('u22016494.txt','a') as writer:#Guardamos los mensajes en el .txt mediante el with para que se cierre automaticamente
                                 writer.write(pickle.loads(data) + "\n")#Debemos de guardar el mensaje deserializado 
                            self.broadcast(data,c)
                            
                            

                    except:
                        pass

s=Servidor()








