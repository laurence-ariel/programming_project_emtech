# programming_project_emtech


## Overview of Battle Sequence

Phase 0: launch program, starting variable
    show header and game rules.
    prompt for player names, assign default names if left blank.

Phase 1: Status reporting
    Display each player's HP and Energy levels at the start, after each sequence (phase 3), and after overheating (phase 4)\
    
Phase 2: input and validation
    3 digit number (no more no less)
    Must be only 1, 2, 3 (both players)
    Reprompts if invalid input

Phase 3: resolution
    program iterates through sequences 1, 2, 3
    after every individual sub sequence, program prints current HP and Energy of both players
    checks for win condition (hp <= 0) (turn ends immediately if win condition is met)

Phase 4: Server event (overheat)
    every 3 turns, server overheats
    -10 hp both players
    show Post-overheat status report (updated hp and energy)

Draw logic: checks if both players have hp <= 0 at the same time for a "Double KO"


## Limitations:

For loops, loop control statements

Advanced data types and corresponding operations
