import random
import tkinter
import _random

comp_check = random.randint(1,10)

def check_Guess():
    #Get a value from text_Guess
    user_guess = int(text_box.get())

    #get the value higher,lower or just right
    if user_guess  < comp_check:
        msg = "Higher!"
    elif user_guess > comp_check:
        msg ="Lower!"
    elif user_guess == comp_check:
        msg = "Correct!"
    else:
       msg= "Error,please try again!"
    # Show the results to the user
    lbl_result["text"] = msg

def reset_Guess():
    #Declare a global variable
   global comp_check
    #Choose the random integer
   comp_check = random.randint(1, 10)
   #Change the lbl_result text
   lbl_result["text"] = "Game Reset. Guess again"




# create a root window
root = tkinter.Tk()
# create the widgets
lbl_title = tkinter.Label(root, text="welcome to the Game")
lbl_title.pack()

lbl_result = tkinter.Label(root, text="good luck")
lbl_result.pack()

btn_check = tkinter.Button(root, text="Check" , fg ="green",command = check_Guess)
btn_check.pack(side ="left")

btn_reset = tkinter.Button(root, text="Reset" , fg ="Red",command = reset_Guess)
btn_reset.pack(side = "right")

text_box = tkinter.Entry(root, width = 3 )
text_box.pack()


#Start the main events loops
root.mainloop()
root.destroy()
