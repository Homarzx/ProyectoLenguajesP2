import Objetos as obj
class Tienda:
    idTienda = 1
    def __init__(self,name,direccion,Vendedor):
        self.name = name
        self.direccion=direccion
        Tienda.idTienda+=1
        self.lista = []
        self.Vendedor=Vendedor

    def append(self, producto):

        self.lista.append(producto)

    def search(self, key, by="idproducto"):
        for index, producto in enumerate(self.lista):
            if producto.__getattribute__(by) == key:
                return index

    def remove(self, key, by="idproducto"):
        index = self.search(key)
        if index != None:
            self.lista.pop(index)
            return index

    def __str__(self):
        s = ""
        for producto in self.lista:
            s += str(producto) + '\n'
        return s




class Vendedor:
        def __init__(self,name,cedula,celular,correo ):
            self.name = name
            self.cedula = cedula
            self.celular = celular
            self.correo = correo



