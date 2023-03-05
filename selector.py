# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:54:07 2020

@author: A109221063
"""

choiceMenu="1:BMI\n2:萬花尺\n-->"
choice= int(input(choiceMenu))

if choice==1:
        
        try:
            import random
            weight=random.randint(30,120)
            print("Weight is {:.2f}".format(weight))
            height=random.randint(120,220)/100
            print("Height is {:.2f}".format(height))
            workload=random.randint(0,2)
            print("Wrokload is ",workload)
    
            bmi=weight/(height**2)

            if (workload==0)and (bmi<18.5):               yourC=35
            elif (workload==0)and (18.5<=bmi and bmi<24 ):yourC=30
            elif (workload==0)and (24<=bmi):              yourC=25
            elif (workload==1)and (bmi<18.5):             yourC=40
            elif (workload==1)and (18.5<=bmi and bmi<24 ):yourC=35
            elif (workload==1)and (24<=bmi):              yourC=30
            elif (workload==2)and (bmi<18.5):             yourC=45
            elif (workload==2)and (18.5<=bmi and bmi<24 ):yourC=40
            elif (workload==2)and (24<=bmi):              yourC=35
   
            calories=yourC*weight

            if(workload==0):workload="light"
            elif(workload==1):workload="middle"
            else:workload="heavy"
            print("weight={:.2f}KG,height={:2f}CM,bmi={:2f},workload={}"\
            .format(weight,height,bmi,workload))
            print("You need {} calories per day.".format(calories))
           
        except:
            print("input are not legal number, processing abort!")

elif choice==2:   
    import turtle
    turtle.bgcolor("black")
    START_X=50
    START_Y=0
    NUM_LINES=36
    LINE_LENGTH=400
    ANGLE=170
    ANIMATION_SPEED=0

    turtle.hideturtle()
    turtle.penup()
    turtle.goto(START_X,START_Y)
    turtle.pendown()
    
    'turtle.speed(ANIMATION_SPEED)'
    
    for x in range (NUM_LINES):
       if x%3==0:turtle.color("magenta")
       if x%3==1:turtle.color("cyan")
       if x%3==2:turtle.color("yellow")
       turtle.forward(LINE_LENGTH)
       turtle.left(ANGLE)
       
    import turtle
    START_X=-150
    START_Y=0
    NUM_CIRCLES=36
    RADIUS=100
    ANGLE=10
    ANIMATION_SPEED=0
    
    turtle.penup()
    turtle.goto(START_X,START_Y)
    turtle.pendown()
    
    for x in range (NUM_CIRCLES):
      if x%3==0:turtle.color("red")
      if x%3==1:turtle.color("green")
      if x%3==2:turtle.color("blue")
      turtle.circle(RADIUS)
      turtle.left(ANGLE)
    
    turtle.penup()              
    turtle.goto(-50,-300)
    turtle.pendown()
    turtle.pencolor("white")
    turtle.write("CT2020F_Ex1Q3\nA109221063_黃雅宜",font=16)   
    turtle.done() 
else:
    print("請輸入1或2")