import math

def calculate_resultant(f1, f2, theta_degrees):
    # Converting degrees to radians for math.cos
    theta_rad = math.radians(theta_degrees)
    
    # Using the formula: R = sqrt(A^2 + B^2 + 2AB cos(theta))
    resultant = math.sqrt(f1*2 + f2*2 + 2 * f1 * f2 * math.cos(theta_rad))
    
    # Calculating the angle (alpha) the resultant makes with f1
    # tan(alpha) = (B sin(theta)) / (A + B cos(theta))
    alpha_rad = math.atan2((f2 * math.sin(theta_rad)), (f1 + f2 * math.cos(theta_rad)))
    alpha_deg = math.degrees(alpha_rad)
    
    return resultant, alpha_deg

print("--- Class 11 Physics: Vector Resultant Calculator ---")
try:
    p = float(input("Enter magnitude of first vector (P): "))
    q = float(input("Enter magnitude of second vector (Q): "))
    angle = float(input("Enter angle between them in degrees: "))

    r, direction = calculate_resultant(p, q, angle)

    print(f"\nResultant Magnitude: {r:.2f}")
    print(f"Angle with respect to P: {direction:.2f}°")
except ValueError:
    print("Please enter valid numerical values.")
