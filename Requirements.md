# Class: COMP 474 - 001 - Software Engineering

#### Instructor: Christopher Stone

##### Project Team:
* Eric Lymberopoulos [Programmer]
* Jarod Navarro [Programmer]
* Jay Kinzie [Programmer]
* Wei Zhang [Programmer]

##### Document Authors:
* Eric Lymberopoulos
* Jarod Navarro
* Jay Kinzie
* Wei Zhang

#### Document Revision History
1. Date: 3/17/19, Jay Kinzie - Added User Stories to the document.
2. Date: 3/17/19, Eric Lymberopoulos - Added Functional Requirements, Non Functional Requirements, Constraints, Glossary.
3. Date: 3/19/19, Eric Lymberopoulos - Added a non-functional requirement. Also added Wei Zhang to the document and project.
4. Date: 3/20/19, Wei Zhang - Added non-functional requirements, Development and Target platforms and Constraints. 
5. Date: 3/20/19, Jarod Navarro - Added End Conditions requirement.
6. Date: 4/2/19, Eric Lymberopoulos - Altering non-functional requirements for less abstract wording.

Overview:
The goal of this project is to create a classic asteroids clone. A link to a suitable example can be found here: 
http://www.arcadedivision.com/classicgame5/shooting/asteroids.html

## Functional Requirements
1. Initial Screen - The welcome menu shall have an option to start the game.
2. Pause Game - If the player presses the pause button "p" then the game shall freeze and be able to be restarted.
3. Map Wrap Around - If the player's ship goes beyond the edge of the map then the ship shall
					  appear at the other side of the map.
4. Ship Rotation - The ship shall be able to rotate in the 2D plane.
5. Ship Thruster - The ship shall be able to propel itself in the direction it is facing.
6. Thruster Details - The ship's thruster shall have a flame and play audio when the user is moving the ship.
7. Inertia - The ship shall continue to move after the user stops pressing the thruster button.
8. Ship Combat - The user shall be able to fire the cannon on the ship. The projectiles will have
				 a limited range and only five can be on the screen at any given time.
9. Asteroids - Upon being hit by the ship's cannon the asteroid shall break into smaller pieces.
			   If the asteroid is in its smallest size then it shall be destroyed and the player score incremented.
10. Ship Collision - If the player's ship collides with an asteroid then it shall be destroyed.
11. Alien Ship - At random points an alien ship shall enter the map.
12. Alien Ship Sound - The alien ship shall have a distinct sound when it is spawned.
13. Alien Ship Combat - The alien ship shall shoot projectiles at the player. If the player's ship is hit
						It shall kill the player and a life will be deducted from the player. If the player
						collides with the alien ship the player shall die and a life will be deducted.

## Nonfunctional Requirements
1. The game shall have the ability to recover from errors so the program does not crash.
3. The game shall be testable.
4. The game shall have clean and legible code with comments for easy maintainability.

## Constraints
* No more than one player shall be able to play this game at one time. 

## Development and Target Platforms
* The project shall be implemented using Pygame 1.9.4 and the Python3 programming language.

### Project Glossary
* Pygame - Pygame is a cross-platform set of Python modules designed for writing video games.
		   It includes computer graphics and sound libraries designed to be used with the Python programming language.
 		   
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
27. If this is not the player's first time playing, the high score history will be displayed. Can be saved in a text file.
28. If the player beats the high score, allow the player to type in their 3 initials, as they would in a normal arcade.

