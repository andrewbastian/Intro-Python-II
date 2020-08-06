# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name_room, description_room):
        self.name_room = name_room
        self.description_room = description_room
        self.room_items = []
