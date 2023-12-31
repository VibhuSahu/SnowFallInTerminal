import os, random, time



# Configuration
SNOW_DENSITY = 1
DELAY = 0.3


# Set of snowflake characters
snowflakes = ["❄️", "●", ".", "❆", "❉"]


# Get terminal dimensions
terminal = os.get_terminal_size()

w = terminal.columns
h = terminal.lines


# Initialize an empty grid
grid = []



# Initialize an empty grid
grid = [[" "] * w for _ in range(h)]

    
    
def draw_grid():
    """
    The function `draw_grid()` clears the terminal and prints the current state of the grid.
    """
    os.system('cls' if(os.name=='nt') else 'clear' )
    print('\033[? 25l')     # Hide the cursor
    output = ''
    for row in grid:
        output += "".join(row)+ "\n"
        
    output += output.strip("\n")
    print(output, end='')
    
    
# Main loop    
while True:
    # Generate a new row with snowflakes based on the density
    row = []
    for _ in range(w):
        if random.random() < SNOW_DENSITY / 100 :
            row.append(random.choice(snowflakes))
        else:
            row.append(random.choice(' '))
    # Add the new row to the top of the grid and remove the bottom row
    grid.insert(0, row)
    
    grid.pop()
    
    # Draw the updated grid
    draw_grid()
    
    # Pause for a short duration to create animation
    time.sleep(DELAY) 