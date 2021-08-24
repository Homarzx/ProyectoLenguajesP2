import Objetos as obj
import Tienda as tie
producto1 = obj.Producto("Manzana",3.4,100,"Link.tree/111","Verdura")
print(producto1.idProducto)
producto2 = obj.Producto("Verdura",3.4,100,"Link.tree/111","Fruta")
print(producto2.idProducto)

print("stock de manzanas actual: ",producto1.stock)
venta= producto1.vender(50)
print("Se ha vendido",50," por un total de",venta)
print("stock de manzanas actual: ",producto1.stock)

vendedor1=tie.Vendedor("Maria","0956777841","0982535859","alevbrunner@gmail.com")
tienda1=tie.Tienda("Rosita","Cdla los vergeles",vendedor1)
tienda1.append(producto1)
tienda1.append(producto2)

