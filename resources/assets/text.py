def draw(buffer, x,y,text,lineLength,size,R,G,B):
        buffer.set_pen(R, G, B)
        buffer.text(text, x, y, lineLength, size) #buffer.text(Text, X Coord, Y Coord, Line Length, Text Size)
    