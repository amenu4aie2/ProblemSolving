class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter=0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if(grid[row][col]==1):
                    # up

                    if(row-1>=0):
                        if( grid[row-1][col]==1):
                            pass
                        else:
                            perimeter+=1
                    else:
                        perimeter+=1
                    
                    # down 
                    if(row+1 < len(grid)):
                        if(grid[row+1][col]==1):
                            pass
                        else:
                            perimeter+=1
                    else:
                        perimeter+=1
                    # left
                    if(col-1>=0):
                        if(grid[row][col-1]==1):
                            pass
                        else:
                            perimeter+=1
                    else:
                        perimeter+=1
                    
                    # right
                    if(col+1 <len(grid[row])):
                        if(grid[row][col+1]==1):
                            pass
                        else:
                            perimeter+=1
                    else:
                        perimeter+=1
        return perimeter

                    