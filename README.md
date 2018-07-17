Using Python3.7


### Overview

  * The application is a simulation of a toy robot moving on a square tabletop, of dimensions **5 x 5 units**.
  * There are no other obstructions on the table surface.
  * The robot is free to roam around the surface of the table, but must be prevented from falling to destruction
    - Any movement that would result in the robot falling from the table should be **ignored**;
    - Further valid movement commands must still be allowed.

### Command Forms

  * Create an application that can read in commands of the following form:

```
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
```

  * *PLACE* will put the toy robot on the table in position X,Y and facing **NORTH**, **SOUTH**, **EAST** or **WEST**.
  * The origin (0,0) can be considered to be the **SOUTH WEST** most corner.
  * The toy robot is implicitly positioned at **0,0,NORTH**, unless an initial *PLACE* command is given
  * After that, any sequence of commands may be issued, in any order, including another *PLACE* command.
  * *MOVE* will move the toy robot one unit forward in the direction it is currently facing.
  * *LEFT* and *RIGHT* will rotate the robot 90 degrees in the specified direction without changing the position of the robot
    - (i.e. counter-clockwise and clockwise, respectively)
  * *REPORT* will announce the **X,Y** and **F** of the robot.
    - This can be in any form, but standard output is sufficient.

### Constraints

  * The toy robot must not fall off the table at any point.
  * Any move that would cause the robot to fall must be ignored.

## Expectations

  * Input can be from a file, or from standard input, as the developer chooses.
  * Provide test data to exercise the application.

## Examples

Without an initial *PLACE* command (implicit **0,0,NORTH**):

    MOVE
    REPORT
    Output: 0,1,NORTH

With an initial *PLACE* command:

    PLACE 1,2,EAST
    MOVE
    MOVE
    LEFT
    MOVE
    REPORT
    Output: 3,3,NORTH

With an ignored invalid move

    PLACE 0,0,NORTH
    LEFT
    MOVE
    MOVE
    MOVE
    RIGHT
    MOVE
    REPORT
    Output: 0,1,NORTH

## Deliverables

  * The source files, the test data and any automated test code, if used.
  * It is not required to provide any graphical output showing the movement of the toy robot.
