def totalNQueens(n):
        # backtracking function 
        def backtrack(row, diagonals, anti_diagonals, cols):
            # The Base Case - N queens have already been placed 
            # We need all the queens to be placed to increment the count of possible board orientations 
            if row == n:
                return 1
            
            solutions = 0
            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col

                # if the queen is not placeable 
                if (col in cols or curr_diagonal in diagonals or curr_anti_diagonal in anti_diagonals):
                    continue 
                
                # adding the queen to the board 
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)

                # moving on to the next row with the updated board state 
                solutions += backtrack(row + 1, diagonals, anti_diagonals, cols)

                # "removing" the queen from the board since we have already explored all valid paths using the previous function call 
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
            
            return solutions
        
        # initial backtrack function call we the set parameters for diagonals, anti-diagonals and columns 
        return backtrack(0, set(), set(), set())
