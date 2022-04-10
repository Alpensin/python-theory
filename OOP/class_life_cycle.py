from time import sleep
from typing import Any


class HumanLife:
    def __new__(cls, *args, **kwargs):
        print("I'm Newborn")
        print(args)
        print(kwargs)
        instance = super().__new__(cls)
        return instance

    def __init__(self, *args, **kwargs) -> None:
        print("I opened my eyes!!")
        print(args)
        print(kwargs)

    def __del__(self):
        print("I'm dead. Goodbye world!")



    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("Why you called me?")
        print(args)


a = HumanLife("my arg", kw="my kw")
sleep(1)
a()
print("1 sec passed")
a = 1
sleep(1)
print("finish")
