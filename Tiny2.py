

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
        output = ""
        for y in range(len(self.screen)):
            for x in range(len(self.screen[y])):
                output = output+str(self.screen[y][x])
            output = output+"\n"

        print(output, end="")


s = Screen(20,10)

s.render()