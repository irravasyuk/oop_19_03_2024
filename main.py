class Human:
    def __init__(self, full_name="", date_of_birth="", phone_number="", city="", country="", home_address=""):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.city = city
        self.country = country
        self.home_address = home_address

    def input_data(self):
        self.full_name = input("Введіть піб: ")
        self.date_of_birth = input("Введіть дату народження: ")
        self.phone_number = input("Введіть контактний телефон: ")
        self.city = input("Введіть місто: ")
        self.country = input("Введіть країну: ")
        self.home_address = input("Введіть домашню адресу: ")

    def display(self):
        print("піб:", self.full_name)
        print("дата народження:", self.date_of_birth)
        print("контактний телефон:", self.phone_number)
        print("місто:", self.city)
        print("країна:", self.country)
        print("домашня адреса:", self.home_address)

    def __str__(self):
        return f"ПІБ: {self.full_name},Дата народження: {self.date_of_birth},Контактний телефон: {self.phone_number},Місто: {self.city},Країна: {self.country},Домашня адреса: {self.home_address} "

    def __eq__(self, other):
        return (self.full_name, self.date_of_birth, self.phone_number, self.city, self.country, self.home_address) == (other.full_name, other.date_of_birth, other.phone_number, other.city, other.country, other.home_address)

    def __lt__(self, other):
        return self.full_name.split()[0] < other.full_name.split()[0]

    def __gt__(self, other):
        return self.full_name.split()[0] > other.full_name.split()[0]

    def __le__(self, other):
        return self.full_name.split()[0] <= other.full_name.split()[0]

    def __ge__(self, other):
        return self.full_name.split()[0] >= other.full_name.split()[0]

    def __ne__(self, other):
        return (self.full_name, self.date_of_birth, self.phone_number, self.city, self.country, self.home_address) != (other.full_name, other.date_of_birth, other.phone_number, other.city, other.country, other.home_address)

person1 = Human()
person1.input_data()
print(person1)

person2 = Human()
person2.input_data()
print(person2)

if person1 == person2:
    print("\nІнформація про людей співпадає")
else:
    print("\nІнформація про людей різна")

if person1 < person2:
    print("Перша людина в алфавітному порядку знаходиться перед другою")
elif person1 > person2:
    print("Перша людина в алфавітному порядку знаходиться після другої")
else:
    print("Розташування в алфавітному порядку співпадає")