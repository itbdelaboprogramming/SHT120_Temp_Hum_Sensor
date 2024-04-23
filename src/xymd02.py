import minimalmodbus

READ_HOLDING_REGISTER_FUN_CODE = 0x03
READ_INPUT_REGISTER_FUN_CODE = 0x04
WRITE_SINGLE_REGISTER_FUN_CODE = 0x06
WRITE_MULTIPLE_REGISTERS_FUN_CODE = 0x10

TEMPERATURE_REGISTER_ADDR = 0x01
HUMIDITY_REGISTER_ADDR = 0x02

TEMPERATURE_NUMBER_OF_DECIMALS = 1
HUMIDITY_NUMBER_OF_DECIMALS = 1


class XYMD02(minimalmodbus.Instrument):
    def __init__(self, 
            port_name, 
            device_addr, 
            device_debug, 
            baud_rate=9600,
            byte_size=8,
            stop_bits=1,
            timeout=0.2):
        minimalmodbus.Instrument.__init__(self, port_name, device_addr, debug=device_debug)
        self.serial.parity   = minimalmodbus.serial.PARITY_NONE
        self.mode = minimalmodbus.MODE_RTU
        self.serial.baudrate = baud_rate
        self.serial.byte_size = byte_size
        self.serial.stop_bits = stop_bits
        self.serial.timeout = timeout
    
    def read_temperature(self):
        return self.read_register(TEMPERATURE_REGISTER_ADDR, TEMPERATURE_NUMBER_OF_DECIMALS, READ_INPUT_REGISTER_FUN_CODE)

    def read_humidity(self):
        return self.read_register(HUMIDITY_REGISTER_ADDR, HUMIDITY_NUMBER_OF_DECIMALS, READ_INPUT_REGISTER_FUN_CODE)
