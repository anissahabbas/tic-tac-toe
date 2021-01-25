import sys

# two board layouts: one original, used to find the indices of the second board
# second board will be updating with X's and O's
originalBoard = [
    " ",
    "1",
    " |  ",
    "2",
    "  | ",
    "3",
    "\n-------------\n ",
    "4",
    " |  ",
    "5",
    "  | ",
    "6",
    "\n-------------\n ",
    "7",
    " |  ",
    "8",
    "  | ",
    "9",
    "\n",
]
changingBoard = [
    " ",
    " ",
    " |  ",
    " ",
    "  | ",
    " ",
    "\n-------------\n ",
    " ",
    " |  ",
    " ",
    "  | ",
    " ",
    "\n-------------\n ",
    " ",
    " |  ",
    " ",
    "  | ",
    " ",
    "\n",
]

# index locations to be used on the changing board:
one = originalBoard.index("1")
two = originalBoard.index("2")
three = originalBoard.index("3")
four = originalBoard.index("4")
five = originalBoard.index("5")
six = originalBoard.index("6")
seven = originalBoard.index("7")
eight = originalBoard.index("8")
nine = originalBoard.index("9")

print(
    " TIC TAC TOE\n Player A starts with X, Player B follows with O\n To move, enter the number for where you would like to place your X/O"
)
print(*originalBoard, sep="")


def playerMove(letter):
    global changingBoard, originalBoard
    print("Player " + letter + " enter your move: ")
    move = input()
    # use the original board to compare the player's input and then update the changing board
    for index, place in enumerate(originalBoard):
        if move == place:
            if letter == "A":
                changingBoard[index] = "X"
            else:
                changingBoard[index] = "O"
    print(*changingBoard, sep="")
    return changingBoard


# function to check who won
# b represents the board and p the player who just went
def checkIfWinner(b, p):
    if (
        b[one] == b[five] == b[nine]
        or b[three] == b[five] == b[seven]
        or b[one] == b[two] == b[three]
        or b[four] == b[five] == b[six]
        or b[seven] == b[eight] == b[nine]
        or b[one] == b[four] == b[seven]
        or b[two] == b[five] == b[eight]
        or b[three] == b[six] == b[nine]
    ):
        print("The winner is player " + p + "!")
        sys.exit()


# the actual game being played out
# we only need to start checking if there's a winner after the first player has played 3 times
for turn in range(5):
    playerMove("A")
    if turn > 2:
        checkIfWinner(changingBoard, "A")
    playerMove("B")
    if turn > 2:
        checkIfWinner(changingBoard, "B")
