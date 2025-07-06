class Product:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def discount(self, percentage):
        self.value = self.value - (self.value * (percentage / 100))
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value.title()
# Getter
    @property
    def value(self):
        return self._value
# Setter
    @value.setter
    def value(self, value):
        if isinstance(value, str):
            value = float(value.replace('R$', ''))
        self._value = value

p1 = Product ('ARROZ', 7.99)
p1.discount(30)
print(p1.name, p1.value)
p2 = Product ('FEIJÃO', 'R$4.49')
p2.discount(20)
print(p2.name, p2.value)