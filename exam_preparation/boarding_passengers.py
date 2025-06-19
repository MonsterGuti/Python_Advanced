def boarding_passengers(capacity, *args):
    groups_info = {}
    boarding_message = ""

    all_boarded = True

    for group in args:
        num_passengers, benefit = group
        if capacity == 0:
            all_boarded = False
            break
        if num_passengers <= capacity:
            capacity -= num_passengers
            if benefit not in groups_info:
                groups_info[benefit] = 0
            groups_info[benefit] += num_passengers
        else:
            all_boarded = False
            continue

    sorted_boarded = sorted(groups_info.items(), key=lambda x: (-x[1], x[0]))
    for benefit, guests in sorted_boarded:
        boarding_message += f"## {benefit}: {guests} guests\n"

    if all_boarded:
        output_message = "All passengers are successfully boarded!"
    else:
        if capacity == 0:
            output_message = "Boarding unsuccessful. Cruise ship at full capacity."
        else:
            output_message = f"Partial boarding completed. Available capacity: {capacity}."

    return f"Boarding details by benefit plan:\n{boarding_message}{output_message}"


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
