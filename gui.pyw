import random
import os
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Atspėk žodį')
root.geometry("600x480")

my_canvas = Canvas(root, width=300, height=200, bg="white")
my_canvas.pack(pady=10)

#nupiesiam kartuves
my_canvas.create_rectangle(100, 180, 110, 10, fill="black")
my_canvas.create_rectangle(110, 20, 180, 10, fill="black")


#nuskaitom zodzius is failo
with open("zodziai.txt", "r") as f:
        words = [line.strip() 
                 for line in f.readlines()
                 if line.strip() !=""]
        
secret_word = random.choice(words).upper()

lives = 7
guesses = [" "]


my_zodis = Label(root, text='Spėjamas žodis: ' + '*' * len(secret_word))
my_zodis.pack(pady=10)
my_zodis2 = Label(root, text='Liko bandymų: ' + '❤'*lives)
my_zodis2.pack(pady=10)

my_text = Text(root, width=10, height=1, font=("Helvetica", 16))
my_text.pack()


#nuskaitom teksta
def get_text():
    global lives, guesses, root
    secret_masked = ""
    spejimas =  my_text.get(1.0, 1.1).upper()
    guesses.append(spejimas)
    temp = my_label.cget("text")
    for letter in secret_word:
            if letter in guesses:
                secret_masked += letter
            else:
                secret_masked += "*"
    print(secret_masked)
    my_label.config(text=temp + spejimas)
    my_text.delete(1.0, END)
    my_zodis.config(text='Spėjamas žodis: ' + secret_masked)
   
    if not spejimas in secret_word:
        lives -= 1
        my_zodis2.config(text='Liko bandymų: ' + '❤'*lives)
        if lives == 6:
            my_canvas.create_rectangle(170, 20, 175, 50, fill="black")
        if lives == 5:
            my_canvas.create_oval(160, 50, 185, 70, fill="black")
        if lives == 4:
            my_canvas.create_rectangle(165, 70, 180, 110, fill="black")
        if lives == 3:
            my_canvas.create_line(165, 75, 135, 75, fill="black")
        if lives == 2:
            my_canvas.create_line(180, 75, 210, 75, fill="black")
        if lives == 1:
            my_canvas.create_line(170, 110, 170, 150, fill="black")
        if lives == 0:
            my_canvas.create_line(175, 110, 175, 150, fill="black")    
        
        if lives <= 0:
            atsakymas = messagebox.askretrycancel("Jus pralaimejote!", "Norite bandyti dar karta?") 
            if not atsakymas:
                root.quit()
            else:  
                root.destroy()
                os.startfile("gui.pyw")   #programos paleidimas is naujo
    if "*" not in secret_masked:
        atsakymas = messagebox.askretrycancel("Jus Laimejote!", "Norite bandyti dar karta?")
        if not atsakymas:
                root.quit()
        else:  
                root.destroy()
                os.startfile("gui.pyw")

get_text_button = Button(root, text="Spėjimas",command=get_text)
get_text_button.pack()


my_label = Label(root, text='Spėtos raidės: ')
my_label.pack(pady=10)


button_quit = Button(root, text="Baigti žaidimą", command=root.quit)
button_quit.pack(pady=20)

root.mainloop()


