# ### encapsulation : ek data ko jis k sath functionality perform kar sakte h wo wali method ek hi jagah p likhna (in class)
# class Phone:
#     def __init__(self, brand, model_name, price):
#         self.brand = brand
#         self.model_name = model_name
#         # self.price = price
#         self.__price = (
#             price  ##doing __price python will convert this itno : _Phone__price
#         )

#     def make_a_call(self, phone_number):
#         print(f"calling {phone_number}...")

#     def full_name(self):
#         return f"{self.brand} {self.model_name}"

#     def send_message(self):
#         pass  ### twilio


# ###abstraction : hide complexity
# # l = [3, 4, 2, 1]
# # l.sort()  ##tim sort
# # print(l)

# ## special naming convection
# ### everything in python is public
# ### _name : _ convection for private name dont touch it (theyy can but shoudnt)
# ## __name__ : dunder/magic methods


# #### name mangling
# phone1 = Phone("nokia", "1100", 1000)
# # print(phone1.price)
# # phone1.price = -1000
# # print(phone1.price)

# ##__name(not a convection)
# # #print(phone1__.price) ###error
# print(
#     phone1.__dict__
# )  ##{'brand': 'nokia', 'model_name': '1100', '_Phone__price': 1000} so now u can print _Phone__price
# print(phone1._Phone__price)  ###1000


####---------------Property and setter decorator :


class Phone1:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
        ### self.complete_specification = (
        #     f"{self.brand} {self.model_name} and price is {self.price}"
        # )

    @property  ### now we dont have to write complete_specification() we can directly write complete_specification to use it
    def complete_specification():
        return f"{self.brand} {self.model_name} and price is {self.price}"

    @property  ###made getter
    def price(self):
        return self.price

    ##now make setter

    def make_a_call(self, phone_number):
        print(f"calling {phone_number}...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


phone2 = Phone1("samsung", "duo", 5000)  ##we can set price negative tha's problem
print(phone2.brand)
print(phone2.model_name)
phone2.price = 3000  ###this will print below line 3000 but in complete_specification it will be still 5000
print(phone2.price)
print(phone2.complete_specification)
