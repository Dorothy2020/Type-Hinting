def myfunction(myparameter:int)->int:
    return myparameter + 10

def otherfunction(otherparameter:str):
    print(otherparameter)

otherfunction(myfunction(20))