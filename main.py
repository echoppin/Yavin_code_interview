
import sys
from move_and_shoot import Move

class InitBoard():
    def check_orientation(self, orientation):
        if orientation in "NEWS":
            return True
        else:
            quit("Wrong ship orientation")

    def ship_to_dict(self, ship):
        if ship[1].isnumeric() and ship[1].isnumeric() and self.check_orientation(ship[5]):
            final_ship = {}
            final_ship["x"] = int(ship[1])
            final_ship["y"] = int(ship[3])
            final_ship["orientation"] = ship[5]
            return final_ship
        else:
            quit("Ship coordinated are not numbers")

    def ship_to_move(self, ship_to_move):
        final_ship_to_move = {}
        final_ship_to_move["x"] = ship_to_move[1]
        final_ship_to_move["y"] = ship_to_move[3]
        if ship_to_move[1].isnumeric() and ship_to_move[1].isnumeric():
            if int(final_ship_to_move["x"]) == self.ship_1["x"] and int(final_ship_to_move["y"]) == self.ship_1["y"]:
                self.ship_moving = 1
            elif int(final_ship_to_move["x"]) == self.ship_2["x"] and int(final_ship_to_move["y"]) == self.ship_2["y"]:
                self.ship_moving = 2
            else:
                quit("Wrong ship to move")
        else:
            quit("ship to move is not numeric")
            
    def check_action(self, actions):
        actions_allowed = "MRL"
        for action in actions:
            if action not in actions_allowed:
                quit("Wrong actions")
        self.actions = actions
        return True

    def shoot(self, shot):
        if shot[1].isnumeric() and  shot[3].isnumeric():
            self.shot = {}
            self.shot["x"] = shot[1]
            self.shot["y"] = shot[3]
        else:
            quit("shooting direction is not a number")
    def table(self, table_size):
        if table_size.isnumeric():
            self.table_size = int(table_size)

    def init_variables(self, argv):
        
        self.table(argv[1])
        self.ship_1 = self.ship_to_dict(argv[2])
        self.ship_2 = self.ship_to_dict(argv[3])
        self.ship_to_move(argv[4])
        self.check_action(argv[5])
        self.shoot(argv[6])
        self.move = Move()
        if self.ship_moving == 1:
            return print(self.move.moving(self.table_size, self.ship_1, self.actions, self.ship_2, self.shot))
        else:
            return print(self.move.moving(self.table_size, self.ship_1, self.actions, self.ship_2, self.shot))

init = InitBoard()
init.init_variables(sys.argv)

# You can run the program by running in your command line
# python main.py 10 "(0,0,W)" "(9,2,E)" "(0,0)" "RRMMM" "(3,0)"