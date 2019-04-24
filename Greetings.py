class Greetings:
    def __init__(self, name="Unknown"):
        self.name = name

    def sayHi(self):
        return "Hi {}".format(self.name)

    def whatsUp(self):
        return "Whats up {}".format(self.name)

