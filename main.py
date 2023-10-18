'''
 @author : sumangal karan
 @version:python 3.11.5
 @date : 18/10/2023
 @contact:9564114832
 @Email:sumangalkaran@outlook.com
 @Gmail:sumangalkaran44@gmail.com
 @project: [+]Random number guessing game write in python cli  [+]
 @github  :https://github.com/Sumangal44/number-guessing-game.git
'''


import random
import math
# taking inputs
lower = int(input("[+]Enter lower bound:"))
upper = int(input("[+]Enter  upper bound:"))  # taking inputs
x = random.randint(lower, upper)
# genarate random number between the lower and upper limit
print("\n\t//You've only//", round(math.log(upper - lower + 1, 2)),
      "//Chances to guess the integer!//\n")
# initializing the number of guesses
count = 0
# for calculation of minimun number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
    # taking guessing number as input
    guess = int(input("[+]Guess the number:"))
    # condition testing
    if x == guess:
        print("//congratulations you did it in//", count, "try")
        # once guessed ,loop will break
        break
    elif x > guess:
        print("//you guees too small!//")
    elif x < guess:
        print("//you guessed too high!// ")
# if guessing is more than required guesses ,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
    print("\n //the number is// %d" % x)
    print("\t //Better luck next time!//")
