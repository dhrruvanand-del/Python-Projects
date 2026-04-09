import math

# Universal Gravitational Constant
G_CONST = 6.674e-11 

def get_escape_velocity(mass, radius):
    # Formula: v = sqrt(2GM / R)
    v_esc = math.sqrt((2 * G_CONST * mass) / radius)
    return v_esc
# This was a pain to code. Anyways it's developed and verified by Zioles(Dhrruv)!
print("--- Planetary Escape Velocity Tool ---")
# Example: Earth Mass = 5.97e24, Radius = 6.37e6
m = float(input("Enter mass of the planet (kg): "))
r = float(input("Enter radius of the planet (m): "))

ve = get_escape_velocity(m, r)
print(f"The Escape Velocity is: {ve:.2f} m/s")
