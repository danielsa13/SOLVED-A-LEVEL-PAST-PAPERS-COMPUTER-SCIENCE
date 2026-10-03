from pathlib import Path

script_folder = Path(__file__).parent
file_path = script_folder / "Toys.txt"

class ToyRecord:
    def __init__(self, ToyName, NumberBricks, Difficulty, Category):
        self.__ToyName = ToyName
        self.__NumberBricks = NumberBricks
        self.__Difficulty = Difficulty
        self.__Category = Category

    def GetToyName(self):
        return self.__ToyName

    def GetNumberBricks(self):
        return self.__NumberBricks

    def GetDifficulty(self):
        return self.__Difficulty

    def GetCategory(self):
        return self.__Category

def ReadData(ToyArray):
    try:
        with open(file_path, 'r') as f:
            data = f.read().strip().split('\n')
    
        for i in data:
            ind = i.split(',')
            ToyArray.append(ToyRecord(ind[0], ind[1], ind[2], ind[3]))
        return ToyArray
    except Exception as e:
        print(f"Error: {e}")

def OutputToys(ToyArray):
    for i in ToyArray:
        print(
            f'Name: {i.GetToyName()} | ' 
            f'NumberBricks: {i.GetNumberBricks()} | ' 
            f'Difficulty: {i.GetDifficulty()} | ' 
            f'Category: {i.GetCategory()}\n' 
        )


ToyArray = [] #Data type Record
ToyArray = ReadData(ToyArray)
OutputToys(ToyArray)

def SearchToys(ToyArray):
    user_input = str(input("Enter a difficulty: "))

    while user_input.lower() not in ['easy', 'medium', 'expert']:
        user_input = int(input("Invalid input. Retry"))

    diffarr = []
    for i in ToyArray:
        if i.GetDifficulty().lower() == user_input.lower():
            diffarr.append(i)

    return diffarr

def WriteToys(ToyArray):
    with open('SelectedToys.txt', 'w') as f:
        for i in ToyArray:
            f.write(f'{i.GetToyName()},{i.GetNumberBricks()},{i.GetDifficulty()},{i.GetCategory()}\n')

WriteToys(SearchToys(ToyArray))