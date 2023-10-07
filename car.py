class Car(object):
    def __init__(self,company,model,price,power):
        self.company = company
        self.model = model
        self.price = price
        self.power = power

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def accelerate(self):
        print("Accelerated")

BMW = Car("BMW", "Seven series", 100000, 540)

print(BMW.price)
print(BMW.power)
print(BMW.model)
print(BMW.company)
print(BMW.start())