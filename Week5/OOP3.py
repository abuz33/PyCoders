# Write a class CITY in Python with following specification:
# Code  # Numeric value
# Name  # String value
# Pop  # Numeric value for Population
# KM  # Numeric value
# Density  # Numeric value for Population Density
# Methods:
# CalDen()  # Method to calculate Density as Pop /KM
# Record()  # Method to allow user to enter values Code, Name, Pop, KM and call CalDen ( ) method
# Method to display all the date members also display a message “Highly Populated Area” is the Density is more than 12000.
# See()

class City:
    def calDen(self):
        self.density = self.pop / self.km

    def record(self, code, name,  pop, km):
        self.name = name
        self.code = code
        self.pop = pop
        self.km = km

        self.calDen()

    def see(self):
        if self.density > 12000:
            self.message = 'Highly Populated Area'
        else:
            self.message = 'You can live here till you die. CHEERS!!!'

        return self.message


amsterdam = City()

amsterdam.record(123, 'Amsterdam', 3000000, 50)

print(amsterdam.see())
print(len(amsterdam.__dict__))
