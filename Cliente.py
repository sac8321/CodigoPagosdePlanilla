from Persona import Persona

class Cliente(Persona):
        def __init__(self,nombre,apellido,cedula,telefono,categoria):            
            self.nombre=nombre
            self.apellido=apellido
            self.cedula=cedula
            self.telefono=telefono
            self.categoria=categoria