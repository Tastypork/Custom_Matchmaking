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
        self.allowed_roles = None
        return

    def get_allowed_roles(self) -> list:
        if self.allowed_roles:
            return self.allowed_roles

        self.allowed_roles = [0,0,0]
        if self.tank_elo:
            self.allowed_roles[0] = 1
        if self.dps_elo:
            self.allowed_roles[1] = 1
        if self.supp_elo:
            self.allowed_roles[2] = 1
        return self.allowed_roles

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
    
    def get_avg_mmr_high(self):
        sum = 0
        for i in self.players:
            sum += i.get_highest_mmr()
        return sum//6

    def get_avg_mmr_role(self):
        sum = 0
        for i in range(len(self.players)):
            break

    def fill_players(self, arr):
        self.players = arr

    def slot_player(self, player, arr):
        pass



class Game:
    def __init__(self, members) -> None:
        self.team1 = Team()
        self.team2 = Team()
        self.players = [] 
        for i,j in members.items():
            self.players.append(Player(i,j[0],j[1],j[2]))

    def matchmaking_combo(self):
        count_ok = 0
        max_gap = 0
        min_gap = 5000
        pool = list(itertools.combinations(self.players,6))
        reasonable = []
        for i in range(len(pool)//2):
            self.team1.fill_players(pool[i])
            self.team2.fill_players(pool[-(i+1)])
            a = self.team1.get_avg_mmr_high()
            b = self.team2.get_avg_mmr_high()
            diff = abs(a - b)
            if diff < min_gap:
                min_gap = diff
            if diff > max_gap:
                max_gap = diff
            if diff < 200:
                count_ok += 1
                reasonable.append((pool[i], pool[-(i+1)]))
        return reasonable

    def matchmaking(self):
        self.players.sort(key=lambda player: sum(player.get_allowed_roles()))
        for i in self.players:
            roles = i.get_allowed_roles()
            team1_mmr = self.team1.get_avg_mmr_role
            team2_mmr = self.team2.get_avg_mmr_role

            if sum(roles) == 1:
                break

            elif sum(roles) == 2:
                break
            else:
                break


def main():
    """
    Extras:
    "Kyanite" : [2200, 2400, 2300]
    "MeloStan" : [3100, 0, 0]
    "DemonWolf" : [1700, 1600, 0]
    
    """
    members = {
            "Kazumi" : [0, 0, 1700],
            "MaleABG": [2000, 1300, 1600],
            "Greasybacon": [2100, 1600, 2300],
            "Stark": [2300, 2000, 1900],
            "Tastypork": [1800, 2300, 1700],
            "Dark" : [3200, 3100, 3600],
            "Sinyx" : [0, 3100, 0],
            "Vaykyll" : [2800, 0, 2900],
            "Shivers": [0, 0, 2700],
            "Zen" : [0, 3550, 3400],
            "Socd" : [2200, 0, 0],
            "Hanzbro" : [1700, 1800, 1700]
        }
    
    game = Game(members)
    mom = game.matchmaking_combo()

    rand = random.randint(0, len(mom))
    
    for i in mom[rand]:
        print("Team:")
        for j in i:
            print(j.get_name())
        print()
        print()
    
if __name__ == "__main__":
    main()
