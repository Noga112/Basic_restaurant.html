print('==================')
print('Area Calculator 📐')
print('==================')

print('1. Triangle')
print('2. Rectangle')
print('3. Square')
print('4. Circle')
print('5. Quit')

choice = int(input("Which shape: "))

if choice == 1:
    base = int(input("Base: "))
    height = int(input("Height: "))

    result = (base*height)/2
    print("The area is "+ str(result))
elif choice == 2:
    base = int(input("Base: "))
    height = int(input("Height: "))

    result = base * height
    print("The area is "+ str(result))
elif choice == 3:
    base = int(input("Base: "))

    result = base **2
    print("The area is "+ str(result))
elif choice == 4:
    rad = int(input("Radius: "))

    result = 4*3.14*(rad)**2
    print("The area is "+ str(result))
elif choice == 5:
    print("OK! BYE-BYE!")
else:
    print("error")
