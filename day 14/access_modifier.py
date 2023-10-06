class Person:
    def __init__(self):
        # PUBLIC
        self.name="Ram"
        #PROTECTED
        self._age=12
        #PRIVATE
        self.__phone_number="974631"
    @property
    def phone_number(self):
        return self.__phone_number
    @phone_number.setter
    def phone_number(self,phone_number):
        self.__phone_number=phone_number

    # @property
    # def age(self):
    #     return self._age
    # @age.setter
    # def age(self,age):
    #     self._age=age
    # # phone_number=property(get_phone_number,set_phone_number)
p=Person()

#yesma error aauxa; private variable cannot be accessed
# print(p.__phone_number)
# print(p._age)
# print(p.get_phone_number())

# p.phone_number="123456789"

# print(p.phone_number)