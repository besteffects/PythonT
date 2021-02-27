import math

# 1. Write a function that computes the volume of a sphere given its radius.
def sphere_volume(radius):
    volume = 4/3*math.pi*pow(radius, 3)
    return volume

# 2. Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    return low <= num <= high

def ran_check1(num,low,high):
    if low <= num <= high:
        return (f"{num} is in the range between {low} and {high}")
    else:
        return ("{0} is outside of the range {1} and {2}".format(num, low, high))

if __name__ == '__main__':
    print(ran_check1(2, 5, 4))