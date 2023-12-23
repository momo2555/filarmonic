from enum import Enum


class AddressType(Enum):
    MAC_ADDRESS = "mac_address"
    IP_ADDRESS = "IP_ADDRESS"
class Address:
    def __init__(self, address : str, type : AddressType = AddressType.MAC_ADDRESS):
        self.__address = address
        self.__type = type
    
    def to_string(self):
        return self.__address
