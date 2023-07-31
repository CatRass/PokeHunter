        # Non-Shiny: shine = 0
        # Shine: shine = 1
def draw(name, buffer, shine, offsetX, offsetY):
    name = "resources.clrs." + name
    pkm = __import__(name, globals(), locals(), [], 0)
    
    for i in range(0, len(pkm.Coords)):
        for j in range(0, len(pkm.Coords[i][0])):
            buffer.set_pen(pkm.CLRS[shine][i][0], pkm.CLRS[shine][i][1], pkm.CLRS[shine][i][2])
            buffer.pixel(pkm.Coords[i][0][j] + offsetX, pkm.Coords[i][1][j] + offsetY)