from random import randrange

def grid():
    print
    print " +---+---+---+---+---+---+---+---+---+---+"
    print " | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|"
    print " +---+---+---+---+---+---+---+---+---+---+"
    print " | 11| 12| 13| 14| 15| 16| 17| 18| 19| 20|"
    print " +---+---+---+---+---+---+---+---+---+---+"
    print " | 21| 22| 23| 24| 25| 26| 27| 28| 29| 30|"
    print " +---+---+---+---+---+---+---+---+---+---+"
    print " | 31| 32| 33| 34| 35| 36| 37| 38| 39| 40|"
    print " +---+---+---+---+---+---+---+---+---+---+"
    print " | 41| 42| 43| 44| 45| 46| 47| 48| 49| 50|"
    print " +---+---+---+---+---+---+---+---+---+---+"
    print " | 51| 52| 53| 54| 55| 56| 57| 58| 59| 60|"
    print " +---+---+---+---+---+---+---+---+---+---+"
    print " | 61| 62| 63| 64| 65| 66| 67| 68| 69| 70|"
    print " +---+---+---+---+---+---+---+---+---+---+"
    print " | 71| 72| 73| 74| 75| 76| 77| 78| 79| 80|"
    print " +---+---+---+---+---+---+---+---+---+---+"
    print " | 81| 82| 83| 84| 85| 86| 87| 88| 89| 90|"
    print " +---+---+---+---+---+---+---+---+---+---+"
    print " | 91| 92| 93| 94| 95| 96| 97| 98| 99|100|"
    print " +---+---+---+---+---+---+---+---+---+---+"
    print
    
def test():
    random = randrange(1,100)
    name = raw_input("Hello, what is your name? ")
    game_on = raw_input("Hello, %s, would you like to practice thinking about numbers? " % name)
    if game_on.lower() == "yes":
        grid()
        print "%s, use the grid to help you practice." % name
        ten_more(random)
        ten_less(random)
    else:
        print "Okay, %s, have a nice day" % name
        #Some exit command? Maybe return?
        
        
def ten_more(number):
    ten_more_counter = 0
    while ten_more_counter <= 2:
        ten_more_input = int(input("What is ten more than %s? " % number))
        if ten_more_input == number + 10:
            print "Great job, %s!" % name
            return
        else: 
            ten_more_counter = ten_more_counter + 1
            if ten_more_counter == 2:
                print "Better luck next time!"
            else:
                print "Try again!"

def ten_less(number):
    ten_less_counter = 0
    while ten_less_counter <= 2:
        ten_less_input = int(input("What is ten less than %s? " % number))
        if ten_less_input == number - 10:
            print "Great job, %s!" % name
            return
        else: 
            ten_less_counter = ten_less_counter + 1
            if ten_less_counter == 2:
                print "Better luck next time, %s!" % name
            else:
                print "Try again!"
#ten_more works. Now how do I make ten_more start over each time it's incorrect?
        
test()

