import math
#Developed and verfied by Zioles(Dhrruv)

def calculate_resultant():
    print("--- Vector Resultant Tool ---")
    try:
        p = float(input("Enter magnitude of P: "))
        q = float(input("Enter magnitude of Q: "))
        angle = float(input("Enter angle (degrees): "))
        # Math part
        rad = math.radians(angle)
        r = math.sqrt(p**2 + q**2 + 2 * p * q * math.cos(rad))
        print(f"The Resultant is: {r:.2f}")
    except ValueError:
        print("Error: Please enter numbers only!")


if __name__ == "__main__":
    calculate_resultant()
    
