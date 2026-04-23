class Product:
    def __init__(self, product_name, product_price, product_stock):
        self.__item_name = product_name
        self.__item_price = product_price
        self.__item_stock = product_stock

    def get_product_info(self):
        print("Product:", self.__item_name)
        print("Price:", self.__item_price)
        print("Quantity:", self.__item_stock)

    def update_quantity(self, new_stock):
        if new_stock >= 0:
            self.__item_stock = new_stock
        else:
            print("Invalid quantity")

    def update_price(self, new_price):
        if new_price > 0:
            self.__item_price = new_price
        else:
            print("Invalid price")


# Create product object
item1 = Product("pc", 5000, 5)

# Display product info
item1.get_product_info()