class House:

    def __init__(self,name="Ram",color="red",garden=True,window=10):
        self.color=color
        self.garden=garden
        self.window=window
        self.name=name

    def set_color(self,color):
        self.color=color

    def __str__(self):
        return f"{self.name}"

ram_ko_ghar=House("Yellow",window=100)
print(ram_ko_ghar)
print(ram_ko_ghar.color)
print(ram_ko_ghar.garden)

# shyam_ko_ghar=House()
# shyam_ko_ghar.set_color("green")
# print(shyam_ko_ghar.color)

# hari_ko_ghar=House()
# hari_ko_ghar.set_color("Orange")
# print((hari_ko_ghar.color))