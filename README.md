# N-Queens

Solution to the N-Queen problem. 

The N-Queens problem revolves around the task of placing N queens on an N x N chessboard such that no two queens are in a position to attack each other. 

The goal of the problem is to count the number of possible solutions to place the N queens on the board.

The solution algorithm utilizes a concept known as backtracking to improve efficiency and reduce the number of potential checks that need to be made. 

Solution Algorithm Outline:
  1. Iterate over each row in the board.
  2. Within each outer iteration, we iterate over each column of the board, along the current row. During this second iteration, we can explore the possibility of placing a queen on a particular tile.
  3. Before we go ahead and place the queen on a given tile with the index (row, col), we need to check to see if the particular cell is in the line of attack of queens that have already been placed for this particular board. To accomplish this task, a helper function is_not_under_attack(row, col) will be used to perform the check. 
  4. If the check passes, we can place a queen on the given tile. After placing a new queen on the board, it is important to mark the potential attack zone of this new queen. For this we write another helper called place_queen(row, col) that will help to mark lanes of attack. 
  5. The last step involves a recursive concept called backtracking. Backtracking is a general algorithm for finding potential solutions to certain problems. It allows us to abandon certain candidate solutions if it is already known that they are incompatible. This greatly improves the efficiency of our approach, and it is crucial that we are able to abandon a previous decision when we want to consider another candidate. 

A brute force solution would have us generate all possible board state with N queens on the N x N board. 

Such an approach is drastically inefficient, although it is still wise to make use of the idea of generating potential board states. 

The key idea for backtracking is to utilize a backtracking function that changes the state, calls itself again and when that call returns it undoes the changes. 

