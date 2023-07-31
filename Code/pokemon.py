import random
import utime
import gc
import json

import resources.bg_clrs as bg
import resources.pokemon as pokemon

def screen_func(buffer):
    
    f = open('data/save.json')
    data = json.load(f)
    for i in data['pokemon']:
        print(i)
    f.close()
    
    count = 0
    while True: #Anything that needs to be updated or put on screen put here        
        bg.bgdraw(buffer)
        gc.collect()        
        
        if count >= 10:
            print("Free Ram:", (gc.mem_free()/gc.mem_alloc())*100, "%")
            count = 0
        count = count+1
        
        buffer.update()
        utime.sleep(0.50)