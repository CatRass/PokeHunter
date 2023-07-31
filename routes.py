import random
import utime
import gc

import resources.bg_clrs as bg
import resources.assets.arrow as arrow
import resources.pokemon as pokemon

def screen_func(buffer): # Put all Algorithms here
    
    def draw_text(x,y,text,lineLength,size,R,G,B):
        buffer.set_pen(R, G, B)
        buffer.text(text, x, y, lineLength, size) #buffer.text(Text, X Coord, Y Coord, Line Length, Text Size)
    
    global routes
    global regions
    global input
    global j
    
    regions = ["Kanto"]
    routes = [['Route 1', 'Route 2', 'Route 3', 'Route 4', 'Route 5', 'Route 6', 'Route 7', 'Route 8', 'Route 9', 'Route 10', 'Route 11', 'Route 12', 'Route 13', 'Route 14', 'Route 15', 'Route 16', 'Route 17', 'Route 18', 'Route 19', 'Route 20', 'Route 21', 'Route 22', 'Route 23', 'Route 24', 'Route 25', 'Route 26', 'Route 27', 'Route 28']]
    
    def routes_picker(region, input):
        draw_text(10,10,"Routes: " + regions[region],200,3,0,0,0)
        
        if input >= len(routes[0]):
            input = 0
        else:
            input = input + 1
        
        j = 15
        for i in range (0,7):
            draw_text(100,j*5,str(routes[region][i]),100,2,0,0,0)
            j=j+4
        
        routes[region].append(routes[region][0])
        routes[region].pop(0)
        print(routes)
        
    while True: #Anything that needs to be updated or put on screen put here
        
        bg.bgdraw(buffer)
        #pokemon.draw("niko", buffer, 0, 50, 100)
        arrow.draw(buffer,30,50)
        routes_picker(0,0)
         
        
        gc.collect()
        print("Free Ram:", (gc.mem_free()/gc.mem_alloc())*100, "%")
        
        buffer.update()
        utime.sleep(0.50)
        