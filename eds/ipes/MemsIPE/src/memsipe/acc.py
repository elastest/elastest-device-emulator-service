#program for testing the acceleration in G-force I2C
import smbus
import time
import os
#import RPi.GPIO as GPIO
 
# Define a class called Accel
class Accel():
         
    myBus=1
    b = smbus.SMBus(myBus)
    def setUp(self):
        self.b.write_byte_data(0x19,0x20,0x9F) # Setup the Mode
        self.b.write_byte_data(0x19,0x21,0x01) # Calibrate
        self.b.write_byte_data(0x19,0x22,0x40) # Setup the Mode
        self.b.write_byte_data(0x19,0x23,0x88) # Setup the Mode
        self.b.write_byte_data(0x19,0x24,0x00) # Setup the Mode
        self.b.write_byte_data(0x19,0x32,0x08) # Setup the Mode
        self.b.write_byte_data(0x19,0x33,0x32) # Setup the Mode
	self.b.write_byte_data(0x19,0x30,0x95) # Setup the Mode
	#self.b.write_byte_data(0x19,0x1F,0xC0) #setup the temperature mode
         
    def getValueX_l(self):
        return self.b.read_byte_data(0x19,0x28)#read the low output
    def getValueX_h(self):
        return self.b.read_byte_data(0x19,0x29)#read the High output
    def getValueY_l(self):
        return self.b.read_byte_data(0x19,0x2A)#read the low output
    def getValueY_h(self):
        return self.b.read_byte_data(0x19,0x2B)#read the High output
    def getValueZ_l(self):
        return self.b.read_byte_data(0x19,0x2c)#read the low output
    def getValueZ_h(self):
        return self.b.read_byte_data(0x19,0x2D)#read the High output
    def getTempl(self):
	return self.b.read_byte_data(0x19,0x0C)#read the low output
    def getTemph(self):
	return self.b.read_byte_data(0x19,0x0D)#read the High output
