import numpy as np

# implementation of matrix multiplication by divide and conquer algorithm
def divide_n_conquer_multiply(A, B):
    
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    split = n//2

    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        # spliting A and B into 4 submatrices using list comprehension
        A1 = [row[:split] for row in A[:split]]
        A2 = [row[split:] for row in A[:split]]
        A3 = [row[:split] for row in A[split:]]
        A4 = [row[split:] for row in A[split:]]
        
        B1 = [row[:split] for row in B[:split]]
        B2 = [row[split:] for row in B[:split]]
        B3 = [row[:split] for row in B[split:]]
        B4 = [row[split:] for row in B[split:]]
        
        # recursively computing the products of submatrices
        C1 = add_to_C (divide_n_conquer_multiply(A1, B1), divide_n_conquer_multiply(A2, B3))
        C2 = add_to_C (divide_n_conquer_multiply(A1, B2), divide_n_conquer_multiply(A2, B4))
        C3 = add_to_C (divide_n_conquer_multiply(A3, B1), divide_n_conquer_multiply(A4, B3))
        C4 = add_to_C (divide_n_conquer_multiply(A3, B2), divide_n_conquer_multiply(A4, B4))
        
        # re-combining all submatrices to C matrix
        for i in range(split):
            for j in range(split):
                C[i][j] = C1[i][j]
                C[i][j+split] = C2[i][j]
                C[i+split][j] = C3[i][j]
                C[i+split][j+split] = C4[i][j]
    return C

def add_to_C(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C



# implementation of matrix multiplication by divide and strassen algorithm
def strassen(A, B):
    n = len(A)
    split = n//2
    
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    # divide matrices into submatrices
    A11 = [row[:split] for row in A[:split]]
    A12 = [row[split:] for row in A[:split]]
    A21 = [row[:split] for row in A[split:]]
    A22 = [row[split:] for row in A[split:]]
    
    B11 = [row[:split] for row in B[:split]]
    B12 = [row[split:] for row in B[:split]]
    B21 = [row[:split] for row in B[split:]]
    B22 = [row[split:] for row in B[split:]]
    
    # recursively compute values for the submatrices
    P1 = strassen(A11, sub(B12, B22))
    P2 = strassen(add(A11, A12), B22)
    P3 = strassen(add(A21, A22), B11)
    P4 = strassen(A22, sub(B21, B11))
    P5 = strassen(add(A11, A22), add(B11, B22))
    P6 = strassen(sub(A12, A22), add(B21, B22))
    P7 = strassen(sub(A11, A21), add(B11, B12))
    
    # combine the computed values 
    C11 = add(sub(add(P5, P4), P2), P6)
    C12 = add(P1, P2)
    C21 = add(P3, P4)
    C22 = sub(sub(add(P5, P1), P3), P7)
    
    # combine submatrices to get the final matrix
    C = [[0] * n for i in range(n)]
    for i in range(split):
        for j in range(split):
            C[i][j] = C11[i][j]
            C[i][j+split] = C12[i][j]
            C[i+split][j] = C21[i][j]
            C[i+split][j+split] = C22[i][j]
            
    return C

# function to add 2 matrices
def add(A, B):
    n = len(A)
    C = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C


# function to subtract 2 matrices
def sub(A, B):
    n = len(A)
    C = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C



# main function
if __name__ == "__main__":
    print("\n---------------------------------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------------------------------\n")
    print("This algorithm works only for 2 power n square matrices\n")
    n = int(input("Enter the size of matrices A and B : "))

    if n%2 == 0:
        A = np.zeros((n,n), dtype=int)
        B = np.zeros((n,n), dtype=int)

        print("\n")

        for i in range(n):
            for j in range(n):
                inp = int(input(f"Enter [{i}][{j}] th element of matrix A : "))
                A[i][j] = inp

        print("\n")

        for i in range(n):
            for j in range(n):
                inp = int(input(f"Enter [{i}][{j}] th element of matrix B : "))
                B[i][j] = inp
        
        print(f"\nMatrix A : {A}")
        print(f"\nMatrix B : {B}")

        C1 = divide_n_conquer_multiply(A, B)
        print("\nThe resulatant matrix is by conquer algorithm : ")
        print(C1)

        print("\n")

        C2 = divide_n_conquer_multiply(A, B)
        print("\nThe resulatant matrix is by strassen algorithm : ")
        print(C2)

    else:
        print("\nMatrices cannot be multiplied")

    print("\n---------------------------------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------------------------------\n")

