# A quick tool I wrote to verify my Physics homework answers
def solve_kinematics(u, a, t):
    v = u + (a * t)
    s = (u * t) + (0.5 * a * (t**2))
    return v, s


print("--- Kinematics Solver (v = u+at) ---")
u = float(input("Initial velocity (u): "))
a = float(input("Acceleration (a): "))
t = float(input("Time (t): "))

v, s = solve_kinematics(u, a, t)
print(f"Final Velocity (v): {v}")
print(f"Displacement (s): {s}")
