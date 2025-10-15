for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] <= 120:
            involved_elements.add(arr[i])
            involved_elements.add(arr[j])

product = 1
for num in involved_elements:
    product *= num

print(product)