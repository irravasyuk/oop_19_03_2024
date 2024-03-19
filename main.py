class City:
    def __init__(self, name="", region="", country="", population=0, postal_code="", phone_code=""):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def input_data(self):
        self.name = input("\nВведіть назву міста: ")
        self.region = input("Введіть назву регіону: ")
        self.country = input("Введіть назву країни: ")
        self.population = int(input("Введіть кількість жителів у місті: "))
        self.postal_code = input("Введіть поштовий індекс міста: ")
        self.phone_code = input("Введіть телефонний код міста: ")

    def display(self):
        print("Назва міста: ", self.name)
        print("Назва регіону: ", self.region)
        print("Назва країни: ", self.country)
        print("Кількість жителів міста: ", self.population)
        print("Поштовий індекс міста: ", self.postal_code)
        print("Телефонний код міста: ", self.phone_code)

    def __str__(self):
        return f"Місто {self.name}, Країна: {self.country}, Населення: {self.population}, Поштовий індекс: {self.postal_code}, Телефонний код: {self.phone_code}"

    def __eq__(self, other):
        return self.population == other.population

    def __lt__(self, other):
        return self.population < other.population

    def __le__(self, other):
        return self.population <= other.population

    def __gt__(self, other):
        return self.population > other.population

    def __ge__(self, other):
        return self.population >= other.population

    def __ne__(self, other):
        return self.population != other.population

    def __eq__(self, other):
        return self.country == other.country

city1 = City()
city1.input_data()

city2 = City()
city2.input_data()

print("\nІнформація про перше місто:")
city1.display()

print("\nІнформація про друге місто:")
city2.display()

if city1 >= city2:
    print("\nПерше місто має більше населення, ніж друге")
else:
    print("\nДруге місто має більше населення, ніж перше")

if city1 == city2:
    print("\nМіста знаходяться в одній країні")
else:
    print("\nМіста розташовані в різних країнах")