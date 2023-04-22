import numpy as np
import matplotlib.pyplot as plt
# Define the x and y values for the points
x = np.array([635, 9617, 21221, 33939, 58658, 76144])
y = np.array([21538, 20441, 21294, 18449, 26008, 20603])

# Find the coefficients of the polynomial function of degree 6
coeffs = np.polyfit(x, y, 6)

# Print the polynomial function
print(f"The polynomial function is: {coeffs[0]:.2f}x^6 + {coeffs[1]:.2f}x^5 + {coeffs[2]:.2f}x^4 + {coeffs[3]:.2f}x^3 + {coeffs[4]:.2f}x^2 + {coeffs[5]:.2f}x + {coeffs[6]:.2f}")