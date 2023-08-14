#Merch Collection Class
class MerchCollection:
    def __init__(self):
        self.merch_items = []

    #Generic Item Functions
    def add_item(self):
        """Create a new merch item and add it to the list of items in the collection."""
        item_type = str(input("Is this item a shirt? (y/n) "))
        if item_type == "y":
            self.add_shirt()
        else:
            name = str(input("What is the name of the merch item you want to add? "))
            price = float(input("How much does this cost? "))
            quantity = int(input("How many are currently in stock? "))
            new_item = str(name)
            new_item = Item(name, price, quantity)
            self.merch_items.append(new_item)
            print(f"{name} has been added to the merch collection")

    def remove_item(self):
        """Remove an item from the merch collection."""
        merch_item = str(input("What item should be removed from the collection? "))
        item = self._get_item(merch_item)
        self.merch_items.remove(item)
        
    def decrease_inventory(self):
        """Sell a given amount of an item."""
        merch_item = str(input("What item is being sold? "))
        item = self._get_item(merch_item)
        if item.item_type == "shirt":
            self.decrease_shirt_inventory(item)
        else:
            num_sold = int(input("How many are being sold? "))
            item.quantity -= num_sold

    def increase_inventory(self):
        """Increase the quantity of an item on hand by a given amount."""
        merch_item = str(input("What item's quantity on hand has increased? "))
        item = self._get_item(merch_item)
        if item.item_type == "shirt":
            self.increase_shirt_inventory(item)
        else:
            num_new_items = int(input("How many are being added? "))
            item.quantity += num_new_items

    def show_items(self):
        """Show the name and quantity of all items on hand in the collection."""
        print("The items currently on hand are: ")
        for item in self.merch_items:
            item.display_details()
    
    def _get_item(self, item_name):
        """Takes a merch item name and returns the corresponding object form the list"""
        for item in self.merch_items:
            if item.name == item_name:
                return item


    #Shirt Specific Functions
    def add_shirt(self):
        """
        Create a new shirt item and add it to the list of items in the collection.
        Use a dictionary for the quantity of specific sizes
        """

        name = str(input("What is the name of the shirt you want to add? "))
        price = float(input("How much does this cost? "))
        sizes = str(input("Please enter the sizes available separated by commas (ex. 'sm, md, lg'): "))
        sizes = sizes.split(", ")
        quantity_by_size = []
        for size in sizes:
            quantity = int(input(f"How many shirts do you have in size {size}? "))
            quantity_by_size.append(quantity)
        quantity_dict = {sizes[i]: quantity_by_size[i] for i in range(len(sizes))}
        new_shirt = str(name)
        new_shirt = Shirt(name, price, quantity_dict)
        self.merch_items.append(new_shirt)
        print(f"{name} has been added to the merch collection")

    def decrease_shirt_inventory(self, shirt):
        """Decrease the inventory of one size of a shirt in the collection."""
        size_sold = str(input("What size shirt is being sold? "))
        num_sold = int(input("How many are being sold? "))
        if size_sold in shirt.quantity.keys():
            shirt.quantity[size_sold] -= num_sold
        else:
            print("Couldn't find that size.  Please select another.")

    def increase_shirt_inventory(self, shirt):
        size_added = str(input("What size shirt is being added? "))
        num_added = int(input("How many are being added? "))
        if size_added in shirt.quantity.keys():
            shirt.quantity[size_added] += num_added
        else:
            print("Couldn't find that size.  Please select another.")


    #Driver functions        
    def menu(self):
        """Display available operations to the user"""
        print("Enter 's' to show the contents of the merch collection "
              "\n'a' to add a new merch item "
              "\n'r' to remove a merch item "
              "\n'i' to increase the inventory of an item "
              "\n'd' to decrease the inventory of an item "
              "\n'q' to quit")
        
    def run_inventory(self):
        """
        Allow the user to to interact with the merch collection through input,
        viewing the items in the collection, adding items, removing items, 
        and increasing and reducing inventory of items.  Perform this continously
        until the user decides to stop.
        """

        while True:

            #Show the user menu options and prompt for their response.
            self.menu()
            choice = input("What would you like to do? ")
    
            if choice == 'q':
                print("Quitting.")
                break
            elif choice == 's':
                self.show_items()
            elif choice == 'a':
                self.add_item()
            elif choice == 'r':
                self.remove_item()
            elif choice == 'i':
                self.increase_inventory()
            elif choice == 'd':
                self.decrease_inventory()
        


#Parent Class for all items
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.item_type = "misc"

    def display_details(self):
        print(f"\n{self.name} \n\tPrice: {self.price} "
              f"\n\tAmount on hand: {self.quantity}")
        
    def __str__(self):
        """
        Display the name and quantity of the item 
        whenever the object is printed to the console.
        """
        return f"\t{self.name} - {self.quantity}"

#Parent classes for types of items
class Shirt(Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.item_type = "shirt"

    def display_details(self):
        print(f"\n{self.name} \n\tPrice: {self.price}")
        print("\tAmount on hand: ")
        for key, value in self.quantity.items():
            print(f"\t\t{key} - {value}")
        
    def __str__(self):
        """
        Display the name and quantity of the item 
        whenever the object is printed to the console.
        """
        return f"\t{self.name}: {self.quantity}"