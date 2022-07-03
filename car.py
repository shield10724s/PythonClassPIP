class Car():
    def __init__(self, model, color, company, topSpeed):
        self.color = color
        self.company = company
        self.model = model
        self.topSpeed = topSpeed

    def start(self):
        print('The car has started')

    def stop(self):
        print('The car has been stopped')

    def accelRate(self):
        print('The car is speeding up')

ferrari = Car('sedan', 'red', 'ferrari', '278kmph')
print(ferrari.color)
print(ferrari.model)
ferrari.start()