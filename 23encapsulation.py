### encapsulation : ek data ko jis k sath functionality perform kar sakte h wo wali method ek hi jagah p likhna (in class)
class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    def make_a_call(self, phone_number):
        print(f"calling {phone_number}...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):
        pass  ### twilio


###abstraction : hide complexity
# l = [3, 4, 2, 1]
# l.sort()  ##tim sort
# print(l)

## special naming convection
### everything in python is public
### _name : _ convection for private name dont touch it (theyy can but shoudnt)
## __name__ : dunder/magic methods


#### name mangling
phone1 = Phone("nokia", "1100", 1000)
print(phone1.price)
phone1.price = -1000
print(phone1.price)
