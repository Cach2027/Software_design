"""
This File controls the logic by which the app will register users.

Author: Carlos Celis - cacelish@udistrital.edu.co
"""
from abc import ABC, abstractmethod

class Register(ABC):
    """This class is the interface of the register of user"""
    @abstractmethod
    def register_user():
        pass
class Realregister(Register):
    """This class is the principal service of register"""
    def __init__(self, user:str, password:str):
        self.user=user
        self.password=password
    def register_user( password, user):
        with open("user.txt", "r") as file:
            for line in file:
                if user in line and password in line:
                    return True
        print(f"The user or password '{user}' / '{password}'  that you are using is already in use")
        return False
        
class ProxiRegister(Register):
    """This class is to proxy tha that accesses the actual data if it is not in data"""
    def __init__(self, user:str, password:str):
        self.user=user
        self.password=password

    def logging(self):
        with open("user.txt", "a") as file:
            file.write(self.password,self.user)
    def register_user(self):
        self.logging()
        realuser=Realregister(self.password,self.user)
        
