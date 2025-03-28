x = float(input("1)Temperature 2)Weight 3)Distance: 0)Quit: "))
while x != 0:
        if x == 1:
            tempF = float(input("Enter the temperature in Fahrenheit: "))
            print(f"The temperature in celcius is {(tempF - 32) * 5//9}")
            x = (input("1)Temperature 2)Weight 3)Distance: 0)Quit: "))
        elif x == 2:
            lbs = float(input("Enter the weight in lbs: "))
            print(f"The weight in kg is {lbs * .454} ")
            x = (input("1)Temperature 2)Weight 3)Distance: 0)Quit: "))
        elif x == 3:
            miles = float(input("Enter the distance in Miles: "))
            print(f"The distance in Kilometers is {miles * 1.6}")
            x = (input("1)Temperature 2)Weight 3)Distance: 0)Quit: "))
print("Have a nice day!")





