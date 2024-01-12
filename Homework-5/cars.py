class Cars:
  def __init__(self, model, name, color, price, km, speed):
      self.model = model
      self.name = name
      self.color = color
      self.price = price
      self.km = km
      self.speed = speed


a = ('Toyota', 'Camry', 'white', 25000, 30000, 180),
b = ('Tesla', 'Model S', 'black', 80000, 10000, 220),
c = ('BMW', 'X5', 'black', 20000, 15000, 320),
d = ('Mercedes', 'C-Class', 'white', 45000, 20000, 250),
e = ('Audi', 'A4', 'white', 35000, 25000, 200),
f = ('Ford', 'Mustang', 'red', 40000, 18000, 250),
g = ('Chevrolet', 'Camaro', 'yellow', 30000, 20000, 210),
h = ('Honda', 'Civic', 'silver', 28000, 22000, 190),
i = ('Nissan', 'GTR', 'red', 30000, 20000, 250),
j = ('Mazda', 'CX-5', 'black', 40000, 18000, 220),
k = ('Dodge', 'Challenger', 'black', 30000, 12000, 280),
l = ('Jeep', 'Wrangler', 'blue', 35000, 16000, 220),
m = ('Subaru', 'Impreza', 'silver', 28000, 22000, 190),
n = ('Lexus', 'RX', 'red', 40000, 18000, 250)]


print(f"Model: {a.model}, Nom: {a.name}, Rang: {a.color}, Narx: {a.price}, Km: {a.km}, Tezlik: {a.speed}")
