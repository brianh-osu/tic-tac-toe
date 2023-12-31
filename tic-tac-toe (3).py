#TODO: GUI

def play_TTC():
    # test values for debugging 
    # board = [['_','_','_','_'],['_','_','_','_'],['_','_','_','_'],['_','_','_','_']]
    # board = [['_','_','O'], ['O','O','O'], ['O','O','O']]
    # board = [['_', '_', 'X'], ['_', 'X', 'X'],['X', 'X', '_']]
    # board = [['_', '_', 'O'], ['O', 'X', 'X'], ['O', 'X', 'O']]
    
    def print_board():
        """prints the board in clean format"""
        for rows in board: 
            print(rows)
    
    def input_validation(player_num):
        """validates placement. Must be within 0 and total spots, and also cannot be on a tile that is already played on. (If placing on a used tile, recursion will occur."""
        choice = 0 
        while choice <= 0 or choice > (total_spots):
            choice = input(f"Player {player_num}, where would you like to place (#1-{total_spots})")
            
            if choice.isdigit():
                choice = int(choice)
                if choice <= 0 or choice > (total_spots):
                    print('Invalid range (placement should be between 1 and '+ str(total_spots)+'. Try again.')
                else: 
                    tile = get_tile(choice) #checking tile 
                    tile_r, tile_c = tile[0], tile[1] 
                    if board[tile_r][tile_c] != '_':
                        print('Placement is used, try again.')
                        spot = input_validation(player_num)
                        return spot 
            else:
                print('Invalid input, please enter only an integer.')
                choice = 0 
                
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
        """intended placement already validated up to this point. This method updates the board"""
        tile_r, tile_c = tile[0], tile[1]
        if player_num == 1:
            board[tile_r][tile_c] = 'O'
        elif player_num == 2:
            board[tile_r][tile_c] = 'X' 
        print('The board is now: ')
        print_board()
    
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
        """checks if there is any remaining plays left"""
        played_tiles = 0 
        for rows in board: 
            for cols in rows: 
                if cols != '_':
                    played_tiles += 1 
        if played_tiles == total_spots:
            return True 
        else:
            return False 
    
    def start_game():
        """begins the game. Validates input, plays the choice, checks win condition. Once game is over, prompts repeat"""
        
        # start game 
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
            print() 
        print()

        # game over 
        start_over = input('Would you like to play again? (Y/N):')
        if start_over.upper() == 'Y':
            print() 
            play_TTC()
        else:
            print() 
            print('Thanks for playing.')
            
    # prompt board size and validate (do not nest within function since we want board and variables to be accessible)
    while True: 
        board = input('How large would you like the board? Type an integer (i,e. 1 = 1x1 board, 2 = 2x2 board, ...)')
        if board.isdigit():
            board = int(board)
            if board <= 0:
                print("Invalid input, integer must be > 0.")
            else:
                board_len = board 
                total_spots = board_len**2 
                board = [['_' for x in range(board)] for x in range(board)]
                print('The board has been initialized as:')
                break 
        else:
            print("Invalid input, please enter only an integer.")
            
    print_board()
    start_game() 
  
if __name__ == '__main__':
    play_TTC()
