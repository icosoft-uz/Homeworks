class Mobile:
    count = 0  # Class attribute

    def __init__(self, model, name, color, price, storage, pixel):
        self.model = model
        self.name = name
        self.color = color
        self.price = price
        self.storage = storage
        self.pixel = pixel
        Mobile.count += 1


a = Mobile('Samsung', 'Galaxy S21', 'black', 1000, '128GB', '108MP')
b = Mobile('iPhone', '13', 'white', 1200, '128GB', '120MP')
c = Mobile('Google', 'Pixel 6', 'white', 800, '256GB', '50MP')
d = Mobile('iPhone', '15 Pro', 'black', 1000, '256GB', '100MP')
e = Mobile('Redmi', 'A9', 'white', 700, '128GB', '50MP')
f = Mobile('Huawei', 'X5', 'blue', 600, '64GB', '80MP')
g = Mobile('Samsung', 'Galaxy S20', 'black', 900, '128GB', '108MP')
h = Mobile('Google', 'Pixel 5', 'white', 700, '256GB', '50MP')
i = Mobile('iPhone', '14 Pro', 'black', 1000, '256GB', '100MP')
j = Mobile('Redmi', 'A8', 'white', 600, '128GB', '50MP')
k = Mobile('Huawei', 'X5', 'blue', 600, '64GB', '80MP')

print(f"Telefonlar soni: {a.count} ta.")
