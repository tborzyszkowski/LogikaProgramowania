

def hanoi(liczbaKrazkow, patykA, patykB, patykX):
    result = []
    if liczbaKrazkow > 0:
        result.extend(hanoi(liczbaKrazkow - 1, patykA, patykX, patykB))
        result.append("%s na %s" % (patykA, patykB))
        result.extend(hanoi(liczbaKrazkow - 1, patykX, patykB, patykA))
    return result


if __name__ == "__main__":
    for i in range(2, 30):
        print("%d : %d : %d" % (i, len(hanoi(i, "A", "B", "X")), 2**i-1))