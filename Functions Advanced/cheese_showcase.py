def sorting_cheeses(**kwargs):
    result = []
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for cheese, quantities in sorted_cheeses:
        result.append(cheese)
        for quantity in sorted(quantities, reverse=True):
            result.append(str(quantity))

    return "\n".join(result)


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
