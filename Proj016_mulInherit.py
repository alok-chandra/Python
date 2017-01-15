class Star:

    def Stoic(self):
        print("Best One Athelete")

class YStar:
    def Saga(self):
        print("Cute and Sweet, No Athelete")

class All_Star(Star,YStar):
    pass

aStar = All_Star()
aStar.Saga()
aStar.Stoic()