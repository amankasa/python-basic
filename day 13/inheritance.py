class GrandFather:
    def __init__(self) -> None:
        print("Grandfather")
    house="luxury house"

class Father(GrandFather):
    def __init__(self) -> None:
        print("Father")
        super().__init__()
    car="ferari"

# class Mother:
#     def __init__(self) -> None:
#         print("Mother")
#     jewellery="Sun Chandi"

class Son(Father):
    def __init__(self) -> None:
        print("son bought 2 houses")
        super().__init__()
    electronics="PS5"

son=Son()
# print(son.jewellery)
# print(son.electronics)
# print(son.car)
# print(son.house)

father=Father()

print(isinstance(son))