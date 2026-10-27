
roads = {}

n = int(input("Enter number of roads: "))

for i in range(n):
    road = input(f"Enter road {i + 1} name: ")
    capacity = int(input("Enter road capacity: "))
    roads[road] = {"capacity": capacity, "traffic": {}}

intervals = int(input("\nEnter number of time intervals: "))

for road in roads:
    print(f"\nEnter traffic details for {road}")

    for i in range(intervals):
        time = input("Enter time interval (e.g. 9 AM): ")
        vehicles = int(input("Enter vehicle count: "))

        if vehicles < 0:
            print("Invalid count! Enter again.")
            vehicles = int(input("Enter vehicle count: "))

        roads[road]["traffic"][time] = vehicles

print("\n===== TRAFFIC ANALYSIS REPORT =====")

for road, data in roads.items():
    traffic = data["traffic"]
    capacity = data["capacity"]

    peak_time = max(traffic, key=traffic.get)
    peak_count = traffic[peak_time]

    print(f"\nRoad: {road}")
    print(f"Peak Traffic: {peak_count} vehicles at {peak_time}")

    for time, vehicles in traffic.items():
        if vehicles > capacity:
            level = "Over Capacity"
        elif vehicles >= capacity * 0.8:
            level = "High Congestion"
        elif vehicles >= capacity * 0.5:
            level = "Moderate Congestion"
        else:
            level = "Low Congestion"

        print(f"{time}: {vehicles} vehicles - {level}")

    if peak_count > capacity:
        print("Warning: Road exceeds its capacity!")
    else:
        print("Road is within capacity.")
