class Manufacturer():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.brands = []
        self.cars = []

    def add_car(self, brand, model, year):
        car = Car(brand, model, year)
        self.cars.append(car)

    def car_details(self):
        print("Manufacturer:", self.name)
        print("Location:", self.location)
        print("Cars:")
        for car in self.cars:
            car.get_details()
            print()

    def add_brand(self, brand):
        # self.brand = brand
        # self.brand=[]
        # s=input("enter brand")
        self.brands.append(brand)

    def get_brands(self):
        return self.brands


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)


# Create two manufacturer objects
m = Manufacturer('Manufacturer A', 'mumbai')
m1 = Manufacturer('Manufacturer B', 'pune')

# calling add_brand function
m.add_brand('ABC')
m.add_brand('ZXC')
m.add_brand('QWE')
print(m.get_brands())

m1.add_brand('QAA')
m1.add_brand('uio')
m1.add_brand('tyu')
print(m1.get_brands())

# Add different brands of cars to each manufacturer

m.add_car("Ford", "Mustang", 2073)
m.add_car("Chevrolet", "Camaro", 2000)
m1.add_car("Toyota", "Corolla", 1985)
m1.add_car("Honda", "Civic", 2014)

# creating car object
c = Car('tata', 'Nexon', 2024)
c.get_details()
m.car_details()
m1.car_details()
