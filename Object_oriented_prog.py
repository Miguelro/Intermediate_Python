class House:
    layout = 'square'
    def paint(self, color):
        self.color = color

# As before, we can access attributes.
print(House.layout)  # 'square'
print(House.paint)  # <function House.paint(self, color)>
print(House.__dict__)

# This is the new syntax! Instantiate a class object to get back an instance object.
home = House()  # `home` is now a _specific_ instance object of type `House`
print(home)  # <House at 0x....>
print(type(home) is House) # True

#Set attribute on the fly
home.size = '1000'
print(home.size)
print(home.__dict__)
home.color = 'red'
print(home.__dict__)

home.num_bathrooms = 2
home.num_bedrooms = 3
print(home.__dict__)  # {'size': '1000', 'color': 'red', 'num_bathrooms': 2, 'num_bedrooms': 3}

home.color = 'blue'
print(home.color)  # blue
print(home.num_bathrooms)  # 2

del home.color #Remove home color
print(home.__dict__) 


class House2():
    def __init__(self, size, color='white'):
        self.size = size
        self.color = color

home2 = House2(size = 1000, color='red')
print(home2.__dict__)

class House:
    layout = 'square'
    def __init__(self, size, color='white'):
        self.size = size
        self.color = color
    def paint(self, color):
        self.color = color

# We can instantiate a `home` from the class object `House`
# (using our `__init__` method!) and resolve attributes.
home = House(1000)
print(home.size)  # 1000
print(home.color)  # white

# We can resolve attributes on the class object too.
print(House.layout)  # square
print(House.paint)  # <function House.paint(self, color)>

print(home.layout)  # square - everything looks normal
print(home.paint)  # <bound method House.paint of <House object at 0x...>> - what's this?!

# The method contains information about the referenced function and the bound instance object.
print(home.paint.__func__)  # <function House.paint(self, color)>
print(home.paint.__self__)  # <House at 0x...>
print(home.paint.__self__ is home)  # True

home.paint('red')
# is equivalent to
House.paint(home, 'red')

# The home's color is indeed changed after painting the home.
print(home.color)  # red

##########################
class House:
    PRICE_PER_SQUARE_FOOT = 2.5
    def __init__(self, size, num_bedrooms, num_bathrooms):
        self.size = size
        self.beds = num_bedrooms
        self.bath = num_bathrooms
    @property
    def price(self):
        return self.size * self.PRICE_PER_SQUARE_FOOT

home = House(1000, 2, 2)
#home.price() #Si no añadimos property se accedería al valor como metodo
home.price

#the @name.setter decorator can decorate a method to assign a new value to a property
#Uses:
#   - Update many data attributes after one is set.
#   - Hide more complex assignments behind the guise of an assignment.

class House_bis:
    PRICE_PER_SQUARE_FOOT = 2.5
    def __init__(self, size, num_bedrooms, num_bathrooms):
        self.size = size
        self.beds = num_bedrooms
        self.bath = num_bathrooms
    @property
    def price(self):
        return self.size * self.PRICE_PER_SQUARE_FOOT
    @price.setter
    def price(self, new_price):
        self.size = new_price / self.PRICE_PER_SQUARE_FOOT

home_bis = House_bis(1000,2,2)
home.price
home.size


home_bis.price = 2000
home.size
 
