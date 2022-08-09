# button.py
# partial code from Zelle chapter 10 (pp. 324)


from graphics import *

#define button class
class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns true if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        #initialize variables
        w, h = width / 2, height / 2
        x, y = center.getX(), center.getY() #2 points from the center
        self.xmin, self.xmax = x - w, x + w
        self.ymin, self.ymax = y - h, y + h #boundary values

        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        #draw button rectangle
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        
        #draw label
        self.label = Text(center, label)
        self.label.draw(win)

        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"

        #test if the point is within the rect area
        #the button must be active to be clicked

        #if (self.active not True):
            #return False

        return (self.active and
                self.xmin < p.getX() < self.xmax and #if the 3 conditions are true - button is clicked
                self.ymin < p.getY() < self.ymax)
            #return True
        #else:
            #return False #if at least one of the 3 conditions not true -- will return false
        
    def getLabel(self):
        "Returns the label string of this button."

        #
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        #change label color to black
        self.label.setFill('black')
        
        #change active status to true
        self.active = True
    def deactivate(self):
        "Sets this button to 'inactive'."

        #change label color to darkgrey
        self.label.setFill('darkgray')
        
        #change active status to false
        self.active = False
        
def main():
    
    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    ##testing Button constructor
    rollButton = Button(win, Point(5,4), 6, 1, "Roll Dice")
    quitButton = Button(win, Point(5,1), 2, 1, "Quit")

    ##testing activate method
    rollButton.activate()

    ##testing clicked() method
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        #when roll button is clicked
        if rollButton.clicked(pt):
            #activate the quit button
            quitButton.activate()
        pt = win.getMouse()
    
    #if quit button is clicked, then loop is broken
    #and we reach this line of code
    win.close()
    
if __name__ == "__main__":
    main()
