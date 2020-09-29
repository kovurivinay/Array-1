def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
    # Time: O(N)
    # Space: O(N)

    if not matrix:
        return []
    
    res=[]
    diagonal_dict=defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            diagonal_dict[i+j].append(matrix[i][j])
    
    for i in range(len(matrix)+len(matrix[0])-1):
        if i in diagonal_dict:
            if i%2==0:
                res+=diagonal_dict[i][::-1]
                continue
            res+=diagonal_dict[i]
    
    # print(diagonal_dict)
    return res