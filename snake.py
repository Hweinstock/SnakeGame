class snake():
    
    def __init__(self, game):
        self.game = game
        self.direction = 0
        self.x = self.game.SCREEN_WIDTH / 2
        self.y = self.game.SCREEN_HEIGHT / 2
        self.tailLength = 1
        self.tail = []
        
    def show(self):
        fill(255)
        rect(self.x, self.y, self.game.TILE, self.game.TILE)
    
    def die(self):
        clear()
        self.game.pause *= -1
        self.game.function_gameOver(self.tailLength)
    
    def checkBounds(self):
        if self.x > self.game.SCREEN_WIDTH - self.game.TILE + self.game.BUFFER or self.x < -1 * self.game.BUFFER:
            self.die()
        elif self.y > self.game.SCREEN_HEIGHT - self.game.TILE + self.game.BUFFER or self.y < -1 * self.game.BUFFER:
            self.die()
    
    def updateTail(self):

        for t in self.tail[0:-1]:
            if self.game.function_within(self.x, t[0], self.y, t[1], 3) and t != self.tail[-1]:
                self.die()
                
        if len(self.tail) < self.tailLength:
            self.tail.append([self.x, self.y])
        else:
            self.tail.append(self.tail.pop(0))
            self.tail[-1] = [self.x, self.y]
    
        for t in range(len(self.tail)):
            
            fill(255 - (len(self.tail)-t)*10 , 255 - (len(self.tail)-t)*10, 255)
            rect(self.tail[t][0], self.tail[t][1], self.game.TILE, self.game.TILE)
    
    def update(self):
        
        self.x += int(self.game.TILE*cos(self.direction))
        self.y += int(self.game.TILE*sin(self.direction))
        self.show()
        
        self.checkBounds()
        if self.tailLength > 0:
            self.updateTail()
        
    def turn(self, k):
        if k == UP and self.direction != PI / 2:
            self.direction = 3 *PI / 2
        elif k == DOWN and self.direction != 3 *PI / 2:
            self.direction = PI / 2
        elif k == LEFT and self.direction != 0:
            self.direction = PI
        elif k == RIGHT and self.direction != PI:
            self.direction = 0
            
    def reset(self):
        self.direction = 0
        self.x = self.game.SCREEN_WIDTH / 2
        self.y = self.game.SCREEN_HEIGHT / 2
        self.tailLength = 1
        self.tail = []
        
    
                
        
    
    
