class Khushi:
    life =4

    def heal(self):
        print("Hurray Healed ")
        self.life +=1

    def hurt(self):
        print("Happy is Hurt")
        self.life +-1

    def checkLife(self):
        if self.life >0 :
            print("Life left "+str(self.life))
        else:
            print("Dead Now !!!!")

happy = Khushi()
happy2 = Khushi()
happy.heal()
happy.checkLife()
happy.hurt()
happy.checkLife()
happy.heal()
happy.heal()
happy.checkLife()
happy2.checkLife()