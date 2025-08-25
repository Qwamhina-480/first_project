def calc_speed(distance, time):
    speed = distance/time
    return speed
abi_speed=calc_speed(2000,600)

def greetings(name):
    print("Hello", name)


greetings("Abi")

print(f"Abigail doesn't understand why {abi_speed} is her actual speed, meanwhile she even feels lazy to walk")


def area_circle(radius):
    area = 3.14*radius**2
    return area

area_of_circle = area_circle(4)

print(f"According to Abigail, the area of her 1 cedi coin was found to be {area_of_circle} squared meter")



num = int(input("Enter any number of your choice "))

def even_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
    
print(even_odd(num))