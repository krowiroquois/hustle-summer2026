
# Ticket 1

ages = [17, 11, 25, 13, 9]
#for age in ages:
   # if age >= 13:
   #     print(f"{age} -- Access granted.")
   # else:
   #     print(f"{age} -- Too young!")
# Predict: 17, 25, and 13 will get the "Access granted." message. 11 and 9 will be too young.
# Answer: come back to this question; i don't get what it's asking

# Ticket 2

keep_checking = "yes"

#while keep_checking == "yes":
 #   age = int(input("Enter an age: "))
  #  if age >= 13:
   #     print(f"{age} -- Access granted")
    #else:
     #   print(f"{age} -- Too young!")
    #keep_checking = input("Check another age? (yes/no): ")
# Predict: The loop will not run if you enter no.
# Answer: A for loop will only run a set number of times; a while loop provides infinite
# possible answers, considering there are many ages greater than 13.

# Ticket 3

#while True:
 #   age = int(input('Enter an age or type "stop": '))
  #  if age == "stop":
   #     break
    #else:
     #   if age >= 13:
      #      print(f"{age} -- Access granted.")
       # else:
        #    print(f"{age} -- Too young!")
# Predict: If the loop did not have a break, the loop would keep going in the terminal.
# Answer: This loop has an extra step to replace the "no" prompt with "stop"

# Ticket 4

#def can_access(age):
#    if can_access(age) >= 13:
#        return True
#    else:
#        return False
#can_access(int(17, 11, 25, 13, 9))

# Ticket 5

def signup_report(age_list):
    approved = 0
    print("--- Streampass Signup Report ---")

# hello y'all, i tried my best with this assignment but due to me being sick and not
# being able to attend thursday's lecture to ask clarifying questions, i got stuck.
# i'm going to submit what i have to show that i at LEAST gave it a try!