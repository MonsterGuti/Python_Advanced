from collections import deque

defenders = deque(int(x) for x in input().split())
attackers = [int(x) for x in input().split()]
DEFENDERS_PER_ATTACKER = 7

while attackers and defenders:
    defender_group = defenders.popleft()
    attacker_group = attackers.pop()

    defender_capacity = defender_group // DEFENDERS_PER_ATTACKER

    if defender_capacity < attacker_group:
        remaining_attackers = attacker_group - defender_capacity
        attackers.append(remaining_attackers)
    elif defender_capacity == attacker_group:
        remaining_defenders = defender_group - attacker_group * DEFENDERS_PER_ATTACKER
        if remaining_defenders > 0:
            defenders.append(remaining_defenders)
    else:
        remaining_defenders = defender_group - attacker_group * DEFENDERS_PER_ATTACKER
        defenders.append(remaining_defenders)

print("The final battle is over!")
if not attackers and not defenders:
    print("But no one made it out alive!")
elif defenders:
    print(f"Bee groups left: {', '.join(map(str, defenders))}")
else:
    print(f"Bee-eater groups left: {', '.join(map(str, attackers))}")
