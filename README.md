# SHT120_Temp_Hum_Sensor
SHT20 Temperature Humidity Transmitter with RS-485 Modbus RTU embedded protocol communication



## Getting Started
### Prerequisites 
The program is running in python and use pip as the package management. Make sure both are installed in your device(s).
To install the dependencies of the program, run the code below. 
```
pip install minimalmodbus python-dotenv
```

### Installation 
If the device has git installed, run the code below to copy the project from github.  
```
git clone https://github.com/itbdelaboprogramming/SHT120_Temp_Hum_Sensor.git
```
If it does not, do anything you prefer to upload this repo to the device like FTP, VNC, etc.

### Usage
First, setup the program environtment variables in `.env`, as specified in `.env.example`. The included `.env.example` should works just fine in most cases. Just rename it to `.env` in your device.

To run the program, run the main.py located in /src. For example, if you are in the project root file, run the command below in the terminal.   
```diff
python ./src/main.py
```

The main program also support inline argument below
```diff
--debug : to run the instrument as minimalmodbus debug mode
--polling_time [polling_time_in_second]: to run
```
Example usage of inline argument to run program in debug mode and poll every 5 seconds.
```diff
python ./src/main.py --debug --polling_time 5
```


### References

This program was developed with reference to the [SAH XY-MD02 manual](https://pages.github.com/) and [minimalmodbus documentation](https://minimalmodbus.readthedocs.io/en/stable/readme.html).