#Calculates the volume of a cylinder
#args: radius and height

import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of a cylinder')
parser.add_argument('radius', type=int, help='Radius of cylinder')
parser.add_argument('height', type=int, help='Height of cylinder')
args = parser.parse_args()

def cylinder_volume(radius, height):
    vol = (math.pi) * (radius ** 2) * (height)
    return vol
if __name__ == '__main__':
    print(cylinder_volume(args.radius, args.height))
