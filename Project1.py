def temperature():
            tempF = float(input("Enter the temperature in Fahrenheit: "))
            print(f"The temperature in celcius is {(tempF - 32) * 5//9}")
            return tempF

def weight():
    lbs = float(input("Enter the weight in lbs: "))
    print(f"The weight in kg is {lbs * .454} ")
    return lbs

def distance():
    miles = float(input("Enter the distance in Miles: "))
    print(f"The distance in Kilometers is {miles * 1.6}")
    return miles

x = float(input("1) Temperature 2) Weight 3) Distance: 0) Quit: "))
while x != "0":
    if x == "1":
        temperature()
    elif x == "2":
          weight()
    elif x == "3":
          distance()





