# Import file
from cuboid import Cuboid

# Create main function
def main():
    # Tell user what the code does
    print("This program compares two cuboids")

    # Ask for input for first input and run class for the object
    length, width, height = eval(input("Enter the length, width, and height for the first cuboid: "))
    cuboid1 = Cuboid()
    cuboid1.setCuboidArea(length, width, height)
    cuboid1.setSurfaceArea(length, width, height)
    cuboid1.setCuboidDetails(length, width, height)

    #Ask for input for the seconf input and run class for the object
    length, width, height = eval(input("Enter the length, width, and height for the second cuboid: "))
    cuboid2 = Cuboid()
    cuboid2.setCuboidArea(length, width, height)
    cuboid2.setSurfaceArea(length, width, height)
    cuboid2.setCuboidDetails(length, width, height)

    # Preform arithmetic operations to see comparisons
    print("cube1 plus cube2 = " + str(cuboid1 + cuboid2))
    print("cube1 minus cube2 = " + str(cuboid1 - cuboid2))
    print("cube1 greater than cube2?: " + str(cuboid1 > cuboid2))
    print("cube1 less than cube2?: " + str(cuboid1 < cuboid2))
    print("cube1 equal to cube2?: " + str(cuboid1 == cuboid2))
    print("Surface Area cube1: " + str(len(cuboid1)))
    print("Surface Area cube2: " + str(len(cuboid2)))
    print("\n String cuboid 1: \n" + str(cuboid1))
    print("\n String cuboid 2: \n" + str(cuboid2))

main()