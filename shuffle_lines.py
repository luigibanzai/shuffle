#!/usr/bin/python3

import sys
import random

if len(sys.argv) - 1 == 0:
    print("missing an argument.")
    exit(1)

with open(sys.argv[1], "r") as f:
    data = [v.rstrip() for v in f.readlines()]

random.shuffle(data)    

for i in range(len(data)):
    print("{}: {}".format(i+1, data[i]))
