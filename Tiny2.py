

class Screen():
    def __init__(self,width,height,clear=True):
        if clear:
            print("\033[2J")
        self.width = width
        self.height = height
        self.screen = []
        for y in range(0,self.height):
            line = []
            for x in range(0,self.width):
                line.append("█")
            self.screen.append(line)

    def render(self, system="windows"):
        # implement efficiancies e.g. previosly renderd screen and only updating changes
        output = "\033[H"
        for y in range(len(self.screen)):
            for x in range(len(self.screen[y])):
                output = output+str(self.screen[y][x])
            output = output+"\n"

        print(output, end="")

    def define(self,x,y,character,colour=(255,255,255)):
        r,g,b = colour
        self.screen[y][x] = f"\033[38;2;{r};{g};{b}m{character}\x1b[0m"

    def fill(self,colour,character = "█"):
        for y in range(self.height):
            for x in range(self.width):
                self.define(x,y,character,colour)

    def line(self):
        pass



class Image():
    def __init__(self,filename,scale):
        image = []
    
        


