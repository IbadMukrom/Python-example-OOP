#
# class MyClass:
#     variable = "blah"
#
#     def function(self):
#         print("This is a message inside the class.")
#
# myobjectx = MyClass()
# myobjecty = MyClass()
#
# myobjecty.variable = "yackity"
#
# # Then print out both values
# print(myobjectx.variable)
# print(myobjecty.variable)
#a Creates class Car
class Car:

    # Creates Car class constructor
    def __init__(self, model):
        # initialize instance variables
        self.model = model

    # Creates model property
    @property
    def model(self):
        return self.__model

    # Create property setter
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model

    def getCarModel(self):
        return "The car model is " + str(self.model)


carA = Car(3000)
print(carA.getCarModel())