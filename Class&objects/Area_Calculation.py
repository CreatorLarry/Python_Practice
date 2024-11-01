# cylinder
# Calculating surface area
# Overall class
class Cylinder:
    def __init__(self,radius,height, color):
        self.r = radius
        self.h = height
        self.rangi = color

    # conditions if closed or not
    def calc_area(self, is_closed = True):
        if is_closed == True:
            area = 2 * 22/7 * self.r ** 2 + 2 * 22/7 * self.r * self.h
            print(f"Area of closed cylinder is: {area}")

        else:
            area = 22/7 * self.r ** 2 + 2 * 22/7 * self.r * self.h
            print(f"Area of open cylinder is: {area}")


    def calc_volume(self):
        v = 22/7 * self.r ** 2 * self.h
        print(f"Volume of cylinder is: {v}")

# Enter values for our various cylinders
c1 = Cylinder(10, 20, "Red")
c2 = Cylinder(12.67, 15.56, "Green")

# Calling the calculation
c1.calc_volume()
# For true meaning it's closed
c2.calc_area()
# For false meaning it's "open"
c2.calc_area(False)