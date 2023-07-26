def square_matrix_simple(matrix=[]):
    # create a new matrix with the same size as the input matrix
    # initialize it as an empty list
    result_matrix = []
    
    # iterate through each row in the matrix
    for row in matrix:
        # create a new row for the new matrix
        new_row = []
        
        #iterate through each element in the row
        for element in row:
            # square the new element and append it in the new row
            new_row.append(element ** 2)
            
        # append the new row to the result matrix
        result_matrix.append(new_row)
    #return result
    return result_matrix
        