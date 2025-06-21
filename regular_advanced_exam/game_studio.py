def sort_games(*args, **kwargs):
    console_games = {}
    pc_games = {}

    for game in args:
        for date, name in kwargs.items():
            if name == game[1]:
                if game[0] == "console":
                    console_games[date] = name
                    break
                elif game[0] == "pc":
                    pc_games[date] = name
                    break

    sorted_console_games = dict(sorted(console_games.items(), key=lambda x: x[0]))
    sorted_pc_games = dict(sorted(pc_games.items(), key=lambda x: x[0], reverse=True))

    result = ""
    if sorted_console_games:
        result += "Console Games:\n"
        for date, name in sorted_console_games.items():
            short_date = date[:-4]
            result += f">>>{short_date}: {name}\n"
    if sorted_pc_games:
        result += "PC Games:\n"
        for date, name in sorted_pc_games.items():
            short_date = date[:-4]
            result += f"<<<{short_date}: {name}\n"

    return result


print(sort_games(
    ("pc", "Iron Comet"),
    ("console", "Jungle Quest"),
    ("console", "Cyber Realm"),
    ("pc", "Neon Skyline"),
    ("console", "Blade Echo"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    July_01_2025_004="Cyber Realm",
    July_01_2025_002="Blade Echo",
    December_31_2024_007="Jungle Quest",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))
