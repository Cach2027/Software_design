"""
this module has a class to control the sending of newsletters. 

Author: Carlos Andres Celis Herrera <cacelish@udistrital.edu.co>
"""
class Publisher:
    """ This class is a class to add and notify subscribers """
    def __init__(self):
        self.__subscribers=[]

    def add_subscriber( self):
        """this method verifies the existence of an email and then adds it or not"""
        email=input("Si desea revisar un boletin actualizado de vehiculos ingresa tu email")
        if email in self.__subscribers:
            print(f"El correo electrónico {email} ya está en la lista de suscriptores.")
        else:
            self.__subscribers.append(email)
            print(f"Se añadió correctamente el correo electrónico {email} a la lista de suscriptores.")


