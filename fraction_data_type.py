# Creating fraction data type 

class Fraction : 
    # parameterize constructor: which requires input
    def __init__(self,x,y):
        self.num=x
        self.den=y

    def __str__(self) :  # Magic method to give the structure when print is called for object
        return "{}/{}".format(self.num,self.den)

    def __add__(self,other):  # magic method for addition
        new_num=self.num*other.den + other.num*self.den
        new_den=self.den*other.den

        return "{}/{}".format(new_num,new_den)


    def __sub__(self,other):  # magic method for subtraction
        new_num=self.num*other.den -other.num*self.den
        new_den=self.den*other.den

        return "{}/{}".format(new_num,new_den)

    def __mul__(self,other):  # magic method for multiplication
        new_num=self.num*other.num
        new_den=self.den*other.den

        return "{}/{}".format(new_num,new_den)


    def __truediv__(self,other):  # magic method for division
        new_num=self.num*other.den
        new_den=self.den*other.num

        return "{}/{}".format(new_num,new_den)

    def convert_to_decimal(self):
        return self.num/self.den

# Making object and printing it
fra1=Fraction(2,2)
print(fra1)

fra2=Fraction(1111111,21)
print(fra2)

# Basic Fraction Operations
print(fra1 + fra2)
print(fra1 - fra2)
print(fra1 * fra2)
print(fra1 / fra2)

# Changing fraction into decimals
print(fra1.convert_to_decimal())



