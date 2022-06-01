#Multiple choice quiz
#Imports
import time
import os

#Quiz Startup

points = 0


#Definitions
#Defines the instructions of the quiz.(When called, it will display the instructions of the quiz one line at a time)
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

#Defines the introduction question. (At the beginning of the code, the intro question is called, and if chosen, will display instructions)
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


#Defines the test question. (If called, will run the test question by user request)  
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


#Defines test qestion response. (Asks the user if they would like to try a test question, and if answered with yes, it will call for the test question)
def test_question_answers():
  
  test = input("Would you like to try a test question? ").lower()

  if test == "yes" or test == "y":
    test_question()
  
  elif test == "no" or test == "n":
    print("")
    
  else:
    print("Please answer 'yes' or 'no'")
    test_question_answers()

def quiz_continue():
  print("")
  print("When you are ready, type 'continue' to continue the quiz ")
  print("")
  continue_answer = input().lower()
    
  if continue_answer == "continue":
    print("")
    print("Here comes your first question")
    time.sleep(1)
    print("")
  
  elif continue_answer != "continue":
    print("Please type 'continue'")
    time.sleep(1)
    os.system('clear')
    quiz_continue()
        
  else:
    begin()
      
def begin():
  begin = input("Alright then. Are you ready to begin this quiz? ").lower()

  if begin == "yes" or begin == "y":
    begin = begin.lower()
    print("")
    print("Here comes your first question")
    time.sleep(2)
    print("")
  
  elif begin == "no" or begin == "n":
    os.system('clear')
    quiz_continue()
    
  
  else:
    os.system('clear')
    quiz_continue()


def ending():
  if points == 10:
    print("Congratulations, you got all of the questions correct! You earned a total of", points, "points!")

  elif points >= 7:
    print("Well done, you almost got them all! You earned", points, "points.")
  
  elif points >= 5:
    print("You earned", points, "points. You know your stuff, but I know you can do better!.")

  elif points >= 3:
    print("You still have some learning to do, but I'm sure you can do it. You earned", points, "points.")

  elif points >= 1:
    print("You only earned", points, "points. I recommend you keep practicing your Maori skills")

  elif points < 1:
    print("You have earned", points, "points. This means that you have answered more questions wrong than right. Please work on your Maori skills")
    
  else:
    print("You have somehow broken my code... If you see this message, please let the author know immediately")
#Question Definitions

#Defines question 1. (When called, runs the first question)
def Question_1():
  global points
  print("")
  print("Question 1: ")
  print("")
  print("What is the Maori word for 'Welcome'? ")
  print("")
  print("A. Haere Mai")
  print("B. Tena Koe")
  print("C. Kei Te Pai")

  question_1_a = input("Your answer: ").lower()

  if question_1_a == "haere mai" or question_1_a == "a":
    print("")
    print("That is correct! You have gained a point")
    points += 1

  else:
    print("That is incorrect. You have lost a point")
    points -= 1

#Defines question 2. (When called, runs the second question)
def Question_2():
  global points
  print("")
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


#Defines question 3. (When called, runs the third question)
def Question_3():
  
  global points
  print("")
  print("Question 3: ")
  print("")
  print("What does the word 'Awa' mean?")
  print("")
  print("A. Ocean")
  print("B. River")
  print("C. Water")

  question_3_a = input("Your answer: ").lower()

  if question_3_a == "river" or question_3_a == "b":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("Incorrect. You have lost 1 point")
    points -= 1


#Defines question 4. (When called, runs the fourth question)
def Question_4():
    
  global points
  print("")
  print("Question 4: ")
  print("")
  print("What is the Maori phrase for a formal greeting to two people?")
  print("")
  print("A. Tena Korua")
  print("B. Tena Koutou")
  print("C. Tena Koe")

  question_4_a = input("Your answer: ").lower()

  if question_4_a == "tena korua" or question_4_a == "a":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("Incorrect. You have lost 1 point")
    points -= 1

#Defines question 5. (When called, runs the fith question)
def Question_5():
      
  global points
  print("")
  print("Question 5: ")
  print("")
  print("What does the word 'Maunga' mean?")
  print("")
  print("A. Island")
  print("B. Mountain")
  print("C. Valley")

  question_5_a = input("Your answer: ").lower()

  if question_5_a == "mountain" or question_5_a == "b":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("Incorrect. You have lost 1 point")
    points -= 1

def Question_6():
      
  global points
  print("")
  print("Question 6: ")
  print("")
  print("What does the question 'Kei te pehea koe?' mean? ")
  print("")
  print("A. Where am I?")
  print("B. What time is it?")
  print("C. How are you? ")

  question_6_a = input("Your answer: ").lower()

  if question_6_a == "how are you?" or question_6_a == "how are you?" or question_6_a == "c":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("That is incorrect. You have lost 1 point")
    points -= 1

#Defines question 7. (When called, runs the seventh question)
def Question_7():
      
  global points
  print("")
  print("Question 7: ")
  print("")
  print("What is the Maori word for 'House'?")
  print("")
  print("A. Whare")
  print("B. Koru")
  print("C. Ake")

  question_7_a = input("Your answer: ").lower()

  if question_7_a == "whare" or question_7_a == "a":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("That is incorrect. You have lost 1 point")
    points -= 1

#Defines question 8. (When called, runs the eighth question)
def Question_8():
      
  global points
  print("")
  print("Question 8: ")
  print("")
  print("What is the Maori word for 'family'?")
  print("")
  print("A. Kauri")
  print("B. Moana")
  print("C. Whanau")

  question_8_a = input("Your answer: ").lower()

  if question_8_a == "whanau" or question_8_a == "c":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("That is incorrect. You have lost 1 point")
    points -= 1

#Defines question 9. (When called, runs the ninth question)
def Question_9():
      
  global points
  print("")
  print("Question 9: ")
  print("")
  print("What does the word 'Teina' mean?")
  print("")
  print("A. Brother")
  print("B. Sister")
  print("C. Mother")

  question_9_a = input("Your answer: ").lower()

  if question_9_a == "brother" or question_9_a == "a":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("That is incorrect. You have lost 1 point")
    points -= 1

#Defines question 10. (When called, runs the tenth question)
def Question_10():
      
  global points
  print("")
  print("Question 10: ")
  print("")
  print("What does the word 'Tuahine' mean?")
  print("")
  print("A. Brother")
  print("B. Sister")
  print("C. Father")

  question_10_a = input("Your answer: ").lower()

  if question_10_a == "Sister" or question_10_a == "b":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("That is incorrect. You have lost 1 point")
    points -= 1

    
#Beggining of quiz code. Calls functions


#Welcomes the user to the quiz
print("Welcome to your favourite Te Reo quiz!")
print("")

intro()
test_question_answers()


#time.sleep(.5)



begin()

#The following code calls ALL 30 questions of the quiz

#Question 1

Question_1()
time.sleep(2)
os.system('clear')

#Question 2

Question_2()
time.sleep(2)
os.system('clear')

#Question 3

Question_3()
time.sleep(2)
os.system('clear')

#Question 4

Question_4()
time.sleep(2)
os.system('clear')

#Question 5

Question_5()
time.sleep(2)
os.system('clear')

#Question 6

Question_6()
time.sleep(2)
os.system('clear')

#Question 7

Question_7()
time.sleep(2)
os.system('clear')

#Question 8

Question_8()
time.sleep(2)
os.system('clear')

#Question 9

Question_9()
time.sleep(2)
os.system('clear')

#Question 10

Question_10()
time.sleep(2)
os.system('clear')
"""
#Question 11

Question_11()
time.sleep(2)
os.system('clear')

#Question 12

Question_12()
time.sleep(2)
os.system('clear')

#Question 13

Question_13()
time.sleep(2)
os.system('clear')

#Question 14

Question_14()
time.sleep(2)
os.system('clear')

#Question 15

Question_15()
time.sleep(2)
os.system('clear')

#Question 16

Question_16()
time.sleep(2)
os.system('clear')

#Question 17

Question_17()
time.sleep(2)
os.system('clear')

#Question 18

Question_18()
time.sleep(2)
os.system('clear')

#Question 19

Question_19()
time.sleep(2)
os.system('clear')

#Question 20

Question_20()
time.sleep(2)
os.system('clear')

#Question 11

Question_21()
time.sleep(2)
os.system('clear')

#Question 22

Question_22()
time.sleep(2)
os.system('clear')

#Question 23

Question_23()
time.sleep(2)
os.system('clear')

#Question 24

Question_24()
time.sleep(2)
os.system('clear')

#Question 25

Question_25()
time.sleep(2)
os.system('clear')

#Question 26

Question_26()
time.sleep(2)
os.system('clear')

#Question 27

Question_27()
time.sleep(2)
os.system('clear')

#Question 28

Question_28()
time.sleep(2)
os.system('clear')

#Question 29

Question_29()
time.sleep(2)
os.system('clear')

#Question 30

Question_30()
time.sleep(2)
os.system('clear')
"""