import pygame as pg
import random as ran


class Model:

    def __init__(self):
        self.square_color_dict = {}
        self.empty_row = []
        self.board = []
        self.queen_coords = []
        self.clone_queen_coords = []
        self.size = 25
        self.alphabet = {
            1: "a",
            2: "b",
            3: "c",
            4: "d",
            5: "e",
            6: "f",
            7: "g",
            8: "h",
            9: "i",
            10: "j",
            11: "k",
            12: "l",
            13: "m",
            14: "n",
            15: "o",
            16: "p",
            17: "q",
            18: "r",
            19: "s",
            20: "t",
            21: "u",
            22: "v",
            23: "w",
            24: "x",
            25: "y",
            26: "z",
        }
        self.queen_index = list(range(self.size))
        self.mod_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.win_check_list = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        self.placed_board = []
        self.colored_board = []
        self.placed_coords = []

    def make_board(self):
        self.empty_row = []
        for _ in range(self.size):
            self.empty_row.append("0")
        for _ in range(self.size):
            self.board.append(self.empty_row)
        return self.board

    def find_solution_queens(self):
        ran.shuffle(self.queen_index)
        print(self.queen_index)
        queens_work = False
        while queens_work is False:
            check_set = [0 for _ in range(len(self.queen_index))]
            for index in range(len(self.queen_index) - 1):
                diff = abs(self.queen_index[index] - self.queen_index[index + 1])
                if diff < 2:
                    check_set[index] = 1
            if set(check_set) != {0}:
                ran.shuffle(self.queen_index)
            else:
                queens_work = True
        for row in range(len(self.board)):
            col = self.queen_index[row]
            self.queen_coords.append((row, col))
        print(f"Queen coords are{self.queen_coords}")
        self.clone_queen_coords = self.queen_coords
        return self.queen_coords

    def place_solution_queens(self):
        queen_val = 1
        for coord in self.queen_coords:
            row = [0 for _ in range(self.size)]
            col = coord[1]
            row[col] = queen_val
            self.board[coord[0]] = row
            queen_val += 1
        return self.board

    def check_new_in_range(self, new_coord, colored_squares, filled_squares):
        val_range = range(self.size)
        adjacent = False
        for point1 in colored_squares:
            if self.check_adjacency(point1, new_coord) == True:
                adjacent = True
        if (new_coord[0] in val_range) and (new_coord[1] in val_range):
            if new_coord not in filled_squares:
                if adjacent == True:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def check_adjacency(self, point1, point2):
        deltax = abs(point1[0] - point2[0])
        deltay = abs(point1[1] - point2[1])
        if deltax + deltay > 1:
            return False
        else:
            return True

    def place_colors(self):
        filled_squares = []
        for queen in self.queen_coords:
            filled_squares.append(queen)
        board_filled = False
        overtime = 0
        while board_filled is False:
            max_time_taken = 25
            time_multiplier = 1.2
            if overtime > 1000:
                self.fill_board()
                return self.board
            for row in range(0, self.size):
                overtime += 1
                queen_pos = self.queen_coords[row]
                colored_squares = [queen_pos]
                time_taken = 0
                max_time_taken *= time_multiplier
                while time_taken < max_time_taken:
                    time_taken += 1
                    base_coord = ran.choice(colored_squares)
                    modifier = ran.choice(self.mod_list)
                    new_coord = tuple(a + b for a, b in zip(base_coord, modifier))
                    self.check_new_in_range(new_coord, colored_squares, filled_squares)
                    if (
                        self.check_new_in_range(
                            new_coord, colored_squares, filled_squares
                        )
                        == False
                    ):
                        continue
                    else:
                        colored_squares.append(new_coord)
                        filled_squares.append(new_coord)
                        self.board[new_coord[0]][new_coord[1]] = self.alphabet[row + 1]
                if len(filled_squares) == self.size**2:
                    board_filled = True
        return self.board

    def fill_board(self):
        steps = 0
        val_range = range(self.size)
        while steps < 100000:
            for row in range(self.size):
                for col in range(self.size):
                    if self.board[row][col] == 0:
                        coord = (row, col)
                        modifier = ran.choice(self.mod_list)
                        new_coord = tuple(abs(a + b) for a, b in zip(coord, modifier))
                        if (new_coord[0] not in val_range) or (
                            new_coord[1] not in val_range
                        ):
                            continue
                        x = new_coord[0]
                        y = new_coord[1]
                        if self.board[x][y] in val_range:
                            continue
                        self.board[row][col] = self.board[x][y]
                    steps += 1
        return self.board

    def make_placed_board(self):
        self.placed_board = self.make_board()
        return self.placed_board

    def update_placed_board_coords(self, coord):
        x = coord[0]
        y = coord[1]
        self.placed_board[x][y] = "QUEEN"
        self.placed_coords.append(coord)
        return self.placed_board, self.placed_coords

    def make_alphabet_board(self):
        self.colored_board = self.board
        for row_num, row in enumerate(self.board):
            for index in range(len(row)):
                letter = row[index]
                if isinstance(letter, int):
                    self.colored_board[row_num][index] = self.alphabet[letter]
        return self.colored_board

    def make_square_color_dict(self):
        for row_num, row in enumerate(self.board):
            for col in range(len(row)):
                key_letter = self.board[row_num][col]
                if isinstance(key_letter, int):
                    key_letter = self.alphabet[key_letter]
                if key_letter in self.square_color_dict:
                    self.square_color_dict[key_letter].append((row_num, col))
                else:
                    self.square_color_dict[key_letter] = [(row_num, col)]
        return self.square_color_dict

    def check_row_col_win(self):
        rows = []
        cols = []
        for coord in self.placed_coords:
            rows.append(coord[0])
            cols.append(coord[1])
        if len(set(rows)) == self.size:
            if len(set(cols)) == self.size:
                return True
        return False
    
    def check_region_win(self):
        region_list = []
        for square in self.square_color_dict:
            color_count = 0
            for coord in self.placed_coords:
                if coord in square:
                    color_count += 1
            region_list.append(color_count)
        if set(region_list) == {1}:
            return True
        return False
    
    def check_square_win(self):
        for coord in self.placed_coords:
            for mod in self.win_check_list:
                new_coord = tuple(abs(a + b) for a, b in zip(coord, mod))
                if (new_coord in self.placed_coords) and (new_coord != coord):
                    return False
        return True
    
    def check_win(self):
        criteria = [self.check_region_win(), self.check_row_col_win(), self.check_square_win()]
        if False in criteria:
            return False
        else: 
            return True
