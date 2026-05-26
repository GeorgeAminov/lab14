class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, restaurant_rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.restaurant_rating = restaurant_rating
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, restaurant_rating, flavors):
        super().__init__(restaurant_name, cuisine_type, restaurant_rating)
        self.flavors = flavors
    def flavour_spisok(self):
        print(f'В ресторане мороженного "{self.restaurant_name}" доступны такие вкусы:')
        for flavor in self.flavors:
            print(f"- {flavor}")
baskin_robbins = IceCreamStand("Баскин Роббинс", "Холодная", "5", ["клубничное", "фисташковое", "шоколадное"])
baskin_robbins.flavour_spisok()