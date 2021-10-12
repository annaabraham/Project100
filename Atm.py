class Client(object):
    def __init__(self, name, age, gender, creditNo, phoneNo, pinNo):
        self.name=name
        self.age=age
        self.gender=gender
        self.creditNo=creditNo
        self.phoneNo=phoneNo
        self.pinNo=pinNo or {}
    def setPin(self, course, pinNo):
        self.pinNo[course]=pinNo

    def getPin(self, course):
        return self.pinNo[course]

    def getPin(self):
        return sum(self.pinNo.values())/len(self.pinNo)

Daisy = Client("Daisy", 20, "female", 1234, 9876543219, 3233)
Rose = Client("Rose", 25, "female", 5678, 1234567891, 4434)

print(Daisy.getPin())
print(Rose.getPin())