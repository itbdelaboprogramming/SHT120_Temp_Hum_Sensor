# SHT-20 Temperature and Humidity Sensor

Reading temperature and humidity using the SHT-120 via RS-485 communication standard with USB adaptor from XY-Mod02. This repo is made for modbus communication training.

## Tools
* XY-Mod02
* USB-Modbus adaptor
* Screwdriver
* SBC/PC

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install serial and time.

```bash
pip install serial
pip install time
```

## Usage

The master (SBC/PC) will send a set of hex data, which is an instruction for the slave (XY-Mod02). Below is an example of the code. __This is the essence of modbus communicaiton__

```python
temp_ref_frame = [0x01, 0x04, 0x00, 0x01, 0x00, 0x01, 0x60, 0x0a] # Request frame for humidity sensor
humid_ref_frame = [0x01, 0x04, 0x00, 0x02, 0x00, 0x01, 0x90, 0x0a] # Request frame for humidity sensor

def get_temp():

  ser.write(bytes(temp_ref_frame))


  buf = ser.read(7)

  temp_value = (buf[3] << 8) | buf[4]

  temperature = temp_value / 10.0

  return temperature
```

``` get_temp ``` will run periodically with the ``` time ``` library.

## Refrence

Please read the XY-Mod02 document  [SAH XY-MD02 manual](https://sah.rs/media/sah/techdocs/xy-md02-manual.pdf)
