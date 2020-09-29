def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Time Complexity: O(M*N)
        # Space: O(1)

        if not matrix:
            return []
        
        rS = 0
        rE = len(matrix)-1
        cS = 0
        cE = len(matrix[0])-1
        res=[]
        while(rS<=rE and cS<=cE):
            
            for i in range(cS,cE+1):
                res.append(matrix[rS][i])
            rS+=1
            
            for i in range(rS,rE+1):
                res.append(matrix[i][cE])
            cE-=1
            
            if(rS<=rE):
                for i in range(cE,cS-1,-1):
                    res.append(matrix[rE][i])
                rE-=1
            
            if(cS<=cE):
                for i in range(rE,rS-1,-1):
                    res.append(matrix[i][cS])
                cS+=1
        
        return res