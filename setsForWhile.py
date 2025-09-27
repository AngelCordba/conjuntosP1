
print("Ejemplo de conjuntos")
print()

nombre = "Julian"

carro = {"Cereal", "Manzana", "Set de cucharas"}
lista = {"Leche", "Sopa Maruchan", "Refresco RED COLA"}

lista.update(carro)

print(nombre, " esta de compras en el supermercado.")
print("en su carrito de compras, el ya tiene los siguentes productos: ")
print(carro)
print(nombre, " tiene una lista de compras, la cual es la siguiente:")
print(lista)

while len(lista) > 0: # No continuar hasta que longitud de lista sea 0
    for objeto in lista: # Comprar primero lo de la lista
        if objeto in carro:
            print()
            print(nombre, " encontro ", objeto, ", pero ya esta en su carro así que lo ignora.")
        else:
            print()
            print(nombre, " encontro ", objeto, " y lo añadio a su carro")
            carro.add(objeto)
            print("El carro contiene los siguientes productos:")
            print(carro)
    print("Una véz finalizada la compra, ", nombre, " se le olvido tachar lo que ya consiguio")
    print("a continuacion, él tacha lo que ya tiene en la lista")
    for cosa in carro:
        print()
        print(nombre, " tacha ", cosa, ", la cual ya esta en su carro, borrandolo de la lista")
        #lista.remove(cosa)
        lista.discard(cosa)
        print("La lista contiene los siguientes productos:")
        print(lista)


print(nombre, " ha finalizado sus compras, pago debidamente y se fue a su casa felíz.")