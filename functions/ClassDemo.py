
class Myclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def my_function(self):
        print("Your name",self.name)

mc=Myclass("Nitesh",23)
print(mc.name)
print(mc.age)
mc.my_function()

