import time

def intro():
  intro_answer = input("Have you played this quiz before? ").lower()   
  if intro_answer == "no" or intro_answer == "n":
    intro_answer_no()

  elif intro_answer == "yes" or intro_answer == "y":
    print("")
    print("Lets continue!")
    print("")
  
  else:
    print("Please answer 'yes' or 'no'")
    intro()

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




intro()

  
  
  
  
  
  
  
  
  
#https://www.w3schools.com/python/python_while_loops.asp
