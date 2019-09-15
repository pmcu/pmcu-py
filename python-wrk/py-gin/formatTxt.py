import os
quantity = input("What numby ?\n> ")
itemno = input("What item numby?\n> ")
price = input("How much moneys?\n> ")
hat = input("What hat?\n> ")
myorder = "I want {} pieces of item {} for {} dollars. And I have a {}"
print(myorder.format(quantity, itemno, price, hat))
os.system("ls /home/padraig/mp3| head -22")
number=input("What numby?\n> ")
os.system("play " + "/home/padraig/mp3/" + number +".mp3")
