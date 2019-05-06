from Greetings import Greetings
from Dog import Dog


def olaaf():
    name = input("Hey what is your name?   ")
    option = input("What greeting do you want:  ")

    greetings = Greetings(name)

    if option == "1":
        print(greetings.sayHi())
    elif int(option) == 2:
        print(greetings.whatsUp())
    else:
        print("Im out")


if __name__ == "__main__":
    olaaf()

