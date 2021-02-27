
# 1 .Write a function that computes the volume of a sphere given its radius.
import math


def sphere_volume(radius):
    volume = 4/3*math.pi*pow(radius, 3)
    return volume


if __name__ == '__main__':
    print(sphere_volume(2))