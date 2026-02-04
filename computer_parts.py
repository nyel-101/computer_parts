class ComputerParts:
    def __init__(self, name, quantity, price):  # CONSTRUCTOR
        self.name = name                        # PUBLIC ATTRIBUTE
        self.quantity = quantity                # PUBLIC ATTRIBUTE
        self.__price = price                    # PRIVATE ATTRIBUTE ENCAPSULATION

    def get_total_value(self):                  # METHOD: calculates total value
        return self.quantity * self.__price

    def get_price(self):                        # GETTER METHOD: accesses private price
        return self.__price

    def set_price(self, new_price):             # SETTER METHOD: updates private price
        if new_price >= 0:
            self.__price = new_price
        else:
            print("Invalid price. Must be non-negative.")

    def display_details(self):                  # METHOD: displays part details
        print(f"Name: {self.name}, Quantity: {self.quantity}, Price: {self.__price:.2f}")

# OBJECT CREATION: instances of ComputerParts
inventory = [
    ComputerParts("RAM", 10, 1500),             # OBJECT: RAM
    ComputerParts("SSD", 5, 2500),              # OBJECT: SSD
    ComputerParts("GPU", 2, 15000)              # OBJECT: GPU
]

# MAIN LOOP AND MENU SYSTEM
while True:
    print("\nCOMPUTER PARTS INVENTORY SYSTEM")
    print("1. Add Product")
    print("2. View All Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Total Value of Selected Products")
    print("6. Exit")

    choice = input("Choose an option (1-6): ").strip()

    # NEW OBJECT
    if choice == "1":
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))

        if quantity < 0 or price < 0:
            print("Error: Quantity and price must be non-negative.")
        else:
            part = ComputerParts(name, quantity, price)  # OBJECT CREATION
            inventory.append(part)
            print(f"'{name}' added to inventory.")

    #  INVENTORY COMPUTER PARTS
    elif choice == "2":
        print("\nInventory List:")
        if not inventory:
            print("No products in inventory.")
        else:
            for i, part in enumerate(inventory, start=1):  # TRAVERSAL
                print(f"{i}. ", end="")
                part.display_details()                     # METHOD CALL

            # ENCAPSULATION TEST: accessing private price via getter
            print("\nEncapsulation Test:")
            for part in inventory:
                price = part.get_price()                   # GETTER CALL
                if price >= 0:
                    print(f"{part.name} price access: {price:.2f}")
                else:
                    print(f"{part.name} has invalid price.")

    # UPDATE OBJECT ATTRIBUTES
    elif choice == "3":
        update_name = input("Enter product name to update: ")
        found = False
        for part in inventory:
            if part.name.lower() == update_name.lower():
                new_quantity = int(input("Enter new quantity: "))
                new_price = float(input("Enter new price: "))

                if new_quantity < 0 or new_price < 0:
                    print("Error: Quantity and price must be non-negative.")
                else:
                    part.quantity = new_quantity           # DIRECT UPDATE PUBLIC
                    part.set_price(new_price)              # SETTER CALL PRIVATE
                    print(f"'{part.name}' updated.")
                found = True
                break
        if not found:
            print("Product not found.")

    # DELETE OBJECT FROM LIST
    elif choice == "4":
        delete_name = input("Enter product name to delete: ")
        for part in inventory:
            if part.name.lower() == delete_name.lower():
                inventory.remove(part)
                print(f"'{delete_name}' removed from inventory.")
                break
        else:
            print("Product not found.")

    # TOTAL SELECTED OBJECT VALUES
    elif choice == "5":
        print("\nTotal Value of Selected Products")
        total = 0
        selected = []
        for part in inventory:
            select = input(f"Include '{part.name}' in total? (Y/N): ").strip().upper()
            if select == "Y":
                selected.append(part)
                total += part.get_total_value()            # METHOD CALL
        if selected:
            print("\nSelected Products:")
            for part in selected:
                part.display_details()                     # METHOD CALL
            print(f"\nTotal Value: {total:.2f}")
        else:
            print("No products selected.")

    # EXIT PROGRAM
    elif choice == "6":
        print("Exiting")
        break

    else:
        print("Invalid choice. Please select from 1 to 6.")