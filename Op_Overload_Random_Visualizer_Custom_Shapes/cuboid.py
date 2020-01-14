# Create class
class Cuboid:
    # Create constructor
    def __init__(self):
        self.area = None
        self.arithmeticArea = None
        self.area3 = None
        self.surfaceArea = None
        self.cuboidDetails = None


    # Create methods to set the area and get the area (width * height* length
    def setCuboidArea(self, length, width, height):
        self.area = (length * width * height)
    def getCuboidArea(self):
        return self.area

    # Create method to set the surface area and get the area 2(length * width) + 2(length * height) + 2(height * width)
    def setSurfaceArea(self, length, width, height):
        self.surfaceArea = (2 * (length * width) + 2 * (length * height) + 2 * (height * width))
    def getSurfaceArea(self):
        return self.surfaceArea

    #Create setters and getters for the width length and height for the cuboids
    def setCuboidDetails(self, length, width, height):
        self.cuboidDetails = str(length) + "," + str(width) + "," + str(height)
    def getCuboidDetails(self):
        return self.cuboidDetails

    # Create method to calculate new object based on plus and minus
        # Rubric says that these operators need to return a new object and thus need length width and height parameters
    def setCuboid3Area(self):
        #The lengths of the object can be found by calculating the cube root of the area and setting it to each of the sides
        sides = (self.arithmeticArea**(1/3))
        self.area3 = (sides * 3)
        return self.area3

    # Redefine arithmetic operators to be applicable to the area of a cuboid
    def __add__(self, other):
        self.arithmeticArea = (self.getCuboidArea() + other.getCuboidArea())
        return self.arithmeticArea
    def __sub__(self, other):
        self.arithmeticArea = (self.getCuboidArea() - other.getCuboidArea())
        return self.setCuboid3Area()
    def __gt__(self, other):
        if self.getCuboidArea() > other.getCuboidArea():
            return True
        else:
            return False
    def __lt__(self, other):
        if self.getCuboidArea() < other.getCuboidArea():
            return True
        else:
            return False
    def __eq__(self, other):
        if self.getCuboidArea() == other.getCuboidArea():
            return True
        else:
            return False

    # Use the surface area of the cuboid to calculate the result of len()
    # NEED TO FIGURE OUT HOW TO USE THE OBJECT SPECIFICALLY
    def __len__(self):
            return (self.getSurfaceArea())

    # For str() return a string that displays the side lengths, volume, and surface area
    # NEED TO FIGURE OUT HOW TO USE THE OBJECT SPECIFICALLY
    def __str__(self):
        message = "Cuboid Details:\nLength, width, and height: " + str(self.getCuboidDetails())
        message += "\nVolume and surface area: "+str(self.getCuboidArea())+","+str(self.getSurfaceArea())+"\n"
        return message



# # Create class
# class Cuboid:
#     # Create constructor
#     def __init__(self):
#         self.area1 = None
#         self.area2 = None
#         self.arithmeticArea = None
#         self.area3 = None
#         self.surfaceArea1 = None
#         self.surfaceArea2 = None
#         self.cuboid1Details = None
#         self.cuboid2Details = None
#
#
#     # Create methods to set the area and get the area (width * height* length
#     def setCuboidArea1(self, length1, width1, height1):
#         self.area1 = (length1 * width1 * height1)
#     def getCuboidArea1(self):
#         return self.area1
#     def setCuboidArea2(self, length2, width2, height2):
#         self.area2 = (length2 * width2 * height2)
#     def getCuboidArea2(self):
#         return self.area2
#
#     # Create method to set the surface area and get the area 2(length * width) + 2(length * height) + 2(height * width)
#     def setSurfaceArea1(self, length1, width1, height1):
#         self.surfaceArea1 = (2 * (length1 * width1) + 2 * (length1 * height1) + 2 * (height1 * width1))
#     def getSurfaceArea1(self):
#         return self.surfaceArea1
#     def setSurfaceArea2(self, length2, width2, height2):
#         self.surfaceArea2 = (2 * (length2 * width2) + 2 * (length2 * height2) + 2 * (height2 * width2))
#     def getSurfaceArea2(self):
#         return self.surfaceArea2
#
#     #Create setters and getters for the width length and height for the cuboids
#     def setCuboid1Details(self, length1, width1, height1):
#         self.cuboid1Details = str(length1 + "," + width1 + "," + height1)
#     def getCuboid1Details(self):
#         return self.cuboid1Details
#     def setCuboid2Details(self, length2, width2, height2):
#         self.cuboid2Details = str(length2 + "," + width2 + "," + height2)
#     def getCuboid2Details(self):
#         return self.cuboid2Details
#
#     # Create method to calculate new object based on plus and minus
#         # Rubric says that these operators need to return a new object and thus need length width and height parameters
#     def setCuboid3Area(self):
#         #The lengths of the object can be found by calculating the cube root of the area and setting it to each of the sides
#         length3, width3, height3 = (self.arithmeticArea**(1/3))
#         self.area3 = (length3 * width3 * height3)
#
#     # Redefine arithmetic operators to be applicable to the area of a cuboid
#     def __add__(self, other):
#         self.arithmeticArea = (self.getCuboidArea1() + other.getCuboidArea2())
#         return self.setCuboid3Area()
#     def __sub__(self, other):
#         self.arithmeticArea = (self.getCuboidArea1() - other.getCuboidArea2())
#         return self.setCuboid3Area()
#     def __gt__(self, other):
#         if self.getCuboidArea1() > other.getCuboidArea2():
#             return "Cuboid 1 is larger"
#         else:
#             return "Cuboid 2 is larger"
#     def __lt__(self, other):
#         if self.getCuboidArea1() < other.getCuboidArea2():
#             return "Cuboid 1 is smaller"
#         else:
#             return "Cuboid 2 is smaller"
#     def __eq__(self, other):
#         if self.getCuboidArea1() == other.getCuboidArea2():
#             return "Cuboid 1 is the same size as Cuboid 2"
#         else:
#             return "Cuboid 1 is not the same size as Cuboid 2"
#
#     # Use the surface area of the cuboid to calculate the result of len()
#     # NEED TO FIGURE OUT HOW TO USE THE OBJECT SPECIFICALLY
#     def __len__(self):
#         return (self.getSurfaceArea1())
#
#     # For str() return a string that displays the side lengths, volume, and surface area
#     # NEED TO FIGURE OUT HOW TO USE THE OBJECT SPECIFICALLY
#     def __str__(self):
#         display1LWH = "Cuboid 1:\nLength, width, and height: "+self.getCuboid1Details()
#         display1VSA = "\nVolume and surface area: "+str(self.getCuboidArea1())+","+str(self.getSurfaceArea1())+"\n"
#         return print(display1LWH, display1VSA)
#
#


