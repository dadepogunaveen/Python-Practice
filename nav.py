class heroine:
    def __init__(self):
        self.name="sai pallavi"
        self.age=30
    def dance(self):
        print("she is a good dancser")
h1=heroine()
print(h1.name)
print(h1.age)
h1.dance()
h1.movie="fidaa"
print(h1.movie)
h1.age=32
print(h1.age)
del (h1.age)
print(h1.age)