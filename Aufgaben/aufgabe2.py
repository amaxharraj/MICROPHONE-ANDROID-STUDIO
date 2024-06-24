#Aufgabe 2

# Stellt euch vor Ihr arbeitet in einem Unternehmen, welches
# einfache Python-Anwendungen zur Verwaltung von Produkten entwickelt hat.

# a) Verbessert folgenden Code für die Verwaltung von Produkten

def Get_product_input():
    name = input("Enter product name (or 'stop' to finish): ")
    if name.lower() == 'stop':
        return None
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    return {'name': name, 'price': price, 'quantity': quantity}

def DisplayProduct(p):
    print("Product:" + p['name'] + ",price:" + str(p['price']) + ", Quantity:" + str(p['quantity']))

def main():
    products = []
    while True:
        product = Get_product_input()
        if product == None:
            break
        products.append(product)
    for p in products:
        DisplayProduct(p)

if __name__ == "__main__":
    main()
