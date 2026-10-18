from pathlib import Path

script_folder = Path(__file__).parent
file_path = script_folder / "AvatarFile.txt"

class Avatar:
    def __init__(self, TheName, Glasses, Hair, Age):
        self.__TheName = TheName #STRING
        self.__Glasses = Glasses #BOOLEAN
        self.__Hair = Hair #STRING
        self.__Age = Age #INTEGER

    def Getname(self):
        return self.__TheName

    def GetAge(self):
        return self.__Age

    def MeetCriteria(self, GlassFlag, HairCol):
        if self.__Glasses == GlassFlag and self.__Hair == HairCol:
            return True
        else:
            return False

AvailableAvatars = []

def LoadAvatars():
    global AvailableAvatars
    try:
        with open(file_path, 'r') as f:
            data = f.read().strip().split('\n')

        for items in data:
            splitted = items.split(' ')
            AvailableAvatars.append(Avatar(splitted[0], bool(splitted[1]), splitted[2], int(splitted[3])))

    except IOError:
        print('File can not be read')

LoadAvatars()
CritMatch = []

def EnterChoices():
    global AvailableAvatars, CritMatch
    glass_input = input("Does your avatar wear glasses? y/n ")
    while glass_input.lower() not in 'yn':
        glass_input = input("Invalid. Please enter y or n ")

    hair_input = input("What color is your avatars hair? ")
    while hair_input.lower() not in ['black', 'blonde', 'brown', 'pink', 'red', 'green']:
        hair_input = input("Invalid. Please enter a valid choice ")

    if glass_input == 'y':
        glassflag = True
    else:
        glassflag = False

    totmatch = 0
    for Avatar in AvailableAvatars:
        if Avatar.MeetCriteria(glassflag, hair_input):
            CritMatch.append(Avatar)
            totmatch += 1

EnterChoices()
print(f'Number of Avatars that match criteria: {len(CritMatch)}')

for Match in CritMatch:
    print(f'Name: {Match.Getname()} | Age: {Match.GetAge()}')

# print(len(AvailableAvatars))