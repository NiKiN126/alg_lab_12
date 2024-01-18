def main():
    str1 = "editing"
    str2 = "distance"
    result = edit_dist(str1, str2)

    for item in result[1]:
        print(f"{item[0]}   {item[1]}")

def edit_dist(a, b):
    matrix = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    def edit_dist_td(i, j):
        nonlocal matrix
        if matrix[i][j] == 0:
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            else:
                ins = edit_dist_td(i, j - 1) + 1
                delete = edit_dist_td(i - 1, j) + 1
                sub = edit_dist_td(i - 1, j - 1) + (0 if a[i - 1] == b[j - 1] else 1)
                matrix[i][j] = min(ins, delete, sub)
        return matrix[i][j]

    def edit_dist_bu():
        nonlocal matrix
        for i in range(len(a) + 1):
            matrix[i][0] = i
        for j in range(1, len(b) + 1):
            matrix[0][j] = j
        for i in range(1, len(a) + 1):
            for j in range(1, len(b) + 1):
                c = 0 if a[i - 1] == b[j - 1] else 1
                matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + c)

    def restore():
        result = []
        i, j = len(a), len(b)
        while i != 0 or j != 0:
            if i != 0 and matrix[i][j] == matrix[i - 1][j] + 1:
                result.append((a[i - 1], '-'))
                i -= 1
            elif j != 0 and matrix[i][j] == matrix[i][j - 1] + 1:
                result.append(('-', b[j - 1]))
                j -= 1
            elif matrix[i][j] == matrix[i - 1][j - 1] + (0 if a[i - 1] == b[j - 1] else 1):
                result.append((a[i - 1], b[j - 1]))
                i -= 1
                j -= 1
        result.reverse()
        return result

    edit_dist_td(len(a), len(b))
    edit_dist_bu()
    solution = restore()

    return (matrix[len(a)][len(b)], solution)

if __name__ == "__main__":
    main()