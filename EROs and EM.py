#matlab function inputs

def rowswap(matrix, row1, row2):
    print(f"{matrix}([{row1},{row2}],:) = {matrix}([{row2},{row1}],:)")

def mult(matrix, row, k):
    print(f"{matrix}({row},:) = {k} * {matrix}({row},:)")

def addmult(matrix, row1, k, row2):
    print(f"{matrix}({row1},:) = {matrix}({row1},:) + {k} * {matrix}({row2},:)")

def em(size, command):
    '''
    RS R1 R2
    RM k R1
    AM R1 k R2
    '''
    # Initialize identity matrix
    matrix = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    # Split command into parts
    parts = command.split()

    # Row Swap (RS R1 R3)
    if parts[0] == "RS":
        r1, r2 = int(parts[1][1:]) - 1, int(parts[2][1:]) - 1
        matrix[r1], matrix[r2] = matrix[r2], matrix[r1]
    
    # Row Multiply (RM 3 R1)
    elif parts[0] == "RM":
        multiplier, r = int(parts[1]), int(parts[2][1:]) - 1
        matrix[r] = [multiplier * matrix[r][i] for i in range(size)]
    
    # Add Multiple of Row (AM R1 3 R2)
    elif parts[0] == "AM":
        r1, multiplier, r2 = int(parts[1][1:]) - 1, int(parts[2]), int(parts[3][1:]) - 1
        matrix[r1] = [matrix[r1][i] + multiplier * matrix[r2][i] for i in range(size)]
    
    # Convert matrix to MATLAB string format
    result = "[" + ";".join(" ".join(map(str, row)) for row in matrix) + "]"

    print(result)


