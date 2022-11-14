# ResearchTrack_Assignment1

Goal of the assignment
---------------------------

The goal of this assignment is to write a python code such that the robot will firstly search for a silver token in the enviroment, grab it and then put it near a golden one, such that at the end we will see every silver token paired to a golden one, as follows:

![Final configuration](screenshot_fine.png)

Flowchart
---------------------------

The code that I wrote uses one while loop that keeps iterating until all six golden tokens are paired to every silver one, to differentiate between silver and golden tokens I used the boolean variable "silver" that changes its value based on the token I want the robot to search for.
 the robot will turn until it finds a token that isn't already paired, then the robot will align with it and aproach it, then, based on the colour of the token, the robot, will either grab it, register its code in the list silver_token (used to distinguish the silver boxes that are already paired from the ones that aren't) and move it near a golden one, or release it, register the code of the golden token in the list golden_token
To command the robot I used one while loop that keeps iterating until the list that collects the golden tokens paired is filled with all of the golden tokens, to diffentiate between silver and golden tokens is used a boolean variable that changes value based on the token I want the robot to search(??????????); the code can be described with the following flowchart:

![Code flowchart](FlowChartAssignment1.png)

how to run the code:?

possible improvements: make a code that can adapt to every situation: avoid tokens in the way between the silver and the golden one, find a way to make it stopa after pairing every token, not based on the lenght of a list... (magari fargli scannerizzare tutta l'arena all'inizio, registrare il numero di siler e golden token, salvarlo su una variabile e farlo fermare dopo che la lista ha raggiunto quel numero
