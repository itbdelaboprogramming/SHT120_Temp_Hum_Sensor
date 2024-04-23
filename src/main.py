from xymd02 import XYMD02
from minimalmodbus import ModbusException
from bootstrap import *
from time import sleep
import argparse


parser = argparse.ArgumentParser(description='XYMD02 Modbus RTU Temperature and Humidity Sensor')
parser.add_argument('--debug', action='store_true', help='Enable debug mode')
parser.add_argument('--polling_time', type=int, default=1, help='Polling time in seconds (default: 1)')
args = parser.parse_args()


def run():
    instrument = XYMD02(PORT_NAME, DEVICE_ADDR, args.debug)
    while True:
        try: 
            print("==============================")
            print("Current temperature: ", instrument.read_temperature())
            print("Current humidity: ", instrument.read_humidity())
        except ModbusException as e:
            print("Modbus error: ", e)
        except Exception as e:
            print("Error: ", e)
        finally: 
            sleep(args.polling_time)
        
if __name__ == "__main__":
    run()

