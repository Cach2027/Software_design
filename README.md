class Vehicle: 
  """This class represents the structure of vehicle"""
  def __init__(self,chasis: str,model: str,consumption: float,year:str):
    self.chasis=chasis
    self.model=model
    self.consumption=consumption
    self.year=year
class Engine:
   def __init__(self, name:str, type_egine: str,potency: float,weight:float):
    self.name=name
    self.type_engine=type_egine
    self.potency=potency
    self.weight=weight
  
  def consumo_de_gasolina(type_engine,potency,weight):
    if (type_engine == "A"):
      consumo_de_gasolina= 

""" This is a class to represents a type of vehicle """
class Truck(Vehicle):
  def __init__(self,chasis,model,consumption,year):
    super().__init__(chasis,model,consumption,year)
    "" This is a class to represents a type of vehicle """
class Motorcycle(Vehicle):
  def __init__(self,chasis:str,model:,consumption,year):
    super().__init__(chasis,model,consumption,year)
    """ This is a class to represents a type of vehicle """
class Car(Vehicle):
  def __init__(self,chasis,model,consumption,year):
    super().__init__(chasis,model,consumption,year)
    """ This is a class to represents a type of vehicle """
class Yacht(Vehicle):
  def __init__(self,chasis,model,consumption,year):
    super().__init__(chasis,model,consumption,year)
