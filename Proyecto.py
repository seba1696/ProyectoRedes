# -*- coding: utf-8 -*-

import time
import os
import random
import socket
import threading
import sys

class Server():

	def __init__(self):
		self.host = 'localhost'
		self.port = 9999
		self.maxcon = 10

	def start(self):
		self.s = socket.socket()
		self.s.bind((self.host, self.port))
		self.s.listen(self.maxcon)
		op = None
		while True:
			client1 = Client(self.s.accept(),"1", op)
			client1.start()
			return client1.op


	tablero1 = [[" "," "," ","1","2","3","4","5","6","7","8","9"," "],[" ","   ------------------"," "],[" ","A","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"], [" ","B","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"], [" ","C","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"], [" ","D","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"], [" ","E","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"],[" ","F","|",'O','O','O','O','O','O','O','O','O',"|"],[" ","G","|",'O','O','O','O','O','O','O','O','O',"|"],[" ","H","|",'O','O','O','O','O','O','O','O','O',"|"],[" ","I","|",'O','O','O','O','O','O','O','O','O',"|"]]
        tablero2 = [[" "," "," ","1","2","3","4","5","6","7","8","9"," "],[" ","   ------------------"," "],[" ","A","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"], [" ","B","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"], [" ","C","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"], [" ","D","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"], [" ","E","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"],[" ","F","|",'O','O','O','O','O','O','O','O','O',"|"],[" ","G","|",'O','O','O','O','O','O','O','O','O',"|"],[" ","H","|",'O','O','O','O','O','O','O','O','O',"|"],[" ","I","|",'O','O','O','O','O','O','O','O','O',"|"]]
        
	def Quit(self, respuesta):
		if respuesta == 'quit':
			time.sleep(0.5)
			os.system("clear")
			sys.exit()
		else:
			print " " 

	def print_tablero(self,tablero):
		print "-----------------------------"
		print "|      BATALLA NAVAL        |"
    		print "-----------------------------"
		print "-----------------------------"
		for fila in tablero:
			print "|"+" ".join(fila)+"  |"
		print "-----------------------------"

	def Barco(self,y):
    		coordenada=[]
    		if len(y)==2:
        		y=y.lower()
        		if y[0]=="a" or y[0]=="b" or y[0]=="c" or y[0]=="d" or y[0]=="e" or y[0]=="f" or y[0]=="g" or y[0]=="h" or y[0]=="i":
            			if y[1]=="1" or y[1]=="2" or y[1]=="3" or y[1]=="4" or y[1]=="5"or y[1]=="6" or y[1]=="7" or y[1]=="8" or y[1]=="9":
                			if y[0]=="a":
                    				coordenada.append(2)
                    				coordenada.append(int(y[1])+2)
                    				coordenada.append("Y") 
                			elif y[0]=="b":
                    				coordenada.append(3)
                    				coordenada.append(int(y[1])+2)
                    				coordenada.append("Y")
                			elif y[0]=="c":
                   				coordenada.append(4)
                   				coordenada.append(int(y[1])+2)
                   				coordenada.append("Y")
                			elif y[0]=="d":
                    				coordenada.append(5)
                    				coordenada.append(int(y[1])+2)
                    				coordenada.append("Y")
                			elif y[0]=="e":
                    				coordenada.append(6)
                    				coordenada.append(int(y[1])+2)
                    				coordenada.append("Y")
					elif y[0]=="f":
                  				coordenada.append(7)
                    				coordenada.append(int(y[1])+2)
                    				coordenada.append("Y")
					elif y[0]=="g":
                    				coordenada.append(8)
                    				coordenada.append(int(y[1])+2)
                    				coordenada.append("Y")
					elif y[0]=="h":
						coordenada.append(9)
                    				coordenada.append(int(y[1])+2)
                    				coordenada.append("Y")
					elif y[0]=="i":
						coordenada.append(10)
                    				coordenada.append(int(y[1])+2)
                    				coordenada.append("Y")
                			return coordenada
           			else:
                			coordenada=[None,None,"N"]
 		        	        return coordenada
        		else:
            			coordenada=[None,None,"N"]
            			return coordenada
    		else:
        		coordenada=[None,None,"N"]
        		return coordenada

	def Posicion1(self):
   		while True:
			print " ----------------------------"
   		  	print "|   Coordenada del barco:   |"
   		     	Coordenada_Jugador= raw_input("  --> ")
			print "|                           |"
			print " ----------------------------"
			time.sleep(0.5)
			self.Quit(Coordenada_Jugador)
   		     	Coordenada_Jugador=self.Barco(Coordenada_Jugador) 
   		     	if Coordenada_Jugador[2]=="Y":
   		         	return Coordenada_Jugador
   		         	break
   		     	else:
   		         	print" ----------------------------"
   		         	print " | !!Coordenada invalida¡¡  |"
				print" ----------------------------"

	def Posicion2(self):
    		while True:
        		print " ----------------------------"
   		  	print "|   Coordenada del barco:   |"
   		     	Coordenada_Jugador2= raw_input("  --> ")
			print "|                           |"
			print " ----------------------------"
			time.sleep(0.5)
			self.Quit(Coordenada_Jugador2)
        		Coordenada_Jugador2=self.Barco(Coordenada_Jugador2)
        		if Coordenada_Jugador2[2]=="Y":
        	    		return Coordenada_Jugador2
        	    		break
        		else:
        	    		print" ----------------------------"
   		         	print " | !!Coordenada invalida¡¡  |"
				print" ----------------------------"

	def Fila_Aleatoria(self,tablero2):
  		return random.randint(2,len(tablero2)-1)
 
	def Columna_Aleatoria(self,tablero2):
        	return random.randint(3,len(tablero2[0])-1)

	def Ataque_Jugador(self):
		while True:
			print " ----------------------------"
			print "|   Coordenada de ataque:   |"
   		     	Coordenada_Jugador= raw_input("  --> ")
			print "|                           |"
			print " ----------------------------"
			time.sleep(0.5)
			self.Quit(Coordenada_Jugador)
        		Coordenada_Jugador=self.Barco(Coordenada_Jugador)
        		if Coordenada_Jugador[2]=="Y":
        	    		return Coordenada_Jugador
        	    		break
        		else:
        	    		print" "
        	    		print "Error, ingrese una coordenada valida.\n" 

	def Ataque_Jugador2(self):
    		while True:
        		print " ----------------------------"
			print "|   Coordenada de ataque:   |"
   		     	Coordenada_Jugador2= raw_input("  --> ")
			print "|                           |"
			print " ----------------------------"
			time.sleep(0.5)
			self.Quit(Coordenada_Jugador2)
        		Coordenada_Jugador2=self.Barco(Coordenada_Jugador2)
        		if Coordenada_Jugador2[2]=="Y":
            			return Coordenada_Jugador2
            			break
        		else:
            			print" "
            			print "Error, ingrese una coordenada valida.\n"

	def VS1(self,Jugador_Fila1,Jugador_Col1,Jugador_FilaY,Jugador_ColY, tablero1):
    		vs=0
    		if Jugador_FilaY == Jugador_Fila1 and Jugador_ColY == Jugador_Col1:
        		tablero1[Jugador_Fila1][Jugador_Col1]="X"
        		os.system("clear")
        		print " "
        		self.print_tablero(tablero1)
        		print "|   __--Barco hundido--__   |"
        		print "-----------------------------"
        		print "|  Jugador1 Gana la partida |"
        		print "-----------------------------"
   			print ""
			self.Quit(Coordenada_Jugador)
        		vs=1
        		return vs 
    		elif tablero1[Jugador_Fila1][Jugador_Col1] =="W":
			print "-----------------------------"
        		print "| _--Coordenada repetida--_ |"
			print "-----------------------------"
    		else:
        		tablero1[Jugador_Fila1][Jugador_Col1]="W"
        		print "-----------------------------"
        		print "|      _--Fallaste--_       |"
			print "-----------------------------"

	def VS2(self,Jugador_Fila2,Jugador_Col2,Jugador_FilaX,Jugador_ColX,tablero2):
    		vs=0
    		if Jugador_FilaX == Jugador_Fila2 and Jugador_ColX == Jugador_Col2:
        		tablero2[Jugador_Fila2][Jugador_Col2]="X"
        		os.system("clear")
        		print " "
        		print " "
        		self.print_tablero(tablero2)
        		print "|   __--Barco hundido--__   |"
        		print "-----------------------------"
        		print "|  Jugador2 Gana la partida |"
        		print "-----------------------------"
			print ""
			self.Quit(Coordenada_Jugador)
        		vs=1
        		return vs
    		elif tablero2[Jugador_Fila2][Jugador_Col2] =="W":
        		print "-----------------------------"
        		print "| _--Coordenada repetida--_ |"
			print "-----------------------------"
    		else:
			tablero2[Jugador_Fila2][Jugador_Col2]="W"
			print "-----------------------------"
        		print "|      _--Fallaste--_       | "
			print "-----------------------------"

	def VSB(self,Jugador_Fila,Jugador_Col,tablero2):
    		print " "
    		self.print_tablero(tablero2)
    		time.sleep(1)
    		while True:
        		Fila_Bot=random.randint(2,len(tablero2)-1)
        		Columna_Bot=random.randint(3,len(tablero2[0])-1)
        		if tablero2[Fila_Bot][Columna_Bot] !="W":
        	    		break
    		os.system("clear")
    		print "-----------------------------"
        	print "|----Turno de tu enemigo----|"
		print "-----------------------------"
    		if Fila_Bot == Jugador_Fila and Columna_Bot == Jugador_Col:
        		tablero2[Fila_Bot][Columna_Bot] ="X"
        		os.system("cls")
        		print " "
        		self.print_tablero(tablero2)
			print "|   _--Barco hundido--__    |"
        		print "----------------------------"
        		print "|       Has Perdido         |"
        		print "----------------------------"
        		print ""
        		vsb=1
        		return vsb
    		else:
        		tablero2[Fila_Bot][Columna_Bot]="W"
        		print "|   _--El Bot a fallado--_  |"
			print "-----------------------------"
        		time.sleep(1)
 
	def jugadorVSbot(self,tablero1,tablero2):
		print " "
    		self.print_tablero(tablero1)
    		Coordenada_Jugador=self.Posicion1()
    		Jugador_Fila=Coordenada_Jugador[0]
    		Jugador_Col=Coordenada_Jugador[1]
    		Barco_Fila = self.Fila_Aleatoria(tablero2)
    		Barco_Col = self.Columna_Aleatoria(tablero2)
    		while True:
        		os.system("clear")
			print "-----------------------------"
        		print "|-----Turno del Jugador-----|"
        		self.print_tablero(tablero1)
        		Coordenada_Jugador=self.Ataque_Jugador()
        		Jugador_Fila=Coordenada_Jugador[0]
        		Jugador_Col=Coordenada_Jugador[1]
        		GanadorA=self.VS1(Jugador_Fila,Jugador_Col,Barco_Fila,Barco_Col, tablero1)
        		if GanadorA==1:
        	    		vs1=1
        	    		return vs1
        	    		print ""
				self.Quit(Coordenada_Jugador)
        	    		break 
        		else:
        	    		print ""
        		os.system("clear")
			print "-----------------------------"
        		print "|----Turno de tu enemigo----|"
        		GanadorB=self.VSB(Jugador_Fila,Jugador_Col,tablero2)
        		if GanadorB==1:
        	    		vsb=1
        	    		return vsb
        	    		print ""
				self.Quit(Coordenada_Jugador)
        	    		break
        		else:
        	    		print ""

	def JugadorVsJugador(self,tablero1,tablero2):
		print "-----------------------------"
    		print "|--------Jugador1-----------|"
    		self.print_tablero(tablero1)
    		print " "
    		Coordenada_Jugador=self.Posicion1()
    		Jugador_FilaX=Coordenada_Jugador[0]
    		Jugador_ColX=Coordenada_Jugador[1]
    		os.system("clear")
    		print "-----------------------------"
    		print "|--------Jugador2-----------|"
    		self.print_tablero(tablero2)
    		print " "
    		Coordenada_Jugador2=self.Posicion2()
    		Jugador_FilaY=Coordenada_Jugador2[0]
    		Jugador_ColY=Coordenada_Jugador2[1]
    		while True:
        		os.system("clear")
        		print "-----------------------------"
        		print "|-----Turno del Jugador1----|"
        		self.print_tablero(tablero1)
        		Coordenada_Jugador=self.Ataque_Jugador()
        		Jugador_Fila1=Coordenada_Jugador[0]
        		Jugador_Col1=Coordenada_Jugador[1]
        		GanadorA=self.VS1(Jugador_Fila1,Jugador_Col1,Jugador_FilaY,Jugador_ColY,tablero1)
        		if GanadorA ==1:
            			print ""
            			break
        		os.system("clear")
        		print "-----------------------------"
        		print "|-----Turno del Jugador2----|"
        		self.print_tablero(tablero2)
        		Coordenada_Jugador2=self.Ataque_Jugador2()
        		Jugador_Fila2=Coordenada_Jugador2[0]
        		Jugador_Col2=Coordenada_Jugador2[1]
        		GanadorB=self.VS2(Jugador_Fila2,Jugador_Col2,Jugador_FilaX,Jugador_ColX,tablero2)
        		if GanadorB==1:
            			print ""
            			break

	def Run(self):
		r = 1
		print "----------------------------------------------------"
		print "|                 BATALLA NAVAL                    |"
    		print "----------------------------------------------------"
    		time.sleep(0.5)
    		while (r == 1):
			tablero1 = [[" "," "," ","1","2","3","4","5","6","7","8","9"," "],[" ","   ------------------"," "],[" ","A","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"], [" ","B","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"], [" ","C","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"], [" ","D","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"], [" ","E","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"],[" ","F","|",'O','O','O','O','O','O','O','O','O',"|"],[" ","G","|",'O','O','O','O','O','O','O','O','O',"|"],[" ","H","|",'O','O','O','O','O','O','O','O','O',"|"],[" ","I","|",'O','O','O','O','O','O','O','O','O',"|"]]
        		tablero2 = [[" "," "," ","1","2","3","4","5","6","7","8","9"," "],[" ","   ------------------"," "],[" ","A","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"], [" ","B","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"], [" ","C","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"], [" ","D","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"], [" ","E","|",'O', 'O', 'O', 'O', 'O','O','O','O','O',"|"],[" ","F","|",'O','O','O','O','O','O','O','O','O',"|"],[" ","G","|",'O','O','O','O','O','O','O','O','O',"|"],[" ","H","|",'O','O','O','O','O','O','O','O','O',"|"],[" ","I","|",'O','O','O','O','O','O','O','O','O',"|"]]
        		print "|-----------------Menu Principal-------------------|"
			print "|	    ------------------------------         |"
        		print "|	    |Selecione el modo de juego: |         |"
        		print "|	    |                            |         |"
        		print "|	    |       1--1 Jugador.        |         |"
        		print "|	    |       2--Multiplayer.      |         |"
			print "|	    |       3--Salir.            |         |"
			print "|	    ------------------------------         |"
			print "----------------------------------------------------"
        		seleccion1 = raw_input(self.start())
        		if seleccion1=="1":
            			os.system("clear")
            			self.jugadorVSbot(tablero1,tablero2)
        		elif seleccion1=="2":
            			os.system("clear")
            			self.JugadorVsJugador(tablero1,tablero2)
 			elif seleccion1=="3":
				r =0
			elif self.Quit(seleccion1):
				print ""
				
        		else:
            			print "|      --->!!Ingrese una obcion valida¡¡<---        "
				print "----------------------------------------------------"
            			time.sleep(1)
        		os.system("clear")

class Client(threading.Thread):

	def __init__(self, (sc, addr), threadID, op):
		threading.Thread.__init__(self)  
		self.sc = sc
		self.addr = addr
		self.threadID = threadID
		self.op = op

	def run(self):
		while True:
			recibido = self.sc.recv(1024)
			if recibido == "quit":
				break
			print recibido
			self.op = recibido
			self.sc.send(self.op)
		print "adios"
		self.sc.close()

if __name__ == "__main__":
	batalla = Server()
	batalla.Run()
