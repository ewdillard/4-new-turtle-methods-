#https://realpython.com/beginners-guide-python-turtle/?__cf_chl_jschl_tk__=4873864d673ca5883fb35235a166394c9c7b2968-1607106358-0-AaW5lNpA4KW5T8S6Y1_jBA8e2R2iYh28U5V7UdqLmcXCswGzvegnCWnpl0kzcEKCIiygN27MrCvdAyDTMTQz3Lr-AZtWAM91filqr-UQPnqFLyBroh4HBkyllhAaqublYtVdYjisWdAlL9294UL8LqjM26esH0PEDyMz8wfw6Felofe0ui27rIvhPJF8h6o1D_V0vORkTehxhU54K63-aUpacLBN7kcWGXgpWkbGcHMKMWtqCAwqrUsO3Jj8_R1f-h6D0ySm8Km1AGyxSBIb-uYoC4uq4LwZcsHNr4vvlhhnIFOm6ePHZSq9PVtE6AaePwWUnTlyeFNRBqDPDobP3hFX1KPbEWlNuzCG0qmhNtwo
import turtle
wn=turtle.Screen()
wn.bgcolor("black")
#---C-I-R-C-L-E------------------------------------------
circle = turtle.Turtle()
circle.pensize(5)
circle.color("yellow")
circle.circle(50)#This is extremely useful when you want a circle. Simply say circle and how big you want it and watch your beautiful circle come to life.
#--------------FILLING/PEN-------------------------
t = turtle.Turtle()
t.pensize(10)
t.shape("circle") #THIS CHANGES THE TYOE OF TIP YOUR PEN HAS. THIS MAY BE USED FOR PIXEL ART MAYBE WHEN YOU HAVE A SQUARE TIP.
t.color("light blue")
t.begin_fill() #This begins the sequence and tells the program, "hey anything after this is going to eventually be filled").It
t.forward(100)
t.left(120)#Makes the shape
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()#ENDS THE FILLING. This is when it finally says, "Oh, he is done with the shape. Lets fill it"

#------SIMPLE ACTIONS-----------------------------------
#t.clear() THESE ARE COMMENTED AS THEY INTERFERE WITH THE OTHER CODE. THIS IS VERY SIMPLE AND CLEARS YOUR TURTLE FROM SIGHT
#t.undo() THIS UNDOS YOUR LAST ACTION FROM SIGHT. ILL MAKE A NEW TURTLE TO SHOW WHAT THEY DO,
#---------------EXAMPLE---------------------------------
an = turtle.Turtle()
an.pensize(10)
an.color("light green")
an.forward(50)
an.clear() #This clears the turtle from sight of the window.
#
a = turtle.Turtle()
a.pensize(10)
a.color("orange")
a.left(180)
a.forward(50)
a.right(90)
a.forward(50)
a.undo() #This will undo the forward