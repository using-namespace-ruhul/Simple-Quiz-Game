# -------------------------------------------------------------------------------------------------------------------------
def newGame(questions, options):
      
      guess = []
      correctAnswers = 0
      qsnNum = 1

      for key in questions:
            print("-"*70)
            print(key)
            for i in options[qsnNum-1]:
                  print(i)
            myGuess = input("Enter option (A / B / C / D): ").upper()
            guess.append(myGuess)

            correctAnswers += check(questions.get(key), myGuess)
            qsnNum += 1

      displayScore(questions,guess,correctAnswers)


# -------------------------------------------------------------------------------------------------------------------------
def check( correctAns, myAns):
      if correctAns == myAns:
            print("Correct!!!!")
            return 1
      else:
            print("Wrong!!!!")
            return 0



# -------------------------------------------------------------------------------------------------------------------------
def playAgain():
      response = input("Do you want to play again? (yes or no): ")
      response = response.upper()

      if response == "YES":
            return True
      else:
            return False


# -------------------------------------------------------------------------------------------------------------------------
def displayScore(questions, guess, correctAns):
      print()
      print("-"*30)
      print("          RESULT")
      print("-"*30)
      print("Answer:", end=" ")
      for value in questions.values():
            print(value, end=" ")
      print()

      print("My guesses: ", end=" ")
      for i in guess:
            print(i, end=" ")
      print()

      score = int((correctAns/len(questions))*100)
      print("Your score is:",str(score)+"%")
      
# -------------------------------------------------------------------------------------------------------------------------

questions = {
      "Which symbol represents the birth of Gautam Buddha?: " : "B",
      "The Vikramshila University was set up by which ruler of Pala dinesty?: " : "A",
      "The earliest evidence of banking transactions in India comes from:? " : "A",
      "Among all the pillar edicts of Ashoka, which is the longest one?: " : "B",
      "Is the earth round?: " : "C"
}

options =  [["A. Bodh tree","B. Lotus","C. Wheel","D. Horse"],
            ["A. Dharmapala","B. Ramapala","C. Gopala","D. Kumarpala"],
            ["A. Vedic era","B. Maurya era","C. Gupta era","D. Medieval era"],
            ["A. 6th pillar edict","B. 7th pillar edict","C. 5th pillar edict","D. 3rd pillar edict"],
            ["A. Yes","B. No","C. None of these","D. Wtf is Earth!!"]]

newGame(questions, options)

while playAgain():
      newGame()

print("Thanks for playing!!!")
# -------------------------------------------------------------------------------------------------------------------------