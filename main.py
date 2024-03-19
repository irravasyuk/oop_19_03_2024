class Country:
    def __init__(self, name="", name_of_continent="", pupulation=0, phone_code="", capital="", city_name=[]):
        self.name = name
        self.name_of_continent = name_of_continent
        self.population = pupulation
        self.phone_code = phone_code
        self.capital = capital
        self.city_name = city_name

    def input_data(self):
        self.name = input("\nВведіть назву країни: ")
        self.name_of_continent = input("Введіть назву континенту: ")
        self.population = int(input("Введіть кількість жителів країни: "))
        self.phone_code = input("Введіть телефонний код країни: ")
        self.capital = input("Введіть столицю країни: ")
        cities = input("Введіть назви міст країни через кому: ")
        self.city_name = [city for city in cities.split(",")]

    def display(self):
        print("Назва країни: ", self.name)
        print("Назва континету: ", self.name_of_continent)
        print("Кількість жителів: ", self.population)
        print("Телефонний код країни: ", self.phone_code)
        print("Столиця країни: ", self.capital)
        print("Назви міст країни: ", ", ".join(self.city_name))

    def __str__(self):
        return f"Назва країни: {self.name}, Назва континенту: {self.name_of_continent}, Кількість жителів: {self.population},Телефонний код країни: {self.phone_code}, Столиця країни: {self.capital}, Міста країни: {', '.join(self.city_name)}"

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


country1 = Country()
country1.input_data()

country2 = Country()
country2.input_data()

print("\nІнформація про першу країну:")
country1.display()

print("\nІнформація про другу країну:")
country2.display()

if country1 >= country2:
    print("\nПерша країна має більше населення, ніж друга")
else:
    print("\nДруга країна має більше населення, ніж перша")

