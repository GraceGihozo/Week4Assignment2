def hangman_game():        # This is function of hangman game
    global mistake_count, win , loss
    mistake_count=0
    win= 0
    loss =0
    Questions = ["question1:\n when was ALU founded ?",
                 "question2:\n Who is the CEO of ALU?",
                 "question3:\n Where are ALU campuses?(separate location by (" and ")",
                 "question4:\n How many campuses does ALU have?",
                 "question5:\n What is the name of ALU Rwanda’s Dean?",
                 "question6:\n Who is in charge of Student Life",
                 "question7:\n What is the name of our Lab",
                 "question8:\n How many students do we have in Year 2 CS?",
                 "question9:\n How many degrees does ALU offer?",
                 "question10:\n Where are the headquarters of ALU?"]       # List of questions
    Answer = ["2015", "Fred Swanike", "Rwanda and Mauritius", "2", "Gaidi Faraj", "Sila Ogidi", "Egypt", "57", "8",
              "Mauritius"]     # List of Correct Answers


    for i in range(len(Questions)):      # Print and loop one by one a question from the question list.
      ans = input(Questions[i])
      if i == 0:
          if ans == Answer[i]:         # Go to the list of right answers to see if your answer is accurate or incorrect.
              print("Correct")
          else:
              print(F"you are hanging the man.{Answer[i]}")
              mistake_count+=1
      else:
          if ans == Answer[i]:       # Go to the list of right answers to see if your answer is accurate or incorrect.
            print("Correct")
          else:
              print(F"you are hanging the man {Answer[i]}")
              mistake_count += 1

      if mistake_count == 6:         # if you miss six questions the man dies
            print(f"Oops the man has died {mistake_count}")
            break
    if mistake_count == 0:         # if your mistakes equal to zero you have been completed all questions right
            print("congratulation!!!you get all questions right.your man lives")

    elif mistake_count < 6:       # if your mistakes is less six  your man will be live
            print(f"your man live, you made{mistake_count} mistake")

def display():         # This is function of count number of loss and win
    global win , loss
    if mistake_count <=5:
         win += 1
         print("win" , win)
    elif mistake_count > 5:
         loss= + 1
         print("loss", loss)

def play_again():              # This is function of play again and ask the user to play again
    response = input("Do you want to play again?( yes or no):")
    response = response.upper()

    if response =="YES":       # check if response is yes,we will return new game
       return True
    else:
        return False          # if response is no we will print bye




hangman_game()
display()

while play_again():
    hangman_game()
    display()
print("Byeeeeee")


