class Car(object):
    def __init__(self,model,color):
        self.model=model
        self.color=color
    def start(self):
        print("started")
carens=Car("Kia","gray")
print(carens.start())            