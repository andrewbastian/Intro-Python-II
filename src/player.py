# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location, inventory=[]):
        self.location = location
        self.inventory = inventory

    def take_item(self, this_item):
        try:
            for item in self.location.room_items:
                if this_item == item.item_name:

                    self.inventory.append(item)
                    self.location.room_items.remove(item)
                    item.pick_up()

        except:
            print(f'the {this_item} is not in this room')

    def drop_item(self, this_item):
        print('DROP CALLED')
        try:
            for item in self.inventory:
                if this_item == item.item_name:
                    self.inventory.remove(item)
                    self.location.room_items.append(item)
                    item.drop_down()

        except:
            print(f'the {this_item} is not in inventory')
