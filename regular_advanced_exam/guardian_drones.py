from collections import deque

drones_to_assemble = {
    "Sentinel-X": 100,
    "Viper-MKII": 85,
    "Aegis-7": 75,
    "Striker-R": 65,
    "Titan-Core": 55
}

sorted_drones = dict(sorted(drones_to_assemble.items(), key=lambda x: x[1], reverse=True))
assembled_drones = []

mechanical_parts = [int(x) for x in input().split()]  # Stack
power_cells = deque(int(x) for x in input().split())  # Queue

while mechanical_parts and power_cells and len(assembled_drones) < len(drones_to_assemble):
    curr_mechanical_part = mechanical_parts.pop()
    curr_power_cell = power_cells.popleft()
    activation_power = curr_mechanical_part + curr_power_cell

    built = False
    for drone, needed_power in sorted_drones.items():
        if needed_power == activation_power and drone not in assembled_drones:
            assembled_drones.append(drone)
            built = True
            break

    if not built:
        for drone, needed_power in sorted_drones.items():
            if needed_power < activation_power and drone not in assembled_drones:
                assembled_drones.append(drone)
                new_energy = curr_power_cell - 30
                if new_energy > 0:
                    power_cells.append(new_energy)
                built = True
                break

    if not built:
        new_energy = curr_power_cell - 1
        if new_energy > 0:
            power_cells.append(new_energy)

if len(assembled_drones) == len(drones_to_assemble):
    print("Mission Accomplished! All Guardian Drones activated!")
else:
    print("Mission Failed! Some drones were not built.")

if assembled_drones:
    print(f"Assembled Drones: {', '.join(assembled_drones)}")

if mechanical_parts:
    print(f"Mechanical Parts: {', '.join(map(str, reversed(mechanical_parts)))}")

if power_cells:
    print(f"Power Cells: {', '.join(map(str, power_cells))}")
