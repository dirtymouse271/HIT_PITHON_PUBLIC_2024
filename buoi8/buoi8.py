class hinhChuNhat:
    def __init__(self,dai,rong):
        self.dai = dai
        self.rong = rong
    def Perimeter(self):
        return (self.dai + self.rong) * 2
    def Area(self):
        return self.dai * self.rong
    def display(self):
        print("Chieu dai: ", self.dai)
        print("Chieu rong: ", self.rong)
        print("Chu vi: ", self.Perimeter())
        print("Dien tich: ", self.Area())

hinhChuNhat1 = hinhChuNhat(9,3)
hinhChuNhat1.display()