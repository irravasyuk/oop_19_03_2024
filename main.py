# Реалізуйте клас «Вебсайт». Збережіть у класі: назву
# вебсайту, адресу та опис вебсайту. Реалізуйте конструктор
# та методи класу для введення-виведення даних, а також
# для інших операцій. Використовуйте механізм перевантаження методів.
class Website:
    def __init__(self, name="", url="", description=""):
        self.name = name
        self.url = url
        self.description = description

    def display(self):
        print("Назва:", self.name)
        print("Адреса:", self.url)
        print("Опис:", self.description)

    def input_data(self):
        self.name = input("Введіть назву сайту: ")
        self.url = input("Введіть адресу сайту: ")
        self.description = input("Введіть опис сайту: ")

    def __str__(self):
        return f"Сайт: {self.name},Адреса :{self.url},Опис сайту: {self.description}"

    def __eq__(self, other):
        return (self.name, self.url, self.description) == (other.name, other.url, other.description)

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __ge__(self, other):
        return self.name >= other.name

website1 = Website()
website1.input_data()

website2 = Website()
website2.input_data()

print("\nІнформація про перший сайт:")
website1.display()

print("\nІнформація про другий сайт:")
website2.display()

if website1 == website2:
    print("Сайти однакові")
else:
    print("Сайти різні")

if website1 < website2:
    print("Перший сайт йде раніше в алфавітному порядку")
else:
    print("Другий сайт йде раніше в алфавітному порядку")
