


class register:
    def __init__(self, tamanho):
        self.r = [0 for c in range(tamanho)]

    def add(self, bit):
        del self.r[-1]
        a = [bit]
        a.extend(self.r)
        self.r = a[:]

    def setRegister(self, registerValue):
        self.r = registerValue[:]