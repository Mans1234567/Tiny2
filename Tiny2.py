

class Screen():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.screen = []
        for y in range(0,self.height):
            line = []
            for x in range(0,self.width):
                line.append(" ")

    def render(self,matrix, system="windows"):
        output = ""
