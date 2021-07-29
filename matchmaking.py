import math
import itertools
import random

class Player:
    def __init__(self, name = "Kazumi", tank = 0, dps = 0, supp = 0) -> None:
        self.name = name
        self.tank_elo = tank
        self.dps_elo = dps
        self.supp_elo = supp
        self.num_roles = math.ceil(tank/5000) + math.ceil(tank/5000) + math.ceil(tank/5000)
        return

    def get_allowed_roles(self) -> list:
        ret = [0,0,0]
        if self.tank_elo:
            ret[0] = 1
        if self.dps_elo:
            ret[1] = 1
        if self.supp_elo:
            supp[1] = 1
        return ret

    def get_mmr(self, role):
        if role == 0:
            return self.tank_elo
        elif role == 1:
            return self.dps_elo
        elif role == 2:
            return self.supp_elo

    def get_highest_mmr(self):
        return max(self.tank_elo,self.dps_elo,self.supp_elo)

    def get_name(self):
        return self.name

class Team:
    def __init__(self) -> None:
        self.tank_slots = 2
        self.dps_slots = 2
        self.supp_slots = 2
        self.players = [None]*6
        return
    
    def get_slots(self) -> list:
        return [tank_slots, dps_slots, supp_slots]
    
    def get_avg_mmr(self):
        sum = 0
        for i in self.players:
            sum += i.get_highest_mmr()
        return sum//6
    
    def fill_players(self, arr):
        self.players = arr


class Game:
    def __init__(self) -> None:
        self.team1 = Team()
        self.team2 = Team()
        self.players = [] 
        
    def matchmaking(self, members):
        ones = []
        twos = []
        threes = []

    def matchmaking_combo(self, members):
        for i,j in members.items():
            self.players.append(Player(i,j[0],j[1],j[2]))
        
        count_ok = 0
        max_gap = 0
        min_gap = 5000
        pool = list(itertools.combinations(self.players,6))
        for i in range(len(pool)//2):
            for j in pool[i]:
                print(j.get_name(), end=" ")
            print(',', end=" ")
            for j in pool[-(i+1)]:
                print(j.get_name(), end=" ")
            print()
            self.team1.fill_players(pool[i])
            self.team2.fill_players(pool[-(i+1)])
            a = self.team1.get_avg_mmr()
            b = self.team2.get_avg_mmr()
            diff = abs(a - b)
            if diff < min_gap:
                min_gap = diff
            if diff > max_gap:
                max_gap = diff
            if diff < 200:
                count_ok += 1
        print(count_ok, max_gap, min_gap)


        

        

            



"""
Add sr numbers to each slot in the dictionary. You can use the comment strings to indicate which user is which.
"""
members = {

            1 : [random.randint(1300,4000),random.randint(1300,4000),random.randint(1300,4000)],
            2 : [random.randint(1300,4000),random.randint(1300,4000),random.randint(1300,4000)],
            3 : [random.randint(1300,4000),random.randint(1300,4000),random.randint(1300,4000)],
            4 : [random.randint(1300,4000),random.randint(1300,4000),random.randint(1300,4000)],
            5 : [random.randint(1300,4000),random.randint(1300,4000),random.randint(1300,4000)],
            6 : [random.randint(1300,4000),random.randint(1300,4000),random.randint(1300,4000)],
            7 : [random.randint(1300,4000),random.randint(1300,4000),random.randint(1300,4000)],
            8 : [random.randint(1300,4000),random.randint(1300,4000),random.randint(1300,4000)],
            9 : [random.randint(1300,4000),random.randint(1300,4000),random.randint(1300,4000)],
            10 : [random.randint(1300,4000),random.randint(1300,4000),random.randint(1300,4000)],
            11 : [random.randint(1300,4000),random.randint(1300,4000),random.randint(1300,4000)],
            12 : [random.randint(1300,4000),random.randint(1300,4000),random.randint(1300,4000)]
        }

def main():
    game = Game()
    game.matchmaking_combo(members)
    
if __name__ == "__main__":
    main()

