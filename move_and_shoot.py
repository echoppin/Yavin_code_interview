
class Move():
    def organize_back_to_strange_string(self, ship, hit):
        to_return = "(" + str(ship["x"]) + "," + str(ship["y"]) + "," + str(ship["orientation"]) + ")" 
        if hit:
            return to_return + " SUNK"
        else:
            return to_return

    def shooting(self, ship_to_move, second_ship, shot):

        if int(shot["x"]) == ship_to_move["x"] and int(shot["y"]) == ship_to_move["y"]:
            ship_to_move_str = self.organize_back_to_strange_string(ship_to_move, True)
            second_ship_str = self.organize_back_to_strange_string(second_ship, False)
        elif int(shot["x"]) == second_ship["x"] and int(shot["y"]) == second_ship["y"]:
            ship_to_move_str = self.organize_back_to_strange_string(ship_to_move, False)
            second_ship_str = self.organize_back_to_strange_string(second_ship, True)
        else:
            ship_to_move_str = self.organize_back_to_strange_string(ship_to_move, False)
            second_ship_str = self.organize_back_to_strange_string(second_ship, False)
        return ship_to_move_str + "\n" + second_ship_str

    def check_still_in_table(self, table_size, ship):
        if 0 <= ship["x"] <= table_size and 0 <= ship["y"] <= table_size:
            return True
        else:
            quit("exited table limits")

    def check_same_position(self, ship_to_move, second_ship):
        if ship_to_move["x"] == second_ship["x"] and ship_to_move["y"] == second_ship["y"]:
            quit("the ships ended in the same position")
        else:
            return True

    def moving(self, table_size, ship_to_move, actions, second_ship, shot):
        compas = "NESW"
        for move in actions:
            index = compas.find(ship_to_move["orientation"])
            if move == "L":
                if index == 0:
                    ship_to_move["orientation"] = compas[3]
                else:
                    ship_to_move["orientation"] = compas[index-1]
            elif move == "R":
                if index == 3:
                    ship_to_move["orientation"] = compas[0]
                else:
                    ship_to_move["orientation"] = compas[index+1]
            elif move == "M":
                if ship_to_move["orientation"] == "N":
                    ship_to_move["y"] += 1
                elif  ship_to_move["orientation"] == "E":
                    ship_to_move["x"] += 1
                elif  ship_to_move["orientation"] == "S":
                    ship_to_move["y"] -= 1
                elif  ship_to_move["orientation"] == "W":
                    ship_to_move["x"] -= 1
                self.check_still_in_table(table_size, ship_to_move)
        self.check_same_position(ship_to_move, second_ship)
        return self.shooting(ship_to_move, second_ship, shot)