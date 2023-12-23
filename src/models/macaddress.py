class MacAddress:
    def __init__(self, address : str):
        self.__address = address
    
    def to_string(self):
        return self.__address
