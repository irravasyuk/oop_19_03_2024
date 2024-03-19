# Реалізуйте клас «Годинник». Збережіть у класі:
# назву моделі годинника, виробника годинника, рік
# випуску, ціну годинника, тип годинника (наручний,
# настінний і т. д.). Реалізуйте конструктор та методи
# класу для введення-виведення даних, а також для
# інших операцій. Використовуйте механізм
# перевантаження методів.
class Watch:
    def __init__(self, model, producer, year, price, watch_type):
        self.model = model
        self.producer = producer
        self.year = year
        self.price = price
        self.watch_type = watch_type

    def __str__(self):
        return f"Модель: {self.model}\nВиробник: {self.producer}\nРік: {self.year}\nЦіна: {self.price}\nТип: {self.watch_type}"

    def __eq__(self, other):
        return (self.model, self.producer, self.year, self.price, self.watch_type) == (other.model, other.producer, other.year, other.price, other.watch_type)

    def __lt__(self, other):
        return self.year < other.year

    def __le__(self, other):
        return self.year <= other.year

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

watch1 = Watch("Vintage A158WEA-1EF", "Casio", "2023", "3600", "наручні")
watch2 = Watch("Vintage LA670WEM-7EF", "Casio", "2022", "3000", "наручні")

print("Інформація про перший годинник:")
print(watch1)

print("\nІнформація про другий годинник:")
print(watch2)

if watch1 == watch2:
    print("\nГодинники однакові")
else:
    print("\nГодинники різні")

if watch1 < watch2:
    print("\nПерший годинник старіший")
else:
    print("\nДругий годинник старіший")
