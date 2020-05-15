#As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:
#
#each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
#each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
#each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
#If you need more details, you can find them here.
#
#Your task is to write a program which:
#
#reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
#outputs Yes if the Sudoku is valid, and No otherwise.
#
#Sample
#Enter row 1 : 295743861
#Enter row 2 : 431865927
#Enter row 3 : 876192543
#Enter row 4 : 387459216
#Enter row 5 : 612387495
#Enter row 6 : 549216738
#Enter row 7 : 763524189
#Enter row 8 : 928671354
#Enter row 9 : 154938672
#
#Ans: Yes
#
#####################################################################

def sudoku_data():
    sudoku = []
    for i in range(9):
        data = input(f"Enter row {i+1} : ")
        if data.isnumeric():
            row = [int(x) for x in list(data)]
            sudoku.append(row)
        else:
            print("Invalid Data")
            return None
    return sudoku


def check_sudoku(sudoku):
    if sudoku == None:
        return "Invalid Data"
    
    for i in range(9):
        row, col = [], []
        for j in range(9):
            row.append(sudoku[i][j])
            col.append(sudoku[j][i])
        if sum(set(row)) != 45 or sum(set(col)) != 45:
            return "Row Col No"
        
    for x in range(3):
        subset = []
        for y in range(3):
            subset = []
            #print(f"(3*x = {3*x},3*x+3 = {3*x+3})(3*y = {3*y},3*y+3 = {3*y+3})")
            for i in range(3*x,3*x+3):
                for j in range(3*y,3*y+3):
                    subset.append(sudoku[i][j])
            #print(subset)
            if sum(set(subset)) != 45:
                return "Subset No"
        
    return "Yes"
                    
            
            
check_sudoku(sudoku_data())
