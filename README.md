# Programing Final Project

The basic idea for this final project is a game with the same physics of the original Legend Of Zelda game. In the game the charecter will be moving along an x and y axis. Each screen will be a "Level" class. This class wil be a collection of "Wall" classes. The charecter will not be able to colide with these walls. let me elaborate:

Wall class: 
litterally just a rectangle, until the graphics are done. You specify the x, y, width, and height in the __init__.

Charecter class:
right now it is a circle, but soon it will be an image of a swordsman. This also has you specify the x, y, width and height. But in this class is where all of the collision detection will take place. It will have a boolean for each side of the wall and it will return True if the charecter is touching the wall and False if not. It will then move away acordingly.

Level class:
Will be a specified collection of walls. Just like in the zelda game, when you move out of frame of the walls, a new "Level" class will start. This will give the effect of moving between rooms or areas within the game.

All of this will be created in PyCharm using PyGame. Though i might choose to use processing instead.

