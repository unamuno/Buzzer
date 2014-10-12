# Import the required module. 
import RPi.GPIO as GPIO 
#Setup the Pins For Input 
GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN) 
GPIO.setup(3, GPIO.IN) 
GPIO.setup(25, GPIO.IN) 
GPIO.setup(11, GPIO.IN) 

#Vars for Checking if there is a change
unoorange=0
dosorange=1

unopink=0
dospink=1

unoblau=0
dosblau=1

unogruen=0
dosgruen=1



while 1:
	# Oranger Buzzer
	 if GPIO.input(2):
		if unoorange==dosorange:
			file = open("buzzer.txt", "r")
			starttest = file.readline(5)
			file.close()
			if starttest =="start":
				#Prints in the shell
				print "Orange"
				#using txt file as a cash for the color, later used by the info-beamer
				file = open("buzzer.txt", "w")
				file.write("Orange")
				file.close()
			unoorange=0
			dosorange=1
	 else: 
		if unoorange!=dosorange:
			if open("buzzer.txt", "r") !="Tot2":
				print "tot1"
			unoorange=dosorange
	 #Pinker Buzzer 
 	 if GPIO.input(3):
 		if unopink==dospink:
 			file = open("buzzer.txt", "r")
 			starttest = file.readline(5)
 			file.close()
 			if starttest =="start":
 				print "Pink"
 				file = open("buzzer.txt", "w")
 				file.write("Pink")
 				file.close()

 			unopink=0
 			dospink=1
 	 else: 
 		if unopink!=dospink:
 			print "Tot2"
 			unopink=dospink
 	
 	#Blauer Buzzer 
 	 if GPIO.input(25):
 		if unoblau==dosblau:
 			file = open("buzzer.txt", "r")
 			starttest = file.readline(5)
 			file.close()
 			if starttest =="start":
 				print "Blau"
 				file = open("buzzer.txt", "w")
 				file.write("Blau")
 				file.close()

 			unoblau=0
 			dosblau=1
 	 else: 
 		if unoblau!=dosblau:
 			print "Tot3"
 			unoblau=dosblau
 			
 	#Gruener Buzzer		
 	 if GPIO.input(11):
 		if unogruen==dosgruen:
 			file = open("buzzer.txt", "r")
 			starttest = file.readline(5)
 			file.close()
 			if starttest =="start":
 				print "Gruen"
 				file = open("buzzer.txt", "w")
 				file.write("Gruen")
 				file.close()

 			unogruen=0
 			dosgruen=1
 	 else: 
 		if unogruen!=dosgruen:
 			print "Tot4"
 			unogruen=dosgruen

	#Neustart-Checker	 
	 file = open("buzzer.txt", "r")
	 starttest = file.readline(5)
	 file.close()
	 if starttest !="start":
		 reset=""
		 reset=raw_input("Neustart? - Return.")
		 file = open("buzzer.txt", "w")
		 file.write("start")
		 file.close()
		 
	 
	 	
