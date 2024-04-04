class Car:
    def __init__(self, mark, color, engine):
        self.mark = mark
        self.color = color
        self.engine = engine

    def drive(self):
        self.make_noise()
        print(f"Поберегись! Машина {self.mark} едет!")

    def make_noise(self):
        print("Врум-вурм")


car = Car("Ford", "Blue", "2.0")
print(f"Машина: марка {car.mark}, цвет {car.color}, объем двигателя {car.engine}")
car.drive()

second_card = Car("Hyundai", "Gray", "1.6")
second_card.drive()
