#This is a Multiple choice quiz based on basic Maori language. This quiz has 30 questions, varying from difficulty to test the users knowledge of Maori language. It will keep track of the users points (The user gains one point if the answer a question correctly, and lose one if they answer incorrectly). At the ned of the quiz, the ending code will be run, giving the user an answer based on how many points the user has gained.


#Imports
import time
import os




#Definitions
#Defines the instructions of the quiz.(When called, it will display the instructions of the quiz one line at a time)
def intro_answer_no():
  print("")
  print("This quiz has 20 questions.") 
  print("")
  time.sleep(2)
  print("Each question will have a multiple choice answer for you to choose from.")
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
    time.sleep(.5)
    print("")
    print("Let's continue!")
    time.sleep(.75)
    os.system('clear')
    print("")
  
  else:
    print("Please answer 'yes' or 'no'")
    time.sleep(.75)
    os.system('clear')
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
    print("")

  else:
    print("")
    print("That is inccorect. You have lost 1 point")
    print("")


#Defines test qestion response. (Asks the user if they would like to try a test question, and if answered with yes, it will call for the test question)
def test_question_answers():
  
  test = input("Would you like to try a test question? ").lower()

  if test == "yes" or test == "y":
    time.sleep(.5)
    test_question()
  
  elif test == "no" or test == "n":
    time.sleep(1)
    os.system('clear')
    print("")
    
  else:
    print("Please answer 'yes' or 'no'")
    time.sleep(.75)
    os.system('clear')
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
    os.system('clear')
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
    os.system('clear')
    print("")
  
  elif begin == "no" or begin == "n":
    time.sleep(1)
    os.system('clear')
    quiz_continue()
    
  
  else:
    os.system('clear')
    quiz_continue()


def ending():
  if points == 20:
    print("Congratulations, you got all of the questions correct! You earned a total of", points, "points!")

  elif points >= 17:
    print("Well done, you almost got them all! You earned", points, "points.")
  
  elif points >= 13:
    print("Wow, you earned", points, "points! You just have a little more to learn.")

  elif points >= 9:
    print("You still have some learning to do, but I'm sure you can do it. You earned", points, "points.")

  elif points >= 5:
    print("You earned", points, "points. I know that you can do better!")

  elif points >= 1:
    print("You have only earned", points, "points. You need to keep practicing")
    
  elif points < 1:
    print("You have earned", points, "points. This means that you have answered more questions wrong than right.\nPlease work on your Maori skills")

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

#Defines question 11. (When called, runs the eleventh question)
def Question_11():
      
  global points
  print("")
  print("Question 11: ")
  print("")
  print("What does the word 'Mahi' mean?")
  print("")
  print("A. Sleep")
  print("B. Run")
  print("C. Work")

  question_11_a = input("Your answer: ").lower()

  if question_11_a == "work" or question_11_a == "c":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("That is incorrect. You have lost 1 point")
    points -= 1

#Defines question 12. (When called, runs the twelth question)
def Question_12():
      
  global points
  print("")
  print("Question 12: ")
  print("")
  print("What is a 'Kauri'?")
  print("")
  print("A. Native Tree")
  print("B. Native Bird")
  print("C. Native Insect")

  question_12_a = input("Your answer: ").lower()

  if question_12_a == "native tree" or question_12_a == "a":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("That is incorrect. You have lost 1 point")
    points -= 1

#Defines question 13. (When called, runs the thirteenth question)
def Question_13():
      
  global points
  print("")
  print("Question 13: ")
  print("")
  print("What is the Maori word for 'food'?")
  print("")
  print("A. Mana")
  print("B. Kai")
  print("C. Puku")

  question_13_a = input("Your answer: ").lower()

  if question_13_a == "kai" or question_13_a == "b":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("That is incorrect. You have lost 1 point")
    points -= 1

#Defines question 14. (When called, runs the fourteenth question)
def Question_14():
      
  global points
  print("")
  print("Question 14: ")
  print("")
  print("What is the Maori word for 'Children'?")
  print("")
  print("A. Manuhiri")
  print("B. Tamariki")
  print("C. Pounamu")

  question_14_a = input("Your answer: ").lower()

  if question_14_a == "tamariki" or question_14_a == "b":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("That is incorrect. You have lost 1 point")
    points -= 1

#Defines question 15. (When called, runs the fifteenth question)
def Question_15():
      
  global points
  print("")
  print("Question 15: ")
  print("")
  print("What does the maori word 'Arpha' mean?")
  print("")
  print("A. Love")
  print("B. Hate")
  print("C. Shoe")

  question_15_a = input("Your answer: ").lower()

  if question_15_a == "love" or question_15_a == "a":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("That is incorrect. You have lost 1 point")
    points -= 1

#Defines question 16. (When called, runs the sixteenth question)
def Question_16():
      
  global points
  print("")
  print("Question 16: ")
  print("")
  print("What does the Maori word 'Haka' mean?")
  print("")
  print("A. Food")
  print("B. Love")
  print("C. Dance")

  question_16_a = input("Your answer: ").lower()

  if question_16_a == "dance" or question_16_a == "c":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("That is incorrect. You have lost 1 point")
    points -= 1
    
#Defines question 17. (When called, runs the seventeenth question)
def Question_17():
      
  global points
  print("")
  print("Question 17: ")
  print("")
  print("What is a 'Moa'?")
  print("")
  print("A. Giant Extinct Bird")
  print("B. Large Group Of Fish")
  print("C. A Small Forest")

  question_17_a = input("Your answer: ").lower()

  if question_17_a == "giant extinct bird" or question_17_a == "a":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("That is incorrect. You have lost 1 point")
    points -= 1

#Defines question 18. (When called, runs the eighteenth question)
def Question_18():
      
  global points
  print("")
  print("Question 18: ")
  print("")
  print("What is a 'Waka'?")
  print("")
  print("A. Truck")
  print("B. Canoe")
  print("C. Plane")

  question_18_a = input("Your answer: ").lower()

  if question_18_a == "canoe" or question_18_a == "b":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("That is incorrect. You have lost 1 point")
    points -= 1

#Defines question 19. (When called, runs the nineteenth question)
def Question_19():
      
  global points
  print("")
  print("Question 19: ")
  print("")
  print("What is a 'Tangi'?")
  print("")
  print("A. Road")
  print("B. House")
  print("C. Funeral")

  question_19_a = input("Your answer: ").lower()

  if question_19_a == "funeral" or question_19_a == "c":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("That is incorrect. You have lost 1 point")
    points -= 1

#Defines question 20. (When called, runs the twentieth question)
def Question_20():
      
  global points
  print("")
  print("Question 20: ")
  print("")
  print("What is a 'Motu'?")
  print("")
  print("A. Ocean")
  print("B. Island")
  print("C. Country")

  question_20_a = input("Your answer: ").lower()

  if question_20_a == "island" or question_20_a == "a":
    print("")
    print("Correct! You have gained 1 point")
    points += 1

  else:
    print("That is incorrect. You have lost 1 point")
    points -= 1

    

#Beggining of quiz code. Calls functions

#Quiz Startup
points = 0
bonus_points = 0
#Welcomes the user to the quiz
print("Welcome to your favourite Te Reo quiz!")
print("")

intro()
test_question_answers()
time.sleep(.5)
begin()

#The following code calls all 30 questions of the quiz 

#Question 1
#This code calls question 1 to be run

Question_1()
time.sleep(2)
os.system('clear')

#Question 2
#This code calls question 2 to be run

Question_2()
time.sleep(2)
os.system('clear')

#Question 3
#This code calls question 3 to be run

Question_3()
time.sleep(2)
os.system('clear')

#Question 4
#This code calls question 4 to be run

Question_4()
time.sleep(2)
os.system('clear')

#Question 5
#This code calls question 5 to be run

Question_5()
time.sleep(2)
os.system('clear')

#Question 6
#This code calls question 6 to be run

Question_6()
time.sleep(2)
os.system('clear')

#Question 7
#This code calls question 7 to be run

Question_7()
time.sleep(2)
os.system('clear')

#Question 8
#This code calls question 8 to be run

Question_8()
time.sleep(2)
os.system('clear')

#Question 9
#This code calls question 9 to be run

Question_9()
time.sleep(2)
os.system('clear')

#Question 10
#This code calls question 10 to be run

Question_10()
time.sleep(2)
os.system('clear')


#Question 11
#This code calls question 11 to be run

Question_11()
time.sleep(2)
os.system('clear')

#Question 12
#This code calls question 12 to be run

Question_12()
time.sleep(2)
os.system('clear')

#Question 13
#This code calls question 13 to be run

Question_13()
time.sleep(2)
os.system('clear')

#Question 14
#This code calls question 14 to be run

Question_14()
time.sleep(2)
os.system('clear')

#Question 15
#This code calls question 15 to be run

Question_15()
time.sleep(2)
os.system('clear')

#Question 16
#This code calls question 16 to be run

Question_16()
time.sleep(2)
os.system('clear')

#Question 17
#This code calls question 17 to be run

Question_17()
time.sleep(2)
os.system('clear')

#Question 18
#This code calls question 18 to be run

Question_18()
time.sleep(2)
os.system('clear')

#Question 19
#This code calls question 19 to be run

Question_19()
time.sleep(2)
os.system('clear')

#Question 20
#This code calls question 20 to be run

Question_20()
time.sleep(2)
os.system('clear')


#ending()