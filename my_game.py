class User(object): 
    def start(self) :
        computer = []
        opponent = [] 
        opt=0
        count_4 = 0
    
        inp = int(raw_input('your ',))
        opponent.append(inp)
	
        x=0 
# input from user and also computer turn by turn

        for i in range (1,5):
 
# computer turn

            if opponent.count(4)==1 and count_4 == 0 and opponent.count(7) == 0:
	        computer.append(7)
	        count_4 = 1
	        print 'computer ',7,
    
	    elif opponent.count(5) ==1 and x == 0 and (opponent.count(1)==1 or opponent.count(4)==1 or opponent.count(3)==1) :
		x=1
		if opponent.count(1) == 1 :
		    computer.append(9)
		    print 'computer ',9,
		elif opponent.count(4) == 1:
		    computer.append(6)
		    print 'computer ',6,
		elif opponent.count(3) == 1:
		    computer.append(7)
		    print 'computer ',7,
            else : 
	        for j in range (1,10):
                    if(computer.count(j) == 0 and opponent.count(j) == 0):
	                computer.append(j)
	                print 'computer ',j,
                        break 
      
        
            if computer.count(1) == 1 and computer.count(2) == 1 and computer.count(3) == 1 :
                print "\nyou lose!!"
	        opt = 1
	        break

            elif computer.count(1) == 1 and computer.count(4) == 1 and computer.count(7) == 1 :
                print "\nyou lose!!"
	        opt = 1
	        break

            elif computer.count(7) == 1 and computer.count(8) == 1 and computer.count(9) == 1 :
                print "\nyou lose!!"
	        opt = 1
	        break

            elif computer.count(3) == 1 and computer.count(6) == 1 and computer.count(9) == 1 :
                print "\nyou lose!!"
	        opt = 1
	        break

            elif computer.count(1) == 1 and computer.count(5) == 1 and computer.count(9) == 1 :
                print "\nyou lose!!"
	        opt = 1
	        break

            elif computer.count(7) == 1 and computer.count(5) == 1 and computer.count(3) == 1 :
	        print "\nyou lose!!"
	        opt = 1
	        break

            elif computer.count(4) == 1 and computer.count(5) == 1 and computer.count(6) == 1 :
	        print "\nyou lose!!"
	        opt = 1
	        break
 
            elif computer.count(2) == 1 and computer.count(5) == 1 and computer.count(8) == 1 :
	        print "\nyou lose!!"
	        opt = 1
	        break


# user turn...
   
            while True:
                k=int(raw_input('your '))
                if (computer.count(k) == 0 and opponent.count(k) == 0):
                    opponent.append(k)
	            break
                else:
                    print 'illegal    ',   
    
            if opponent.count(1) == 1 and opponent.count(2) == 1 and opponent.count(3) == 1 :
                print "\nyou win!!"
	        opt = 1
	        break

            elif opponent.count(1) == 1 and opponent.count(4) == 1 and opponent.count(7) == 1 :
                print "\nyou win!!"
	        opt = 1
	        break

            elif opponent.count(7) == 1 and opponent.count(8) == 1 and opponent.count(9) == 1 :
                print "\nyou win!!"
	        opt = 1
	        break

            elif opponent.count(3) == 1 and opponent.count(6) == 1 and opponent.count(9) == 1 :
                print "\nyou win!!"
	        opt = 1
	        break

            elif opponent.count(1) == 1 and opponent.count(5) == 1 and opponent.count(9) == 1 :
                print "\nyou win!!"
	        opt = 1
	        break

            elif opponent.count(7) == 1 and opponent.count(5) == 1 and opponent.count(3) == 1 :
	        print "\nyou win!!"
	        opt = 1
	        break

            elif opponent.count(4) == 1 and opponent.count(5) == 1 and opponent.count(6) == 1 :
	        print "\nyou win!!"
	        opt = 1
	        break

            elif opponent.count(2) == 1 and opponent.count(5) == 1 and opponent.count(8) == 1 :
	        print "\nyou win!!"
	        opt = 1
	        break
# if nobody win

        if opt == 0 :
            print "\n\n nice try\ndraw\n try again "



#computer first
class Computer(object):
    def start(self) :
        computer = []
        opponent = [] 
        opt=0
        count_4 = 0

        computer.append(5)
        print '\ncomputer ',computer[0],

# input from user and also computer turn by turn

        for i in range (1,5):
 
# user turn...
   
            while True:
                k=int(raw_input('your '))
                if (computer.count(k) == 0 and opponent.count(k) == 0):
                    opponent.append(k)
	            break
                else:
                    print 'illegal  ',   
    
            if opponent.count(1) == 1 and opponent.count(2) == 1 and opponent.count(3) == 1 :
                print "\nyou win!!"
	        opt = 1
	        break

            elif opponent.count(1) == 1 and opponent.count(4) == 1 and opponent.count(7) == 1 :
                print "\nyou win!!"
	        opt = 1
	        break

            elif opponent.count(7) == 1 and opponent.count(8) == 1 and opponent.count(9) == 1 :
                print "\nyou win!!"
	        opt = 1
	        break

            elif opponent.count(3) == 1 and opponent.count(6) == 1 and opponent.count(9) == 1 :
                print "\nyou win!!"
	        opt = 1
	        break

# computer turn

            if opponent.count(4)==1 and count_4 == 0 and opponent.count(7) == 0 :
	        computer.append(7)
	        count_4 = 1
	        print 'computer ',7,
    
            else : 
	        for j in range (1,10):
                    if(computer.count(j) == 0 and opponent.count(j) == 0):
	                computer.append(j)
	                print 'computer ',j,
                        break 
      
        
            if computer.count(1) == 1 and computer.count(2) == 1 and computer.count(3) == 1 :
                print "\nyou lose!!"
	        opt = 1
	        break

            elif computer.count(1) == 1 and computer.count(4) == 1 and computer.count(7) == 1 :
                print "\nyou lose!!"
	        opt = 1
	        break

            elif computer.count(7) == 1 and computer.count(8) == 1 and computer.count(9) == 1 :
                print "\nyou lose!!"
	        opt = 1
	        break

            elif computer.count(3) == 1 and computer.count(6) == 1 and computer.count(9) == 1 :
                print "\nyou lose!!"
	        opt = 1
	        break

            elif computer.count(1) == 1 and computer.count(5) == 1 and computer.count(9) == 1 :
                print "\nyou lose!!"
	        opt = 1
	        break

            elif computer.count(7) == 1 and computer.count(5) == 1 and computer.count(3) == 1 :
	        print "\nyou lose!!"
	        opt = 1
	        break

            elif computer.count(4) == 1 and computer.count(5) == 1 and computer.count(6) == 1 :
	        print "\nyou lose!!"
	        opt = 1
	        break

# if nobody win

        if opt == 0 :
            print "\n\n nice try\ndraw\n try again "

# "matrix" is a simple variable with the help of which print the matrix for user's help

matrix=1
for i in range(0,3):
    for j in range(0,3):
	print matrix,
	matrix+=1
    print '\n'

computer = []
opponent = []

print "anyone who choose any row, column and diagonal will be winner"
print "now start the game"
print "you can choose any no. from the above which is legal (not illegal) "

print " 1 -> computer and 2 -> you  choose 1 or 2 for first turn"
input_1 = int(raw_input())

computer = Computer()
user = User()

if input_1 == 1 :
    computer.start()

else :
    user.start()



