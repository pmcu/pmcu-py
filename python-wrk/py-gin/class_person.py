class Person:
  def __init__(self, name, hata, nota):
    self.name = name
    self.hata = hata
    self.nota = nota

  def myfunc(abc):
    print("Hello my name is " + abc.name)
    print("My hat is " + abc.hata)

nonota = """
Agus an banana man,
bhí seisean ann fosta,
agus chonaic mé é, Agus
bhí sé scanrúil.

"""

p = Person("Barney", "roundy", nonota)

print(p.name)
print(p.nota)
p.myfunc()
