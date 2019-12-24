from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.uix.behaviors import FocusBehavior

class Bomberman(Widget, FocusBehavior):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def __init__(self, *args, **kwargs):
    	super().__init__(*args, **kwargs)
    	self.focus=True

    def move(self, key):
    	step=10

    	if key=='up':
    		self.pos = self.pos[0], self.pos[1]+step
    	elif key=='down':
    		self.pos = self.pos[0], self.pos[1]-step
    	elif key=='right':
    		self.pos = self.pos[0]+step, self.pos[1]
    	elif key=='left':
    		self.pos = self.pos[0]-step, self.pos[1]
    	else:
    		return False
    	return True
        # self.pos = Vector(*self.velocity) + self.pos

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
    	if keycode[1] in ['left', 'up', 'right', 'down']:
    		print(keycode[1])
    		self.move(keycode[1])


class Jeu(Widget):
    perso = ObjectProperty(None)

    def serve_ball(self):
        self.perso.center = self.center
        self.perso.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.perso.move()

        # bounce off top and bottom
        if (self.perso.y < 0) or (self.perso.top > self.height):
            self.perso.velocity_y *= -1

        # bounce off left and right
        if (self.perso.x < 0) or (self.perso.right > self.width):
            self.perso.velocity_x *= -1


class BombermanApp(App):
    def build(self):
        game = Jeu()
        game.serve_ball()
        # Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    BombermanApp().run()