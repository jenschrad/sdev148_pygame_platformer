# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:56:36 2022

@author: JenSc
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 23:33:46 2022

@author: JenSc
"""
# *-- LEVEL EDITOR --*
# *************************************
# attempt at making a program that allows
# more efficient level design
# following Coding With Russ's level editor tutorial
# https://www.youtube.com/watch?v=xYhniILN6Ls
# *************************************

# *-- HOW TO USE --*
# *************************************
# use left mouse to click on img you want to select
# selected tile will be highlighted blue
# use left mouse to click on tile you want to place the img
# right click to delete img from tile
# use up arrow to change lvl by one
# use down arrow to decrease lvl by one (cannot go below 0)
# left click on save button to save data to file
# left click on load button to load data to screen


# *-- REMINDERS --*
# this lvl editor saves the indexes of where imgs are
# on screen into list, and is then written to a file
# to save. loading reads the file that corresponds
# with lvl num on screen
# there aren't functions for confirmation of saving/loading
# so, if save button is hit, it cannot be undone and previous
# file will be overwritten. lvl 0 can act as a place to experiment
# there are two methods for saving in this code
# one using csv module and one using pickle module
# csv will write to a file you can open and see/read
# and pickle will write to a file that can't be opened or read
# but takes much less code and work 
# csv method is commented out
# *************************************


import pygame
# import csv
import pickle
from tkinter import messagebox as mb 


pygame.init()

clock = pygame.time.Clock()
fps = 60

SCREEN_W = 600
SCREEN_H = 600
BOTTOM_MAR = 100
SIDE_MAR = 200


screen = pygame.display.set_mode((SCREEN_W, SCREEN_H + BOTTOM_MAR))
pygame.display.set_caption = ("Level Editor")

# game variables
ROWS = 15
colS = 15
t_size = 40
tile_set = 14
tile_on = 0
level = 0
click = False
#load images
bg = pygame.image.load("bkg.png")
save_bttn = pygame.image.load("save_image.png")
save_bttn = pygame.transform.scale(save_bttn, (90, 70))
load_bttn = pygame.image.load("load_image.png")
load_bttn = pygame.transform.scale(load_bttn, (90, 70))
brick = pygame.image.load("brick.png")
ceiling = pygame.image.load("ceiling.png")
ground = pygame.image.load("ground.png")
l_side = pygame.image.load("l_side.png")
r_side = pygame.image.load("r_side.png")
l_top_corner = pygame.image.load("l_top_corner.png")
r_top_corner = pygame.image.load("r_top_corner.png")
l_bot_corner = pygame.image.load("l_bot_corner.png")
r_bot_corner = pygame.image.load("r_bot_corner.png")
door = pygame.image.load("door.png")
evil_character = pygame.image.load("evil_character1.png")
filler = pygame.image.load("filler.png")
soul = pygame.image.load("soul.png")
# color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (95, 205, 208 )
GRAY = (79, 86, 128)

# font
font = pygame.font.Font( "PressStart2P-Regular.ttf", 10)

# empty tile list for data
scene_data = []
for row in range(15):
    r = [0] * 15
    scene_data.append(r)
    


# boundary
#for tile in range( 0, 15):
 #   scene_data[14][tile] = 2
  #  scene_data[0][tile] = 1
   # scene_data[tile][0] = 1
   # scene_data[tile][14] = 1

# class for buttons
# reminder **** make this a module ****
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.click = False
    def draw(self, surface):
        click_action = False
        # mouse pos
        pos = pygame.mouse.get_pos()
        
        # check if mouse on bttn
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                click_action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False
            
        # display button
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return click_action



# display text function
def display_text(text, font, text_col, x, y):
    txt_img = font.render(text, True, text_col)
    screen.blit(txt_img, (x, y))
    
# display bg function
def display_bg():
    screen.fill(GRAY)
    screen.blit(bg, (0,0))
# grid function
def create_grid():
    for line in range(0, 15):
        pygame.draw.line(screen, (WHITE), (0, line * t_size), (SCREEN_W, line * t_size))
        pygame.draw.line(screen, (WHITE), (line * t_size, 0), (line * t_size, SCREEN_H))
   
# creating and displaying tiles function
def create_scene():
        for row in range(15):
            for col in range(15):
                if scene_data[row][col] > 0:
                    if scene_data[row][col] == 1:
                        img = pygame.transform.scale(ground, (t_size, t_size))
                        screen.blit(img,(col * t_size, row * t_size))
                        
                        
                    if scene_data[row][col] == 2:
                        img = pygame.transform.scale(ceiling, (t_size, t_size))
                        screen.blit(img, (col * t_size, row * t_size))
                        
                        
                    if scene_data[row][col] == 3:
                        img = pygame.transform.scale(l_side, (t_size, t_size))
                        screen.blit(img, (col * t_size, row * t_size))
                        
                        
                    if scene_data[row][col] == 4:
                        img = pygame.transform.scale(r_side, (t_size, t_size))
                        screen.blit(img, (col * t_size, row * t_size))
                        
                        
                    if scene_data[row][col] == 5:
                        img = pygame.transform.scale(l_bot_corner, (t_size, t_size))
                        screen.blit(img, (col * t_size, row * t_size))
                        
                        
                    if scene_data[row][col] == 6:
                        img = pygame.transform.scale(r_bot_corner, (t_size, t_size))
                        screen.blit(img, (col * t_size, row * t_size))
                        
                        
                    if scene_data[row][col] == 7:
                        img = pygame.transform.scale(r_top_corner, (t_size, t_size))
                        screen.blit(img, (col * t_size, row * t_size))
                        
                        
                    if scene_data[row][col] == 8:
                        img = pygame.transform.scale(l_top_corner, (t_size, t_size))
                        screen.blit(img, (col * t_size, row * t_size))
                        
                        
                    if scene_data[row][col] == 9:
                        img = pygame.transform.scale(brick, (t_size, t_size))
                        screen.blit(img, (col * t_size, row * t_size))
                    
                        
                    if scene_data[row][col] == 10:
                        img = pygame.transform.scale(door, (70, 80))
                        screen.blit(img, (col * t_size, row * t_size - (t_size // 2)))
                        
                        
                    if scene_data[row][col] == 11:
                        img = pygame.transform.scale(evil_character, (50, 60))
                        screen.blit(img, (col * t_size, row * t_size + (t_size * 0.50)))
                        
                        
                    if scene_data[row][col] == 12:
                        img = pygame.transform.scale(filler, (t_size, t_size))
                        screen.blit(img, (col * t_size, row * t_size))
                        
                    if scene_data[row][col] == 13:
                        img = pygame.transform.scale(soul, (t_size, t_size))
                        screen.blit(img, (col * t_size, row * t_size))
                        
                
# buttons
save_button = Button(SCREEN_W // 2 + 100, SCREEN_H + BOTTOM_MAR - 80, save_bttn)
load_button = Button(SCREEN_W // 2 + 200, SCREEN_H + BOTTOM_MAR - 80, load_bttn)








run = True
while run:
    
    clock.tick(fps)
    
    display_bg()
    
    display_text(f"level: {level}", font, WHITE, 10, SCREEN_H + BOTTOM_MAR - 80)
    display_text("press up or down to change lvl", font, WHITE, 10, SCREEN_H + BOTTOM_MAR - 60)
    

# *************************************
# *-- PICKLE MODULE METHOD FOR SAVE/LOAD --*
    # save lvl data
    if save_button.draw(screen):
        # saves data to python list
        pickle_write = open(f"lvl{level}_data", "wb")
        pickle.dump(scene_data, pickle_write)
        pickle_write.close()
    # load lvl data
    if load_button.draw(screen):
        # reset scene data list for loading
        scene_data = []
        pickle_read = open(f"lvl{level}_data", "rb")
        scene_data = pickle.load(pickle_read)
   
#*************************************
# *-- CSV MODULE METHOD FOR SAVE/LOAD --*
    # saving and loading level/scene data
   # if save_button.draw(screen):
        # save lvl data ()
        # with open(f"lvl{level}_data.csv", "w", newline = "") as csvfile:
            # commas seperate list
           # csv_write = csv.writer(csvfile, delimiter = ",")
            # iterate through row list and write to csv to create file
            # reminder: ***** come back and add function for where to save & confirmation *****
            # for row in scene_data:
               # csv_write.writerow(row)
   # if load_button.draw(screen):
        # load lvl data
       # with open(f"lvl{level}_data.csv", newline = "") as csvfile:
            # read file
           # csv_read = csv.reader(csvfile, delimiter = ",")
            # change strings to int and 
            # iterate through csv read file
           # for x, row in enumerate(csv_read):
                # iterate through loaded row
               # for y, tile in enumerate(row):
                    # store in scene data list and convert to int
                   # scene_data[x][y] = int(tile)
# *************************************               
            
    create_grid()
    create_scene()
    #side tile panel
    #pygame.draw.rect(screen, WHITE, (SCREEN_W, 0, SIDE_MAR, SCREEN_H), 2)
    # bottom tile panel
    pygame.draw.rect(screen, WHITE, (0,SCREEN_W, SCREEN_H + 200, BOTTOM_MAR), 2)
    # pick tile

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and click == False:
                click == True
                pos = pygame.mouse.get_pos()
                x = pos[0] // t_size
                y = pos[1] // t_size
                
                if x < 15 and y < 15:
                    if pygame.mouse.get_pressed()[0] == 1:
                        scene_data[y][x] += 1
                        if scene_data[y][x] > 13:
                            scene_data[y][x] = 0
                    elif pygame.mouse.get_pressed()[2] == 1:
                        scene_data[y][x] -= 1
                        if scene_data[y][x] < 0:
                            scene_data[y][x] = 13
        if event.type == pygame.MOUSEBUTTONUP:
                click = False
                

         
         # key presses
        if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_UP:
                 level += 1 
              if event.key == pygame.K_DOWN and level > 0:
                 level -= 1
                 
                 
    pygame.display.update()


pygame.quit()