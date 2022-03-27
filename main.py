from logging.config import dictConfig
from Empleado import Empleado
from Cliente import Cliente

emp = Empleado('Juan','Moy','342','+506985658','$5000')
cli = Cliente('Juan','Moy','342','+506985658','vip')

def cargar():
    respuesta = input('Desea agregar un empleado')
    nombre = input('Ingrese su nombre')
    apellido = input('Ingrese su apellido')
    cedula = input('Ingrese su cedula')
    telefono = input('Ingrese su telefono')
    

    if (respuesta =='si'):
        salario = input ('Ingrese el salario')
        emp = Empleado(nombre,apellido,cedula,telefono,int(salario))
        personas.append(emp)
    else:
        tipo= input("Ingrese tipo de cliente")
        cli = Cliente(nombre,apellido,cedula,telefono,tipo)
        personas.append(cli)

personas= []
cargar()
cargar()
for persona in personas:
    print(persona)

