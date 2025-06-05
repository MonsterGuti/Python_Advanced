def grocery_store(**kwargs):
    sorted_result = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = ""
    for product_name, quantity in sorted_result:
        result += f"{product_name}: {quantity}\n"
    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
