#Multiple choice quiz
#Imports
import time


#Quiz Startup

points = 0




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


def intro():
  intro_answer = input("Have you played this quiz before? ").lower()   
  if intro_answer == "no" or intro_answer == "n":
    intro_answer_no()

  elif intro_answer == "yes" or intro_answer == "y":
    intro_answer = intro_answer.lower()
    print("")
    print("Lets continue!")
    print("")
  
  else:
    print("Please answer 'yes' or 'no'")
    intro()

    
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
    test_answer = test_answer.lower()
    print("")
    print("That is correct! You have gained 1 point")

  else:
    print("")
    print("That is inccorect. You have lost 1 point")
    
#Question Definitions

def Question_1():
  global points
  print("Question 1: ")
  print("")
  print("What is the Maori word for 'Welcome'? ")
  print("")
  print("A. Haere Mai")
  print("B. Tena Koe")
  print("C. Kei Te Pai")

  question_1_a = input("Your answer: ").lower()

  if question_1_a == "Haere Mai" or question_1_a == "a":
    print("")
    print("That is correct! You have gained a point")
    points += 1

  else:
    print("That is incorrect. You have lost a point")
    points -= 1

def Question_2():
  global points
  print("Question 2: ")
  print("")
  print("What does the word 'Waiata' mean?")
  print("")
  print("A. Water")
  print("B. Love")
  print("C. Song")

  question_2_a = input("Your answer: ").lower()

  if question_2_a == "song" or question_2_a == "c":
    print("")
    print("That is the right answer! You have gained a point")
    points += 1

  else:
    print("That is the wrong answer. You have lost a point")
    points -= 1


def Question_3():
  
  global points
  print("Question 3: ")
  print("")
  print("What does the word 'Awa' mean?")
  print("")
  print("A. Ocean")
  print("B. River")
  print("C. Water")

  question_3_a = input("Your answer: ").lower()

  if question_3_a == "River" or question_3_a == "b":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("Incorrect. You have lost 1 point")
    points -= 1


def Question_4():
    
  global points
  print("Question 4: ")
  print("")
  print("What is the Maori phrase for a formal greeting to two people?")
  print("")
  print("A. Tena Korua")
  print("B. Tena Koutou")
  print("C. Tena Koe")

  question_4_a = input("Your answer: ").lower()

  if question_4_a == "Tena Korua" or question_4_a == "a":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("Incorrect. You have lost 1 point")
    points -= 1

def Question_5():
      
  global points
  print("Question 5: ")
  print("")
  print("What does the word 'Maunga' mean?")
  print("")
  print("A. Island")
  print("B. Mountain")
  print("C. Valley")

  question_5_a = input("Your answer: ").lower()

  if question_5_a == "Mountain" or question_5_a == "b":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("Incorrect. You have lost 1 point")
    points -= 1




#Intro


print("Welcome to your favourite Te Reo quiz!")
print("")

intro()


test = input("Would you like to try a test question? ").lower()

if test == "yes" or test == "y":
  test = test.lower()
  test_question()
  
else:
  print("")

time.sleep(.5)
print("")
begin = input("Alright then. Are you ready to begin this quiz? ").lower()

if begin == "yes" or begin == "y":
  begin = begin.lower()
  print("")
  print("Here comes your first question")
  time.sleep(2)
  print("")

elif begin == "no" or begin == "n":
  print("")
  print("When you are ready, type 'continue' to continue the quiz ")
  continue_answer = input().lower()

  if continue_answer == "continue":
    print("")
    print("Here comes your first question")
    time.sleep(1)
    print("")
  
  else:
    print("Placeholder")

else:
  print("Placeholder")



#Question 1

Question_1()

#Question 2

Question_2()

#Question_3

Question_3()

#Question 4

Question_4()

#Question 5

Question_5()