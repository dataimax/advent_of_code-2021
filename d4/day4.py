boards = []
def createBoards(rows):
    board = [0,0,0,0,0]
    for j in range(0,len(rows)-1,5):
        board[0] = rows[j]
        board[1] = rows[j+1]
        board[2] = rows[j+2]
        board[3] = rows[j+3]
        board[4] = rows[j+4]
        board_c = board[:]
        boards.append(board_c)
    
with open('day4input.txt') as f:
    numbers =  f.readline().split(',')
    boardrows_and_spaces = f.read().splitlines()
    boardrows =[]
    for row in boardrows_and_spaces:
        if row == '':
            pass
        else:
            row = [x for x in row.strip().replace('  ',' ').replace(' ', ',').split(',')]
            boardrows.append(row)
createBoards(boardrows)
boll =all(elem == 'x' for elem in ['x','x','x'])
winner = None
i = 0

def mark(_boards, num):
    boards_c = [[['x' if rnum == num else rnum for rnum in row] for row in board]for board in _boards]
    global boards
    boards = boards_c[:]
    return boards
def check_winner(boards):
    for i, board in enumerate(boards):
        for row in board:
            if all(elem == 'x' for elem in row):
                return i
        #test = [['x','1','2','3','4'],['x','1','2','3','4'],['x','1','2','3','4'],['x','1','2','3','4'],['x','1','2','3','4']]
        columns = [[y[x] for y in board] for x in range(len(board[0]))]
        for row in columns:
            if all(elem == 'x' for elem in row):
                return i
    else: return None

def win_loop(boards):
    global winner
    winner = check_winner(boards)

    if winner != None:
        #print(winner)
        #print(boards[winner])
        currnum=numbers[i]
        #print(boards_c[winner])
        if len(boards)==1:
            print(boards)
            print(numbers[i])
            return True
        boards.remove(boards[winner])
        print(numbers[i], "removed winner")
        win_loop(boards)
    return False

currnum=0
boards_c = boards[:]
while i < len(numbers):
    mark(boards,numbers[i])
    x = win_loop(boards)
    if x:
        break
    i+=1

import numpy as np
print(boards)

sum = 0