import snap7
import time
from snap7.util import*
from snap7.types import*
IP = '192.168.0.1'
RACK = 0
SLOT = 1

DB_NUMBER = 3
START_ADDRESS = 0
SIZE = 769

plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)

plc_info = plc.get_cpu_info()
print(f'Module Type: {plc_info.ModuleTypeName}')

state = plc.get_cpu_state()
print(f'State:{state}')

# db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
# print (db)
# product_name1 = db[2:256].decode('UTF-8').strip('\x00')
# print(f'PRODUCT NAME: {product_name1}')
# product_name2 = db[258:512].decode('UTF-8').strip('\x00')
# print(f'PRODUCT NAME: {product_name2}')
# product_name3 = db[514:768].decode('UTF-8').strip('\x00')
# print(f'PRODUCT NAME: {product_name3}')
# product_value = int.from_bytes(db[256:258], byteorder='big')
# print(f'PRODUCT VALUE: {product_value}')

# product_status = bool(db[768])
# print(product_status)

time.sleep(1)