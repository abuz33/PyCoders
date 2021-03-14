class Person:
    def __init__(self, name, heatlh, color):
        self.name = name
        self.heatlh = heatlh
        self.color = color

    def __str__(self):
        s = "\nName of the Person: "+self.name
        s += "\nHealth of the Person: " + str(self.heatlh)
        s += "\nColor of the Person: "+self.color
        return s

    def tut(self, esya):
        self.tool_box = []
        self.tool_box.append(esya)


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        s = "Brand of the Car: "+self.name
        s += "\nModel of the Car: " + str(self.model)
        s += "\nYear of the Car: "+self.year
        return s


insan = Person("Abuzer", 100, 'white')

insan.tut('Tornavida')

print((insan))
