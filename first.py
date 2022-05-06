#Multiple choice quiz
#Imports
import time

#Definitions
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

def test_question():
  print("")
  print("*** TEST QUESTION ***")
  print("")
  print("What is the Maori word for 'Hello'")
  print("")
  print("A. Hangi") 
  print("B. Kia Ora")
  print("C. Aroha")


  test_answer = input("Your answer: ").lower()

  if test_answer == "b" or test_answer == "kia ora":
    print("That is correct! You have gained 1 point")

  else:
    print("That is inccorect. You have lost 1 point")

def continue_first():
  print("")
  print("When you are ready, type 'continue' to continue the quiz ")
  continue_answer = input()

  
#Intro

print("Welcome to your favourite Te Reo quiz!")
print("")
intro_answer = input("Have you played this quiz before? ").lower()

if intro_answer == "no" or intro_answer == "n":
  intro_answer_no()

else:
  print("")
  print("Lets continue!")
  print("")


test = input("Would you like to try a test question? ").lower()

if test == "yes" or test == "y":
  test_question()

else:
  print("")

begin = input("Alright then. Are you ready to begin this quiz? ").lower()

if begin == "yes" or begin == "y":
  print("Here comes your first question")

elif begin == "no" or begin == "n":
  continue_first()
  if continue_answer == "continue":
    print("Here comes your first question")