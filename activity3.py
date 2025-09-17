class america():
    def capital(self):
        print("Washington DC is the capital of America")

    def language(self):
            print("English is the primary language of America")

    def type(self):
            print("USA is a developed contry")

class india():
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is the most widely spoken language of India")

    def type(self):
        print("India is a devoloping contry")

obj_ind = india()
obj_usa = america()

for contry in (obj_ind, obj_usa):
    contry.capital()
    contry.language()
    contry.type()