from dictable import Dictable


class ClassA:
    def __init__(self, str_value: str, dict_value: dict, int_value: int):
        self.str_field = str_value
        self.dict_field = dict_value
        self.int_field = int_value


class ClassB(Dictable):
    def __init__(self, bool_value:bool, str_value: str, dict_value: dict, int_value: int):
        self.bool_field = bool_value
        self.a = ClassA(str_value, dict_value, int_value)

class ClassC(Dictable):
    def __init__(self, float_value: float, bool_value:bool, str_value: str, dict_value: dict, int_value: int):
        self.float_value = bool_value
        self.b = ClassB(bool_value,  str_value, dict_value, int_value)


print(ClassA("str", {"key": "value"}, 1).__dict__)
#{'str_field': 'str', 'dict_field': {'key': 'value'}, 'int_field': 1}

print(ClassB(False, "str", {"key": "value"}, 1).__dict__)
#{'bool_field': False, 'a': <__main__.ClassA object at 0x01F22DB0>}

print(ClassC(1.1, False, "str", {"key": "value"}, 1).__dict__)
#{'float_value': False, 'b': <__main__.ClassB object at 0x01F22DD0>}

print(ClassB(False, "str", {"key": "value"}, 1).dict())
#{'a': {'dict_field': {'key': 'value'}, 'int_field': 1, 'str_field': 'str'}, 'bool_field': False}

print(ClassC(1.1, False, "str", {"key": "value"}, 1).dict())
#{'float_value': False, 'b': {'a': {'dict_field': {'key': 'value'}, 'int_field': 1, 'str_field': 'str'}, 'bool_field': False}}
