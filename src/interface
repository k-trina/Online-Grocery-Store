from pygame import * 
import os
import random
import sys # Added this library to correct program exit -- Coco

# Import stuff for connection handling
from Connect import Connect
from Tunnel import Tunnel

# Constants - connection definition files
DCRIS_FILE = "dcris.txt"
HOPPER_FILE = "hopper.txt"

# Connect to the DCRIS database with an option file
conn = Connect(DCRIS_FILE)
# Get the connection cursor object
cursor = conn.cursor


# Define a SQL query
sql = "SELECT * FROM employee"
# sql = "SELECT " +  "FROM " + "WHERE " + "ORDER BY "
# Execute the query from the connection cursor
cursor.execute(sql)

#moving screen to top left corner
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0, 20)
init()

size = 1000, 700
screen = display.set_mode(size)

#colours
BLACK = (0, 0, 0)
WHITE = (255,255,255)
PASTELRED = (255,153,153)
PASTELPURPLE = (204,153,255)
PASTELGREEN = (102, 255,178)
DEEPBLUE = (0,0,102)
STRONGTEAL = (0,128,255)
PASTELYELLOW = (255,255,102)

#fonts
Modern = font.SysFont("Modern No. 20",60)
Heading = font.SysFont("Modern No. 20",75)
ModernSubHeading = font.SysFont("Modern No. 20",50)
ModernWriting = font.SysFont("Modern No. 20",26)

# button text
DROP = "DROP"
CREATE = "CREATE"
FILL = "FILL"


# booleans
quitting = False

mx = my = 0
posx = posy = 0
button = 0

# button

def menuButton(backColour,textColour,text,width):
    #DROP button
    #if buttonID == 1:
    draw.rect (screen, backColour, (250,width,450,75))
    buttonRect = Rect(250,width,450,75)
        
        # Setting up the AI Text
    text1 = Modern.render(text, 1, textColour) 
        # getting the width of the text
    text1Width = Modern.size(text)[0] 
        # getting the height of the text
    text1Height = Modern.size(text)[1] 
        # blitting "AI" to the screen
    screen.blit(text1, Rect(175 + (600 - text1Width)/2, width + (80 - text1Height)/2, text1Width, text1Height))
    
    return buttonRect


# main screen - menu page
def mainMenu (): # Returns a list of menu rectangles
    screen.fill(WHITE)
    dropRect = menuButton(DEEPBLUE, PASTELPURPLE,"DROP", 150)
    createRect = menuButton(DEEPBLUE, PASTELRED,"CREATE", 275)
    addRect = menuButton(DEEPBLUE, PASTELGREEN, "ADD", 400)
    queryRect = menuButton(DEEPBLUE, STRONGTEAL, "QUERY", 525)
    return [dropRect, createRect, addRect, queryRect]
    
# SQL FUNCTIONS
def drop():
    screen.fill(PASTELPURPLE)
    print("drop function running")

def create():
    screen.fill(PASTELRED)
    
def add():
    screen.fill(PASTELGREEN)

def query():
    screen.fill(STRONGTEAL)

def click(button,mousex,mousey,width,height):
    if button == 1: # if button is being pressed
        if height <= mousex <= height + 450: # if mouse in range of button
            if width <= mousey <= width + 125:
                # create table
                drop()
                print("hello")
    return


menuRects = mainMenu()

display.flip()
#action = ""
while quitting == False: # Main program
    mouse_pos = mouse.get_pos()
    for evnt in event.get():
        if evnt.type == QUIT:
            quitting = True
            sys.exit() # Added this line since quitting program caused crash -- Coco
        if evnt.type == MOUSEBUTTONDOWN: # Note: If the user holds down the mouse button and puts cursor on the button, it is activated
            if menuRects[0].collidepoint(mouse_pos): # drop button being pressed
                print("Drop")
                drop()
            elif menuRects[1].collidepoint(mouse_pos): # create button being pressed
                print("Create")
                create()
            elif menuRects[2].collidepoint(mouse_pos): # create button being pressed
                print("Add")
                add()
            elif menuRects[3].collidepoint(mouse_pos): # create button being pressed
                print("Query")
                query()
                
    
                
            
#         if evnt.type == MOUSEBUTTONDOWN:
#             mx,my = evnt.pos
#             button = evnt.button
#             click(button,mx,my,150,250)

#         if action == "CREATE":
#             screen.fill(PASTELPURPLE)

    display.update() # this line was missing, the display would never change regardless of the user's interactions without it