import math
#STAGE 1
def hypotenuse(leg1, leg2): #defines the function hypotenuse and gives it two parameters leg1 and leg2
    square1 = leg1 ** 2 #creates a variable square1 and stores the value of the expression log1 ** 2
    square2 = leg2 ** 2 #creates a variable square2 and stores the value of the expression log2 ** 2
    print("the square of leg1 is ", square1) #prints the value of square1
    print("the square of leg2 is ", square2) #prints the value of square2
    return 0.0 #returns 0.0
#The hypotenuse of a right triangle is the square-root of the sum of the square of the other two legs. So Stage 1 is the first development phase that calculates the squares of the other legs.

#STAGE 2
def hypotenuse(leg1, leg2):
    square1 = leg1 ** 2
    square2 = leg2 ** 2
    sum_square = square1 + square2 #creates a variable sum_square and stores the value of the sum of the values of square1 and square2
    print("sum of the squares is ", sum_square) #prints the value of sum_square
    return 0.0 #returns 0.0
#Stage 2 is the second development phase that  sums the value of square1 and square2

#STAGE 3
def hypotenuse(leg1, leg2):
    square1 = leg1 ** 2
    square2 = leg2 ** 2
    sum_square = square1 + square2
    result = math.sqrt(sum_square) #creates a variable result and stores the value of the square-root of the value of sum_square
    return result #returns the value of result
print(hypotenuse(6, 8))

