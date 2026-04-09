# Tool to convert units and verify dimensional consistency
def convert_to_si(value, unit):
    conversions = {
        "km": 1000,    # km to m
        "cm": 0.01,    # cm to m
        "mm": 0.001,   # mm to m
        "hr": 3600,    # hr to sec
        "min": 60      # min to sec
    }
    return value * conversions.get(unit, 1)

print("--- Physics Unit Converter (SI) ---")
val = float(input("Enter value: "))
unit = input("Enter current unit (km, cm, mm, hr, min): ").lower()

si_val = convert_to_si(val, unit)
print(f"Standard SI Value: {si_val}")
