import random
import utime
import gc

import resources.bg_clrs as bg
import resources.pokemon as pokemon
import resources.assets.buttons as button

def draw_text(buffer,x,y,text,lineLength,size,R,G,B):
    buffer.set_pen(R, G, B)
    buffer.text(text, x, y, lineLength, size) #buffer.text(Text, X Coord, Y Coord, Line Length, Text Size)

def menu_buttons(buttonArray,Dir):
    #Right = 1, Down = 2, Left = 3, Up = 6
    for i in range(0,Dir):
        buttonArray.append(buttonArray[0])
        buttonArray.pop(0)
        return buttonArray

class screenFunc():
    def __init__(self,buffer):
        
        self.animateX = 0
        self.buttons = ["Egg", "Pokemon", "PokeDex", "Comm"]
        self.buffer = buffer
        
        bg.bgdraw(buffer)
        
        button.draw(buffer,45,150,5,20,50,30,"Map",0,2,255,0,0,0,0,0)
        button.draw(buffer,105,150,10,20,95,30,"Pokemon",0,2,0,255,0,0,0,0)
        button.draw(buffer,45,190,8,20,85,30,"PokeDex",0,2,255,255,0,0,0,0)
        button.draw(buffer,145,190,30,20,55,30,"Comm",0,2,0,50,220,0,0,0)
        
        self.buffer.set_clip(40, 110, 20, 20)
        
    def processes(self):
        while True:
            
            self.buffer.clear()
            
            if self.animateX == 0:
                self.animateX = 1
            else:
                self.animateX = 0
                
            self.buffer.set_clip(40, 110+(self.animateX)*4, 20, 20)
            pokemon.draw("bulb",self.buffer,0,40,110+(self.animateX)*4)
            
            print("New Button Order:\n",menu_buttons(self.buttons,1))
                
            gc.collect()
            print("Free Ram:", (gc.mem_free()/gc.mem_alloc())*100, "%")
            self.buffer.update()
            utime.sleep(0.50)
