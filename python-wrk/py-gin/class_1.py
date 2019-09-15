import os
class Myclass:
    def __init__(self, name, number, track):
        self.name = name
        self.number = number
        self.track = track
    def myfunc(self):
        print("Heh agus ho is mise " + self.name)
        os.system("play /home/padraig/mp3/" + self.track + ".mp3")


p1 = Myclass("Tom",23,"OuterTemple")

print(p1.name)
print(p1.number)

p1.myfunc()
