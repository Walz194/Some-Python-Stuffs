class PlayerCharacter:
    def __init__(self,name = 'anonymous', age=0):
        self.age = age
        self.name = name

    def can_play(self):
        if(self.age < 18):
            return 'Sorry kid, You are too young to play this game.\nCome back when you balls drop'
        else:
            return f'Oh, Welcome {self.name}, We\'ve bee waiting for you \nHere are some R-rated games for your pleasure'

    def shout(self, word):
        return f'{word.upper()}' if self.age > 18 else 'I\'m a f**cking baby'.upper()
