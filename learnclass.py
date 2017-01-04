class Fruit:
    num = 0

    def __init__(self): # 都不让我调用，为什么不提示出错咯
        self.Name = 'Fruit'
        self.Weight = 20

    def __init__(self, name, weight):
        self.Name = name
        self.Weight = weight

    #
    # def __init__(self, name, weight, high):
    #     self.Name = name
    #     self.Weight = weight

    if num > 0:
        we = 1

    def AddNum(self, n):
        self.num += n

    def AddVal(self):
        # num = num + n  # error

        self.Juiceable = True
        pass
    def AddVal2(self):
        self.GoodTaste = False

class Banana(Fruit):
    def __init__(self):
        Fruit.__init__(self, "banana", 20)
        self.HavePeel = True
    def AddVal2(self, val):
        self.NoGoodTaste = False


def test_normal_classval():
    # apple = Fruit() # error
    apple = Fruit("apple", 10)
    print("Fruit", Fruit.num)  # 0
    print(apple.Name, apple.num)  # 0
    # print(apple.we) error
    Fruit.num += 1
    banana = Fruit("banana", 30)
    print(vars(banana).items())
    print("Fruit", Fruit.num)  # 1
    print(banana.Name, banana.num)  # 1
    print(apple.Name, apple.num)  # 1
    # print(apple.we) error
    # print(banana.we) error
    banana.num += 2
    apple.num += 3
    print("Fruit", Fruit.num)  # 1
    print(banana.Name, banana.num)  # 3
    print(apple.Name, apple.num)  # 4
    banana.AddNum(10)
    print("Fruit", Fruit.num)  # 1
    print(banana.Name, banana.num)  # 13
    print(apple.Name, apple.num)  # 4

    print(vars(banana).items())
    banana.AddVal()
    print(banana.Juiceable)
    print(vars(banana).items())
    del banana.Weight
    print(vars(banana).items())
    del banana.num
    print(vars(banana).items())
    print(banana.Name, banana.num)  # 1


def test_Inheritance():
    banana = Banana()
    print(vars(banana).items())
    print(banana.Name, banana.num)
    banana.AddVal()
    banana.AddNum(20)
    print(vars(banana).items())
    print(banana.Name, banana.num)
    # banana.AddVal2() error
    banana.AddVal2(1)
    print(vars(banana).items())



if __name__ == '__main__':
    # test_normal_classval()
    test_Inheritance()
    pass
