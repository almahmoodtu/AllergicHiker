"""
ALLERGIC HIKER
"""


'''IMPORTS'''
import random


'''CLASS'''
class Player:

    def __init__(self, name: str, x: int = 0, y: int= 0) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.path = []

    def __repr__(self):
        return f"Current location of {self.name}: ({self.x}, {self.y})"

    def go_left(self, distance: int) -> str:
        if self.x > 0:
            self.x -= distance
            return f'\t{self.name}: Motion complete'
        else:
            return f'\t{self.name}: Motion not allowed'

    def go_right(self, distance: int) -> str:
        self.x += distance
        return f'\t{self.name}: Motion complete'

    def go_up(self, distance: int) -> str:
        self.y += distance
        return f'\t{self.name}: Motion complete'

    def go_down(self, distance: int) -> str:
        if self.y > 0:
            self.y -= distance
            return f'\t{self.name}: Motion complete'
        else:
            return f'\t{self.name}: Motion not allowed'

    def show_path(self):
        return f"\tPath of {self.name}: ({self.path})"

    def save_path(self) -> None:
        self.path.append(f"({self.x}, {self.y})")

    def enemy_direction(self):
        return random.choice(['w', 'a', 's', 'd'])

    def motion(self, user_input: str):
        task = {
            'w': self.go_up,
            'a': self.go_left,
            's': self.go_down,
            'd': self.go_right,
            'o': self.go_up,
            'l': self.go_left,
            'u': self.go_down,
            'r': self.go_right,
        }
        try:
            result = task.get(user_input)(1)
            self.save_path()
            return result
        except TypeError:
            return 'Invalid input'

    def current_location_display(self):
        return f"Current location of {self.name}: ({self.x}, {self.y})"

    def current_location(self):
        return f"({self.x}, {self.y})"

    def current_location_coordinates(self):
        return self.x, self.y


'''OUTSIDE CLASS'''
def blitz(me_x, me_y, enemy_x, enemy_y):
    chance = random.randint(1, 2)
    difference = abs(me_x - enemy_x) + abs(me_y - enemy_y)
    if difference <= 4 and chance == 1:
        return f"DISTANCE {difference} i.e. POLEN ATTACK!"
    elif difference <= 4 and chance == 2:
        return f"DISTANCE {difference} i.e. CONGRATS! POLEN DODGED!"
    else:
        return f"DISTANCE {difference} i.e. SAFE!"


'''SETTING UP PLAYERS'''
me = Player('ALLERGIC HIKER')
print(me.current_location_display())

enemy = Player('POLEN', 4, 4)
print(enemy.current_location_display())


'''GAME BEGINS'''
while me.current_location() != enemy.current_location():
    direction = str(input("\t>> Enter direction WASD/OLUR (or show/quit): ")).lower()
    if direction == "quit":
        print("QUITTER!")
        break
    elif direction == "show":
        print(me.show_path())
        print(enemy.show_path())
    else:
        print(me.motion(direction))
        print(enemy.motion(enemy.enemy_direction()))
    print(me.current_location_display())
    print(enemy.current_location_display())

    '''checking distance'''
    me_x, me_y = me.current_location_coordinates()
    enemy_x, enemy_y = enemy.current_location_coordinates()
    enemy_fire = blitz(me_x, me_y, enemy_x, enemy_y)
    print(enemy_fire)

    if 'ATTACK' in enemy_fire:
        print("ALLERGIC REACTION! GAME OVER!")
        break

else:
    print("GAME OVER!")
