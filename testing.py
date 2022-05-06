def test_question():
  print("*** TEST QUESTION ***")
  print("")
  print("What is the Maori word for 'Hello'")
  print("")
  print("A. Hangi") 
  print("B. Kia Ora")
  print("C. Aroha")

test = input("Would you like to try a test question? ").lower()

if test == "yes" or test == "y":
  print("move")
  test_question()

elif test == "no" or test == "n":
  print("ok")

else:
  print("Continue")