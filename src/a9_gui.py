
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
                    return self.text
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
        
    text1 = Modern.render(text, 1, textColour) 
        # getting the width of the text
    text1Width = Modern.size(text)[0] 
        # getting the height of the text
    text1Height = Modern.size(text)[1] 
    screen.blit(text1, Rect(175 + (600 - text1Width)/2, width + (80 - text1Height)/2, text1Width, text1Height))
    
    return buttonRect

"""
def clickableButton(backColour,textColour,text,width, x, y):
    def center_text(text,button_rect):
        text_rect=text.get_rect()
        text_x=(button_rect[0]+button_rect[2])//2
        text_y=button_rect[1]+10
        centered_text=(text_x,text_y,button_rect[2],button_rect[3])
        return centered_text
    def display_buttontext(text,textfont,rect,centertext):
        Button_text=textfont.render(text,True,(255,255,255))
        if centertext==True:
            text_rect=ClickableButton.center_text(Button_text,rect)
        else:
            text_rect=rect
            text_rect[1]+=10
        screen.blit(Button_text,text_rect)
    
    
    draw.rect (screen, backColour, (250,width,450,75))
    buttonRect = Rect(250,width,450,75)
        
    text1 = ModernWriting.render(text, 1, textColour) 
        # getting the width of the text
    text1Width = ModernWriting.size(text)[0] 
        # getting the height of the text
    text1Height = ModernWriting.size(text)[1]
    centered_text = center_text(text1, buttonRect)
    
    screen.blit(text1, Rect(x, y, text1Width, text1Height))
    
    return buttonRect
"""

# main screen - menu page
def mainMenu (): # Returns a list of menu rectangles
    screen.fill(WHITE)
    dropRect = menuButton(DEEPBLUE, PASTELPURPLE,"DROP", 150)
    createRect = menuButton(DEEPBLUE, PASTELRED,"CREATE", 275)
    addRect = menuButton(DEEPBLUE, PASTELGREEN, "ADD", 400)
    queryRect = menuButton(DEEPBLUE, STRONGTEAL, "QUERY", 525)
    return [dropRect, createRect, addRect, queryRect]
    
# SQL FUNCTIONS
# SQL FUNCTIONS
def drop():
    def drop_screen():
        screen.fill(PASTELPURPLE)
        
        text_str = "Table to be dropped :"
        text = ModernSubHeading.render(text_str,True,BLACK)
        screen.blit(text,(100,150))
        
        # Put "done" button here
    
    input_box1 = InputBox(550, 150, 500, 50)
    
    input_boxes = [input_box1]

        
    done = False
    clock = time.Clock()
    while done == False:
        for evnt in event.get():
            if evnt.type == QUIT:
                done = True
                sys.exit()
                
            #for box in input_boxes:
            text = input_box1.handle_event(evnt)

        for box in input_boxes:
            box.update()

        drop_screen() # used to enable backspaces on input text boxes
        
        for box in input_boxes:
            box.draw(screen)

        display.flip()
        clock.tick(30)
    
    # ADD SQL CODE HERE
    

def create():
    def create_screen():
        screen.fill(PASTELRED)
        # DISPLAY TEXT TO SCREEN (not input boxes)
        text_str = "Table name :"
        text = ModernSubHeading.render(text_str,True,BLACK)
        screen.blit(text,(150,150))
        
        text_str = "Attributes :"
        text = ModernSubHeading.render(text_str,True,BLACK)
        screen.blit(text,(150,250))
        
        text_str = "For Attributes, the format should be as follows: (type varName, type varName2)"
        text = ModernWriting.render(text_str,True,BLACK)
        screen.blit(text,(150,550))
        
        # doneRect = clickableButton(PASTELGREEN, BLACK,"DONE", 150, 800, 500)

        
    input_box1 = InputBox(450, 150, 500, 50)
    input_box2 = InputBox(450, 250, 500, 50)

    input_boxes = [input_box1, input_box2]

        
    done = False
    clock = time.Clock()
    while done == False:
        for evnt in event.get():
            if evnt.type == QUIT:
                done = True
                sys.exit()
                
            #for box in input_boxes:
            text1 = input_box1.handle_event(evnt)
            text2 = input_box2.handle_event(evnt)

        for box in input_boxes:
            box.update()

        create_screen() # used to enable backspaces on input text boxes
        
        for box in input_boxes:
            box.draw(screen)

        display.flip()
        clock.tick(30)
    
    create_backend(text1, text2)

def create_backend(text1, text2): 
    #tableName= input("Enter the table name: ")
    #attributes= input("Enter all the attribute names you would like to enter ( Ex: int name,varchar(20) name2: ") 
    text2= text2.split(",")
    sql= "CREATE TABLE " + text1 + " (\n"
    for i in range(len(text2)): 
        if i != (len(text2)-1):
            sql= sql+text2[i][:-1]+",\n"
        else: 
            sql= sql+text2[i][:-1]+"\n"
            
    sql=sql+");"

    cursor.execute(sql)
    
    return
    
def add():
    def add_screen():
        screen.fill((102, 200,178))
        cursor.execute("Show tables;")
        tables = cursor.fetchall()
        for i, n in enumerate(tables):
            n= ''.join(n) 
            tables[i]= n
        #tables = ["employee", "customer", "order"] # Hardcoded sample data
        
        #tables_str = "Your database has the following tables:"
        text = ModernWriting.render("Your database has the following tables :",True,BLACK)
        screen.blit(text,(100,150))
        
        tables_str = ""
        
        for table in tables:
            tables_str += table
            if table != tables[-1]:
                tables_str += ", "
        
        text = ModernWriting.render(tables_str,True,(150,40,40))
        screen.blit(text,(100,200))
                
        #print(tables_str)
        
        text = ModernWriting.render("Please enter the name of the table which you want to add data to:",True,BLACK)
        screen.blit(text,(100,250))
        
    COLOR_ACTIVE = WHITE # background is too light, so temporarily changing the active input box colour

    input_box1 = InputBox(100, 300, 500, 50)
    
    input_boxes = [input_box1]

    done = False
    clock = time.Clock()
    while done == False:
        for evnt in event.get():
            if evnt.type == QUIT:
                done = True
                sys.exit()
                
            #for box in input_boxes:
            text = input_box1.handle_event(evnt)

        for box in input_boxes:
            box.update()

        add_screen() # used to enable backspaces on input text boxes
        
        for box in input_boxes:
            box.draw(screen)

        display.flip()
        clock.tick(30)
  

def query():
    def query_screen():
        screen.fill(STRONGTEAL)
        
        # DISPLAY TEXT TO SCREEN (not input boxes)
        text_str = "SELECT :"
        text = ModernSubHeading.render(text_str,True,BLACK)
        screen.blit(text,(150,150))
        
        text_str = "FROM :"
        text = ModernSubHeading.render(text_str,True,BLACK)
        screen.blit(text,(150,250))
        
        text_str = "WHERE :"
        text = ModernSubHeading.render(text_str,True,BLACK)
        screen.blit(text,(150,350))
        
        text_str = "ORDER BY :"
        text = ModernSubHeading.render(text_str,True,BLACK)
        screen.blit(text,(150,450))
        
        text_str = "For ORDER BY, enter either ASC or DES"
        text = ModernWriting.render(text_str,True,BLACK)
        screen.blit(text,(150,550))
        
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
                
            selectText = input_boxes[0].handle_event(evnt)
            fromText = input_boxes[1].handle_event(evnt)
            whereText = input_boxes[2].handle_event(evnt)
            orderbyText = input_boxes[3].handle_event(evnt)

        for box in input_boxes:
            box.update()

        query_screen() # used to enable backspaces on input text boxes
        
        for box in input_boxes:
            box.draw(screen)

        display.flip()
        clock.tick(30)
    
    #Write a done button

    query_backend(selectText, fromText, whereText, orderbyText)

def query_backend(selectText, fromText, whereText, orderbyText):
    sql = "SELECT " + selectText + " FROM " + fromText + " WHERE " + whereText + " ORDER BY " + orderbyText + ";"
    
    # Execute the query from the connection cursor
    cursor.execute(sql)

    # Print the column names from the query result
    print("Columns:")
    print(mycursor.column_names)
    print()
    
    # Get and print the contents of the query results (raw results)
    rows = mycursor.fetchall()
    print(f"Row count: {mycursor.rowcount}")
    print()

    print("Data:")
    for row in rows:
        print(row)
    
    # Close the Connect object
    conn.close()
    
    return

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
            
