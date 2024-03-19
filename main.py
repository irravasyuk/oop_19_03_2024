class Watch:
    def __init__(self, model="", manufacturer="", year=0, price=0.0, watch_type=""):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.watch_type = watch_type

    def display(self):
        print("Модель:", self.model)
        print("Виробник:", self.manufacturer)
        print("Рік випуску:", self.year)
        print("Ціна:", self.price)
        print("Тип:", self.watch_type)

    def input_data(self):
        self.model = input("Введіть модель:")
        self.manufacturer = input("Введіть виробника:")
        self.year = int(input("Введіть рік випуску:"))
        self.price = float(input("Введіть ціну:"))
        self.watch_type = input("Введіть тип годинника:")

    def __str__(self):
        return f"Годинник: {self.model}, Виробник: {self.manufacturer}, Рік випуску: {self.year}, Ціна: {self.price}, Тип: {self.watch_type}"
    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __ne__(self, other):
        return self.price != other.price

watch1 = Watch()
watch1.input_data()

watch2 = Watch()
watch2.input_data()

print("\nІнформація про перший годинник:")
watch2.display()

print("\nІнформація про другий годинник:")
watch2.display()

if watch1 >= watch2:
    print("\nПерший годинник дорожчий за другий")
else:
    print("\nДругий годинник дорожчий за перший")

if watch1 == watch2:
    print("\nЦіна годинників однакова")
else:
    print("\nЦіна годинників різна")