from __future__ import print_function

import time
from sr.robot import *


a_th = 2.0 #Threshold for the control of the orientation

d_th = 0.4 #Threshold for the control of the linear distance

silver = True;
""" boolean: variable for letting the robot know if it has to look for a silver or for a golden marker"""

R = Robot()
""" Instance of the Class Robot """

golden_token = [] #This will keep track of the silver token that will be moved
silver_token = [] #This will keep track of the golden token that are already paired

def drive(speed, seconds):
    """
    Function for setting a linear velocity:
    Allows the robot to move into a straight line for a certain time and with a defined speed
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity:
    Allows the robot to turn on its axis
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_silver_token():
    """
    Function to find the closest SILVER token

    Returns:
	dist (float): distance of the closest silver token (-1 if no silver token is detected)
	rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)
	code (int): the code of the corresponding token (-1 if no silver token is detected)
    """
    dist=100
    
    #Iterate through all the detected tokens
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER:
            for i in silver_token: #Check that the token isn't already paired
                if i == token.info.code:
                    break
            else: #If it isn't already paired: update distance, rotation and code
                dist=token.dist
	        rot_y=token.rot_y
	        code = token.info.code
	        
    if dist==100:
	return -1, -1, -1
    else:
   	return dist, rot_y, code

def find_golden_token():
    """
    Function to find the closest GOLDEN token

    Returns:
	dist (float): distance of the closest golden token (-1 if no golden token is detected)
	rot_y (float): angle between the robot and the golden token (-1 if no golden token is detected)
	code (int): the code of the corresponding token (-1 if no golden token is detected)
    """
    dist=100
    
    #Iterate through all the detected tokens
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD:
            for i in golden_token: #Check that the token isn't already paired
                if i == token.info.code:
                    break
            else: #If it isn't already paired: update distance, rotation and code 
                code = token.info.code
                dist=token.dist
	        rot_y=token.rot_y
	    
    if dist==100:
	return -1, -1, -1
    else:
   	return dist, rot_y, code
  
#ROBOT OPERATIONAL LOOP

while len(golden_token) < 6: #the iterations will stop when every token is paired

	#The robot will search for a silver token, after grabbing it, it will seacrh for a golden one to complete the pair, this process will be repeated until every token is paired
	if silver == True:
	
		dist, rot_y, code_silver = find_silver_token()
		
	else:
	
		dist, rot_y, code_golden = find_golden_token()       
   
	if dist == -1: # If no token is detected, the robot will turn to search for another one 
       
           print("I don't see any token!!")
           
	   turn(-10, 1)
	   
	elif dist < d_th and silver == True: #If it is close to a silver token it grabs it
	
		print("Found it!!")
		
	   	if R.grab():
	   	
			print("Gotcha!!")
			
			#The robot gets the code for the silver token it just grabbed
	       	dist, rot_y, code_silver = find_silver_token()
	       	
	       	#This code will be saved in a list, to ditinguish the ones that are already paired from the ones that aren't
	       	silver_token.append(code_silver)
	       	
	       	#We change the value of the variable "silver", so that the robot will search for a golden token in the next iteration
	       	silver = False
	
	elif dist < 1.5*d_th and silver == False: #If it is close to a golden token it releases the silver token that it grabbed in the previous iteration
	
		print("Found it!!")

		if R.release():
		
			print("Paired!!")
		
			#The robot gets the code for the golden token it just paired
			dist, rot_y, code_golden = find_golden_token()
			
			#This code will be saved in a list, to ditinguish the ones that are already paired from the ones that aren't
			golden_token.append(code_golden)
			
			#We change the value of the variable "silver", so that the robot will search for a silver token in the next iteration
			silver = True
			
			#Before starting the next iteration the robot drives back a little bit
			drive(-50,2)
	   
	elif rot_y < -a_th: #If the robot is not well aligned with the token, it will move on the left to adjust itself
           print("Left a bit...")
           
     	   turn(-2, 0.5)
     	   
	elif rot_y > a_th: #If the robot is not well aligned with the token, it will move on the right to adjust itself
   	   print("Right a bit..")
   	   
   	   turn(+2, 0.5)
   	   
	elif -a_th <= rot_y <= a_th: #If the robot is well-aligned it will go for the token
           
           print("Ah here we are")
           
	   drive(10, 2)        

