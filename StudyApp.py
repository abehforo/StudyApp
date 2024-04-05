#imprting tkinter as tk and messagebox
import tkinter as tk
from tkinter import messagebox

# create an empty list to store all the questions
questionsList = []

# Function that creates a new question
def createQ():
    #getting all the question, answer and hint from the inputs
    question = question_entry.get()
    answer = answer_entry.get()
    hint = hint_entry.get()
    #setting them inputs in order
    newQ = (question, answer, hint)
    #appending/adding the new inputs into the questionsList List
    questionsList.append(newQ)
    #confirmation message
    messagebox.showinfo("Question Registered", "Your question has been registered!")

    #clearing out all three entries/inputs after we have stored them into the list
    question_entry.delete(0, tk.END)
    answer_entry.delete(0, tk.END)
    hint_entry.delete(0, tk.END)

# Function that lets the user test thier knowledge
def test():
    #checking the list to see if we have enough questions to even test the user, if not we give user error and return to main window
    if len(questionsList) == 0:
        messagebox.showwarning("No Questions", "No questions available. Please create questions first.")
        return
    # initializing the score variable that keeps the users score
    score = 0
    #loop that runs for the number of questions in the list
    for question in questionsList:
        #calling askUser function and returning userans which is the user's response to the question
        userans = askUser(question[0])
        
        # comparing user input to the user answer, making them both lower case
        if userans.lower() == question[1].lower():
            #if correct display correct and add 1 to the user's score
            messagebox.showinfo("Correct!", "Correct answer!")
            score += 1
        #if wrong display incorrect and display the Hint
        else:
            messagebox.showinfo("Incorrect!", "Incorrect answer!")
            messagebox.showinfo("Hint", question[2])
        #allow the user to guess one last time by showing the question
            userans = askUser("Retry: " + question[0])
            
            #comparing user input to the user answer, making them both lower case
            if userans.lower() == question[1].lower():
                #if correct display correct and add 1 to the user's score
                messagebox.showinfo("Correct!", "Correct answer!")
                score += 1
            else:
                #if user gets it wrong a second time show them the right answer and dont add to their score
                messagebox.showinfo("Incorrect!", "The correct answer was: " + question[1])
    #calculate total questions by the length of the list
    totalQ = len(questionsList)
    #calculate the percatage of the score
    percentage = (score / totalQ) * 100
    #lastly show the user their score and their percentage
    messagebox.showinfo("Quiz Complete", "Score: {}/{}\nPercentage: {:.2f}%".format(score, totalQ, percentage))

# Function to create a dialog for user input
def askUser(prompt):
    #setting the window for input
    input_dialog = tk.Toplevel(window)
    #setting the dimensions
    input_dialog.geometry('500x200')
    #title of window
    input_dialog.title("Answer")
    #creating label setting it as input_label
    input_label = tk.Label(input_dialog, text=prompt)
    #setting the location
    input_label.pack()
    # creating an input spot and setting it as user_input
    user_input = tk.Entry(input_dialog)
    #setting location
    user_input.pack()
    # sets the cursor on the text box so the user can just start typing
    user_input.focus()

    def submit():
        # Declare answer as a global variable
        global answer  
        #setting user_input as answer
        answer = user_input.get()
        #closes the input window
        input_dialog.destroy()
    #creating a submit button that starts the submit function once clicked
    submit_button = tk.Button(input_dialog, text="Submit", command=submit)
    #button location
    submit_button.pack()

    #waiting untill user input to procceed
    input_dialog.wait_window(input_dialog)
    return answer

# Create the main window
window = tk.Tk()
#setting the size of the main window
window.geometry('400x200')
#setting the title of the main window
window.title("Flashcard App")

# Create labels and entry fields
question_label = tk.Label(window, text="Enter The Question:")
question_label.pack()
#window to input the question
question_entry = tk.Entry(window)
#manage the location of question
question_entry.pack()

#making the label to enter the answer to the question
answer_label = tk.Label(window, text="Enter The Answer:")
#location of answer
answer_label.pack()
# assigning the input to answer_entry
answer_entry = tk.Entry(window)
#location of input
answer_entry.pack()

#making the label for hints
hint_label = tk.Label(window, text="Enter The Hint:")
# location for the label 
hint_label.pack()
# assigning input to hint_entry
hint_entry = tk.Entry(window)
# location of input
hint_entry.pack()

# Creating the buttons and specifiying the functions that are associated
create_button = tk.Button(window, text="Submit Question", command=createQ)
#location of the button
create_button.pack()

# Creating the quiz me button that will trigger the test function once clicked
quiz_button = tk.Button(window, text="Test yourself", command=test)
# location of button
quiz_button.pack()

# Telling the app to run
window.mainloop()
