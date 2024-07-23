
import time
import random


def print_board(bo):
    print("\n\n")
    for i in range(len(bo)):
        if i % 3 ==  0:
            print("- - -   - - -   - - -")

        for j in range(len(bo[i])): 
            print(bo[i][j], end=" ")
            if (j + 1) % 3 == 0:
                print('|', end=" ")
        print()
    time.sleep(0.1)
 


def find_empty(bo) -> (int,int):
    for row in range(len(bo)):
        for column in range(len(bo[row])):
            if bo[row][column] == 0:
                return (row, column)
            
def number_valid_position(bo,row,column,number) -> bool:
    # validate column
    if number in bo[row]:
        return False

    # validade row
    for x in range(len(bo)):
        for y in range(len(bo[row])):
            if y != column: continue
            if bo[x][y] == number:
                return False

    subgrid_row = row // 3
    subgrid_column = column // 3

    for r in range(subgrid_row * 3, subgrid_row * 3 + 3):
        for c in range(subgrid_column * 3, subgrid_column * 3 + 3):
            if bo[r][c] == number:
                return False
            
    return True

def resolve(bo) -> bool:
    print_board(bo)

    find = find_empty(bo)

    if not find:
        return True
    
    row, column = find

    for candidate in range(1,10):
        if number_valid_position(bo,row,column,candidate):
            bo[row][column] = candidate

            if resolve(bo):
                return True
            
            bo[row][column] = 0
    
    return False



def generate_sudoku(size: int, numbers_to_fill: int = 27) -> [[int]]:
    if size % 3 != 0:
        raise Exception("Size must be multiple of 3")
    
    board = [[0 for _ in range(size)] for _ in range(size)]

    def generate_number() -> int:
        return random.randint(1,9)
    
    def generante_random_position() -> (int,int):
        return (random.randint(0,size - 1),random.randint(0,size - 1))
    
    for _ in range(numbers_to_fill):
        row,column = generante_random_position()
        number = generate_number()
        while not number_valid_position(board,row,column,number):
            row,column = generante_random_position()
            number = generate_number()
        board[row][column] = number

                    

    return board             

board = generate_sudoku(9)


resolve(board)