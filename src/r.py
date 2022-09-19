def reverse_borders(x):

    if len(x) == 0:
        return []

    length = len(x)
    r = [0]*length
    for i in range(1, length):
        b = r[-i]
        while b > 0 and x[-(i+1)] != x[-(b+1)]:
            b = r[-b]
        if x[-(i+1)] == x[-(b+1)]:
            r[-(i+1)] = b+1
        else:
            r[-(i+1)] = 0

    return r

def border_array(x):

    if len(x) == 0:
        return []

    else:
        ba = [0]
        for i in range(len(x)-1):
            b = ba[i]
            while b > 0 and x[i+1] != x[b]:
                b = ba[b-1]
            if x[i+1] == x[b]:
                ba.append(b+1)
            else:
                ba.append(0)
        return ba

def main():
    st = "abaabaa"
    print(reverse_borders(st))
    rev = st[::-1]
    print(border_array(rev))


if __name__ == '__main__':
    main()