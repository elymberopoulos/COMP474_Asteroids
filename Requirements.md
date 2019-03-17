Class: COMP 474 - 001 - Software Engineering

Instructor: Christopher Stone

Overview:
The goal of this project is to create a classic asteroids clone. A link to a suitable example can be found here: 

http://www.arcadedivision.com/classicgame5/shooting/asteroids.html

Language: The game will be created in python using the pygame engine.

User Stories:

###----------Beginning Conditions----------###
1. There will be a welcome screen that displays the name of the game and the controls.
2. If the user presses the spacebar, the game will begin.
3. The game can be paused at any time by pressing the “p” key.

###----------Space----------###
4. The game takes place in a 2D space with a defined area. 
5. If an object reaches the edge of the 2D space, the object will wrap around to the other side of the space

###----------Player’s Ship----------###
6. The ship should be able to rotate.
7. The ship can apply a force vector in the direction it is pointing.
8. When the ship is attempting to move forward, a “flame” can be seen from the ship’s engine, and a “engine” sound will play.
9. The ship should move as if it were in real space e.g. an object in motion stays in motion

###----------Cannon----------###
10. As a player, I want to be able to shoot the asteroids with a cannon
11. Only 5 cannon balls are allowed on the field at the same time
12. The cannon balls have a limited range

###----------Asteroids----------###
13. When the asteroids are hit by a cannon ball or ship, I want the asteroids to break apart into multiple pieces and play a sound.
14. After some number of divisions, the asteroids cannot be broken apart anymore. If the asteroid cannot be broken apart, then it is destroyed.
15. If an asteroid is broken apart or destroyed, the score is increases.
16. If the ship comes in contact with an asteroid, the ship is destroyed and loses a life from some total of lives.

###----------Baddies----------###
17. There are alien ships that appear at some interval to harass the player.
18. As the levels increase, the rate the alien ships appear will increase. 
19. If there is an alien ship in play, a distinctive sound will play.
20. The alien ships will attempt to fire their cannon at the player.
21. If the alien cannon ball hits the player, the player is destroyed and loses a life
22. If the alien ship hits the player, the player is destroyed and loses a life
23. The alien ship can be destroyed by touching the player’s cannon balls.

###----------End Conditions----------###
24. A level is completed once all asteroids and alien ships are destroyed. 
25. Once a level is completed, the field will reset with more asteroids than the previous stage, and the score will increase.
26. If the player runs out of lives, the score will be displayed prominently and the game will reset. 

