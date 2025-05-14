import pygame as pg
from Model import Model
import random as ran


class View(Model):

    def __init__(self, model):
        self.model = model
        self.board = model.board
        self.size = model.size
        self.alphabet = model.alphabet
        self.screen_width = 800
        self.screen_height = 800
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.color_dict = {}
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        self.square_edge = self.screen_height // self.size
        self.vertical_boundary = (
            self.screen_height - (self.size * self.square_edge)
        ) // 2
        self.horizontal_boundary = (
            self.screen_width - (self.size * self.square_edge)
        ) // 2
        print(self.horizontal_boundary)

    def start_display(self):
        pg.init()
        pg.mixer.init()
        screen = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption("Main Menu")
        return screen

    def divide_screen(self):
        bottom = 0 - self.vertical_boundary
        top = self.screen_height + self.vertical_boundary
        right = self.screen_width - self.horizontal_boundary
        left = 0 + self.horizontal_boundary
        for i in range(self.size):
            left_point = (left, bottom + i * self.square_edge)
            right_point = (right, bottom + i * self.square_edge)
            bottom_point = (left + i * self.square_edge, bottom)
            top_point = (left + i * self.square_edge, top)
            pg.draw.line(self.screen, self.black, left_point, right_point, 2)
            pg.draw.line(self.screen, self.black, top_point, bottom_point, 2)

    def make_colors(self):
        for index in range(1, self.size + 2):
            letter = self.alphabet[index]
            a = ran.randrange(0, 225, 20)
            b = ran.randrange(0, 225, 20)
            c = ran.randrange(0, 225, 20)
            self.color_dict[letter] = (a, b, c)

    def fill_color(self):
        for row_num, row in enumerate(self.board):
            for index in range(len(row)):
                letter = row[index]
                if isinstance(letter, int):
                    letter = self.alphabet[letter]
                color = self.color_dict[letter]
                top_left = (index * self.square_edge, row_num * self.square_edge)
                top_right = ((index + 1) * self.square_edge, row_num * self.square_edge)
                bottom_left = (index * self.square_edge, (row_num + 1) * self.square_edge)
                bottom_right = (
                    (index + 1) * self.square_edge,
                    (row_num + 1) * self.square_edge,
                )
                pg.draw.polygon(
                    self.screen, color, [top_left, top_right, bottom_right, bottom_left]
                )
