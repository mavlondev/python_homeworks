# Task 1. Write a Python function that converts a temperature from Fahrenheit to Celsius. Use `numpy.vectorize` to apply this function to an array of temperatures: `[32, 68, 100, 212, 77]`. 
#    - Formula: $C = (F - 32) \times \frac{5}{9}$

# ---

# Task 2. Create a custom function that takes two arguments: a number and a power. Use `numpy.vectorize` to calculate the power for each pair of numbers in two arrays: `[2, 3, 4, 5]` and `[1, 2, 3, 4]`.

# ---

# Task 3. Solve the system of equations using `numpy`:

# $$
# \begin{cases}
# 4x + 5y + 6z = 7 \\
# 3x - y + z = 4 \\
# 2x + y - 2z = 5
# \end{cases}
# $$

# ---

# Task 4. Given the electrical circuit equations below, solve for $I_1, I_2, I_3$ (currents in the branches):

# $$
# \begin{cases}
# 10I_1 - 2I_2 + 3I_3 = 12 \\
# -2I_1 + 8I_2 - I_3 = -5 \\
# 3I_1 - I_2 + 6I_3 = 15
# \end{cases}
# $$

# ---


# **Image Manipulation with NumPy and PIL**

# Image file: `images/birds.jpg`. Your task is to perform the following image manipulations using the **NumPy** library while leveraging **PIL** for reading and saving the image.

# **Instructions:**

# 1. **Flip the Image**:
#    - Flip the image horizontally and vertically (left-to-right and up-to-down).

# 2. **Add Random Noise**:
#    - Add random noise to the image.

# 3. **Brighten Channels**:
#    - Increase the brightness of the channels (r.g. red channel) by a fixed value (e.g., 40). Clip the values to ensure they stay within the 0 to 255 range.

# 4. **Apply a Mask**:
#    - Mask a rectangular region in the image (e.g., a 100x100 area in the center) by setting all pixel values in this region to black (0, 0, 0).

# **Requirements:**
# - Use the **PIL** module onyl to:
#   - Read the image.
#   - Convert numpy array to image.
#   - Save the modified image back to a file.
# - Perform all manipulations using NumPy functions. Avoid using image editing functions from PIL or other libraries.


# **Bonus Challenge**:
# - Create a function for each manipulation (e.g., `flip_image`, `add_noise`, `brighten_channels`, `apply_mask`) to promote modularity and reusability of code.

# ---

import numpy as np
from PIL import Image

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)
# Task 1
temperatures_f = np.array([32, 68, 100, 212, 77])  # Array of temperatures in Fahrenheit
temperatures_c = np.vectorize(fahrenheit_to_celsius)(temperatures_f)  # Convert to Celsius

def power(base, exponent):
    return base ** exponent
# Task 2
bases = np.array([2, 3, 4, 5])  # Array
exponents = np.array([1, 2, 3, 4])  # Array
results = np.vectorize(power)(bases, exponents)  # Calculate power for each pair
# Task 3
A = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])  # Coefficient matrix
B = np.array([7, 4, 5])  # Constants
solution = np.linalg.solve(A, B)  # Solve the system of equations
# Task 4
A_circuit = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])  # Coefficient matrix for circuit
B_circuit = np.array([12, -5, 15])  # Constants for circuit
currents = np.linalg.solve(A_circuit, B_circuit)  # Solve for currents
# Image Manipulation
def flip_image(image_array):
    return np.flip(image_array, axis=(0, 1))  # Flip horizontally and vertically
def add_noise(image_array, noise_level=30):
    noise = np.random.randint(-noise_level, noise_level + 1, image_array.shape)  # Generate random noise
    noisy_image = image_array + noise  # Add noise to the image
    return np.clip(noisy_image, 0, 255)  # Clip values to stay within valid range
def brighten_channels(image_array, brightness_increase=40):
    brightened_image = image_array + brightness_increase  # Increase brightness
    return np.clip(brightened_image, 0, 255)  # Clip values to stay within valid range
def apply_mask(image_array, mask_size=(100, 100)):
    height, width, _ = image_array.shape
    center_y, center_x = height // 2, width // 2
    mask_half_height, mask_half_width = mask_size[0] // 2, mask_size[1] // 2
    image_array[center_y - mask_half_height:center_y + mask_half_height,
                center_x - mask_half_width:center_x + mask_half_width] = [0, 0, 0]  # Set masked region to black
    return image_array
# Load the image
image = Image.open('images/birds.jpg')
image_array = np.array(image)  # Convert image to NumPy array
# Perform manipulations
flipped_image = flip_image(image_array)  # Flip the image
noisy_image = add_noise(image_array)  # Add random noise
brightened_image = brighten_channels(image_array)  # Brighten channels
masked_image = apply_mask(image_array)  # Apply mask
# Save the modified images
Image.fromarray(flipped_image).save('images/birds_flipped.jpg')  # Save flipped image
Image.fromarray(noisy_image).save('images/birds_noisy.jpg')  # Save
Image.fromarray(brightened_image).save('images/birds_brightened.jpg')  # Save brightened image
Image.fromarray(masked_image).save('images/birds_masked.jpg')  # Save masked image
