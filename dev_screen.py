import random
import utime
import gc

import resources.bg_clrs as bg
import resources.pokemon as pokemon

def screen_func(buffer): # Put all Algorithms here
    
    def draw_text(x,y,text,lineLength,size,R,G,B):
        buffer.set_pen(R, G, B)
        buffer.text(text, x, y, lineLength, size) #buffer.text(Text, X Coord, Y Coord, Line Length, Text Size)
    
    buttons = ["Map", "Pokemon", "PokeDex", "Comm"]
    
    def menu_buttons(Dir):
        #Right = 1
        #Down = 2
        #Left = 3
        #Up = 6
        for i in range(0,Dir):
            buttons.append(buttons[0])
            buttons.pop(0)
    
    print("Original Buttons Order:\n", buttons)
    menu_buttons(1)
    menu_buttons(3)
    print("New Buttons Order:\n", buttons)
    
    def draw_button(x, y, modulusx, modulusy, Boxw, Boxh, text, Textw, Texth, BoxR, BoxG, BoxB, TextR, TextG, TextB):
        
        # x: X-coord of Button
        # y: Y-coord of Button
        # modulusx & modulusy: The variable used in the modulus operation for centering the text in a button
        # Boxw & Boxh: Width and Height of Button
        # text: Button Text
        # Textw & Texth: Width and Height of Text
        # BoxR, BoxG, BoxB & TextR, TextG, TextB: Colours of Text and Button
        
        buffer.set_pen(BoxR,BoxG,BoxB)      #Box Drawing
        buffer.rectangle(x, y ,Boxw ,Boxh)  
        buffer.set_pen(TextR, TextG, TextB) #Text Drawing
        buffer.text(text, x+(x//modulusx), y+(y//modulusy), 0, 2)
    
    animateX = 0
    count = 10
    
    while True: #Anything that needs to be updated or put on screen put here        
        
        bg.bgdraw(buffer)
        draw_text(70,10,"PokeHunter",0,2,0,0,0)
        draw_text(35,30,"This is a Dev Screen",250,2,0,0,0)
        
        draw_button(45,150,5,20,50,30,"Map",0,2,255,0,0,0,0,0)
        draw_button(105,150,10,20,95,30,"Pokemon",0,2,0,255,0,0,0,0)
        draw_button(45,190,8,20,85,30,"PokeDex",0,2,255,255,0,0,0,0)
        draw_button(145,190,30,20,55,30,"Comm",0,2,0,50,220,0,0,0)
        
        if animateX == 0:
            animateX = 1
        else:
            animateX = 0
        
        pokemon.draw("bulbasaur",buffer,0,40,70+(animateX)*4)
        pokemon.draw("ivysaur",buffer,0,100,70+(animateX)*4)
        pokemon.draw("venusaur",buffer,0,160,70+(animateX)*4)
        #pokemon.draw("bulb",buffer,0,40,110+(animateX)*4)
        
        gc.collect()        
        
        if count >= 10:
            print("Free Ram:", (gc.mem_free()/gc.mem_alloc())*100, "%")
            count = 0
        count = count+1
        
        buffer.update()
        utime.sleep(0.50)
