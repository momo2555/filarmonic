from enum import Enum
import json
import logging
from typing import Any

from models.address import Address


class RequestType(Enum):
    EMPTY = "empty"
    REQUEST = "request"
    DATA_EXCHANGE = "data_exchange"
    DEVICE_EVENT = "device_event"
    DEVICE_DATA = "device_data"
    IDENTIFICATION = "identification"


class RequestHeader:
    type: RequestType = RequestType.EMPTY
    _from: str
    to: str
    from_addr: Address
    to_addr: Address


class DirectRequest:
    exec: str
    params : dict = {}


class Request:
    def __init__(self):
        self.__header : RequestHeader = RequestHeader()
        self.__request : DirectRequest = DirectRequest()
        self.__data : dict = {}
        self.__event : str = ""
        self.__log = logging.getLogger("Filarmonic")
    
    def get_header_el(self, key) -> Any:
        match key:
            case "from":
                return self.__header._from
            case "to":
                return self.__header.to
            case "from_addr":
                return self.__header.from_addr
            case "to_addr":
                return self.__header.to_addr
            case "type":
                return self.__header.type

    def set_type(self, type: RequestType):
        self.__header.type = type

    def set_request_action(self, name : str):
        self.__request.exec = name

    def create_param(self, param, value):
        self.__request.params[param] = value

    def add_data(self, key, value):
        self.__data[key] = value

    def from_json(self, raw_json : str):
        try:
            json_obj : dict = json.loads(raw_json)
        except Exception as e:
            self.__log.error("Invalid socket frame : JSON parse failed")
            self.__log.error(f"Request tried to parse : {raw_json}")
            return
        
        keys = json_obj.keys()
        if("data" in keys):
            self.__data = json_obj["data"]
        if("request" in keys):
            request : dict = json_obj["request"]
            rkeys = request.keys()
            if("exec" in rkeys):
                self.__request.exec = request["exec"]
            if("params" in rkeys):
                self.__request.params = request["params"]
        if("event" in keys):
            self.__event = json_obj["event"]
        if("header" in keys):
            header : dict = json_obj["header"]
            hkeys = header.keys()
            if("type" in hkeys):
                try:
                    self.__header.type = RequestType._value2member_map_[header["type"]]
                except:
                    self.__log.error(f"Cannot convert header type '{header['type']}', it's not a valid request type.")
            if("from" in hkeys):
                self.__header._from = header["from"]
            if("to" in hkeys):
                self.__header.to = header["to"]
            if("from_addr" in hkeys):
                self.__header.from_addr = Address(header["from_addr"])
            if("to_addr" in hkeys):
                self.__header.to_addr = Address(header["to_addr"])

    def to_object(self):
        obj = {
            "header" : {
                "type" : self.__header.type.value,
                "from" : self.__header._from,
                "to" : self.__header.to,
                "to_addr" : self.__header.to_addr,
                "from_addr" : self.__header.from_addr,
            }
        }
        if (self.__header.type == RequestType.DATA_EXCHANGE \
            or self.__header.type == RequestType.DEVICE_DATA \
            or self.__header.type == RequestType.IDENTIFICATION):
            obj["data"] = self.__data
        elif (self.__header.type == RequestType.DEVICE_EVENT):
            obj["event"] = self.__event
        elif (self.__header.type == RequestType.REQUEST):
            obj["params"] = self.__params
        return obj