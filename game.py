class game():
    
    def __init__(self):
        
        self.SCREEN_WIDTH = 600
        self.SCREEN_HEIGHT = 600
        self.TILE = self.SCREEN_WIDTH/40
        self.BUFFER = self.TILE/2
        self.speed = 15
        self.pause = 1
        self.over = False
        
        
    def function_within(self, x1, x2, y1, y2, r):
        if r/self.TILE >= (abs(x1 - x2)**2 + abs(y1 - y2)**2)**0.5:
            return True
        return False
     
    def function_gameOver(self, score):
        self.over = True
        clear()
        textSize(35)
        textAlign(CENTER)
        text("You recieved a score of " + str(score), self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2)
    
    def displayScore(self, score):
        textSize(15)
        textAlign(CENTER)
        text(str(score), self.SCREEN_WIDTH / 2, 25)
        
    def reset(self, s, f):
        clear()
        self.pause *= -1
        self.over = False
        
        s.direction = 0
        s.x = self.SCREEN_WIDTH / 2
        s.y = self.SCREEN_HEIGHT / 2
        s.tailLength = 1
        s.tail = []
        
        f.x = int(random(0, self.SCREEN_WIDTH / self.TILE)) * self.TILE
        f.y = int(random(0, self.SCREEN_HEIGHT / self.TILE)) * self.TILE
        f.col = [255, 0, 0]
         
