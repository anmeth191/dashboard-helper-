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
        self.canvas_new_height =  self.height - (self.navbar_height + self.footer_height + (self.outer_space * 2))  
        #self.canvas_new_height =  self.height - (((self.vertical * 2) + (self.outer_space * 2) + self.navbar_height) + self.footer_height) 
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
       print("Canvas Calculations Results: ")
       print(tabulate(self.table_values , headers = self.table_headers , tablefmt="grid"))
       print(tabulate([[self.padding]] , headers= ["Inner Canvas Padding"] , tablefmt="grid"))
       
    #this method calculates the grids inside of the work inner canvas to space the grids equally so the dashboard will look better  
    def inner_canvas(self , rows , columns , spacing):
        self.columns = columns
        self.rows = rows
        self.space = spacing  
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
        print(tabulate([[rows , columns , spacing , rows*columns]] , headers=["Total Rows:" , "Total Columns" , "Spacing in Between:" , "Total Grids:"] , tablefmt="grid"))
        print(tabulate(self.inner_table_values , headers=self.inner_table_headers , tablefmt="grid"))
        

def canvas_data():
    system('cls')
    main_canvas = canvas_intake()
    predefined_sections = predefine_layouts()
    

    print(main_canvas , predefined_sections)
    create_main_canvas = ChartDims(main_canvas[0] , #height 
                                    main_canvas[1] , #width
                                    main_canvas[2] , #horizontal
                                      main_canvas[3] , #vertical
                                        main_canvas[4] , #padding
                                        predefined_sections[0] , #navbar
                                        predefined_sections[1] , #footer
                                        predefined_sections[2]  #sidenav
                                        )
    
    print("Canvas Calculations Results: ")
    create_main_canvas.canvas_information()
    inner_canvas = inner_canvas_grid_and_spacing()
    create_main_canvas.inner_canvas(inner_canvas[0] , inner_canvas[1] , inner_canvas[2])
    
    modify_canvas(main_canvas[0] , #height 
                    main_canvas[1] , #width
                     main_canvas[2] , #horizontal
                      main_canvas[3] , #vertical
                       main_canvas[4] , #padding
                        predefined_sections[0] , #navbar
                         predefined_sections[1] , #footer
                          predefined_sections[2],  #sidenav
                          inner_canvas[0],#rows
                          inner_canvas[1],#columns
                          inner_canvas[2]#spacing
                            )#end of the modify canvas function call
     

def modify_canvas(height , width , horizontal , vertical , padding , navbar , footer , side_nav , rows , columns , spacing):
    new_Canvas_data = [height,width, horizontal , vertical , padding ]
    new_predefined_layout = [navbar , footer , side_nav]
    new_inner_canvas = [rows , columns , spacing]
    modifier = False
  
    modify_canvas = input("Would you like to modify the Canvas ? Y/N: ")
    if modify_canvas.lower() == "y":
        modifier = True    
    while modify_canvas.lower() == "y":     
        system("cls")
       # print("What would you like to modify") 
       # print("[1] Main Canvas \n[2] Predefined Layouts \n[3] Rows, Columns and space")
        print(tabulate([["What would you Like to Modify ?" , "[1] - Main Canvas" , "[2] - Predefined Layouts" , "[3] - Rows and Columns"]])) 
        option = input("Please select an option: ")
        #Modify the Main Canvas of the Dashboard
        if option == "1":
            system('cls')
            print("Current Canvas values: ")
           #print old values y there is no data in the new values to modify
            if modifier == False:
                print(tabulate([[height , width , horizontal, vertical , padding]] , headers=["Height" , "Width" , "Horizontal" , "Vertical" , "Padding"] , tablefmt="grid"))
            else: 
                print(tabulate([new_Canvas_data] , headers=["Height" , "Width" , "Horizontal" , "Vertical" , "Padding"] , tablefmt="grid"))   
            new_canvas_dims = canvas_intake()
            new_Canvas_data = []
            for item in new_canvas_dims:
                new_Canvas_data.append(item)
                                   
        #Modify the predefined Layouts  
        elif option == "2":
           
           print("Current Predefined Items values: ")
           if modifier == False:
                 print(tabulate([[navbar , footer , side_nav]] , headers=["Navbar" , "Footer" , "SideNav"], tablefmt="grid"))
           else:
               print(tabulate([new_predefined_layout] , headers=["Navbar" , "Footer" , "SideNav"], tablefmt="grid"))
            
           predefined_modified_values = predefine_layouts()
           new_predefined_layout = []    
           for item in predefined_modified_values:
               new_predefined_layout.append(item)
                   
        #modify the rows and columns 
        elif option == "3":
            print("Current Inner Canvas Values: ")
            if modifier == False:
                print(tabulate([[rows , columns , spacing ]] , headers=["Rows:" , "Columns:" , "Spacing:"] , tablefmt="grid"))
            else:
                print(tabulate([ new_inner_canvas ] , headers=["Rows:" , "Columns:" , "Spacing:"] , tablefmt="grid"))

            inner_modified_values = inner_canvas_grid_and_spacing()
            new_inner_canvas = []
            for item in inner_modified_values:
                new_inner_canvas.append(item)
            
        
                
        #else the option is incorrect 
        else:
            print("Option not Available")
        
        modified_canvas = ChartDims(new_Canvas_data[0] , #height 
                                    new_Canvas_data[1] , #width
                                    new_Canvas_data[2] , #horizontal
                                      new_Canvas_data[3] , #vertical
                                        new_Canvas_data[4] , #padding
                                        new_predefined_layout[0] , #navbar
                                        new_predefined_layout[1] , #footer
                                        new_predefined_layout[2])  #sidenav
     
        modified_canvas.canvas_information()
        modified_canvas.inner_canvas(new_inner_canvas[0] , new_inner_canvas[1] , new_inner_canvas[2])
        modify_canvas = input("Would you like to do another modification ? Y/N: ")
         
            

##This function captures the main Canvas dims 
def canvas_intake():
    
    height = int(input("Enter the Canvas Height: "))
    width = int(input("Enter the Canvas Width: "))
    horizontal = int(input("Enter horizontal Position of the Canvas: "))
    vertical = int(input("Enter vertical Position of the Canvas: "))
    padding = int(input("Enter the Padding would like to use for this Dashboard:  "))
    return [height , width , horizontal , vertical , padding ]



##This function captures the data for the predefined layouts and sends the data to the class if an item is activated or deactivated 
def predefine_layouts():
    predefined_layouts = input("Are you using a Navbar, Footer , side_nav ? Y/N: ")
    
    if predefined_layouts.lower() == 'y':
        navbar = input("Are you using a Navbar ? Y/N: ")
        footer = input("Are you using a Footer ? Y/N: ")
        side_nav = input("Are you using a Side navigation Pane ? Y/N: ") 
    else:
        navbar = "n"
        footer = "n"
        side_nav = "n"
    
    return [navbar , footer , side_nav]


def inner_canvas_grid_and_spacing():

    rows = int(input("How many Rows do you want in your Canvas ?: "))
    columns = int(input("How many Columns do you want in your Canvas ?: "))
    space = int(input("Space in between ?: ")) 
    return [rows , columns , space] 

    


##Here we start the program
canvas_data()

