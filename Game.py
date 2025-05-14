import random as ran
import pygame as pg
from Model import Model
from View import View


def run_game():

    model = Model()
    view = View(model)
    screen = view.screen
    model.make_board()
    model.find_solution_queens()
    print(model.queen_coords)
    model.place_solution_queens()
    print(2, model.queen_coords)
    model.place_colors()
    print(3, model.queen_coords)
    view.start_display()
    print(4, model.queen_coords)
    screen.fill((225, 225, 225))
    view.divide_screen()
    print(5, model.queen_coords)
    view.make_colors()
    print(6, model.queen_coords)
    model.make_square_color_dict()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill((225, 225, 225))
        view.fill_color()
        view.divide_screen()
        pg.display.flip()
    pg.quit()


run_game()
