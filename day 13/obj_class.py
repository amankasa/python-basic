class Vehicles:
    def __init__(self) -> None:
        print("There are many types of vehicles")

class LMV(Vehicles):
    def __init__(self) -> None:
        print("LMV are mostly used for passenger cars or taxi")
        super().__init__()

class Motorbike(Vehicles):
    def __init__(self) -> None:
        print("Motorcycles are used for easy mobility")

class SUV(LMV):
    def __init__(self) -> None:
        print ("Suv are a type of LMV")
        super().__init__()

s=SUV()
