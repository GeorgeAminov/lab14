from tkinter import *

root = Tk()

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

    def add_flavor(self, new_flavor):
        if new_flavor not in self.flavors:
            self.flavors.append(new_flavor)
            return(f'Вкус "{new_flavor}" успешно добавлен в меню.')
        else:
            return(f'Вкус "{new_flavor}" и так уже в меню.')

    def delete_flavor(self, bad_flavor):
        if bad_flavor in self.flavors:
            self.flavors.remove(bad_flavor)
            return(f'Вкус "{bad_flavor}" успешно удалён из меню.')
        else:
            return(f'Вкуса "{bad_flavor}" и так нет в меню.')

kiosk = IceCreamStand("Киоск дяди Тома", "Мороженое", "4", ["ванильное", "шоколадное"], "Гостинный двор", "с 10:00 до 18:00")

def update_menu():
    menu_text = "\n".join(kiosk.flavors)
    label_menu["text"] = menu_text

def add_menu():
    if flavor_field.get() != "":
        status = kiosk.add_flavor(flavor_field.get())
        label_status["text"] = status
        update_menu()
    else:
        label_status["text"] = "Поле не может быть пустым."

def delete_menu():
    if flavor_field.get() != "":
        status = kiosk.delete_flavor(flavor_field.get())
        label_status["text"] = status
        update_menu()
    else:
        label_status["text"] = "Поле не может быть пустым."

root['bg'] = "#F5F5F5"
root.title("Киоск дяди Тома")
root.geometry("400x500")
root.resizable(width=False, height=False)

label_info = Label(root, text=f"{kiosk.restaurant_name}\n{kiosk.working_time}", bg="#F5F5F5",  font=("Calibri", 20, "bold"))
label_info.pack()

label_flavors = Label(root, text="Доступные вкусы мороженого:", bg="#F5F5F5",  font=("Calibri", 16, "bold"))
label_flavors.pack()

label_menu = Label(root, text="", font=("Calibri", 14), bg="#F5F5F5")
label_menu.pack()

update_menu()

flavor_field = Entry(root, bg="#FFFAFA", font=("Calibri", 14))
flavor_field.pack()

add_btn = Button(root, bg="#7FFFD4",text="добавить вкус", command=add_menu)
add_btn.pack()

del_btn = Button(root, bg="#DB7093", text="удалить вкус", command=delete_menu)
del_btn.pack()

label_status = Label(root, text="️⬆️\n    введите название вкуса", bg="#F5F5F5",  font=("Calibri", 12))
label_status.place(relx=0.24, rely=0.8)

root.mainloop()