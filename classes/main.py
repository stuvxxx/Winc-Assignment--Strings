# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'


# Add your code after this line

class Player:
    def __init__(self, name, speed, endurance, accuracy):
        float_array = [0, 0.1 , 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        if speed not in float_array:
            raise ValueError
        if endurance not in float_array:
            raise ValueError
        if accuracy not in float_array:
            raise ValueError
        else:
            self.name = name
            self.speed = speed
            self.endurance = endurance
            self.accuracy = accuracy

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."

    def strength(self):
        spd = ("speed", self.speed)
        end = ("endurance", self.endurance)
        acc = ("accuracy", self.accuracy)
        highest = max(spd[1], end[1], acc[1])
        if highest in spd:
            return spd
        if highest in end: 
            return end
        if highest in acc:
            return acc

        
Marc = Player("Marc", 0.8, 0.8, 0.7)
print(Marc.strength())


class Commentator:
    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        return player.speed + player.accuracy + player.endurance

    def compare_players(self, player1, player2, att):
        if att == "speed":
            result = player1.speed - player2.speed
            if result == 0:
                strength_result = player1.strength()[1] - player2.strength()[1]
                if result > 0:
                    return player1.name
                else:
                    return player2.name
            if result > 0:
                return player1.name
            else:
                return player2.name
            if result == 0:
                strength_result = player1.strength() - player2.strength()
                print(strength_result)
                if result > 0:
                    return player1.name
                else:
                    return player2.name
        if att == "accuracy":
            result = player1.accuracy - player2.accuracy
            if result > 0:
                return player1.name
            else:
                return player2.name
        if att == "endurance":
            result = player1.endurance - player2.endurance
            if result > 0:
                return player1.name
            else:
                return player2.name
alice = Player('Alice', 0.8, 0.2, 0.9)
bob = Player('Bob', 0.8, 0.2, 0.1)
ray = Commentator('Ray Hudson')
print(ray.compare_players(alice, bob, 'speed'))

        


