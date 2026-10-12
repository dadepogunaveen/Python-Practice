class fan:
    def __init__(self):
        self.brand="usha"
        self.cost=1500
        self.color="black"
        self.wings=3
    def on(self):
        print("fan is on")
    def rotate(self):
        print("fan is rotating")
    def off(self):
        print("fan is off")
f1=fan()
print(f1.brand)
print(f1.cost)
print(f1.color)
print(f1.wings)
f1.on()
f1.rotate()
# f1.off()
a=10
b=10
c=10
d=20
print(id(a))
print(id(b))
print(id(c))
print(id(d))
# f1.off
class hero:
    def __init__(self):
        self.name="yash"
        self.age=40
        self.numOfMovies=25
    def act(self):
        print("yash is a good actor")
h1=hero()
print(h1.name)
print(h1.age)
print(h1.numOfMovies)
h1.act()
# f1.off()
class heroine:
    def __init__(self):
        self.name="sai pallavi"
        self.age=30
    def dance(self):
        print("she is a good dancser")
h1.heroine()
print(h1.name)
print(h1.age)
h1.dance()
h1.movie="fidaa"
print(h1.movie)
h1.age=32
print(h1.age)
del (h1.age)