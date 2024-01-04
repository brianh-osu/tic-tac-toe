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
    print(board)
    
board_len = len(board[0])
total_spots = len(board[0])**2 

p1_tile = input_validation(1)
play_tile(1, p1_tile)
p2_tile = input_validation(2)
play_tile(2, p2_tile) 

