
# Integrated Manufacturing Production Planner

materials = {
    "Steel": {"available": 500, "required_per_unit": 2},
    "Plastic": {"available": 300, "required_per_unit": 1}
}

order_demand = 200
production_quantity = 200
defect_count = 12
max_defect_percentage = 5

print("MANUFACTURING PRODUCTION PLANNER")
print("-" * 40)

feasible = True

# Check raw material availability
for material, data in materials.items():
    required = production_quantity * data["required_per_unit"]
    shortage = max(0, required - data["available"])

    print(f"\nMaterial: {material}")
    print("Available:", data["available"])
    print("Required:", required)
    print("Shortage:", shortage)

    if shortage > 0:
        feasible = False
        print("Status: Material shortage")
    else:
        print("Status: Sufficient material")

# Check production feasibility
print("\nOrder Demand:", order_demand)
print("Planned Production:", production_quantity)

if production_quantity >= order_demand and feasible:
    print("Production Feasibility: Feasible")
else:
    print("Production Feasibility: Not Feasible")

# Check quality
defect_percentage = (defect_count / production_quantity) * 100

print("\nDefect Count:", defect_count)
print("Defect Percentage:", round(defect_percentage, 2), "%")
print("Maximum Allowed Defects:", max_defect_percentage, "%")

if defect_percentage > max_defect_percentage:
    print("Quality Status: Quality Violation")
else:
    print("Quality Status: Acceptable")
