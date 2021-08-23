
class Producto:
    idPro = 1
    def __init__(self,name,precio,stock,imageDirection,tipo):
        self.name = name
        self.idProducto = Producto.idPro
        self.stock = stock
        self.precio = precio
        self.imageDirection  = imageDirection
        self.tipo = tipo
        Producto.idPro+=1

    def vender(self,cantidad):
        self.stock -= cantidad
        return cantidad * self.precio

    def abastecer(self,cantidad):
        id += cantidad

    def cambiarImagen(self,imageDirection):
        self.imageDirection = imageDirection

class Usuario:
    def __init__(self,name,cedula,direccion,correo ):
        self.name = name
        self.cedula = cedula
        self.direccion = direccion
        self.correo = correo


