import pickle


#Merch Collection Class
class MerchCollection:
    def __init__(self):
        self.merch_items = []

    #Generic Item Functions
    def add_item_menu(self):
        """Display available operations to the user"""
        print("Enter 'sh' to add a shirt "
              "\n'h' to add a hat "
              "\n'st' to add a sticker "
              "\n'cd' to add a CD "
              "\n'v' to add a vinyl "
              "\n'm' to add a miscellaneous item")

    def add_item(self):
        """Create a new merch item and add it to the list of items in the collection."""
        self.add_item_menu()
        item_type = self._request_item_type("add")
        if item_type == "sh":
            self.add_shirt()
        elif item_type == 'h':
            self.add_hat()
        elif item_type == 'st':
            self.add_sticker()
        elif item_type == 'cd':
            self.add_cd()
        elif item_type == 'v':
            self.add_vinyl()
        else:
            name = self._request_item_name("add")
            price = self._request_item_price("add")
            quantity = self._request_num_of_items("add")
            new_item = str(name)
            new_item = Item(name, price, quantity)
            self.merch_items.append(new_item)
            print(f"{name} has been added to the merch collection")

    def remove_item(self):
        """Remove an item from the merch collection."""
        merch_item = self._request_item_name("remove")
        item = self._get_item(merch_item)
        self.merch_items.remove(item)
        
    def decrease_inventory(self):
        """Sell a given amount of an item."""
        merch_item = self._request_item_name("decrease")
        item = self._get_item(merch_item)
        if item.item_type == "shirt":
            self.decrease_shirt_inventory(item)
        else:
            num_sold = self._request_num_of_items("decrease")
            item.quantity -= num_sold

    def increase_inventory(self):
        """Increase the quantity of an item on hand by a given amount."""
        merch_item = self._request_item_name("increase")
        item = self._get_item(merch_item)
        if item.item_type == "shirt":
            self.increase_shirt_inventory(item)
        else:
            num_new_items = self._request_num_of_items("increase")
            item.quantity += num_new_items

    def show_items(self):
        """Show the name and quantity of all items on hand in the collection."""
        print("The items currently on hand are: ")
        for item in self.merch_items:
            item.display_details()
    
    def _get_item(self, item_name):
        """Takes a merch item name and returns the corresponding object form the list"""
        for item in self.merch_items:
            if item.name.lower() == item_name.lower():
                return item
            
    #User Input Functions
    def _request_item_name(self, function):
        """Get user input on the name of the item they want to deal with."""
        if function == "remove":
            merch_item = str(input("What item should be removed from the collection? "))
        elif function == "increase":
            merch_item = str(input("What item's quantity on hand has increased? "))
        elif function == "decrease":
            merch_item = str(input("What item is being sold? "))
        elif function == "add":
            merch_item = str(input("What is the name of the merch item you want to add? "))
        return merch_item
    
    def _request_num_of_items(self, function):
        """Get user input on how many items the user wants to deal with."""
        if function == "increase":
            num_of_items = int(input("How many are being added? "))
        elif function == "decrease":
            num_of_items = int(input("How many are being sold? "))
        elif function == "add":
            num_of_items = int(input("How many are currently in stock? "))
        return num_of_items
    
    def _request_item_type(self, function):
        """Get user input on what type of item they want to deal with."""
        if function == "add":
            item_type = str(input("What type of item do you want to add? "))
        return item_type

    def _request_item_price(self, function):
        """Get user input on what the price is of the item they want to deal with."""
        if function == "add":
            item_price = float(input("How much does this cost? "))
        return item_price


    #Shirt Specific Functions
    def add_shirt(self):
        """
        Create a new shirt item and add it to the list of items in the collection.
        Use a dictionary for the quantity of specific sizes
        """

        name = self._request_shirt_name("add")
        price = self._request_item_price("add")
        quantity_dict = self._request_shirt_sizes("add")
        new_shirt = str(name)
        new_shirt = Shirt(name, price, quantity_dict)
        self.merch_items.append(new_shirt)
        print(f"{name} has been added to the merch collection")

    def decrease_shirt_inventory(self, shirt):
        """Decrease the inventory of one size of a shirt in the collection."""
        size_sold = self._request_shirt_sizes("decrease")
        num_sold = self._request_num_of_items("decrease")
        if size_sold in shirt.quantity.keys():
            shirt.quantity[size_sold] -= num_sold
        else:
            print("Couldn't find that size.  Please select another.")

    def increase_shirt_inventory(self, shirt):
        size_added = self._request_shirt_sizes("increase")
        num_added = self._request_num_of_items("increase")
        if size_added in shirt.quantity.keys():
            shirt.quantity[size_added] += num_added
        else:
            print("Couldn't find that size.  Please select another.")

    #Shirt Specific User Input Functions
    def _request_shirt_name(self, function):
        """Get user input on the name of the item they want to deal with."""
        if function == "add":
            merch_item = str(input("What is the name of the shirt you want to add? "))
        return merch_item
    
    def _request_shirt_sizes(self, function):
        """Get user input on what sizes of shirt they want to deal with"""
        if function == "add":
            sizes = str(input("Please enter the sizes available separated by commas (ex. 'sm, md, lg'): "))
            sizes = sizes.split(", ")
            quantity_by_size = []
            for size in sizes:
                quantity = int(input(f"How many shirts do you have in size {size}? "))
                quantity_by_size.append(quantity)
            quantity_dict = {sizes[i]: quantity_by_size[i] for i in range(len(sizes))}
            return quantity_dict
        elif function == "decrease":
            size_sold = str(input("What size shirt is being sold? "))
            return size_sold
        elif function == "increase":
            size_added = str(input("What size shirt is being added? "))
            return size_added


    
    #Functions to add other item classes
    def add_hat(self):
        name = self._request_item_name("add")
        price = self._request_item_price("add")
        quantity = self._request_num_of_items("add")
        new_item = str(name)
        new_item = Hat(name, price, quantity)
        self.merch_items.append(new_item)
        print(f"{name} has been added to the merch collection")

    def add_sticker(self):
        name = self._request_item_name("add")
        price = self._request_item_price("add")
        quantity = self._request_num_of_items("add")
        new_item = str(name)
        new_item = Sticker(name, price, quantity)
        self.merch_items.append(new_item)
        print(f"{name} has been added to the merch collection")

    def add_cd(self):
        name = self._request_item_name("add")
        price = self._request_item_price("add")
        quantity = self._request_num_of_items("add")
        new_item = str(name)
        new_item = CD(name, price, quantity)
        self.merch_items.append(new_item)
        print(f"{name} has been added to the merch collection")

    def add_vinyl(self):
        name = self._request_item_name("add")
        price = self._request_item_price("add")
        quantity = self._request_num_of_items("add")
        new_item = str(name)
        new_item = Vinyl(name, price, quantity)
        self.merch_items.append(new_item)
        print(f"{name} has been added to the merch collection")


    #File Handling
    def open_file(self):
        open_file_choice = input("Would you like to open a merch collection "
                                 "you've previously saved? (y/n) ")
        open_file_choice = open_file_choice.lower()
        if open_file_choice == 'y':
            fileroot = input("What merch collection would you like to load? ")
            fileroot = fileroot.replace(" ", "")
            fileroot = fileroot.lower()
            filename = f"{fileroot}.pkl"
    
            try:
                with open(filename, "rb") as f:
                    while True:
                        try:
                            self.merch_items.append(pickle.load(f))
                        except EOFError:
                            break
            except FileNotFoundError:
                    print(f"Sorry, the file {filename} does not exist."
                          f"\n Quit and try again or begin a new collection.")



    def save_file(self):
        save_file_choice = input("Would you like to save this merch collection? (y/n) ")
        save_file_choice = save_file_choice.lower()
        if save_file_choice == 'y':
            fileroot = input("What would you like to name this merch collection? ")
            fileroot = fileroot.replace(" ", "")
            fileroot = fileroot.lower()
            filename = f"{fileroot}.pkl"
    
            with open(filename, 'wb') as file_object:
                for item in self.merch_items:
                    pickle.dump(item, file_object)
                    print(f"Object successfully saved to '{filename}'")


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

        self.open_file()

        while True:

            #Show the user menu options and prompt for their response.
            self.menu()
            choice = input("What would you like to do? ")
    
            if choice == 'q':
                print("Quitting.")
                self.save_file()
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
    
class Hat(Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.item_type = "hat"

class Sticker(Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.item_type = "sticker"

class CD(Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.item_type = "cd"

class Vinyl(Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.item_type = "vinyl"