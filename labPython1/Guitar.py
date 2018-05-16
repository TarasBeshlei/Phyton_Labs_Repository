class Guitar:
    total_amount = 0


    def __init__(self, brand = "ESP", price=3000, amount=4, guitar_type="Explorer", color = "White"):
        self.brand = brand
        self.price = price
        self.amount = amount
        self.color = color
        self.guitar_type = guitar_type
        Guitar.total_amount += amount

    def to_string(self):
        print("Brand:" + self.brand + " Price:", self.price,
              " Amount:", self.amount, "; Guitar type:" + self.guitar_type + " Color:", self.color)

    def print_sum(self):
        print("Amount " + self.brand, self.guitar_type, self.amount)


    @staticmethod
    def print_static_sum():
        print("Amount", Guitar.total_amount)



if __name__ == '__main__':
    gibson = Guitar("Gibson", 2500, 32, "Les Paul", "Yellow")
    esp = Guitar()
    fender = Guitar("Fender", 2900, 10, "Stradocaster", "Black")
    gibson.to_string()
    esp.to_string()
    fender.to_string()
    gibson.print_sum()
    esp.print_sum()
    fender.print_sum()
    Guitar.print_static_sum()
