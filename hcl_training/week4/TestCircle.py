from circle import circle

# Main method used for testing the functionality of the circle class
def main():
        circle1 = circle()
        circle2 = circle(2.5)
        circle3 = circle(color = "Green")
        circle4 = circle(3.5, "Yellow")
        print("Circle No.\tRadius\t\tColor\tArea",\
        "\n1.\t\t{:.2f} units\t{:s}\t{:.2f}sq. units".\
        format(circle1.getRadius(), circle1.getColor(), circle1.getArea()), \
        "\n2.\t\t{:.2f} units\t{:s}\t{:.2f}sq. units".\
        format(circle2.getRadius(), circle2.getColor(), circle2.getArea()), \
        "\n3.\t\t{:.2f} units\t{:s}\t{:.2f}sq. units".\
        format(circle3.getRadius(), circle3.getColor(), circle3.getArea()), \
        "\n4.\t\t{:.2f} units\t{:s}\t{:.2f}sq. units".\
        format(circle4.getRadius(), circle4.getColor(), circle4.getArea()), \
        )

if __name__ == "__main__" :
        main()