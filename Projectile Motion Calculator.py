import math
# Acceleration due to gravity (m/s^2)
g = 9.81


def calculate_projectile(u, theta_deg):
    # Convert angle to radians
    theta_rad = math.radians(theta_deg)

    # Range = (u^2 * sin(2*theta)) / g
    r = (u**2 * math.sin(2 * theta_rad)) / g

    # Max Height = (u^2 * sin^2(theta)) / 2g
    h = (u**2 * (math.sin(theta_rad)**2)) / (2 * g)

    # Time of Flight = (2 * u * sin(theta)) / g
    t = (2 * u * math.sin(theta_rad)) / g

    return r, h, t


print("--- Projectile Motion Simulator ---")
u = float(input("Enter initial velocity (m/s): "))
angle = float(input("Enter projection angle (degrees): "))

r, h, t = calculate_projectile(u, angle)

print(f"\nHorizontal Range: {r:.2f} m")
print(f"Maximum Height: {h:.2f} m")
print(f"Total Time of Flight: {t:.2f} s")

