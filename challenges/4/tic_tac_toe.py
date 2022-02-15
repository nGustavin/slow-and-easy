# Tic tac toe input

# Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, where the board looks like this:

# 1:  X | O | X
#    -----------
# 2:    |   |  
#    -----------
# 3:  O |   |

#     A   B  C

# The board is represented as a 2D list:

# board = [
#     ["X", "O", "X"],
#     [" ", " ", " "],
#     ["O", " ", " "],
# ]

# Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board. To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].

# Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.

# For example, calling get_row_col("A3") should return the tuple (2, 0) because A3 corresponds to the row at index 2 and column at index 0in the board.
import string

class TicTacToe:
  def __init__(self):
    self.board = [
      ["", "", ""],
      ["", "", ""],
      ["", "", ""]
    ]
  
  def __write(self, position, player_mark, player):
    """Write in the board on the gived position:
    Ex: Gived position: C3 ~ Will write an "X" or "O" on the last line (3) on the last column (C)
    """
    column = string.ascii_uppercase.index(position[0].upper())
    row = int(position[1]) - 1

    if self.board[row][column] != "":
      new_position = input("Position already written in the board!\nType a new position: ")
      self.__write(new_position, player_mark)
      return

    self.board[row][column] = player_mark
    self.info[player]['score'] += 1
    for line in self.board:
      print(str(line) +'\n')

  def start(self, player1, player2):
    self.info = {
      player1: {
        "score": 0,
        "mark": 'X',
      },
      player2: {
        "score": 0,
        "mark": 'O'
      }
    }
    for plr in self.info.keys():
      while self.info[plr]['score'] < 3:
        for player in self.info.keys():
          while self.info[player]['score'] < 3:
            move = input(f"{player} type your move: ")
            self.__write(move, self.info[player]['mark'], player)
            break   

board = TicTacToe()
board.start("Gutavos", "gustavos 2")
