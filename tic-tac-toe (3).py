#TODO: GUI
#TODO: Initialize board using an input length (prompt user)

board = [['_','_','_','_'],['_','_','_','_'],['_','_','_','_'],['_','_','_','_']]
# board = [['_','_','O'], ['O','O','O'], ['O','O','O']]
# board = [['_', '_', 'X'], ['_', 'X', 'X'],['X', 'X', '_']]
# board = [['_', '_', 'O'], ['O', 'X', 'X'], ['O', 'X', 'O']]
print('The board has been initialized as:')
# print(board)

def print_board():
    for rows in board: 
        print(rows)

def input_validation(player_num):
    choice = 0 
    while choice <= 0 or choice > (board_len**2):
        choice = int(input(f"Player {player_num}, where would you like to place (#1-{total_spots})"))
        if choice <= 0 or choice > (board_len**2):
            print('Invalid range (placement should be between 1 and '+ str(total_spots)+'. Try again.')
        else: 
            tile = get_tile(choice) #checking tile 
            tile_r, tile_c = tile[0], tile[1] 
            if board[tile_r][tile_c] != '_':
            # while board[tile_r][tile_c] != '_':
                # choice = prompt_choice(player_num)
                print('Placement is used, try again.')
                spot = input_validation(player_num)
                return spot 
    # print(tile)
    return tile 
    
def get_tile(choice):
    """converts choice to tile# (returns an array)"""
    row = choice // board_len 
    col = (choice % board_len) - 1 
    if col == -1:
        row = int(choice / board_len) - 1 
        col = board_len - 1 
    return [row, col] 
    
def play_tile(player_num, tile):
    tile_r, tile_c = tile[0], tile[1]
    if player_num == 1:
        board[tile_r][tile_c] = 'O'
    elif player_num == 2:
        board[tile_r][tile_c] = 'X' 
    print('The board is now: ')
    print_board()
    #print(board)
    
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
        # return True 
    if win_satisfied[1] is True:
        print('You have won by vertical, player:', player_num)
        # return True 
    if win_satisfied[2] is True:
        print('You have won by diaganol, player:', player_num)
        # return True 
    if win_satisfied.count(False) == 3:
        # print('Continue playing..')
        return False 
    else:
        return True 
        
def check_full():
    played_tiles = 0 
    for rows in board: 
        for cols in rows: 
            if cols != '_':
                played_tiles += 1 
    if played_tiles == total_spots:
        return True 
    else:
        return False 
    
board_len = len(board[0])
total_spots = len(board[0])**2 

print_board()
while True:
    p1_tile = input_validation(1)
    play_tile(1, p1_tile)
    if check_win_conditions('O', 1) is True:
        print('The game is over, you have won player 1.')
        break 
    if check_full() is True:
        print('The game is over. All tiles played. Draw.')
        break 
    
    p2_tile = input_validation(2)
    play_tile(2, p2_tile) 
    if check_win_conditions('X', 2) is True:
        print('The game is over, you have won player 2.')
        break 
    if check_full() is True:
        print('The game is over. All tiles played. Draw.')
        break 
    print() #blank line 
