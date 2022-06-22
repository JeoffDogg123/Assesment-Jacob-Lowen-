bonus_points = 0



def bonus_question1():
  global bonus_points
  print("")
  print("Bonus Question 1: ")
  print("")
  print("What does the word 'Kapua' mean in english?")
  print("")
  print("A. Cloud")
  print("B. Fog")
  print("C. Storm")

  bonus_2_a = input("Your answer: ").lower()

  if bonus_2_a == "cloud" or bonus_2_a == "a":
    print("")
    print("Correct! You have gained 1 point")
    bonus_points += 3

  else:
    print("That is incorrect. You have lost 1 point")
    bonus_points -= 3

    
def bonus_question2():
  global bonus_points
  print("")
  print("Bonus Question 2: ")
  print("")
  print("What does the word 'Rorohiko' mean in english?")
  print("")
  print("A. Phone")
  print("B. Television")
  print("C. Computer")

  bonus_1_a = input("Your answer: ").lower()

  if bonus_1_a == "computer" or bonus_1_a == "c":
    print("")
    print("Correct! You have gained 1 point")
    bonus_points += 3

  else:
    print("That is incorrect. You have lost 1 point")
    bonus_points -= 3

def bonus_question3():
  global bonus_points
  print("")
  print("Bonus Question 3: ")
  print("")
  print("What is the Maori word for 'Community'?")
  print("")
  print("A. Hapori")
  print("B. ")
  print("C. ")

  bonus_3_a = input("Your answer: ").lower()

  if bonus_3_a == "computer" or bonus_3_a == "c":
    print("")
    print("Correct! You have gained 1 point")
    bonus_points += 3

  else:
    print("That is incorrect. You have lost 1 point")
    bonus_points -= 3