class Items:
    """docstring for Items"""
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description

    def pick_up(self):
        print(f'\nYou pick up: {self.item_name}.')

    def drop_down(self):
        print(f'\nYou drop: {self.item_name}.')

    def __str__(self):
        return f'\n{self.item_name} - {self.item_description}'

    def __repr__(self):
        return f'\n{self.item_name} - {self.item_description}'
