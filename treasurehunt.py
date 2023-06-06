print("Welcome to  the Girlfriend treasure hunt")
print(''' 
|\_____/|     ////\
|/// \\\|    /// \\\
 |/O O\|     |/o o\|
 d  ^ .b     C  )  D    "A Night Out On The Town"
  \\m//      | \_/ |
   \_/        \___/
 __ooo__    _/<|_|>\_
/_     _\  / |/\_/\| \
| \_v_/ | |    |\|    |
|| _/ _/\\| |  |\|  | |
||)    ( \| |  |\|  | |
||      \ | \\ |\|  | |
||  --  |  (())\_/  | |
((      |   |___|___|_|
 |______|   |   Y   |))
  |-||-|    |   |   |
  | || |    |   |   |
  | || |    |   |   |
  | || |    |___|___|prs
 /u\||/u\   /qp| |qp\
(_/\||/\_) (___/ \___)''')
       

print("Your mission is to answer a series of questions about your partner Taiyesi \n Win the game and you might get lucky tonight!")
answer1 = (input("Has your partner ever been stung by a bee? \n").lower())
if answer1 == "no":
    print("correct!")
else:
    quit("boo")

answer2 = (input("Would your gf rather have chicken or steak? \n").lower())
if answer2 == "chicken":
    print("correct!")
else:
    quit("booo")


answer3 = (input("Would your gf rather go to a park or to the beach? \n").lower())
if answer3 == "beach" or "the beach":
    print("correct!")
else:
    quit("booo")

answer4 = (input("If the zombie apocolypse happened today, would your gf stockpile food or weapons? \n").lower())
if answer4 == "weapons":
    print("correct!")
else:
    quit("boo")

answer5 = (input("what highschool did your gf go to? \n").lower())
if answer5 == "Rhodes park school" or "Rhodespark school" or "Rhodes park":
    print("correct!")
else:
    quit("Looks like Jeppe Boys taught you math but not how to love :(")



