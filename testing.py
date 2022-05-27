"""import time

def intro_answer_no():
  print("")
  print("This quiz has 30? levels.") 
  print("")
  time.sleep(2)
  print("Each level will have multiple choice answers for you to choose from.")
  print("")
  time.sleep(2)
  print("If you choose the correct answer, you will be awarded a point.")
  print("")
  time.sleep(2)
  print("If you answer incorrectly, a point will be taken away.")
  print("")
  time.sleep(2)


def intro_answer():
  intro_answer = input("Have you played this quiz before? ").lower()

  while intro_answer != "yes" or intro_answer != "no":
  
    if intro_answer == "yes" or intro_answer == "y":
      break
  
    elif intro_answer == "no" or intro_answer == "n":
      intro_answer_no()
      break
    
    else:
      print("Placeholder")
      intro_answer()


intro_answer()

print("Placeholder")







    
if intro_answer == "no" or intro_answer == "n":
  intro_answer_no()

elif intro_answer == "yes" or intro_answer == "y":
  print("")
  print("Lets continue!")
  print("")
  
else:
  print("Please answer 'yes' or 'no'")





  
  
  
  
  
  
  
  
  
#https://www.w3schools.com/python/python_while_loops.asp"""


