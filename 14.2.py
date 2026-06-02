class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, restaurant_rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.restaurant_rating = restaurant_rating
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, restaurant_rating, flavors, location, working_time):
        super().__init__(restaurant_name, cuisine_type, restaurant_rating)
        self.flavors = flavors
        self.location = location
        self.working_time = working_time
        self.stick_ice_cream = []
        self.waffle_ice_cream = []

    def add_flavor(self, new_flavor):
        if new_flavor not in self.flavors:
            self.flavors.append(new_flavor)
        else:
            print(f'Вкус "{new_flavor}" и так уже в меню.')

    def delete_flavor(self, bad_flavor):
        if bad_flavor in self.flavors:
            self.flavors.remove(bad_flavor)
        else:
            print(f'Вкуса "{bad_flavor}" и так нет в меню.')

    def chek_flavor(self, search_flavor):
        if search_flavor in self.flavors:
            print(f'Вкус "{search_flavor}" есть в наличии.')
        else:
            print(f'Вкуса "{search_flavor}" нету в наличии.')

    def add_stick_ice_cream(self, new_stick_ice_cream):
        if new_stick_ice_cream not in self.stick_ice_cream:
            self.stick_ice_cream.append(new_stick_ice_cream)
        else:
            print("Это мороженое на палочке уже есть в меню.")

    def add_waffle_ice_cream(self, new_waffle_ice_cream):
        if new_waffle_ice_cream not in self.waffle_ice_cream:
            self.waffle_ice_cream.append(new_waffle_ice_cream)
        else:
            print("Этот вафельный стаканчик уже есть в меню.")

kiosk = IceCreamStand("Киоск дяди Тома", "Мороженое", "4", ["ванильное", "шоколадное"], "Гостинный двор", "с 10:00 до 18:00")

print(f'"{kiosk.restaurant_name}" располагается в локации: "{kiosk.location}"') #1
print(f'"{kiosk.restaurant_name}" работает: {kiosk.working_time}')

kiosk.add_flavor("фисташковое") #2
print(kiosk.flavors)
kiosk.delete_flavor("шоколадное")
print(kiosk.flavors)

kiosk.chek_flavor("шоколадное") #3
kiosk.chek_flavor("фисташковое")

kiosk.add_stick_ice_cream("фруктовый лёд") #4
print(f'Такие вкусы мороженого на палочке мы предлагаем: {kiosk.stick_ice_cream}.')
kiosk.add_waffle_ice_cream("пьяная вишня")
print(f'Такие вкусы мороженого в вафельном стаканчике мы предлагаем: {kiosk.waffle_ice_cream}.')