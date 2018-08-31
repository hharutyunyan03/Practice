from random import randrange

def draw_board(board):
    for i in range(row_num):
        for j in range(col_num):
            print(board[i][j], end="")
        print()


def write_board(board):
    with open("board.txt", "w") as outfile:
        for i in range(row_num):
            for j in range(col_num):
                if type(board[i][j]) == str:
                    outfile.write(board[i][j])
                else:
                    outfile.write(str(board[i][j]))
            outfile.write("\n")


def neighbours(board, i, j):
    return [(x, y) for x in [i-1, i, i+1] for y in [j-1, j, j+1]
            if x in range(0, len(board)) and y in range(0, len(board[x])) and
            (x, y) != (i, j)]


while True:
    inp_list = input("Enter in format 4 * 4 5: ").split()
    
    if len(inp_list) == 4:
        row_valid = inp_list[0].isdecimal()
        col_valid = inp_list[2].isdecimal()
        bomb_valid = inp_list[3].isdecimal()
    else:
        print("The input is not correct. Try again.")
        continue
    
    if row_valid is False or col_valid is False or\
            bomb_valid is False or inp_list[1] != "*":
        print("The input is not correct. Try again.")
        continue
    else:
        row_num = int(inp_list[0])
        col_num = int(inp_list[2])
        bomb_num = int(inp_list[3])
        
    if row_num * col_num < bomb_num:
        print("The input is not correct. Try again.")
        continue
    
    board = []
    
    for i in range(row_num):
        board.append([])
        for j in range(col_num):
            board[i].append(0)
    
    while bomb_num > 0:
        ind1 = randrange(row_num)
        ind2 = randrange(col_num)
        if board[ind1][ind2] != "*":
            board[ind1][ind2] = "*"
            bomb_num -= 1
            
    for i in range(row_num):
        for j in range(col_num):
            if board[i][j] == "*":
                neighbours_list = neighbours(board, i, j)
                for x in neighbours_list:
                    if board[x[0]][x[1]] != "*":
                        board[x[0]][x[1]] += 1
            
    draw_board(board)
    write_board(board)
    
    break