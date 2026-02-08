# Given a shape, write the function
"""
🧱🧱🧱🧱
🧱🧱🧱🧱
🧱🧱🧱🧱
🧱🧱🧱🧱
"""
def draw_square(n):
    for i in range(4):
        print("🧱" * 4)
draw_square(4)

#Draw a 5 x 3 rectangle and write the function
"""
***
***
***
***
***
"""
def draw_rect(n):
    for i in range(5):
        print("*" * 3)
draw_rect(5)

#Write a function called triangle that takes a string and an integer and draws a pyramid with the given height, made up using copies of the string. For example, triangle('+', 5) should print:
"""
+
++
+++
++++
+++++
"""
def draw_tri(n):
    for i in range(5):
        print("+" * (i+1))
draw_tri(5)

"""
    #
   ##
  ###
 ####
#####
"""
def draw_tri_right(n):
    for i in range(5):
        print(" " * (n-(i+1)) + "#" * (i+1))
draw_tri_right(5)

#create a function to draw a pyramid
"""
    #
   ###
  #####
 #######
"""
#def pyramid_shape(n):
    #for i in range(4):
        #print(" " * (n-(2*i +1) + "#" * 2*i + 1))
#pyramid_shape(4)

#Draw the shape
def shape(q, r):
    for s in range(r):
        print(q*(s+1))
shape("#", 4)

def pattern(z, y):
    for x in range(y):
        print(z * (y - x))

pattern('*', 4)