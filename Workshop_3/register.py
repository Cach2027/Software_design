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
        self.user = user
        self.password = password

    def register_user(self):
        with open("user.txt", "r") as file:
            for line in file:
                if self.user in line and self.password in line:
                    print(f"The user or password '{self.user}' / '{self.password}' that you are using is already in use")
                    return False
        with open("user.txt", "a") as file:
            file.write(f"{self.user}:{self.password}\n")
        print(f"User '{self.user}' successfully registered.")
        return True
        
class ProxiRegister(Register):
    """This class is to proxy that accesses the actual data if it is not in data"""
    def __init__(self, user:str, password:str):
        self.user = user
        self.password = password
    def logging(self):
        with open("user.txt","a") as file:
            file.write(f"User accessed trend data for '{self.user}'")
    def register_user(self):
        self.logging()
        real_register = Realregister(self.user, self.password)
        return real_register.register_user()

# Example usage:
proxy_register = ProxiRegister("new_user", "new_password")
proxy_register.register_user()