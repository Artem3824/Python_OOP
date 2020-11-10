from player import Player
import re


class Game:
    def __init__(self):
        self.player = Player()

    def render_map(self):
        s = """****\n****"""
        li = s.split('\n')
        row = li[self.player.position[1]]
        row = row[:self.player.position[0]] + 'x' + row[self.player.position[0] + 1:]
        li[self.player.position[1]] = row
        s = '\n'.join(li)
        print(s)

    def move_player(self, destination):
        '''destination = w, s, a, d'''
        if destination == 's':
            self.player.position[1] += 1


game = Game()
game.render_map()
