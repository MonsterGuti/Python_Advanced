def accommodate(*args, **kwargs):
    unaccommodated = 0
    result = ""
    sorted_rooms = sorted(kwargs.items(), key=lambda x: (x[1], x[0]))
    room_status = dict(sorted_rooms)
    accommodated_rooms = {}

    for group in args:
        is_accommodated = False
        for name in list(room_status.keys()):
            if group <= room_status[name]:
                room_number = name.split("_")[1] if "_" in name else name
                if room_number not in accommodated_rooms:
                    accommodated_rooms[room_number] = 0
                accommodated_rooms[room_number] = group
                del room_status[name]
                is_accommodated = True
                break
        if not is_accommodated:
            unaccommodated += group

    if accommodated_rooms:
        result += f"A total of {len(accommodated_rooms)} accommodations were completed!\n"
        sorted_accommodation_rooms = dict(sorted(accommodated_rooms.items(), key=lambda x: x[0]))
        for number, guests in sorted_accommodation_rooms.items():
            result += f"<Room {number} accommodates {guests} guests>\n"
    else:
        result += "No accommodations were completed!\n"

    if unaccommodated > 0:
        result += f"Guests with no accommodation: {unaccommodated}\n"

    if room_status:
        result += f"Empty rooms: {len(room_status)}"

    return result


print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))