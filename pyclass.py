class ipl:
    team = "mumbai_indians"
    status = "retained"
    def __init__(self,player_name,type,strike_rate):
        self.player_name  = player_name
        self.type =  type
        self.strike_rate = strike_rate
    def print_player(self):
        print(f"| {self.player_name } | {self.type } | {self.strike_rate} | {ipl.team} | {ipl.status} |  ")    
p1= ipl('Rohit_sharma', 'right hand batsmen',200)        
p2= ipl('suryakumar yadav', 'left hand batsmen',198)
p3= ipl('hardik pandya','left hand batsmen',199)
p4= ipl('tilak verma','left hand batsmen',180)
p5= ipl('jasprit bumrah','right hand batsmen',150)
p1.print_player()
p2.print_player()
p3.print_player()
p4.print_player()
p5.print_player()

