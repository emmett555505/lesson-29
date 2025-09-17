class BMW:
    def fuel_type(self):
        print("\nfuel type is desil")

    def max_speed(self):
        print("\nmax speed is 115")

class Ferrari:
    def fuel_type(self):
        print("\nfuel type is normal")
    
    def max_speed(self):
        print("\nmax speed is 135")

f = Ferrari()
b = BMW()

for i in (f,b):
    i.fuel_type()
    i.max_speed()