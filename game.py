import random
'''
1 = snake
-1 = water
0 = gun
'''

computer = random.choice([1, 0 , -1])   # computer will choose 

yourstr = input("Enter your choice:")

intdic = {"s" : 1 , "w" : -1 , "g" : 0}

reversedic = {1: "Snake" , -1 : "Water" , 0 : "Gun"}

your = intdic[yourstr]   # you will be chosed and display 

# Now we have two numbers variables (Your and computer)

print(f"you choose, {reversedic[your]}\nComputer choose, {reversedic[computer]}")  # yhan pr reversdic likh taqay python ko pta lg jay k ma kis ki baat kr rha hon mtlb agr s likha to s 1 k pas jay ga or 1 phir snake k pas jay ga or print hojay ga
# we use reversedict in up because reversedict have power to make 1,0 -1 to snake,gun and water, we dont use intdict

if (computer == your):
    print ("Its a draw")

else:
    if (computer == -1 and your == 1):   # -2 computer - your = -2 then again all 
        print ("you win!")
    elif (computer == -1 and your == 0):  # -1  
        print ("you Loose!")
    elif (computer == 1 and your == -1):  # 2
        print ("you Loose!")
    elif (computer == 1 and your == 0):   # 1
        print ("you win!")
    elif (computer == 0 and your == -1):  # 1
        print ("you Win!")
    elif (computer == 0 and your == 1):   # -1   ya dosray method k lia ha is pr focus nhi krna okkk,..
        print ("you Loose!")
    else:
        print ("something went wrong")



# if (computer - your == -1 or computer - your == 2) :
#     print ("You loose")
# else: 
#     print ("You win")    ya sirf smjhhay k lia tha k ham is logic ko is tarah bhi design kr skta hain but ap dosray pr hi focus kro



# Note: Some comments in this code were written during the learning and development process. They are kept for educational purposes and can be ignored when reviewing the project.
