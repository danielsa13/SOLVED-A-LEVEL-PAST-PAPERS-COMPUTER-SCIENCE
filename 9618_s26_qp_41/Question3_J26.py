class TheObject:
    def __init__(self, ObjectType, Amount):
        self.ObjectType = ObjectType #String
        self.Amount = Amount #Integer

class Path:
    def __init__(self, NumberSpaces):
        self.BoardArray = [TheObject('', -1) for i in range(100)] #TheObject
        self.NumberSpaces = NumberSpaces #Integer

    def GetNumberSpaces(self):
        return self.NumberSpaces

    def InitialiseData(self, TheObjArray):
        if self.NumberSpaces < len(TheObjArray):
            return False

        for index, item in enumerate(TheObjArray):
            self.BoardArray[index] = item
            self.NumberSpaces -= 1

        return True

    def ReturnPath(self):
        string = ""
        for item in self.BoardArray:
            if item.Amount != -1:
                string += f"{item.ObjectType}-{item.Amount} "

        return string

    def GetPathObject(self, index):
        return self.BoardArray(index)


ArrayOfObjects = [
    TheObject("Money", 50),
    TheObject("Expereince", 100),
    TheObject("Money", 200),
    TheObject("Money", 20),
    TheObject("Experience", 30)
]

Path1 = Path(5)
Path1.InitialiseData(ArrayOfObjects)
print(Path1.ReturnPath())
