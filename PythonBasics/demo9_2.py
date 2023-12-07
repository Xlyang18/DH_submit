import math


class Triangle:
    def __init__(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c

    def calculate_area(self):
        # 计算半周长
        s = (self.side_a + self.side_b + self.side_c) / 2
        # 使用海伦公式计算面积
        area = math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
        return area


# 创建一个三角形对象并计算其面积
triangle = Triangle(3, 4, 5)
area = triangle.calculate_area()
print(f"三角形的面积为: {area}")
