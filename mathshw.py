import math

angle_degrees = int(input("Enter angle in degrees: "))

angle_radians = math.radians(angle_degrees)

sine_value = math.sin(angle_radians)
cosine_value = math.cos(angle_radians)
tangent_value = math.tan(angle_radians)

print(f"Sine of {angle_degrees}°: {sine_value}")
print(f"Cosine of {angle_degrees}°: {cosine_value}")
print(f"Tangent of {angle_degrees}°: {tangent_value}")
