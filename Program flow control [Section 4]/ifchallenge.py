name = input("Enter your name: ")
age = int(input("Enter your age: "))

if 18 <= age < 30:
    print("{} You can go to the holiday".format(name))
else:
    print("{}, you are not allow to go on vacations".format(name))
