from tabulate import tabulate
from os import system 


class CanvasDims():
   def __init__(self , height , width , horizontal , vertical , padding):
       self.height = height
       self.width = width
       self.horizontal = horizontal
       self.vertical = vertical
       self.padding = padding
       self.available_height = []

   def update_canvas_height(self , new_height):
       self.new_height = new_height
       self.height = self.new_height
      

  

class PredefinedCharts(CanvasDims):
       
       def __init__(self , height , width , horizontal , vertical , padding, navbar, footer , sidenav):
           super().__init__(height , width , horizontal , vertical , padding)
           self.navbar = navbar
           self.footer = footer
           self.sidenav = sidenav
           
           
           #Navbar dims by default
           if self.navbar.lower() == 'y':
               self.navbar_height = 90 - self.vertical
               self.navbar_width = self.width - (self.horizontal * 2)
               self.navbar_horizontal = 0 + self.horizontal
               self.navbar_vertical = 0 + self.vertical
           else:
               self.navbar_height = 0
               self.navbar_width = 0
               self.navbar_horizontal = 0
               self.navbar_vertical = 0
         
           if self.footer.lower() == 'y':
                #Footer dims by default
                self.footer_height = (90 - (self.vertical * 2)) 
                self.footer_width = self.width - (self.horizontal * 2)
                self.footer_horizontal =  0 + self.horizontal
                self.footer_vertical = (self.height - self.footer_height)  - self.vertical  
           else:
                self.footer_height = 0
                self.footer_width = 0
                self.footer_horizontal = 0
                self.footer_vertical = 0

           if self.sidenav.lower() == 'y':
               #sideNav dims by default
               self.side_nav_height = (self.height - self.navbar_height) - self.footer_height
               self.side_nav_width = 250 - self.horizontal 
               self.side_nav_horizontal = 0 + self.horizontal
               self.side_nav_vertical = self.navbar_height + self.vertical 
           else:
               #sideNav dims by default
               self.side_nav_height = 0
               self.side_nav_width = 0
               self.side_nav_horizontal = 0
               self.side_nav_vertical = 0   
            
      
class ChartDims( PredefinedCharts ):
    def __init__(self , height , width , horizontal , vertical , padding , navbar,  footer , sidenav):
        super().__init__(height , width , horizontal , vertical , padding, navbar , footer , sidenav)
        
        self.outer_space = padding
        self.canvas_new_height =  self.height - (((self.vertical * 2) + (self.outer_space * 2) + self.navbar_height) + self.footer_height)
        self.canvas_new_width = ((self.width - self.horizontal) -  (self.side_nav_width + self.horizontal)) - (self.outer_space *2) 
        self.canvas_new_horizontal = self.horizontal + self.side_nav_width + self.outer_space    
        self.canvas_new_vertical = (self.vertical + self.navbar_height) + self.outer_space
        
        if self.sidenav == 'y':
            self.sidenav_new_height =  self.height - (((self.vertical * 2) + (self.outer_space * 2) + self.navbar_height) + self.footer_height)       
            self.sidenav_new_vertical = self.side_nav_vertical + self.outer_space
        else: 
            self.sidenav_new_height = 0
            self.sidenav_new_vertical = 0

        

    def canvas_information(self):
       self.table_headers = ["Item" , "Height" , "Width" , "Horizontal" , "Vertical"]
       self.table_values = [["Canvas:", self.height , self.width , self.horizontal, self.vertical],
                       ["Navbar:",self.navbar_height, self.navbar_width,self.navbar_horizontal,self.navbar_vertical],
                       ["Footer:",self.footer_height,self.footer_width,self.footer_horizontal,self.footer_vertical],
                       ["SideNav:", self.sidenav_new_height, self.side_nav_width , self.side_nav_horizontal , self.sidenav_new_vertical],
                       ["Inner Canvas:", self.canvas_new_height, self.canvas_new_width,self.canvas_new_horizontal, self.canvas_new_vertical],
                       ] 
       
       system('cls')
       print(tabulate(self.table_values , headers = self.table_headers , tablefmt="grid"))
       print(tabulate([[self.padding]] , headers= ["Inner Canvas Padding"] , tablefmt="grid"))
       #print(f"Inner Padding: {self.outer_space}")
       
      
    def inner_canvas(self):
#columns 4 rows 3 space 10
        

        self.columns = int(input("How many Columns do you want in your Canvas ?: "))
        self.rows = int(input("How many Rows do you want in your Canvas ?: "))
        self.space = int(input("Space in between ?: "))  
        self.canvases_horizontal =  (self.canvas_new_width  - (self.space * (self.columns - 1))) / self.columns
        self.canvases_vertical = (self.canvas_new_height  - (self.space * (self.rows - 1))) / self.rows
        self.first_canvas_horizontal = self.canvas_new_horizontal
        self.last_canvas_horizontal =  (self.canvas_new_width - self.canvases_horizontal) + self.canvas_new_horizontal 
        self.first_canvas_vertical = self.canvas_new_vertical
        self.last_canvas_vertical = (self.canvas_new_height - self.canvases_vertical) + self.canvas_new_vertical 
        self.inner_table_headers = ["Item","Height","Width","First Item Horizontal","First Item Vertical","Last Item Horizontal","Last Item Vertical"]
        self.inner_table_values = [["Grid",self.canvases_vertical, self.canvases_horizontal, self.first_canvas_horizontal,self.first_canvas_vertical,self.last_canvas_horizontal, self.last_canvas_vertical]]  
        

        print("\nInner Canvas Dims:")
        #print(f"Your canvas is a table with: {self.columns} Columns and {self.rows} Rows for a total of {self.columns * self.rows } grids") 
        print(tabulate(self.inner_table_values , headers=self.inner_table_headers , tablefmt="grid"))
        

def CanvasData():
    system('cls')
    height = int(input("Enter the Canvas Height: "))
    width = int(input("Enter the Canvas Width: "))
    horizontal = int(input("Enter horizontal Position of the Canvas: "))
    vertical = int(input("Enter vertical Position of the Canvas: "))
    padding = int(input("Enter the Padding would like to use for this Dashboard:  "))
    new_canvas = CanvasDims(height , width , horizontal , vertical , padding)

    
    predefined_layouts = input("Are you using a Navbar, Footer , side_nav ? Y/N: ")
    
    if predefined_layouts.lower() == 'y':
        navbar = input("Are you using a Navbar ? Y/N: ")
        footer = input("Are you using a Footer ? Y/N: ")
        side_nav = input("Are you using a Side navigation Pane ? Y/N: ")
        predefined_layouts  = PredefinedCharts ( new_canvas.height , new_canvas.width , new_canvas.horizontal , new_canvas.vertical , new_canvas.padding, navbar , footer , side_nav )
       
        display_chart_data = ChartDims(new_canvas.height , new_canvas.width , new_canvas.horizontal , new_canvas.vertical , new_canvas.padding , predefined_layouts.navbar , predefined_layouts.footer , predefined_layouts.sidenav)
        display_chart_data.canvas_information()
        display_chart_data.inner_canvas()  

       
    else:
        predefined_layouts  = PredefinedCharts ( new_canvas.height , new_canvas.width , new_canvas.horizontal , new_canvas.vertical , new_canvas.padding,"No Navbar", "No Footer", "No SideNav" )
        display_chart_data = ChartDims(new_canvas.height , new_canvas.width , new_canvas.horizontal , new_canvas.vertical , new_canvas.padding, predefined_layouts.navbar , predefined_layouts.footer , predefined_layouts.sidenav)
        display_chart_data.canvas_information() 
        display_chart_data.inner_canvas()
    
   
    modify_Canvas = input("Do you want to Modify the Canvas ? Y/N: ")
    while modify_Canvas.lower() == 'y':
        print("[1]-Modify Height\n[2]-Modify Width\n[3]-Modify Horizontal\n[4]Modify Vertical")
        option = input("Select an Option: ")
        if option == '1':
            print(f"Canvas current Height: {new_canvas.height}")
            new_height = int(input("Enter new Canvas Height"))
            new_canvas.height = new_height
            display_chart_data.canvas_information() 
        elif option == '2':
            print("World hello")
        modify_Canvas = input("Do you want to do another Modification ? Y/N: ")



CanvasData()

