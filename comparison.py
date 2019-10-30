#  less than 2 < 3  Greater than 3 > 2
# boolean value true or false by comparison.
# math1 would be 20 math2 10 math3 100
def max(math1, math2, math3):
    if math1 >= math2 and math3 <= math2: #greater then or equal to
        return math2
    else:
        return math3
print(max(20, 10, 100))# math1 would be 20 math2 10 math3 100 
