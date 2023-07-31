def draw(buffer, x, y, modulusx, modulusy, Boxw, Boxh, text, Textw, Texth, BoxR, BoxG, BoxB, TextR, TextG, TextB):
        
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