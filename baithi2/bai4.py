class tamThucBacHai:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __str__ (self):
        print(self.a,"x2 +",self.b,"x +",self.c)
    def cong(self, a1, b1, c1):
        self.a += a1
        self.b += b1
        self.c += c1
        return self.a, self.b, self.c
    def tru(self, a1, b1, c1):
        self.a -= a1
        self.b -= b1
        self.c -= c1
        return self.a, self.b, self.c
tamThuc1 = tamThucBacHai(2, 4, 1)
tamThuc2 = tamThucBacHai(1, 2, 3)
tamThuc1.a*=-1
tamThuc1.b*=-1
tamThuc1.c*=-1
tamThuc2.a*=-1
tamThuc2.b*=-1
tamThuc2.c*=-1
tamThuc1.cong(tamThuc2.a, tamThuc2.b, tamThuc2.c)
tamThuc1.tru(tamThuc2.a, tamThuc2.b, tamThuc2.c)