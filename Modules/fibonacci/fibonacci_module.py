def create_sequence(n: int) -> list:
    if n < 2:
        return n
    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq


def locate(n: int, sequence: list) -> int:
    if n in sequence:
        return sequence.index(n)
    else:
        print("Not found")
        return -1



