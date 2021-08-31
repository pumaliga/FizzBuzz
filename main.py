class FizzBuzzDetector:
    count_fizz = 0
    count_buzz = 0

    def __init__(self, s):
        self.s = s.split(' ')
        if not 7 <= len(s) <= 100:
            raise ValueError("Incorrect input")

    def fizz(self):
        fizz_s = self.s
        print(fizz_s)
        for index, item in enumerate(fizz_s):
            if index != 0 and index % 3 == 0:
                self.count_fizz += 1
        return f"Fizz count: {self.count_fizz}"

    def buzz(self):
        buzz_s = self.s
        for i in buzz_s:
            for ind, it in enumerate(i):
                if ind != 0 and ind % 5 == 0:
                    self.count_buzz += 1
        return f"Buzz count: {self.count_buzz}"

    def getOverlappings(self):
        return self.buzz(), self.fizz()


a = FizzBuzzDetector('В своём стремлении повысить качество жизни они забывают')
print(a.getOverlappings())



