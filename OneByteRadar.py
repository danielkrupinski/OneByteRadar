import pymem
import re

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle,
                                        "client_panorama.dll")

clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
address = client.lpBaseOfDll + re.search(rb'\x80\xB9.{5}\x74\x12\x8B\x41\x08',
                                         clientModule).start() + 6

pm.write_char(address, chr(0 if ord(pm.read_char(address)) != 0 else 2))
pm.close_process()
