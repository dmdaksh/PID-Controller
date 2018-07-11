from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
import time
import sys

class FloatModbusClient(ModbusClient):
    def read_float(self, address, number=1):
        reg_l = self.read_holding_registers(address, number * 2)
        if reg_l:
            return [utils.decode_ieee(f) for f in utils.word_list_to_long(reg_l)]
        else:
            return None
    def write_float(self, address, floats_list):
        b32_l = [utils.encode_ieee(f) for f in floats_list]
        b16_l = utils.long_list_to_word(b32_l)
        return self.write_multiple_registers(address, b16_l)
"""
host = "192.168.111.222"
port = 502

try:
    c = FloatModbusClient(host, port, unit_id=1, auto_open=True)
except ValueError:
    print("Error with host and port parameters.")

c.debug(True)

while True:
    if not c.is_open:
        if not c.open:
            print('Unable to connect %s at port %s' %(host,str(port)))
    
    if c.is_open:
        num = int(input("Enter '1' to read PV or '2' to write target SP or '3' to exit : "))
        print("\n")
        print(c.read_input_registers(45056,1))
        if(num == 1 or num == 2 or num == 3):
            
            if(num == 1):
                temp1 = c.read_float(33280,1)
                temp2 = c.read_float(33288,1)
                temp3 = c.read_float(33296,1)
                temp4 = c.read_float(33304,1)
                
                if temp1 and temp2 and temp3 and temp4:
                    print("Temperature : %s"%(''.join(str(i) for i in temp1)))
                    print("Temperature : %s"%(''.join(str(i) for i in temp2)))
                    print("Temperature : %s"%(''.join(str(i) for i in temp3)))
                    print("Temperature : %s"%(''.join(str(i) for i in temp4)))
                    print("\n")
            
            if(num == 2):
                sp_value = float(input("Enter the target SP value : "))
                temp = c.write_float(33796,[sp_value])
                print("\n")
            
            if(num == 3):
                c.close()
                sys.exit()
        
            time.sleep(1)
    
        else:
            print("Enter '1' or '2' only for query and '3' to exit the program\n")
            """