import random
import utime
import gc
from breakout_colourlcd240x240 import BreakoutColourLCD240x240
import json

import menu as menu
import routes as routes
import pokemon as pokemonSelect

buffer = bytearray(BreakoutColourLCD240x240.WIDTH * BreakoutColourLCD240x240.HEIGHT * 2)
display = BreakoutColourLCD240x240(buffer)
display.set_backlight(1)
display.clear()

while True:
    menuScreen = menu.screenFunc(display)
    menuScreen.processes()
    
    #pokemonSelect.screen_func(display)
    #routes.screen_func(display)
    #import dev_screen as ds
    #ds.screen_func(display)
