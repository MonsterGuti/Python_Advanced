children_ratings = list(map(int, input().split()))
n = len(children_ratings)
candies = [1] * n

for i in range(1, n):
    if children_ratings[i] > children_ratings[i - 1]:
        candies[i] = candies[i - 1] + 1

for i in range(n - 2, -1, -1):
    if children_ratings[i] > children_ratings[i + 1]:
        candies[i] = max(candies[i], candies[i + 1] + 1)

print(sum(candies))
