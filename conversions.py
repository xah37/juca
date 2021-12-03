from rich import print


class Temperature():

    def __init__(self, t, cels):
        self.t = t
        self.cels = cels

    def fromCelsius(self):
        print(f"{self.cels}\u00b0 celsius is {(self.cels * 9/5)+32}\u00b0 fahrenheit.")
        # print((self.cels * 9/5)+32)

    def fromFahrenheit(self):
        print(f"{self.t}\u00b0 fahrenheit is {(self.t - 32) * 5/9}\u00b0 celsius.")
        # print((self.t - 32) * 5/9)


halp = Temperature(212, 100)
halp.fromCelsius()
halp.fromFahrenheit()
