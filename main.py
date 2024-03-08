"""
This script serves as a collection of helper functions throughout the tutorial series."""
import os

# function to convert cities to lwoercase
# open cities.txt
with open('cities.txt', 'r') as file:
    cities = file.read().split('\n')

for i in range(len(cities)):
    cities[i] = cities[i].lower()

with open('cities.txt', 'w') as file:
    file.write('\n'.join(cities))
