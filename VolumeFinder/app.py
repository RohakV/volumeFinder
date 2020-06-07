print("Welcome to volume finder!")
y_or_n = input("Do you want to start (Y/N)? : ")
y = False

if y_or_n.lower() == 'y':
    print("You said yes!")
    y = True
elif y_or_n.lower() == 'n':
    print("Bye Bye Then!")
    quit()
else:
    print("You wrote something wrong!")

def cylinder(r, h):
    answer = 3.14*r*r*h
    print(f"The volume is : {answer}")
    print(f"Thanks for using our product. Review it at www.github.com")

def cube(s):
    answer = s*s*s
    print(f"The volume is : {answer}")
    print(f"Thanks for using our product. Review it at www.github.com")


def cuboid(w, l, h):
    answer = w*l*h
    print(f"The volume is : {answer}")
    print(f"Thanks for using our product. Review it at www.github.com")


if y == True:
    category = input("Do you want to find the volume of a cylinder, cube or a cuboid. (1, 2, 3)")
    if category == '1':
        radius = int(input("Enter the radius : "))
        height = int(input("Enter the cylinder's height : "))
        cylinder(radius, height)
    elif category == '2':
        side = int(input("Enter the side's length : "))
        cube(side)
    elif category == '3':
        width = int(input("Enter the width : "))
        length = int(input("Enter the length : "))
        height = int(input("Enter the height : "))

