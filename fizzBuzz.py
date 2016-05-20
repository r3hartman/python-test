def fizzBuzz(tested): 
    if tested % 5 == 0 and tested % 3 == 0:
        return False #False if tested is divisible by both 3 and 5
    elif tested % 3 == 0:
        return True #True if tested is divisble by either 3 or 5
    elif tested % 5 == 0:
        return True
    return False
if fizzBuzz(5):
    print "this is good"
if fizzBuzz(3):
    print "this is good"
if fizzBuzz(15):
    print "this is bad"
