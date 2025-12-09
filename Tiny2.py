

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
        print("\033[H",end="")
        for y in range(len(self.screen)):
            line = ""
            for x in range(len(self.screen[y])):
                line = line + str(self.screen[y][x])
            print(line)
            

        

    def define(self,x,y,character="█",colour=(255,255,255)):
        r,g,b = colour
        self.screen[y][x] = f"\033[38;2;{r};{g};{b}m{character}\x1b[0m"

    def fill(self,colour,character = "█"):
        for y in range(self.height):
            for x in range(self.width):
                self.define(x,y,character,colour)

    

    def line(self,start,end,colour=(255,255,255)):
        if start[0] == end[0]:
            for y in range(min(start[1],end[1],max(start[1],end[1]))):
                self.define(start[0],y,colour=colour)
        elif start[1] == end[1]:
            for x in range(min(start[0],end[0]),max(start[0],end[0])):
                self.define(x,start[1],colour=colour)
        else: 
            if start[0] > end[0]:
                temp = end
                end = start
                start = temp
            x1,y1 = start
            x2, y2 = end
            m = (y2-y1)/(x2-x1)
            for x in range(x1,x2+1):
                y = int(round((m*x)+y1,0))
                self.define(x,y,colour=colour)
        




class Sprite():
    def __init__(self,x,y,z,image):
        self.x = x
        self.y = y
        self.z = z 
        self.image = image
        assert type(image) == Image, "image must be of type tiny Image"
        

    
    def show(self):
        return self.image
    
    

class Universe():
    def __init__(self):
        self.universe = [] #array of all renderable objects
    


class Image():
    def __init__(self,filename,scale):
        from PIL import Image as im
        self.points = []
        self.width = int(image.width*scale)
        self.hight = int(image.height*scale)
        with im.open(filename).convert('RGB') as image:
            image = image.resize((self.width,self.hight))
            for y in range(0,self.hight):
                line = []
                for x in range(0,self.width):
                    R,G,B = image.getpixel((x,y))
                    line.append((R,G,B))
                self.points.append(line)
    def get_pixels(self):
        return self.points

        


