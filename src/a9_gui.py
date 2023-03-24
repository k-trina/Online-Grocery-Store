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
COLOR_INACTIVE = DEEPBLUE
COLOR_ACTIVE = PASTELYELLOW
FONT = font.Font(None, 32) # temporary font

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

# input text box class
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, evnt):
        if evnt.type == MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(evnt.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if evnt.type == KEYDOWN:
            if self.active:
                if evnt.key == K_RETURN:
                    print(self.text)
                    # self.text = ''
                elif evnt.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += evnt.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        draw.rect(screen, self.color, self.rect, 2)


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
#     dropText = Modern.render("All tables have been dropped. Check MySQL Workbench.", 1, (255,255,255)) 
#         # getting the width of the text
#     textWidth = Modern.size(dropText)[0] 
#         # getting the height of the text
#     textHeight = Modern.size(dropText)[1] 
#         # blitting text to the screen
#     screen.blit(dropText, Rect(175 + (600 - textWidth)/2, width + (80 - textHeight)/2, textWidth, textHeight))
#     
#     #dropText = ("All tables have been dropped. Check MySQL Workbench.", 1, (255, 255, 255))
#     
    text="All tables have been dropped."
    dropText = ModernSubHeading.render(text,True,BLACK)
    screen.blit(dropText,(205,270))
    
    text="Check MySQL Workbench."
    dropText = ModernSubHeading.render(text,True,BLACK)
    screen.blit(dropText,(220,350))
    
    #print("drop function running")
    
    # ADD SQL CODE HERE
    

def create():
    screen.fill(PASTELRED)
    
def add():
    screen.fill(PASTELGREEN)

def query():
    def query_screen():
        screen.fill(STRONGTEAL)
            
        select_attribute = "SELECT :"
        text = ModernSubHeading.render(select_attribute,True,BLACK)
        screen.blit(text,(150,150))
        
        table = "FROM :"
        text = ModernSubHeading.render(table,True,BLACK)
        screen.blit(text,(150,250))
        
        value = "WHERE :"
        text = ModernSubHeading.render(value,True,BLACK)
        screen.blit(text,(150,350))
        
        order_attribute = "ORDER BY :"
        text = ModernSubHeading.render(order_attribute,True,BLACK)
        screen.blit(text,(150,450))
        
        order = "For ORDER BY, enter either ASC or DES"
        text = ModernWriting.render(order,True,BLACK)
        screen.blit(text,(150,550))

        # Concatenate input and define SQL query
        sql = "SELECT " + select_attribute + " FROM " + table + " WHERE " + select_attribute + " = " + value + " ORDER BY " + order_attribute + order + ";"

        # Execute the query from the connection cursor
        cursor.execute(sql)
        
        # Print the column names from the query result
        print("Columns:")
        print(cursor.column_names)
        print()
        
        # Get and print the contents of the query results (raw results)
        rows = cursor.fetchall()
        print(f"Row count: {cursor.rowcount}")
        print()

        print("Data:")
        for row in rows:
            print(row)
        
        # Close the Connect object
        conn.close()
        
        return
    
    input_box1 = InputBox(450, 150, 500, 50)
    input_box2 = InputBox(450, 250, 500, 50)
    input_box3 = InputBox(450, 350, 500, 50)
    input_box4 = InputBox(450, 450, 500, 50, "ASC")

    
    
    input_boxes = [input_box1, input_box2, input_box3, input_box4]
    done = False
    clock = time.Clock()
    while done == False:
        for evnt in event.get():
            if evnt.type == QUIT:
                done = True
                sys.exit()
                
            for box in input_boxes:
                box.handle_event(evnt)

        for box in input_boxes:
            box.update()

        query_screen() # used to enable backspaces on input text boxes
        
        for box in input_boxes:
            box.draw(screen)

        display.flip()
        clock.tick(30)
    
    
    """
    done = False
    while done == False:
        clock = time.Clock()
        for evnt in event.get():
            if evnt.type == QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(evnt)

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        display.flip()
        clock.tick(30)
        """


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
on_menu = True
#action = ""
while quitting == False: # Main program
    mouse_pos = mouse.get_pos()
    for evnt in event.get():
        if evnt.type == QUIT:
            quitting = True
            sys.exit() # Added this line since quitting program caused crash -- Coco
        if on_menu == True:
            if evnt.type == MOUSEBUTTONDOWN: # Note: If the user holds down the mouse button and puts cursor on the button, it is activated
                if menuRects[0].collidepoint(mouse_pos): # drop button being pressed
                    print("Drop")
                    drop()
                    on_menu = False
                elif menuRects[1].collidepoint(mouse_pos): # create button being pressed
                    print("Create")
                    create()
                    on_menu = False
                elif menuRects[2].collidepoint(mouse_pos): # create button being pressed
                    print("Add")
                    add()
                    on_menu = False
                elif menuRects[3].collidepoint(mouse_pos): # create button being pressed
                    print("Query")
                    query()
                    on_menu = False
                    
    
                
            
#         if evnt.type == MOUSEBUTTONDOWN:
#             mx,my = evnt.pos
#             button = evnt.button
#             click(button,mx,my,150,250)

#         if action == "CREATE":
#             screen.fill(PASTELPURPLE)

    display.update() # this line was missing, the display would never change regardless of the user's interactions without it
            
            

    
