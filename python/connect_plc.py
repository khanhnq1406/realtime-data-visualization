
from pymodbus.client.sync import ModbusTcpClient as mbclient

client = mbclient('192.168.0.1',port=502)
client.connect()
UNIT= 0x1
print ('Connect')

# print(client.write_register(0,2,unit=UNIT))
# print(client.write_coil(0,'3',unit=UNIT))

