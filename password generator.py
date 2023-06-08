from tkinter import *
from random import randint, shuffle

# Function to generate a password
def generate_password():
    # Get the number of characters entered by the user
    num_chars = int(entry.get())
    
    # Generate a list of random ASCII characters in the range 33-126
    password_list = [chr(randint(33,126)) for _ in range(num_chars)]
    
    # Shuffle the list to create a random order of characters
    shuffle(password_list)
    
    # Convert the list of characters into a string
    password = ''.join(password_list)
    
    # Update the password entry with the generated password
    pw_entry.delete(0, END)
    pw_entry.insert(0, password)


# Create the main window
root = Tk()
root.title("Password genertor🔒")
root.geometry("400x290")


#icon set & background color
root.iconbitmap('C:\\Users\\boses\\Music\\Bing-wallpaper-2013-01-07.ico')
root.configure(bg='#5C6D7E')

# Create a label frame to hold the widgets
lf = LabelFrame(root, text="Number of Characters",bg='#5C6D7E')
lf.pack(pady=20)

# Create an entry widget to accept the number of characters
entry = Entry(lf, font=("Arial", 24))
entry.pack(pady=20, padx=20)

# Create an entry widget to display the generated password
pw_entry = Entry(root, font=("Arial", 24))
pw_entry.pack(pady=20)

# Create a button to generate the password
button = Button(root, text="Generate Password", command=generate_password,bg='#F0F0F0')
button.pack(pady=20)

# Start the main event loop
root.mainloop()
