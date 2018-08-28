class food():
    
    def __init__(self, game):
        self.game = game
        self.x = int(random(0, self.game.SCREEN_WIDTH / self.game.TILE)) * self.game.TILE
        self.y = int(random(0, self.game.SCREEN_HEIGHT / self.game.TILE)) * self.game.TILE
        self.col = [255, 0, 0]
        self.poison = False
        
    def show(self):
        fill(self.col[0], self.col[1], self.col[2])
        rect(self.x, self.y, self.game.TILE, self.game.TILE)

    
    def respawn(self):
        self.col = [255, 0, 0]
        self.x = int(random(0, self.game.SCREEN_WIDTH / self.game.TILE)) * self.game.TILE
        self.y = int(random(0, self.game.SCREEN_HEIGHT / self.game.TILE)) * self.game.TILE
    
    def update(self, snake):
        # if self.col == [0, 255, 0]:
        #     self.poison = True
            
        if self.game.function_within(snake.x + self.game.TILE / 2, self.x + self.game.TILE / 2, snake.y + self.game.TILE / 2, self.y + self.game.TILE / 2, 2):
            if self.poison:
                # snake.die()
                pass
            else:
                self.respawn()
                snake.tailLength += 1
        else:
            self.show()
            
            # if self.col[0] > 0:
            #     self.col[0] -= 1.25
            # if self.col[1] < 255:
            #     self.col[1] += 1.25
    
        

    

        
        
