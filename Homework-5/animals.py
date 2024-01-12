class Animals:
    count = 0

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
        self.count = Animals.count
        Animals.count += 1


q = ('Lion', 'yellow', 8),
p = ('Elephant', 'blue', 15),
o = ('Dog', 'black', 7),
n = ('Cat', 'white', 3),
m = ('Horse', 'green', 5),
l = ('Tiger', 'orange', 10),
k = ('Bear', 'brown', 12),
j = ('Giraffe', 'yellow', 9),
i = ('Penguin', 'white', 2),
h = ('Kangaroo', 'black', 6),
g = ('Monkey', 'brown', 4),
f = ('Wolf', 'gray', 6),
e = ('Fox', 'orange', 5),
d = ('Panda', 'black and white', 8),
b = ('Owl', 'gray', 2),
a = ('Lemur', 'gray', 1)

print(l.count)
