item_name = input("Enter product name: ")
item_price = input("Enter price: ")

with open("inventory.txt", "a") as file_writer:
    file_writer.write(item_name + "," + item_price + "\n")

print("Item stored successfully")