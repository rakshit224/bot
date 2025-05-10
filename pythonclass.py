class player:
    player_team = "team1"
    def __init__(self,runrate,bowlingrate):
        self.runrate = runrate
        self.bowlingrate = bowlingrate
    def print_player(self):
        print(f"Player runrate {self.runrate} player's bowlingrate {self.bowlingrate} and team is {player.player_team} ")
    def is_allrounder(self):
        if self.runrate >= 10 and self.bowlingrate <=20:
            return "TRUE"
        else:
            return "FALSE"
p1= player(7,20)
p2= player(25,12)
p1.print_player()
p2.print_player()
print(p1.is_allrounder())
print(p2.is_allrounder())
print(player.player_team) 

        
            