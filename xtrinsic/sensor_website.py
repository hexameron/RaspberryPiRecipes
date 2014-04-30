#!/usr/bin/env python
import math
import time
import threading
import queue
import termios, fcntl, sys, os
from ctypes import *
#cdll.LoadLibrary("./bcm2835.so")

sensor = CDLL("./sensor.so")

class MMA8491Q_DATA(Structure):
	_fields_  = [("Xout", c_int16),
	("Yout", c_int16),
	("Zout", c_int16)]

class mag3110:
		
	def __init__(self):

		if ( True == os.path.exists('mag_calibration.data')):
			f_cal = open("mag_calibration.data", 'r')
			s = f_cal.readline()
			[self.x_off, self.y_off, self.z_off] = s.split()
			f_cal.close()
		else:
			self.x_off = -565
			self.y_off = 700
			self.z_off = 0
		
		if (0 == sensor.bcm2835_init()):
			#print "bcm3835 driver init failed."
			return
		
	def writeRegister(self, register, value):
	    sensor.MAG3110_WRITE_REGISTER(register, value)

	def readRegister(self, register):
		return sensor.MAG3110_READ_REGISTER(register)
	
	def __str__(self):
		ret_str = ""
		(x, y, z) = self.getAxes()
		ret_str += "X: "+str(x) + "  "
		ret_str += "Y: "+str(y) + "  "
		ret_str += "Z: "+str(z)
		
		return ret_str

	def init(self):
		sensor.MAG3110_Init()
	def readRawData_x(self):
		return sensor.MAG3110_ReadRawData_x()

	def readRawData_y(self):
		return sensor.MAG3110_ReadRawData_y()

	def readRawData_z(self):
		return sensor.MAG3110_ReadRawData_z()

	def getAxes(self):
		x = self.readRawData_x()
		y = self.readRawData_y()
		z = self.readRawData_z()

		return (x, y, z)

	def readAsInt(self):
		x = self.readRawData_x() / 40
		y = self.readRawData_y() / 40 
		z = self.readRawData_z() / 40

		return (x, y, z)
		 		
	def getHeading(self):
		(x, y, z) = self.getAxes()
		
		heading = math.atan2((y-int(self.y_off)), (x-int(self.x_off))) * 180/math.pi + 180
		
		return heading

	def calibrate(self, x, y, z):
		max_x = max(x)
		max_y = max(y)
		max_z = max(z)

		min_x = min(x)
		min_y = min(y)
		min_z = min(z)
		
		self.x_off = (max_x + min_x) / 2
		self.y_off = (max_y + min_y) / 2 
		self.z_off = 0 #(max_z + min_z) / 2

		
class mpl3115a2:
	def __init__(self):
		if (0 == sensor.bcm2835_init()):
			#print "bcm3835 driver init failed."
			return
			
	def writeRegister(self, register, value):
	    sensor.MPL3115A2_WRITE_REGISTER(register, value)
	    
	def readRegister(self, register):
		return sensor.MPL3115A2_READ_REGISTER(register)

	def active(self):
		sensor.MPL3115A2_Active()

	def standby(self):
		sensor.MPL3115A2_Standby()

	def initAlt(self):
		sensor.MPL3115A2_Init_Alt()

	def initBar(self):
		sensor.MPL3115A2_Init_Bar()

	def readAlt(self):
		return sensor.MPL3115A2_Read_Alt()

	def readTemp(self):
		return sensor.MPL3115A2_Read_Temp()

	def setOSR(self, osr):
		sensor.MPL3115A2_SetOSR(osr);

	def setStepTime(self, step):
		sensor.MPL3115A2_SetStepTime(step)

	def getTemp(self):
		t = self.readTemp()
		t_m = (t >> 8) & 0xff;
		t_l = t & 0xff;

		if (t_l > 99):
			t_l = t_l / 1000.0
		else:
			t_l = t_l / 100.0
		return (t_m + t_l)

	def getAlt(self):
		alt = self.readAlt()
		alt_m = alt >> 8 
		alt_l = alt & 0xff
		
		if (alt_l > 99):
			alt_l = alt_l / 1000.0
		else:
			alt_l = alt_l / 100.0
			
		return self.twosToInt(alt_m, 16) + alt_l
	def getBar(self):
		alt = self.readAlt()
		alt_m = alt >> 6 
		alt_l = alt & 0x03
		
		if (alt_l > 99):
			alt_l = alt_l 
		else:
			alt_l = alt_l 

		return (self.twosToInt(alt_m, 18))

	def twosToInt(self, val, len):
		# Convert twos compliment to integer
		if(val & (1 << len - 1)):
			val = val - (1<<len)

		return val

class mma8491q:
	def __init__(self):
		if (0 == sensor.bcm2835_init()):
			#print "bcm3835 driver init failed."
			return	

	def init(self):
		sensor.MMA8491Q_Init()
		
	def enable(self):
		sensor.MMA8491Q_Enable()

	def disEnable(self):
		sensor.MMA8491Q_DisEnable()
		
	def writeRegister(self, register, value):
		sensor.MMA8491Q_WRITE_REGISTER()

	def readRegister(self, register):
		return sensor.MMA8491Q_READ_REGISTER()

	def read(self, data):
		sensor.MMA8491_Read(data)	

	def getAccelerometer(self):
		data = 	MMA8491Q_DATA()
		pdata = pointer(data)
		self.read(pdata)
		return (data.Xout, data.Yout, data.Zout);
		
	def __str__(self):
		ret_str = ""
		(x, y, z) = self.getAccelerometer()
		ret_str += "X: "+str(x) + "  "
		ret_str += "Y: "+str(y) + "  "
		ret_str += "Z: "+str(z)
		
		return ret_str
		
	def twosToInt(self, val, len):
		# Convert twos compliment to integer
		if(val & (1 << len - 1)):
			val = val - (1<<len)

		return val
		

import time
import urllib.request
#from board_revision import revision

def sensor_thread():
	while True:
		if (c == 1):
			heading = mag3110.getHeading()
			url = 'http://127.0.0.1/sensors/compass.php?heading=%d' % heading
			urllib.request.urlopen(url)	
		elif (c == 2):
			temper = mpl.getTemp()
			url = 'http://127.0.0.1/sensors/temper.php?temper=%f' % temper
			urllib.request.urlopen(url)
		elif (c == 3):
			mma.init()
			mma.enable()
			(x, y, z) = mma.getAccelerometer()
			url = 'http://127.0.0.1/sensors/gsensor.php?x=%d&y=%d' %(x, y)
			urllib.request.urlopen(url)
			time.sleep(0.3)
		else:
			break
		

c = 1
mag3110 = mag3110()
mag3110.init()
mpl = mpl3115a2()
mpl.initAlt()
mpl.active()
time.sleep(1)
mma = mma8491q()

t_sensor = threading.Thread(target=sensor_thread)
t_sensor.start()

print ("Input your choice for sensor\n 1. mag3110\n 2. mpl3115\n 3. mma8491\n 0. exit")
while True:
	c = int(input("Your choice: "))
	if (c == 0):
		break
	elif (c == 1):
		print ("=================================================================")
		print ("mag3110 sensor data will upload to compass.html")
		print ("Use browser to open http://<rpi IP>/sensors/compass.html")
		print ("Horizontally rotate your board, you can see the compass rotation")
		print ("=================================================================")
	elif (c == 2):
		print ("=================================================================")
		print ("mpl3115 sensor data will upload to temper.html")
		print ("Use browser to open http://<rpi IP>/sensors/temper.html")
		print ("Touch your sensor board, you can see temperature value")
		print ("=================================================================")
	elif (c == 3):
		print ("=================================================================")
		print ("mma8491 sensor will upload to gsensor.html")
		print ("Use browser to open http://<rpi IP>/sensors/gsensor.html")
		print ("The small car on the web will be controled by the board.")
		print ("Vertical and horizontal rotation will move the car correspondingly")
		print ("=================================================================")


	





	
