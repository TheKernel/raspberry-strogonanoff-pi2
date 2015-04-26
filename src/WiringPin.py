import wiringpi2

wiringpi2.wiringPiSetup()

class WiringPin:

    def __init__(self, gpio_number, direction="out"):
        self.gpio_number = gpio_number
        self.direction = direction

    def export(self):
        wiringpi2.pinMode(self.gpio_number,
            1 if self.direction == "out" else 0)
        return self

    def set_value(self, value):
        wiringpi2.digitalWrite(self.gpio_number, value)

    def get_value(self):
        return wiringpi2.digitalRead(self.gpio_number)

    def unexport(self):
        pass # for now
