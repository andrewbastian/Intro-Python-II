# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location, inventory=[]):
        self.location = location
        self.inventory = inventory

    def keep_item(self, this_item):
        try:
            for item in self.location.items:
                if this_item == item.item_name:
                    self.inventory.append(item)
                    self.locaiton.items.remove(item)
                    item.keep_item()

        except:
            print(f'the {this_item} is not in this room')

    def drop_item(self, this_item):
        try:
            for item in self.location.items:
                if this_item == item.item_name:
                    self.inventory.remove(item)
                    self.locaiton.items.append(item)
                    item.drop_item()

        except:
            print(f'the {this_item} is not in inventory')
            