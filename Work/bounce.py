# bounce.py
#
# Exercise 1.5
initial_height = 100
bounce = 3/5
bounces = 10

height = initial_height
for i in range(0, bounces):
    height = bounce * height
    print(height)

height = initial_height
for i in range(0, bounces):
    height = bounce * height
    print(round(height, 4))