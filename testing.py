#Ending code testing
points = 20

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





ending()