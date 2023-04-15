class Country:
    geo = 'Asia'
    def __init__(self, country_name, capital, language, currency):
        self.country_name = country_name
        self.cap = capital
        self.language = language
        self.currency = currency

    def speak(self):
        return f'Hi, we speak {self.language}'

    def capital_1(self):
        return f'Our capital is {self.cap}'
    def money(self):
        return f'Our currency is {self.currency}'

#
# Country_1 = Country('India', 'Delhi', 'Hindi', 'INR')
# print(Country_1.country_name)
# print(Country_1.speak())
# print(Country_1.money())
# print(Country_1.capital_1())
# print(Country_1.geo)
#
# Country_2 = Country('Thailand', 'Bangkok', 'Thai', 'THB')
# print(Country_2.country_name)
# print(Country_2.speak())
# print(Country_2.money())
# print(Country_2.capital_1())
# print(Country_2.geo)
class city(Country):
    def __init__(self, city_name, country_name, capital,  language, currency, population):
        super().__init__(country_name, capital, language, currency)
        self.city_name = city_name
        self.population = population

    def popul(self):
        return f'Population of the {City_1.city_name} is {self.population}'

City_1 = city('Bangkok', 'Thailand', 'Bangkok', 'Thai', 'THB', 11000000)
print(City_1.city_name)
print(City_1.population)
print(City_1.popul())