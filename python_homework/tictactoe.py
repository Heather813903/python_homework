#Task 6


class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board:
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"

    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3

        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        # Check for win first
        for i in range(3):  # Check rows
            if self.board_array[i][0] != " " and self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2]:
                winner = "O" if self.turn == "X" else "X"
                return (True, f"{winner} wins!")

        for i in range(3):  # Check columns
            if self.board_array[0][i] != " " and self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i]:
                winner = "O" if self.turn == "X" else "X"
                return (True, f"{winner} wins!")

        # Check diagonals
        if self.board_array[1][1] != " ":
            if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2] or \
               self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0]:
                winner = "O" if self.turn == "X" else "X"
                return (True, f"{winner} wins!")

        # Check for tie (cat's game)
        for row in self.board_array:
            if " " in row:
                return (False, f"{self.turn}'s turn.")
        return (True, "Cat's Game.")

def main():
    board = Board()
    print("Welcome to Tic Tac Toe!\n")
    print(board)

    while True:
        print(f"\n{board.turn}'s move.")
        move = input("Enter your move ('center', 'upper right', etc.): ").strip().lower()

        try:
            board.move(move)
            print(board)
        except TictactoeException as e:
            print(f"Invalid move: {e.message}")
            continue

        
        done, message = board.whats_next()
        print(message)
        if done:
            break

if __name__ == "__main__":
    main()
