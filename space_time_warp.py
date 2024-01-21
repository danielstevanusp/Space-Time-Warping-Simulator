import numpy as np
import matplotlib.pyplot as plt

# Function to calculate time dilation due to gravity
def time_dilation(gravity, height):
    c = 299792458  # Speed of light in a vacuum (meters per second)
    delta_phi = gravity * height / (c**2)
    return np.sqrt(1 - 2 * delta_phi)

# Simulation parameters
gravity_strength = 9.8  # gravitational acceleration on the Earth's surface (m/s^2)
heights = np.linspace(0, 1000, 100)  # Heights in meters

# Calculating time dilation for each height
time_dilations = time_dilation(gravity_strength, heights)

# Visualization of the results
plt.plot(heights, time_dilations)
plt.title('Time Dilation Due to Gravity')
plt.xlabel('Height (meters)')
plt.ylabel('Time Dilation')
plt.show()
