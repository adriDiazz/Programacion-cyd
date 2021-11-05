import threading
import sys
import socket
import pickle
import os

class Cliente():
    
    #Inicizlizamos pasandole mediante inout del usuario el host(ip) y el puerto deseado
    def __init__(self, host = input("Introduzca la IP:"), port = int(input("Introduzca el puerto deseado:"))):

        nickname = input("Nickname:")#Pedimos al usuario el nickname para que pueda identificarse antes de entrar al chat
        
        self.sock = socket.socket()#Creamos el socket
        self.sock.connect((str(host), int(port)))#Nos conectamos al host remoto mediante los datos recividos en los inputs
        self.sock.send(pickle.dumps(nickname))#Enviamos el nickname para posteriormente poder mostrar los usuarios conectados
        hilo_recv_mensaje = threading.Thread(target=self.recibir)#Creamos un hilo que tratara de recibir mensajes continuamente para ver si nos llega alguno 
        hilo_recv_mensaje.daemon = True
        hilo_recv_mensaje.start()
        print('Hilo con PID',os.getpid())
        print('Hilos activos', threading.active_count())

        while True:
            msg = input('\nEscriba texto ? ** Enviar = ENTER ** Abandonar Chat = Q \n')#Pedimos el mensaje al usuario
            if msg != 'Q' :
                self.enviar(nickname + ": " + msg)#Si es distinto de Q el mensaje se enviara
            else:
                print(" **** TALOGOOO  ****")
                self.sock.close()
                sys.exit()
    
    def recibir(self):#Funcion para recibir mensajes que mandaremos ejecutar al hilo 
        while True:
            try:
                data = self.sock.recv(32)
                if data:
                    print(pickle.loads(data))
            except:
                pass

    def enviar(self, msg):#Funcion para enviar el mensaje mediante la libreria pickle para que la informacion viaje serializada
        self.sock.send(pickle.dumps(msg))

c=Cliente()

            

                


        