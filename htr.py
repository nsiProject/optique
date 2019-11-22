from PIL import Image


carte = Image.open("foo.png")           #J'ouvre mon Image test, et je la rotationne de 90°
carte = Carte.rotate(90)

width, height = Carte.size              #Je la rogne pour avoir le principal
left = 124
top = -100
right = 290
bottom = 260

Carte= Carte.crop((left, top, right, bottom))



Carte.show()
