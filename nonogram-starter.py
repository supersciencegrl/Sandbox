import time
import winsound

Debug = False

def set_globals():
    """
    Prompts the user to input the row length and column height for the Nonogram puzzle.
    If in debug mode, sets the row length and column height to 10.
    If the user input is invalid, prompts the user to enter valid integer values.

    Globals:
    row_length: an integer representing the length of each row in the puzzle grid
    col_length: an integer representing the height of each column in the puzzle grid
    """
    
    global row_length, col_length
    
    if Debug:
        row_length = 10
        col_length = 10
    else:
        while not row_length:
            try:
                row_length = int(input('Row length: '))
                col_length = int(input('Column height: '))
            except ValueError:
                row_length = 0

# Audio feedback
def sad_beep():
    ''' Makes a negative double-beep sound '''
    winsound.Beep(800,100)
    time.sleep(0.01)
    winsound.Beep(800,350)
def happy_beep():
    ''' Makes an affirmative beep '''
    winsound.Beep(2000,200)
def triumphant_beep():
    ''' Makes a triumphant double-beep sound '''
    winsound.Beep(2400,100)
    time.sleep(0.01)
    winsound.Beep(2400,500)

def visualize(filled, grid_length):
    """
    Displays a visualization of the Nonogram puzzle grid with filled squares and numbers representing their locations

    Args:
    filled: a list of integers representing the indices of filled squares in the grid
    grid_length: an integer representing the length of the row or column

    Returns:
    None
    """
    
    grid = ['·' for x in range(grid_length)]
    numbers = [' ' for x in range(grid_length)]
    for n in filled:
        grid[n-1] = '█'
        numbers[n-1] = str(n)
    visualized_numbers = [n if len(n)>1 else f'{n} ' for n in numbers]
    
    print(('').join(visualized_numbers))
    print((' ').join(grid))

def validate_instructions(instructions: str, grid_length: int) -> list:
    """
    Validates the input numerical clues for a single row or column, and converts them to a list
    of integers

    Args:
    instructions: a list of integers representing the numerical clues for a Nonogram puzzle
    grid_length: the length of the row or column

    Returns:
    list: the set of instructions, converted to a list of integers

    Raises:
    ValueError: the instructions are invalid
    """

    try:
        result = [int(i) for i in instructions.split()]
    except ValueError:
        raise
    
    # Audio feedback when bad instructions given
    if 0 in result:
        raise ValueError
    elif sum(result) + len(result) - 1 > grid_length:
        raise ValueError

    return result

def run():
    """
    Returns filled in squares for a single row or columnthat was initially blank, and
    displays them as a table.
    Gives a happy_beep() if filled squares are found, and a triumphant_beep() if a whole
    row can be filled.

    Returns:
    filled: a list of integers representing the indices of filled squares in the grid

    Raises:
    ValueError: from validate_instructions(), if invalid instructions provided
    """
    
    # Set parameters
    row_column = 'row' # default
    if not row_length:
        set_globals()
        
    if Debug:
        instructions = '5 1'
    else:
        instructions = input('Instructions: ')
        if row_length != col_length:
            row_column = input('Row or column? ')
            if 'c' in row_column.lower():
                row_column = 'col'

    if row_column == 'row':
        grid_length = row_length
    elif row_column == 'col':
        grid_length = col_length
    else:
        raise TypeError

    # Validate instructions and convert to list of integers
    try:
        instructions = validate_instructions(instructions, grid_length)
    except ValueError:
        sad_beep()
        raise
        
    # Remove duplicates
    block_lengths = []
    _ = [block_lengths.append(item) for item in instructions if item not in block_lengths]
    # Order the block size list
    block_lengths.sort(reverse = True)

    # Find filled in squares
    filled = []
    for length in block_lengths:
        indices = [i for i, x in enumerate(instructions) if x==length]
        for idx in indices:
            before = instructions[:idx]
            after = instructions[idx+1:]
            min_block_start = sum(before) + len(before) + 1
            min_block_end = min_block_start + length - 1
            max_block_end = row_length - sum(after) - len(after)
            max_block_start = max_block_end - length + 1
            if Debug:
                print(min_block_start, min_block_end, max_block_end, max_block_start)
            if max_block_start <= min_block_end:
                newly_filled = list(range(max_block_start, min_block_end+1))
                if not newly_filled:
                    break
                else:
                    filled += newly_filled
    # Audio feedback
    if 1 in filled: # Whole row is filled
        triumphant_beep()
    elif filled:
        happy_beep()

    visualize(filled, grid_length)

    return filled

row_length = 0
while True:
    try:
        filled = run()
    except ValueError:
        pass
