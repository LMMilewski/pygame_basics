def foo():
    print "hello world"

class Ferris:
    def __init__(self, life, mana = 25):
        self.life = life
        self.mana = mana

    def display(self):
        print "Ferris", self.life, self.mana


ferris = Ferris(10)
ferris.display()
