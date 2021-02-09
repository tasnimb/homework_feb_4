from math import pi, tan, cos
g = 9.81
y0_height = 1
x_horizontal = 0.5
theta = 80 * (pi/180)
v0_initial = 44
y = y0_height +(x_horizontal * tan(theta)) - ((g*x_horizontal**2)/ (2*(v0_initial*cos(theta)**2)))
print("y is equal to ", y)