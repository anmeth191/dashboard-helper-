from tabulate import tabulate
from os import system 


class CanvasDims():
   def __init__(self , height , width , horizontal , vertical):
       self.height = height
       self.width = width
       self.horizontal = horizontal
       self.vertical = vertical
       self.available_height = []

     

class PredefinedCharts(CanvasDims):
       
       def __init__(self , height , width , horizontal , vertical , navbar, footer , sidenav):
           super().__init__(height , width , horizontal , vertical)
           self.navbar = navbar
           self.footer = footer
           self.sidenav = sidenav
            #Navbar dims by default
           if self.navbar.lower() == 'y':
               self.navbar_height = 90 
               self.navbar_width = self.width - (self.horizontal * 2)
               self.navbar_horizontal = self.horizontal
               self.navbar_vertical = self.vertical
           else:
               self.navbar_height = 0
               self.navbar_width = 0
               self.navbar_horizontal = 0
               self.navbar_vertical = 0
         
           if self.footer.lower() == 'y':
                #Footer dims by default
                self.footer_height = 50
                self.footer_width = self.width - (self.horizontal * 2)
                self.footer_horizontal = self.horizontal
                self.footer_vertical = (self.height - self.footer_height) - self.vertical
           else:
                self.footer_height = 0
                self.footer_width = 0
                self.footer_horizontal = 0
                self.footer_vertical = 0

           if self.sidenav.lower() == 'y':
               #sideNav dims by default
               self.side_nav_height = (self.height - self.navbar_height) - self.footer_height
               self.side_nav_width = 220 
               self.side_nav_horizontal = self.horizontal
               self.side_nav_vertical = (self.navbar_height + self.vertical) + self.vertical 
           else:
               #sideNav dims by default
               self.side_nav_height = 0
               self.side_nav_width = 0
               self.side_nav_horizontal = 0
               self.side_nav_vertical = 0


               
               
       
class ChartDims( PredefinedCharts ):
    def __init__(self , height , width , horizontal , vertical , navbar, footer , sidenav, total_charts , horizontal_space_charts , outside_chart_space ):
        super().__init__(height , width , horizontal , vertical , navbar , footer , sidenav)
        
        self.total_charts = total_charts
        #define the space between charts
        self.inner_space = horizontal_space_charts
        
        #padding for main canvas
        self.padding_main_canvas = outside_chart_space
        
        
        self.canvas_new_height = ((self.height - self.navbar_height) - self.footer_height) - (self.padding_main_canvas * 2) 
        self.canvas_new_width = (self.width - self.side_nav_width) - (self.padding_main_canvas *2) 
        self.canvas_new_horizontal = self.horizontal + self.side_nav_width + self.padding_main_canvas    
        self.canvas_new_vertical = (self.vertical + self.navbar_height) + self.padding_main_canvas
        
        self.sidenav_new_height = self.side_nav_height - (self.padding_main_canvas * 2)
        self.sidenav_new_vertical = self.navbar_height + self.padding_main_canvas
             l


    def canvas_information(self):
       
       table_headers = ["Item |","Height |","Width |","Horizontal |","Vertical |"]
       table = [ ["Main Canvas:", self.height , self.width , self.horizontal , self.vertical],
                 ["Navbar:" ,self.navbar_height ,self.navbar_width, self.navbar_horizontal , self.navbar_vertical ],
                 ["Footer:" ,self.footer_height ,self.footer_width, self.footer_horizontal , self.footer_vertical ],
                 ["Sidenav:" , self.sidenav_new_height , self.side_nav_width, self.side_nav_horizontal , self.sidenav_new_vertical],
                 ["Inner Canvas:",self.canvas_new_height, self.canvas_new_width, self.canvas_new_horizontal , self.canvas_new_vertical ]
                 ] 
        
       system('cls')
       print(tabulate(table , headers= table_headers , showindex="always"))
       
       
       #print(f"{self.footer_height} {self.footer_width} {self.footer_vertical} {self.footer_horizontal}")
       #print(f"{self.side_nav_height - (self.outer_space * 2 )} {self.side_nav_width} {self.side_nav_vertical + self.outer_space} {self.side_nav_horizontal}")
       #print(f"{self.canvas_new_height}{self.canvas_new_width}{self.canvas_new_vertical}{self.canvas_new_horizontal}")



    
def verify_predefined_items(navbar , footer , side_nav ):
    print("Predefined items")

def CanvasData():
    system('cls')
    height = int(input("Enter the Canvas Height: "))
    width = int(input("Enter the Canvas Width: "))
    horizontal = int(input("Enter horizontal Position of the Canvas: "))
    vertical = int(input("Enter vertical Position of the Canvas: "))
    padding = int(input("Enter the Padding would like to use for this Dashboard:  "))
    
    predefined_layouts = input("Are you using a Navbar, Footer , side_nav ? Y/N: ")
    
    if predefined_layouts.lower() == 'y':
        navbar = input("Are you using a Navbar ? Y/N: ")
        footer = input("Are you using a Footer ? Y/N: ")
        side_nav = input("Are you using a Side navigation Pane ? Y/N: ")
        main_canvas  = ChartDims(height , width , horizontal , vertical , navbar , footer , side_nav , 50 , 50 , padding)
        main_canvas.canvas_information()
    
    
    
    
    
CanvasData()

