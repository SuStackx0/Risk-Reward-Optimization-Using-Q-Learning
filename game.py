import random

class BettingGame:
    def __init__(self):
        self.coins=100
        self.win_prob=0.6
        
        
    def step(self,bet:int):
        if bet>self.coins:
            bet=self.coins
            
        win=random.random() < self.win_prob
        
        old_coins=self.coins
        
        # if win:
        #     self.coins += bet
        # else:
        #     self.coins -= bet
        if not win:
            self.coins -=bet
        else :
            self.coins +=bet
            
        reward=self.coins-old_coins
        
        return self.coins,reward,win
    
    
game = BettingGame()

coins, reward, win = game.step(1)

print("coins= ", coins)
print("reward = ",reward)
print("win = ",win)
