#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def check():
    turn_left()
    while(wall_on_right()=="TRUE"):
        move()    
    turn_right()
    move()
    turn_right()
    while(wall_in_front()!="TRUE"):
        move()
    turn_left()   
    
       
    
while not at_goal():
    if(wall_in_front() == "TRUE"):
       check() 
    else:
        move()
