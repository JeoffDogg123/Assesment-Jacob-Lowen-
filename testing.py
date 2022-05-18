import time

STARTING_POINTS = 0
points = STARTING_POINTS





def question_1():
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
    print(points)
    question_2()

  else:
    print("That is incorrect. You have lost a point")
    points -= 1


def question_2():
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
    print(points)

  else:
    print("That is incorrect. You have lost a point")
    points -= 1

question_1()
