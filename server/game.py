#!/usr/bin/python

import time

""" This represents a ball object in pong """
class Ball:
    def __init__(self, position_x, position_y, direction, speed):
        self.px = position_x  # x coordinate (in pixels)
        self.py = position_y  # y coordinate (in pixels)
        self.dir = direction  # ball direction (in degrees)
        self.vel = speed      # ball velocity (in pixels per second)

    def update(self):
        print 'update'

    def serialize(self):
        return ','.join([str(self.px), str(self.py)])

""" This represents a player object in pong """
class Player:
    def __init__(self, section_id, paddle_place, paddle_size, player_id):
        self.sid = section_id      # Section enum representing where we are
        self.place = paddle_place  # Place of the paddle relative to the section
        self.size = paddle_size    # Size of the paddle, this is for the future
        self.id = player_id        # ID of the player, preferably FBID

    def serialize(self):
        return ','.join([str(self.place), str(self.size)])

""" This keeps track of the game state for pong """
class GameState:
    def __init__(self, num_players):
        self.players = [ Player(i, 0, 0, 0) for i in range(num_players) ]
        self.ball = Ball(0, 0, 0, 0)

    def runInstance(self):
        self.ball.update();

    def run(self):
        # Wake up every 10ms
        while True:
            self.runInstance()
            time.sleep(.01)

    def serialize(self):
        parts = [ self.ball.serialize() ]
        for player in self.players:
            parts.append(player.serialize())
        return '\n'.join(parts)

""" TESTING """
if __name__ == '__main__':
    plr = Player(10, 0, 0, 0)
    print plr.sid
