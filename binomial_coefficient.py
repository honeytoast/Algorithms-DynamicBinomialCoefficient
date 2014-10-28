import sys

def binomial_coefficient(n, k):
    table = [ [ None for j in range(k + 1) ] for i in range(n + 1) ]

    for i in range(n + 1):
        table[i][0] = 1

    for i in range(n + 1):
        for j in range(1, k + 1):
            if i == j:
                table[i][j] = 1
            elif j == 1 and i != 0:
                table[i][j] = i
            elif i < j:
                continue
            else:
                table[i][j] = table[i - 1][j - 1] + table[i - 1][j]
    return table[n][k]

def binomial_coefficient2(n, k):
        
    table = [ [ None for j in range(k + 1) ] for i in range(2) ]

    for i in range(2):
        table[i][0] = 1

    for i in range(n + 1):
        row = i % 2
        if row == 0:
            prev_row = 1
        else:
            prev_row = 0
        for j in range(1, k + 1):
            if j == i:
                table[row][j] = 1
            elif j == 1 and i != 0:
                table[row][j] = i
            elif i < j:
                continue
            else:
                table[row][j] = table[prev_row][j - 1] + table[prev_row][j]
    return table[row][k]

def main():
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    print(binomial_coefficient(n, k))
    print(binomial_coefficient2(n, k))

if __name__ == '__main__':
    main()
