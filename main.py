def agregar_producto(inventario):
    nombre = input("nombre del producto")
    precio =float(input("precio:"))
    cantidad = int(input("cantidad:"))

    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })

def lista_productos(inventario):
    for producto in inventario:
        print(producto)