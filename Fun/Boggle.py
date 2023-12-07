import time, threading, os, sys, termios, fcntl

longest_word = 0
WORD_LENGTH_LIMIT = 4
BOARD_SIZE = 5


def find_longest_word(word):
    global longest_word
    word_length = len(word)
    if word_length > longest_word:
        longest_word = word_length
    return word.lower().strip()


def writeRandomBoardToFile():
    import random
    # Define the 25 Boggle dice and their letter distribution
    boggle_dice_4x4 = [['R', 'I', 'F', 'O', 'B', 'X'],
                       ['I', 'F', 'E', 'H', 'E', 'Y'],
                       ['D', 'E', 'N', 'O', 'W', 'S'],
                       ['U', 'T', 'O', 'K', 'N', 'D'],
                       ['H', 'M', 'S', 'R', 'A', 'O'],
                       ['L', 'U', 'P', 'E', 'T', 'S'],
                       ['A', 'C', 'I', 'T', 'O', 'A'],
                       ['Y', 'L', 'G', 'K', 'U', 'E'],
                       ['Qu', 'B', 'M', 'J', 'O', 'A'],
                       ['E', 'H', 'I', 'S', 'P', 'N'],
                       ['V', 'E', 'T', 'I', 'G', 'N'],
                       ['B', 'A', 'L', 'I', 'Y', 'T'],
                       ['E', 'Z', 'A', 'V', 'N', 'D'],
                       ['R', 'A', 'L', 'E', 'S', 'C'],
                       ['U', 'W', 'I', 'L', 'R', 'G'],
                       ['P', 'A', 'C', 'E', 'M', 'D'],
                       ]
    boggle_dice_5x5 = [['R', 'I', 'F', 'O', 'B', 'X'],
                       ['I', 'F', 'E', 'H', 'E', 'Y'],
                       ['D', 'E', 'N', 'O', 'W', 'S'],
                       ['U', 'T', 'O', 'K', 'N', 'D'],
                       ['H', 'M', 'S', 'R', 'A', 'O'],
                       ['L', 'U', 'P', 'E', 'T', 'S'],
                       ['A', 'C', 'I', 'T', 'O', 'A'],
                       ['Y', 'L', 'G', 'K', 'U', 'E'],
                       ['Qu', 'B', 'M', 'J', 'O', 'A'],
                       ['E', 'H', 'I', 'S', 'P', 'N'],
                       ['V', 'E', 'T', 'I', 'G', 'N'],
                       ['B', 'A', 'L', 'I', 'Y', 'T'],
                       ['E', 'Z', 'A', 'V', 'N', 'D'],
                       ['R', 'A', 'L', 'E', 'S', 'C'],
                       ['U', 'W', 'I', 'L', 'R', 'G'],
                       ['P', 'A', 'C', 'E', 'M', 'D'],
                       ['T', 'I', 'C', 'E', 'T', 'S'],
                       ['K', 'L', 'N', 'O', 'T', 'u'],
                       ['N', 'U', 'F', 'E', 'S', 'P'],
                       ['O', 'D', 'M', 'I', 'T', 'B'],
                       ['V', 'E', 'R', 'I', 'Y', 'F'],
                       ['B', 'A', 'W', 'J', 'O', 'A'],
                       ['E', 'H', 'R', 'T', 'V', 'W'],
                       ['P', 'S', 'D', 'N', 'A', 'K'],
                       ['A', 'A', 'F', 'S', 'R', 'S']
                       ]
    boggle_dice_6x6 = [['A', 'A', 'A', 'F', 'R', 'S'],
                       ['A', 'A', 'E', 'E', 'E', 'E'],
                       ['A', 'A', 'E', 'E', 'O', 'O'],
                       ['A', 'A', 'F', 'I', 'R', 'S'],
                       ['A', 'B', 'D', 'E', 'I', 'O'],
                       ['A', 'D', 'E', 'N', 'N', 'N'],
                       ['A', 'E', 'E', 'E', 'E', 'M'],
                       ['A', 'E', 'E', 'G', 'M', 'U'],
                       ['A', 'E', 'G', 'M', 'N', 'N'],
                       ['A', 'E', 'I', 'L', 'M', 'N'],
                       ['A', 'E', 'I', 'N', 'O', 'U'],
                       ['A', 'F', 'I', 'R', 'S', 'Y'],
                       ['Qu', 'In', 'Th', 'Er', 'He', 'An'],
                       ['B', 'B', 'J', 'K', 'X', 'Z'],
                       ['C', 'C', 'E', 'N', 'S', 'T'],
                       ['C', 'D', 'D', 'L', 'N', 'N'],
                       ['C', 'E', 'I', 'I', 'T', 'T'],
                       ['C', 'E', 'I', 'P', 'S', 'T'],
                       ['C', 'F', 'G', 'N', 'U', 'Y'],
                       ['D', 'D', 'H', 'N', 'O', 'T'],
                       ['D', 'H', 'H', 'L', 'O', 'R'],
                       ['D', 'H', 'H', 'N', 'O', 'W'],
                       ['D', 'H', 'L', 'N', 'O', 'R'],
                       ['E', 'H', 'I', 'L', 'R', 'S'],
                       ['E', 'I', 'I', 'L', 'S', 'T'],
                       ['E', 'I', 'L', 'P', 'S', 'T'],
                       ['E', 'I', 'O', '+', '+', '+'],
                       ['E', 'M', 'T', 'T', 'T', 'O'],
                       ['E', 'N', 'S', 'S', 'S', 'U'],
                       ['G', 'O', 'R', 'R', 'V', 'W'],
                       ['H', 'I', 'R', 'S', 'T', 'V'],
                       ['H', 'O', 'P', 'R', 'S', 'T'],
                       ['I', 'P', 'R', 'S', 'Y', 'Y'],
                       ['J', 'K', 'Qu', 'W', 'X', 'Z'],
                       ['N', 'O', 'O', 'T', 'U', 'W'],
                       ['O', 'O', 'O', 'T', 'T', 'U']]  # '+' is used as a blank tile

    boggle_dice = boggle_dice_4x4 if BOARD_SIZE == 4 else boggle_dice_5x5 if BOARD_SIZE == 5 else boggle_dice_6x6
    random.shuffle(boggle_dice)

    # Roll the dice and generate a random board
    with open("letters.txt", "w") as file:
        die = 0
        for _ in range(BOARD_SIZE):
            for _ in range(BOARD_SIZE):
                file.write(random.choice(boggle_dice[die]) + " ")
                # file.write(choice("abcdefghijklmnopqrstuvwxyz") + " ")
                die += 1
            file.write("\n")


def printBoard(boggle):
    global timeLeftText, topText
    os.system('clear')
    print(topText)
    for row in boggle:
        for letter in row:
            print(letter + " " * (5 - len(letter)), end="")
        print()
    print(timeLeftText, end="")


def manageInputBuffer():
    global input_buffer
    # Save the current terminal settings
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    # Make the terminal non-blocking
    fcntl.fcntl(fd, fcntl.F_SETFL, os.O_NONBLOCK)

    # Read the input buffer until it's empty
    while True:
        try:
            # Read a single character from the input buffer
            char = sys.stdin.read(1)
            if char == '':
                # End of input buffer reached
                break
            else:
                # Add the character to the input buffer string
                input_buffer += char
        except IOError:
            # No input available yet
            break

    # Restore the original terminal settings
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    # Clear the input buffer
    os.system('stty -icanon')


# Uncomment this lines to generate a random board
#writeRandomBoardToFile()

# reads words into list
with open("dictionary.txt") as f:
    dictionary = [find_longest_word(line) for line in f.readlines()]

# reads letters into list
with open("letters.txt") as letters:
    boggle = [[letter.lower() for letter in line.split()] for line in letters.readlines()]

if len(boggle) != len(boggle[0]):
    print("Board must be square")
    exit()
else:
    BOARD_SIZE = len(boggle)


###   SLOWEST METHOD   ###

# Simplified/New method
def find_words(boggle):
    found_words = set()

    def dfs(i, j, current_str):
        nonlocal found_words
        if len(current_str) > 3 and current_str in dictionary:
            found_words.add(current_str)
        if len(current_str) >= longest_word:
            return
        for row, col in (
                (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1),
                (i + 1, j + 1)):
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and not visited[row][col]:
                visited[row][col] = True
                dfs(row, col, current_str + boggle[row][col])
                visited[row][col] = False

    visited = [[False] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            visited[i][j] = True
            dfs(i, j, boggle[i][j])
            visited[i][j] = False

    with open('solutions.txt', 'w') as f:
        f.write('\n'.join(found_words))


# Main code
# find_words(boggle)

# Old method
"""# A recursive function to find all words present on boggle
def find_words_util(boggle, visited, i, j, current_str, found_words):
    global longest_word
    # Mark current cell as visited and append current character to current_str
    visited[i][j] = True
    current_str += boggle[i][j]

    # If current_str is present in dictionary then add it to found_words
    if len(current_str) > 3 and current_str in dictionary:
        found_words.add(current_str)

    # If current_str is longer than longest_word, no need to explore further
    if len(current_str) >= longest_word:
        visited[i][j] = False
        return

    # Traverse 8 adjacent cells of boggle[i,j]
    for row in range(max(i - 1, 0), min(i + 2, BOARD_SIZE)):
        for col in range(max(j - 1, 0), min(j + 2, BOARD_SIZE)):
            if not visited[row][col]:
                find_words_util(boggle, visited, row, col, current_str, found_words)

    # Erase current character from current_str and mark visited of current cell as false
    visited[i][j] = False
    current_str = current_str[:-1]


# Find all words present in dictionary
def find_words(boggle):
    # Mark all characters as not visited
    visited = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    found_words = set()

    # Consider every character and look for all words starting with this character
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            find_words_util(boggle, visited, i, j, current_str="", found_words=found_words)

    # Write found words to file
    with open('solutions.txt', 'w') as f:
        for word in found_words:
            f.write(word + '\n')


# Main code
find_words(boggle)"""


###   FASTEST METHOD   ###

def dfs(board, string, i, j, index):
    if not 0 <= i < BOARD_SIZE or not 0 <= j < BOARD_SIZE or string[index] != board[i][j]: #board[i][j] not in string[index:]:
        return False
    if index == len(string) - 1:
        return True
    board[i][j], res = '*', False
    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
        res = dfs(board, string, i + di, j + dj, index + 1)
        if res: break
    board[i][j] = string[index]
    return res


def wordBoggle(board, dictionary):
    wordsFound = {w for w in dictionary if len(w) >= WORD_LENGTH_LIMIT and any(
        dfs(board, w, i, j, 0) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))}

    with open("solutions.txt", "w") as file:
        file.write('\n'.join(wordsFound) + '\n')
        file.write(f"The longest word found is {max(wordsFound, key=len)}\n")


# Main Code
wordBoggle(boggle, dictionary)

exit()
# Play the game
def PlayWithTimer():
    global running, gameTime, input_buffer, timeLeftText, topText
    while gameTime > 0:
        time.sleep(1)
        gameTime -= 1
        if gameTime % 60 == 0 and gameTime != 0:
            # manageInputBuffer()
            # timeLeftText = f"{gameTime // 60} minutes left\nEnter a guess: {input_buffer}"
            # printBoard(boggle)
            topText = f"Approximately {gameTime // 60} minutes left as of last input"
    timeLeftText = "Time's up!\nPress enter to see the final tally... "
    printBoard(boggle)
    running = False


# Start the timer in a separate thread
running = True
initialGameTime = 3 if BOARD_SIZE == 4 else 4 if BOARD_SIZE == 5 else 5
gameTime = initialGameTime * 60
topText = f"Starting {initialGameTime} minute timer now!"
timeLeftText = ""
input_buffer = ""
timer_thread = threading.Thread(target=PlayWithTimer)
timer_thread.start()

# Get user input and write it to file in the main thread
with open("guesses.txt", "w") as f:
    while running:
        printBoard(boggle)
        user_input = input("Enter a guess: ")
        f.write(user_input + "\n")

# Wait for the timer thread to finish
timer_thread.join()

# Read the solutions file
with open("solutions.txt") as file:
    solutions = file.readlines()
    solutions = [x.strip() for x in solutions]

# Print the results
print("Each guess will have a score next to it for valid guesses, and an X for invalid guesses.")
print("Your results were: ")
totalScore = 0
with open("guesses.txt") as guesses:
    guessesSet = set()
    for line in guesses.readlines():
        line = line.strip()
        guessesSet.add(line)

    for line in guessesSet:
        if line in solutions:
            totalScore += len(line) - 3
            print(f"{line} - {len(line) - 3}")
        elif line != "\n" and len(line):
            print(f"{line} - X")

print(f"Your total score is {totalScore}")
