from string import ascii_letters


class Person:
    S_ENG = 'abcdefghijklmnopqrstuvwxyz'
    S_ENG_UPPER = S_ENG.upper()

    def __init__(self, fio, old, psw, weight):
        self.varify_fio(fio)
        self.varify_old(old)
        self.varify_pasw(psw)
        self.varify_weight(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__weight = weight
        self.__psw = psw

    @classmethod
    def varify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("FIO will be str")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Invalid format")

        letters = ascii_letters + cls.S_ENG + cls.S_ENG_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("FIO have has more than 1 symbol")
            if len(s.strip(letters)) != 0:
                raise TypeError('Only letters and defise')

    @classmethod
    def varify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('Age can be [14 - 120]')

    @classmethod
    def varify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError('Weight can be more than 20')

    @classmethod
    def varify_pasw(cls, psw):
        if type(psw) != str:
            raise TypeError('Ps can be str')

        s = psw.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Invalid format in passport')

        for p in s:
            if not p.isdigit():
                raise TypeError('Symbols on ps can be num')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):

        return self.__old

    @old.setter
    def old(self, old):
        self.varify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.varify_weight(weight)
        self.__weight = weight

    @property
    def psw(self):
        return self.__psw

    @psw.setter
    def psw(self, psw):
        self.varify_pasw(psw)
        self.__psw = psw


p = Person('Kulink Maksim Sergeevich', 30, '1234 465665', 90.0)
print(p.weight)
