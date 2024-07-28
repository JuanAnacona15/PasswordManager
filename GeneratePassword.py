import random


class GeneratePassword:
    def __init__(self):
        self.lowrcase = "abcdefghijklmnopqrstuvwxyz"
        self.capitalLetters = self.lowrcase.upper()
        self.numbers = "0123456789"
        self.characters = "!'#$%&/()=?¡¿*@{}]._;><[+-:,"
        self.DefaultLegth = 15
        
    def Custom(self, lowers, capitals, numbers, characters):
        baseLower = "".join(random.sample(self.lowrcase, lowers))
        baseCapital = "".join(random.sample(self.capitalLetters, capitals))
        baseNumbers = "".join(random.sample(self.numbers, numbers))
        baseCharacters = "".join(random.sample(self.characters, characters))

        basePassword = baseLower + baseCapital + baseNumbers + baseCharacters
        legthPassword = lowers + capitals + numbers + characters

        password = "".join(random.sample(basePassword, legthPassword))
        
        return password
    
    def CustomLegth(self, legth):
        password = "".join(random.sample(self.lowrcase + self.capitalLetters + self.numbers + self.characters, legth))
        
        return password
    
    def Default(self):
        password = "".join(random.sample(self.lowrcase + self.capitalLetters + self.numbers + self.characters, self.DefaultLegth))