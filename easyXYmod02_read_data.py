import serial

import time



temp_ref_frame = [0x01, 0x04, 0x00, 0x01, 0x00, 0x01, 0x60, 0x0a] # Request frame for humidity sensor

humid_ref_frame = [0x01, 0x04, 0x00, 0x02, 0x00, 0x01, 0x90, 0x0a] # Request frame for humidity sensor



ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600) # Remember, you might need to replace '/dev/ttyUSB0' with the port name where your USB to RS485 converter is connected



def get_temp():

  ser.write(bytes(temp_ref_frame))


  buf = ser.read(7)

  temp_value = (buf[3] << 8) | buf[4]

  temperature = temp_value / 10.0

  return temperature





def get_humidity():

  ser.write(bytes(humid_ref_frame))

  buf = ser.read(7)

  humid_value = (buf[3] << 8) | buf[4]

  humidity = humid_value / 10.0

  return humidity





while True:



  print("-----------------------------------------------")

  print("Temp: ", get_temp())
  print("Humidity: " , get_humidity())


  time.sleep(10)
