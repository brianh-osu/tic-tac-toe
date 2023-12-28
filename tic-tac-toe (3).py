#TODO: Add GUI 
#TODO: Data validation for input prompts ( 2. user cannot play on a used tile)
#TODO: Game should end if win condition is met, and prompt user to play again or exit. 
#TODO: If game is a draw (all tiles used, no plays remain) then game must break.

board = [['O' for x in range(3)] for x in range(3)]
board = [['O','O','O'],['X','X','X'],['X','X','X']]
board = [['X','X','X'],['O','O','O'],['X','X','X']]
board = [['O','X','O'], ['O', 'O', 'X'], ['O', 'O', 'X']]
board = [['O','X','O'], ['X','O','X'],['O','O','O']]
board = [['O','X','O'], ['X','O','X'],['X','X','X']]
board = [['X', 'O', 'O'], ['O', 'X', 'O'], ['O', 'O', 'X']]
board = [['O','O','X'], ['O', 'X', 'O'], ['X', 'O', 'O']]
board = [['O','O','O'], ['O','O','O'], ['O','O','O']]
board = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]
board = [['O', 'X', '_'], ['_', 'O', 'X'],['_', '_', '_']]
board = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]
#board = [['_','_','_','_'],['_','_','_','_'],['_','_','_','_'],['_','_','_','_']]
print('The board has been initialized as:')
print(board)


def check_win_conditions(letter, player_num):
    """Pass in letter which is a string of the player's piece 
    checks if win conditions exist, if it does return True otherwise return False"""
    def horizontal_win():
        for row in board: 
            if row.count(letter) == len(board[0]): 
                #print('Horizontal win')
                return True 
        return False 
            
    #vertical win 
    def vertical_win():
        #initialize count array and iterate through board row, cols 
        count_arr = [0 for x in board]
        for r in range(len(board[0])):
            for c in range(len(board[0])):
                row = board[r][c]
                for l in row:
                    if l == letter: 
                        count_arr[c] += 1 
            if count_arr.count(0) == 4: #if there is no counts in first row, no vertical win condition
                return False 
                
        #check the indicies within count_arr. If any sum up correct then it is a vertical win 
        for x in count_arr:
            if x == len(board[0]):
                #print('Vertical win')
                return True 
        return False 
    
    #diaganol win 
    def diaganol_win():
        count = 0 
        if board[0][0] == letter:
            count = 1 
            #while board[cur][cur] == letter: 
            for x in range(1, len(board[0])):
                if board[x][x] == letter: 
                    count += 1 
        if count == len(board[0]):
            return True 
        
        count = 0 
        row = 0 
        if board[row][len(board[0])-1] == letter:
            count = 1 
            cur = len(board[0])-1  
            #while board[cur][cur]: 
            for col in range(cur-1,-1,-1):
                row += 1 
                if board[row][col] == letter: 
                    count += 1 
                    cur -= 1 
        if count == len(board[0]):
            return True 
        
        return False 
    
    win_satisfied = [horizontal_win(), vertical_win(), diaganol_win()]
    if win_satisfied[0] is True:
        print('You have won by horizontal, player:', player_num)
        return True 
    elif win_satisfied[1] is True:
        print('You have won by vertical, player:', player_num)
        return True 
    elif win_satisfied[2] is True:
        print('You have won by diaganol, player:', player_num)
        return True 
    if win_satisfied.count(False) == 3:
        # print('Continue playing..')
        return False 

def input_validation(choice, player_num):
    while choice == 0 or choice > (board_len**2):
        choice = int(input(f"Player {player_num}, where would you like to place (#1-{total_spots})"))
    return choice 
    
total_spots = len(board[0])**2
while True: 
    #prompt play 
    board_len = len(board[0])
    p1_choice = input_validation(0, 1)
    p2_choice = input_validation(0, 2)
    
    #calculate positions to place on board 
    p1_r = p1_choice // board_len 
    p1_c = (p1_choice % board_len) - 1 
    if p1_c == -1: 
        p1_r = int(p1_choice / board_len)-1
        p1_c = board_len -1

    p2_r = p2_choice // board_len 
    p2_c = (p2_choice % board_len) - 1 
    if p2_c == -1: 
        p2_r = int(p2_choice / board_len)-1
        p2_c = board_len-1

    #place on board 
    board[p1_r][p1_c] = 'O' 
    board[p2_r][p2_c] = 'X'
    
    #print results 
    print(board)
    if check_win_conditions('O', 1 ) is True:
        print('The game is over, you have won player 1.')
        break 
    elif check_win_conditions('X', 2) is True:
        print('The game is over, you have won player 2.')
        break
    print() #blank line
    
