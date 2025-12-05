

class Screen():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.screen = []
        self.previosly_rendered_screen = None
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

    def line(self):
        pass


#testing code

s = Screen(20,10)
x = 0
y = 0

while True:
    s.define(x,y,"█")
    x = x + 1
    y = y + 1
    if x >= 20:
        x = 0
    if y >= 10:
        y = 0
    s.define(x,y,"█",(255,0,0))
    s.render()